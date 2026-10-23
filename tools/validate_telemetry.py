"""Check one station/session of telemetry. Supplied input is synthetic."""
import argparse
import csv
from datetime import datetime, timezone
import json
import math
from pathlib import Path

NUMERIC = (
    'irradiance_w_m2', 'ambient_temp_c', 'panel_temp_c',
    'relative_humidity_pct', 'wind_speed_m_s', 'wind_direction_deg',
    'pv_voltage_v', 'pv_current_a', 'pv_power_w', 'battery_voltage_v',
)
REQUIRED = ('timestamp_utc', 'station_id', 'sequence', *NUMERIC,
            'quality_flag', 'data_origin')

def parse_time(value):
    stamp = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if stamp.tzinfo is None or stamp.utcoffset() is None:
        raise ValueError('timestamp must include a timezone')
    return stamp.astimezone(timezone.utc)

def validate(path, interval_s=60, expected_start=None, expected_end=None):
    if interval_s <= 0:
        raise ValueError('interval_s must be positive')
    with Path(path).open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        missing = set(REQUIRED) - set(reader.fieldnames or [])
        if missing:
            raise ValueError('missing columns: ' + ', '.join(sorted(missing)))
        rows = list(reader)
    if not rows:
        raise ValueError('CSV has no records')
    errors, parsed, ids, stations, origins = [], [], set(), set(), set()
    for index, row in enumerate(rows, 2):
        row_errors = []
        try:
            stamp = parse_time(row['timestamp_utc'])
            seq = int(row['sequence'])
            if seq < 0:
                raise ValueError('sequence must be non-negative')
            nums = {key: float(row[key]) for key in NUMERIC}
            if not all(math.isfinite(v) for v in nums.values()):
                raise ValueError('all numeric readings must be finite')
        except (ValueError, TypeError, AttributeError) as exc:
            errors.append(f'line {index}: {exc}')
            continue
        station = row['station_id'].strip()
        stations.add(station)
        origins.add(row['data_origin'].strip())
        if not station:
            row_errors.append('empty station_id')
        if not row['data_origin'].strip():
            row_errors.append('empty data_origin')
        identity = (station, seq)
        if identity in ids:
            row_errors.append('duplicate station/sequence')
        ids.add(identity)
        for key in ('irradiance_w_m2','wind_speed_m_s','pv_voltage_v',
                    'pv_current_a','pv_power_w','battery_voltage_v'):
            if nums[key] < 0:
                row_errors.append(f'{key} is negative under this draft sign convention')
        if not 0 <= nums['relative_humidity_pct'] <= 100:
            row_errors.append('relative humidity outside [0, 100]')
        if not 0 <= nums['wind_direction_deg'] < 360:
            row_errors.append('wind direction outside [0, 360)')
        expected_power = nums['pv_voltage_v'] * nums['pv_current_a']
        if abs(nums['pv_power_w']-expected_power) > max(1.0, 0.02*abs(expected_power)):
            row_errors.append('P differs from V*I beyond draft tolerance')
        if row['quality_flag'].strip() != 'ok':
            row_errors.append('quality_flag is not ok')
        if parsed and stamp <= parsed[-1][0]:
            row_errors.append('timestamp duplicate or not increasing')
        errors.extend(f'line {index}: {message}' for message in row_errors)
        parsed.append((stamp, not row_errors, index))
    if len(stations) != 1:
        errors.append('checker expects exactly one station/session')
    if not parsed:
        return {'rows': len(rows), 'expected_records': None,
                'valid_grid_records': 0, 'coverage_pct': None,
                'coverage_scope': 'no parseable timestamps', 'data_origins': [],
                'ok': False, 'errors': errors}
    stamps = [item[0] for item in parsed]
    start = parse_time(expected_start) if expected_start else min(stamps)
    end = parse_time(expected_end) if expected_end else max(stamps)
    if end < start:
        raise ValueError('expected end precedes start')
    span = (end-start).total_seconds()
    if abs(span/interval_s-round(span/interval_s)) > 1e-8:
        raise ValueError('expected window must span an integer number of intervals')
    expected = round(span/interval_s) + 1
    valid_slots = set()
    for stamp, valid, index in parsed:
        offset = (stamp-start).total_seconds()/interval_s
        slot = round(offset)
        if abs(offset-slot) > 1e-8:
            errors.append(f'line {index}: timestamp off expected sampling grid')
        elif not 0 <= slot < expected:
            errors.append(f'line {index}: timestamp outside expected window')
        elif valid:
            valid_slots.add(slot)
    missing_count = expected-len(valid_slots)
    if missing_count:
        errors.append(f'{missing_count} expected grid slots lack a valid unique record')
    return {'rows':len(rows), 'expected_records':expected,
            'valid_grid_records':len(valid_slots),
            'coverage_pct':round(100*len(valid_slots)/expected,6),
            'coverage_scope':'explicit window' if expected_start and expected_end
                             else 'observed or partly bounded window only',
            'data_origins':sorted(origins), 'ok':not errors, 'errors':errors}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('csv_file')
    parser.add_argument('--interval-s',type=int,default=60)
    parser.add_argument('--expected-start')
    parser.add_argument('--expected-end')
    args=parser.parse_args()
    try:
        report=validate(args.csv_file,args.interval_s,args.expected_start,args.expected_end)
    except (ValueError,OSError,csv.Error) as exc:
        parser.error(str(exc))
    print(json.dumps(report,indent=2))
    return 0 if report['ok'] else 1

if __name__=='__main__':
    raise SystemExit(main())
