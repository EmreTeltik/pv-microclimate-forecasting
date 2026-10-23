# Open engineering decisions

| ID | Question | Evidence needed to close it |
| --- | --- | --- |
| D01 | Does each purchased sensor expose Modbus, analog, resistance, or pulse output? | Exact variant datasheets and interface matrix |
| D02 | What PV power is being predicted: available power or actual load/charger-limited power? | Measurement point, controller operating modes, and target definition |
| D03 | Can the selected modem/operator/cloud path meet authentication and transport requirements? | Bench connectivity test without publishing credentials |
| D04 | What are actual battery chemistry, voltage, and usable capacity? | Battery/BMS/charger documents and measured load budget |
| D05 | What are UTC conversion, RTC drift, synchronization, and replay timestamp rules? | Timing design and drift test |
| D06 | How will SD and TFT share buses/pins without acquisition delays? | Board-revision pin map and timing trace |
| D07 | Which weather inputs will actually be known at each forecast issue time? | Issue-time dataset definition and archived weather-forecast availability |
| D08 | What is the daytime/low-power MAPE rule? | Written evaluation rule frozen before final testing |
| D09 | Which optimized ANN configuration wins under equal comparison conditions? | Repeated training/validation experiments; held-out test used only for final reporting |
| D10 | What material may be released publicly and under what license? | Team/advisor publication decision |

These are design tasks, not reported failures. Record the decision, date, rationale, and supporting evidence when each is resolved.
