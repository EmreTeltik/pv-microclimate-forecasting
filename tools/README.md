# Telemetry starter utility

From the repository root, with Python 3.10+:

```bash
python tools/validate_telemetry.py examples/telemetry_synthetic.csv
python -m unittest discover -s tests -v
```

Windows may use `py` instead of `python`. No additional Python packages are required. Exit code 0 means the implemented schema checks passed; 1 means data problems were found; 2 means a CLI/input error.

The checker requires one station, ordered timezone-aware timestamps on an exact 60-second grid by default, unique sequences, finite numeric values, simple physical sign/range checks, `quality_flag=ok`, and approximate `P=V×I` consistency. The default P tolerance is 1 W or 2%, whichever is greater. It reports **observed-window** grid coverage, not deployment-wide completeness. A truncated file with consecutive samples can still show 100% observed-window coverage.

The expected-window options prevent a missing start/end period from being ignored:

```bash
python tools/validate_telemetry.py examples/telemetry_synthetic.csv --expected-start 2026-01-01T09:00:00Z --expected-end 2026-01-01T09:05:00Z
```

This is a strict initial CSV checker, not a production telemetry service. The default quality/range rules, single-session constraint, timestamp tolerance, and electrical convention need review before use with real firmware logs. Preserve raw invalid records rather than deleting them merely to make the checker pass.
