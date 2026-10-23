# Proposed system architecture

![Architecture](media/architecture.svg)

## Acquisition and record ownership

The sensor layer will convert each validated device response into engineering units. A central acquisition record should carry one timestamp, a stable station/sequence identity, and quality flags. Invalid sensor responses must be recorded as missing/invalid rather than silently replaced with zero.

RTC-to-UTC conversion, power-cycle behavior, clock correction, and acceptable cross-channel skew remain to be defined. A shared timestamp is not by itself proof that sensors were sampled simultaneously.

## Local storage and cellular transfer

Local storage is intended to remain operational while cloud access fails. A recommended implementation is an append-only queue with per-record identities and an upload acknowledgement/checkpoint. Replay should be idempotent so retransmission cannot silently duplicate training rows. Reconnection traffic must not starve acquisition.

The proposal names SIM800L, Firebase, and FreeRTOS tasks. Exact modem capabilities, authenticated transport, cloud interface, task priorities, stack sizes, queues, shared SPI access, and watchdog behavior require validation before firmware choices are frozen. Pinning work to two cores does not guarantee timing isolation.

## HMI

The touch display will show recent measurements, their age, link status, SD status, and battery-related observations. Refresh and touch handling should have bounded execution time. Voltage-only battery indication must not be presented as calibrated state of charge without a supported battery model.

## Analysis boundary

Model training is planned in Python outside the acquisition loop. Data exports need a documented schema and provenance. The firmware should continue collecting measurements even if no trained model is available. Prediction issue time, forecast horizon, and model version belong in prediction records rather than being confused with acquisition timestamps.

## Interface contracts

| Boundary | Proposed contract | Open item |
| --- | --- | --- |
| Sensor → acquisition | Unit-aware reading plus status | Per-device interface/register maps |
| Acquisition → storage | Versioned timestamped telemetry record | Serialization and durable-write policy |
| Storage → cloud | Stable record identity, original timestamp, retry state | Authentication and acknowledgement |
| Cloud → analysis | Versioned historical export | Access rules and data provenance |
| Analysis → clients | Horizon, issue time, model version, predicted power | Deployment and latency definition |
