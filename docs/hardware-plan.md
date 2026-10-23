# Preliminary hardware integration plan

The proposal supplies candidate hardware, not a finished wiring design. Do not wire a device from this table alone; use its exact datasheet and the reviewed schematic.

| Subsystem | Proposal candidate | Before integration |
| --- | --- | --- |
| Controller/modem | ESP32 TTGO T-Call with SIM800L | Confirm board revision, power rails, modem peak current, accessible GPIO, and operator coverage |
| RS485 | MAX485-class module | Confirm logic-level compatibility with ESP32, direction control, bus topology, termination, and isolation needs |
| DC measurement | PZEM-017 and shunt | Confirm measurement location, ratings, orientation, register definitions, and reference instrument |
| Irradiance | PV pyranometer | Obtain calibration and output-interface documents; align with panel plane |
| Panel temperature | PT1000-based sensor assembly | Confirm transmitter/interface; document rear-surface attachment and cell-temperature interpretation |
| Ambient conditions | Temperature/humidity sensor and wind sensors | Confirm output types; plan radiation shield and wind exposure |
| Time/storage | DS1302 and SPI microSD | Confirm voltage levels, RTC drift, card integrity, and SPI bus sharing |
| Local display | ILI9341-based TFT/touch assembly | Confirm touch controller, pin budget, voltage levels, and refresh timing |
| Power | 550 W panel, charge controller, battery, buck rails | Confirm battery chemistry/series count, BMS, charge compatibility, cold/load limits, and protection |
| Mechanics | Sigma-profile structure and weather enclosure | Review mounting, cable entries, panel shading, sensor exposure, and service access |

## Power budget

The proposal uses approximately 80 Wh/day, 5 days, a nominal 12 V battery assumption, and 80% usable depth of discharge for an initial estimate:

`C_ideal = (80 Wh/day × 5 days) / (12 V × 0.8) ≈ 41.7 Ah`.

This is an ideal proposal calculation. The actual battery voltage, usable energy, conversion losses, temperature, ageing, GSM current peaks, and measured consumption must be incorporated before procurement. The proposal mentions a 45–50 Ah design band; no autonomy result is claimed.

## First bench evidence

Publish a reviewed block/pin map, one sensor's raw and converted values, a reference-instrument comparison, and a short log. Do not upload serial numbers, SIM credentials, personal phone numbers, or private cloud keys.
