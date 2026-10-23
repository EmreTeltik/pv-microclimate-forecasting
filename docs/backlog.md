# Initial issue backlog

Copy one task at a time into GitHub Issues. Uploading this file does not create issues automatically. These are suggested tasks, not completed work.

## PV-T01 — Confirm sensor interfaces and Modbus register maps

Goal: establish what can actually connect to the acquisition layer.

- [ ] List exact manufacturer/model variants and datasheet links.
- [ ] Record supply voltage, output type, scaling, address, register, and sampling limits.
- [ ] Review logic-level and wiring compatibility.

Acceptance: a reviewed interface matrix is committed; uncertain register addresses are not invented.

## PV-T02 — Define the PV measurement point and prediction target

- [ ] Draw the panel/charger/battery/load measurement path.
- [ ] Define whether the target is available or actual operating-point power.
- [ ] Explain how charge limiting and curtailment are identified in the dataset.

Acceptance: the target and measurement topology are documented before model comparisons.

## PV-T03 — Acquire one real sensor and save timestamped samples

- [ ] Read one sensor with status/error reporting.
- [ ] Save raw and converted values with units and original timestamps.
- [ ] Compare one operating point against a suitable reference.

Acceptance: publish a sanitized bench log and repeatable run instructions.

## PV-T04 — Implement durable local logging and replay

- [ ] Define session/sequence identity and schema version.
- [ ] Keep acquiring during a simulated link outage.
- [ ] Reconcile unique local and cloud records after reconnecting.

Acceptance: report missing, duplicate, and replayed records with a reproducible outage test.

## PV-T05 — Run the 72-hour acquisition and HMI test

- [ ] Log requests, valid responses, CRC failures, retries, and timeouts.
- [ ] Exercise TFT refresh/touch and modem traffic.
- [ ] Calculate completeness from the predetermined expected grid.

Acceptance: report actual metrics against PV-02/03/04/12, including failed targets.

## PV-T06 — Freeze the forecast evaluation protocol

- [ ] Define targets, horizons, known-at-issue-time features, split dates, and target-window gap.
- [ ] Freeze normalization, nighttime MAPE, and missing-data rules.
- [ ] Prepare persistence and same-time previous-day baselines.

Acceptance: one reviewed configuration governs all compared models.

## PV-T07 — Publish the first held-out baseline result

- [ ] Record data version, code version, training-only preprocessing, and model settings.
- [ ] Evaluate on the held-out period without tuning on it.
- [ ] Include error plots and coverage limitations.

Acceptance: another team member can reproduce the result from the documented inputs.

## PV-T08 — Compare optimized ANN candidates

- [ ] Use equal optimization budgets, fixed splits, and multiple seeds.
- [ ] Compare micro-weather and macro-weather inputs under equal availability rules.
- [ ] Report skill, uncertainty, runtime, and targets not achieved.

Acceptance: the selected method is justified by recorded experiments.
