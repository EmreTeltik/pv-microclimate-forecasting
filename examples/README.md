# Synthetic telemetry example

`telemetry_synthetic.csv` contains six manually constructed one-minute records solely to demonstrate the proposed CSV schema and validator. It is not recorded at Ege University or any physical station. It does not support forecasting, accuracy, autonomy, or communication-performance claims.

Every row has `data_origin=synthetic`. Production logs need a schema/session identifier and documented calibration, clock, and quality rules. Avoid treating a successful checker run as proof that sensor readings are physically accurate.
