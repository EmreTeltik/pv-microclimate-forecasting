# Current status

Status date: 23 October 2026. Update this file when actual project work changes the evidence.

| Area | State | Evidence available in this repository |
| --- | --- | --- |
| Research support | TÜBİTAK 1002-A support approved | Team-reported status; no grant identifier published |
| Project definition | Proposal prepared | Public overview and derived requirements |
| Public repository materials | Initial draft prepared | README, architecture, targets, backlog, and test plan |
| Small software utility | Initial telemetry validator included | Source, synthetic input, and automated edge-case tests |
| Sensor acquisition firmware | Planned | Interface and integration plan only |
| Local HMI and cloud connection | Planned | Architecture and open decisions |
| Field data collection | Not reported here | No field dataset published |
| ANN and optimization experiments | Planned | Evaluation protocol only |
| Forecast scores and autonomy | Not measured here | Targets only |

## What counts as progress

A documentation task can be marked complete when its reviewed document exists. Hardware or model tasks require the relevant measurement, log, plot, or reproducible experiment. Passing a synthetic utility test does not verify the station.

## Next evidence to collect

1. Confirmed sensor part numbers and interface/register documentation.
2. One sensor reading saved with a timestamp, unit, and quality flag.
3. A repeatable Modbus transaction log and a short local-storage test.
4. A reviewed pin/power map before multi-module integration.
