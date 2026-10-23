# Requirements and acceptance evidence

These requirements translate the proposal into an initial verification matrix. Target definitions should be reviewed before testing.

| ID | Requirement / target | Evidence to produce | State |
| --- | --- | --- | --- |
| PV-01 | Record five primary environmental channels and DC electrical measurements | Data dictionary and simultaneous sensor log | Planned |
| PV-02 | Schedule raw records every 60 s | RTC/clock logs and timestamp-gap report | Planned |
| PV-03 | ≥98% valid expected records | Expected-grid definition, uptime window, valid/expected calculation | Planned |
| PV-04 | ≥99% valid Modbus transactions, CRC errors ≤1%, 72 h | First-attempt/retry-aware transaction counters | Planned |
| PV-05 | Preserve samples during a cloud outage | Power-cut/outage test and SD replay reconciliation | Planned |
| PV-06 | 5-day no-sun autonomy | Measured load profile, battery configuration, endurance log | Planned |
| PV-07 | Collect ≥4 months, target 6 months | Dataset manifest and quality summaries | Planned |
| PV-08 | 1/6 h: nRMSE ≤10%, R² ≥0.95; conditional MAPE ≤8% | Frozen held-out evaluation by horizon | Planned |
| PV-09 | 12/24 h: nRMSE ≤15%, R² ≥0.90 | Frozen held-out evaluation by horizon | Planned |
| PV-10 | RMSE skill ≥15% versus macro-weather reference | Same target period, model budget, and metric definitions | Planned |
| PV-11 | Monitoring latency ≤60 s and interface agreement ≥99% | Issue-time/receive-time logs and UI comparison | Planned |
| PV-12 | Local display remains usable without network access | Offline HMI demonstration and acquisition timing trace | Planned |

The prototype will use the proposal's IEC 61724-1 monitoring approach as a design reference. No certification or verified standard-compliance claim is made by this repository.
