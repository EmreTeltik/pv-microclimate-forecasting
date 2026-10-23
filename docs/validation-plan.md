# Validation and experiment plan

## 1. Acquisition tests

| Test | Procedure | Evidence / acceptance |
| --- | --- | --- |
| Unit conversion | Compare raw registers, conversion code, and a known reference | Units, scaling, sign, and calibration record |
| 72 h communication | Count issued requests, first-attempt valid replies, retries, timeouts, CRC failures | Proposal targets ≥99% valid transactions and ≤1% CRC errors; denominators reported |
| Sample completeness | Define start/end, expected 60 s grid, tolerances, valid-channel requirement | Unique valid records / expected records; target ≥98% |
| Network outage | Disable cellular link while acquisition continues, then reconnect | Local record count reconciles with cloud unique IDs; loss and duplicates reported |
| HMI load | Operate touch/display while acquisition, SD writes, and modem traffic run | Timing jitter, missed deadlines, and queue high-water marks |
| Autonomy | Use reviewed load/battery setup under a defined no-charge scenario | Actual duration, energy and temperature; target 5 days |
| Monitoring | Compare acquisition, arrival, and display timestamps | Explicit definition of ≤60 s latency and ≥99% data agreement |

## 2. Forecast dataset construction

For each horizon h, define a forecast issued at time t and a target at t+h or over an explicitly named future interval. Inputs must be available at t. Historical observations, known calendar features, and weather forecasts archived with issue times are different from future measured weather.

Split chronologically. Reserve the last 20% of the period for final testing; use the earlier 80% for model development with walk-forward folds. Remove training examples whose target windows overlap validation/test periods. Fit scalers, imputers, feature selection, and hyperparameters inside the training folds only. Log dropped rows and keep baseline/model evaluation masks identical.

The micro-weather versus macro-weather study must compare equivalent target windows and feature availability. An analysis using simultaneous measured weather is a retrospective analysis and must be labelled accordingly, rather than called an operational 24-hour forecast.

## 3. Models and comparison fairness

Start with persistence and an appropriate same-time previous-day baseline. Then compare linear regression, SVR, standard ANN, and optimized ANN candidates. PSO, GWO, WOA, and GA are candidates, not established winners. Record search space, objective, random seeds, compute budget, stopping criteria, and repeated-run results.

## 4. Metrics

For N matched observations `y` and predictions `y_hat`:

- `MAE = mean(abs(y - y_hat))`.
- `RMSE = sqrt(mean((y - y_hat)^2))`.
- `nRMSE_pct = 100 × RMSE / P_rated`, where the rated power and its use as denominator are declared.
- `R² = 1 - sum((y-y_hat)^2) / sum((y-mean(y))^2)`; report as undefined for a constant target.
- `MAPE_pct = 100 × mean(abs((y-y_hat)/y))` on a **predefined valid-power subset**. Publish the threshold and included/excluded counts; report a full-period absolute-error metric too.
- `Skill_pct = 100 × (1 - RMSE_model / RMSE_reference)`; report as undefined if reference RMSE is zero.

Use identical paired samples for skill comparisons. Include day/night breakdowns, season coverage, and uncertainty across time blocks. Four to six months of data do not establish full-year generalization. Do not tune an acceptance threshold using the final test results.

## 5. Evidence to publish

For each experiment record the data version/hash, split dates, forecast issue-time rules, feature list, configuration, software versions, model/seed, held-out metrics, and limitations. Add plots only after the corresponding experiment exists. Synthetic example output remains labelled synthetic.
