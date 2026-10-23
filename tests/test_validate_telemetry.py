"""Edge cases for the CSV utility; these do not test real station hardware."""
import csv
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('telemetry',ROOT/'tools/validate_telemetry.py')
telemetry=importlib.util.module_from_spec(spec)
spec.loader.exec_module(telemetry)

class TelemetryTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path=Path(self.tmp.name)/'input.csv'
        with (ROOT/'examples/telemetry_synthetic.csv').open(newline='') as f:
            reader=csv.DictReader(f); self.fields=reader.fieldnames; self.rows=list(reader)

    def report(self):
        with self.path.open('w',newline='') as f:
            writer=csv.DictWriter(f,fieldnames=self.fields)
            writer.writeheader();writer.writerows(self.rows)
        return telemetry.validate(self.path)

    def test_synthetic_fixture_and_explicit_window(self):
        self.assertTrue(self.report()['ok'])
        result=telemetry.validate(self.path,expected_start='2026-01-01T09:00:00Z',expected_end='2026-01-01T09:06:00Z')
        self.assertFalse(result['ok']); self.assertEqual(result['expected_records'],7)

    def test_missing_middle_record_is_detected(self):
        self.rows.pop(2)
        result=self.report()
        self.assertFalse(result['ok']);self.assertEqual(result['expected_records'],6)
        self.assertEqual(result['valid_grid_records'],5)

    def test_duplicate_is_not_extra_coverage(self):
        self.rows.insert(2,dict(self.rows[1]))
        result=self.report()
        self.assertFalse(result['ok']);self.assertEqual(result['valid_grid_records'],6)

    def test_naive_timestamp_is_rejected(self):
        self.rows[2]['timestamp_utc']='2026-01-01T09:02:00'
        self.assertFalse(self.report()['ok'])

    def test_nonfinite_reading_is_rejected(self):
        self.rows[1]['pv_power_w']='nan'
        self.assertFalse(self.report()['ok'])

    def test_humidity_and_power_inconsistency(self):
        self.rows[1]['relative_humidity_pct']='101'
        self.rows[2]['pv_power_w']='999'
        result=self.report()
        self.assertFalse(result['ok']);self.assertEqual(result['valid_grid_records'],4)

    def test_timezone_offsets_map_to_same_instant(self):
        self.rows[1]['timestamp_utc']='2026-01-01T12:01:00+03:00'
        self.assertTrue(self.report()['ok'])

    def test_off_grid_timestamp_is_rejected(self):
        self.rows[2]['timestamp_utc']='2026-01-01T09:02:30Z'
        self.assertFalse(self.report()['ok'])

if __name__=='__main__':
    unittest.main()
