# Proposed telemetry data dictionary

Schema version for the starter example: `0.1-draft`. Names below are an initial public data contract and may change after firmware review. Missing values remain empty/null with an explicit quality flag; they do not become numeric zero.

| Field | Type / unit | Meaning |
| --- | --- | --- |
| timestamp_utc | ISO 8601 with timezone | Original measurement timestamp, normalized to UTC |
| station_id | String | Public-safe station identity |
| sequence | Non-negative integer | Monotonic identity within an acquisition session |
| irradiance_w_m2 | W/m² | Panel-plane irradiance |
| ambient_temp_c | °C | Shielded ambient temperature |
| panel_temp_c | °C | Measured panel/backsheet temperature; calibration describes interpretation |
| relative_humidity_pct | % | Relative humidity, 0–100 |
| wind_speed_m_s | m/s | Local wind speed |
| wind_direction_deg | degrees | Auxiliary direction, [0, 360) |
| pv_voltage_v | V | Voltage at the documented DC measurement point |
| pv_current_a | A | Current with documented sign convention |
| pv_power_w | W | Power at the documented DC measurement point |
| battery_voltage_v | V | Battery observation, not calibrated state of charge |
| quality_flag | String | Example uses `ok`; real firmware must define all failure states |
| data_origin | String | `synthetic` for the supplied file; field data must have actual provenance |

## Record identity and timing

The final record identity should include a boot/session identifier to survive sequence resets. The starter CSV uses a single station/session only. Sample-time, cloud-receipt-time, and forecast-issue-time are separate concepts. Store all necessary times; do not overwrite original sample time during replay.

## Aggregation and forecasting

Document whether timestamps label the start or end of a window. Define minimum valid samples per window and missing-channel rules. Mean, median, standard deviation, minimum, and maximum are planned statistics; circular wind direction needs an appropriate circular method rather than an ordinary arithmetic mean.

The supplied checker validates a single regular timestamp grid and a small set of fields. It does not establish calibration accuracy, clock accuracy, all sensor limits, or full field-data completeness for a multi-month deployment.
