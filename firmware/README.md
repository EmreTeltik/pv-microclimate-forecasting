# Firmware development area

Production acquisition firmware is not included in this initial repository. The planned implementation covers sensor drivers, unit conversion, timestamps, durable logging, modem transfer, and a local touch display.

Begin with a single confirmed sensor and reviewed power/pin map. Add shared resources and FreeRTOS scheduling only after single-device evidence exists. Record board revision, framework/toolchain version, library versions, and build instructions when actual firmware is added.

Suggested future modules: sensor interface, acquisition scheduler, clock service, telemetry serializer, local queue, modem transport, HMI renderer, health monitor. These are planned module names, not existing source files.
