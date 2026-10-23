# Development roadmap

This is a proposed sequence. It is not a record of completed work or a promise of calendar dates.

| Milestone | Deliverables | Exit condition |
| --- | --- | --- |
| M0 — Public project definition | README, requirements, proposed architecture, task backlog | Team reviews scope and attribution |
| M1 — Hardware and measurement design | Interface matrix, power map, measurement point, sensor datasheets | Key procurement and measurement decisions recorded |
| M2 — Single-sensor acquisition | Timestamped readings, error flags, local CSV | Bench trace and repeatable one-sensor test |
| M3 — Station integration | Multi-sensor scheduler, SD queue, HMI, cellular transfer | 72 h acquisition test and outage/replay checks |
| M4 — Field collection | Calibration records, completeness report, versioned dataset | ≥4 months collected or shortfall explicitly reported |
| M5 — Forecast baseline | Leakage-aware splits, persistence/regression/SVR/ANN results | Held-out evaluation reproducible |
| M6 — Optimized ANN comparison | Equal-budget optimizer comparisons and micro/macro study | Results include uncertainty and failed targets |
| M7 — Demonstration and reporting | Public-safe photos, plots, short demo, final summary | Every published claim has linked evidence |

## Initial checklist

- [x] Initial public-facing documentation prepared.
- [x] Synthetic telemetry example and validator supplied.
- [ ] Review this repository with the team.
- [ ] Finalize hardware interfaces and power measurement point.
- [ ] Read and log one physical sensor.
- [ ] Integrate storage, HMI, and communication.
- [ ] Collect and review field data.
- [ ] Train and evaluate reference models.
- [ ] Compare optimized models and publish verified results.

Do not tick a project milestone just because its plan has been written.
