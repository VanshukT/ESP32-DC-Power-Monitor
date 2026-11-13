# Hardware Test Plan and Results Log

**Current status:** Not tested — physical components are not yet available.

Do not mark a test passed until it has been performed on the physical prototype.

## Pre-power checks

- [ ] Confirm exact ESP32 board pinout.
- [ ] Confirm INA219 breakout shunt value and rated current.
- [ ] Confirm OLED controller, I²C address, and 3.3V supply compatibility.
- [ ] Check VIN+ and VIN− direction.
- [ ] Check all grounds are common.
- [ ] Inspect for loose strands, shorts, and reversed polarity.
- [ ] Confirm no AC mains is connected.

## Functional tests

| Test | Method | Expected observation | Actual result / notes |
|---|---|---|---|
| ESP32 upload | Upload sketch over USB | Upload completes; Serial Monitor starts | Not tested |
| OLED I²C | Run display initialization / I²C scan | OLED responds at its actual address | Not tested |
| INA219 I²C | Run I²C scan / sensor initialization | INA219 responds at its actual address | Not tested |
| Bus voltage | Compare INA219 with multimeter | Readings are reasonably close within device/module tolerance | Not tested |
| Current | Compare with an appropriate series measurement/reference | Readings are reasonably close | Not tested |
| Power | Compare with V × I | Displayed power follows voltage × current | Not tested |
| Display refresh | Observe OLED over time | Values update without freezing | Not tested |

## Measurement record

| Trial | Load description | Supply voltage (V) | INA219 voltage (V) | INA219 current (A) | Calculated power (W) | Reference meter result | Notes |
|---:|---|---:|---:|---:|---:|---|---|
| 1 |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |  |

## Photo log

After assembly, add genuine photos of:

- [ ] Top view of the complete prototype.
- [ ] Close-up of ESP32, INA219, OLED labels and wiring.
- [ ] OLED showing a live reading while the real load is connected.
- [ ] Laptop Serial Monitor during the physical measurement.

Do not use the concept render as proof that hardware has been built.
