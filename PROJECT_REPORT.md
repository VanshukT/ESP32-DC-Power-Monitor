# Project Report: ESP32 DC Power Monitor

**Project type:** Embedded systems / DC instrumentation  
**Status:** Design and software-preparation stage; hardware not yet assembled or measured.

## Abstract

The ESP32 DC Power Monitor is a proposed low-voltage instrumentation project. It uses an INA219 current and power monitor to sense the DC bus voltage and load current. An ESP32 reads the sensor through the I²C interface, calculates power, and presents the readings on a 0.96-inch SSD1306 OLED. A serial output is also provided for debugging and logging. The first physical prototype will use a regulated 5V DC source and a small, safely rated load.

## 1. Introduction

Many electronic systems operate from DC supplies. Knowing only the supply voltage does not show how much current a load draws or how much power it consumes. A DC power monitor combines voltage and current measurement to estimate the electrical power being used by a load. This project introduces practical sensor interfacing, I²C communication, embedded firmware, display handling, and measurement verification.

## 2. Problem statement

A simple and low-cost way is needed to observe the voltage, current, and power of a small DC load without repeatedly connecting a separate meter for every reading. The proposed system reads these quantities and shows them continuously on a small display.

## 3. Objectives

1. Interface an INA219 sensor breakout with an ESP32.
2. Read the DC bus voltage and load current.
3. Calculate load power using the electrical relation `P = V × I`.
4. Display voltage, current, and power on an SSD1306 OLED.
5. Send the same readings to the Serial Monitor for debugging.
6. Verify the hardware measurements against a multimeter and document the results after assembly.

## 4. Components and their functions

| Component | Function |
|---|---|
| ESP32 DevKit | Main controller; runs firmware and acts as the I²C master. |
| INA219 breakout | Measures shunt voltage and bus voltage; provides measurement registers over I²C. |
| SSD1306 OLED | Displays the live readings locally. |
| Breadboard | Supports temporary, solderless circuit construction. |
| Jumper wires | Make the logic and signal connections. |
| Regulated 5V DC supply | Provides low-voltage power to the test load. |
| DC load | Device or resistor whose power consumption is monitored. |
| USB data cable | Connects ESP32 to the laptop for programming and serial output. |
| Multimeter | Provides an independent reference for validation. |

## 5. Theory

### 5.1 Current sensing

The INA219 measures the differential voltage across a shunt resistor. By Ohm's law:

`I = V_shunt / R_shunt`

The shunt resistor is part of the INA219 breakout. Its value and power/current capability must be identified from the actual board; different breakout designs must not be assumed to have the same rating. The INA219 IC datasheet specifies a 0–26V bus-voltage input range and a 3–5.5V IC supply range, but those IC limits do not automatically establish the safe voltage/current capability of a particular breakout board.

### 5.2 Bus voltage measurement

The INA219 also measures the DC bus voltage at its bus input. In the usual high-side arrangement, the supply positive is connected to `VIN+` and the load positive is connected to `VIN−`. The device measures the shunt drop and bus voltage and provides data through I²C.

### 5.3 Power calculation

Electrical power is:

`P (W) = V (V) × I (A)`

For example, a hypothetical measurement of 5.00V and 0.050A gives 0.25W. This is an example calculation only, not a project result.

### 5.4 I²C communication

I²C uses two signal wires: SDA (data) and SCL (clock). The ESP32 is the bus master. Both INA219 and OLED can share these wires because they normally use different I²C addresses. On a generic classic ESP32, GPIO21 is commonly SDA and GPIO22 is commonly SCL; confirm the selected board before wiring. The INA219 commonly uses address 0x40 and many SSD1306 modules use 0x3C, but the actual modules should be checked with an I²C scanner.

## 6. System design

The INA219 is placed in series with the positive supply line (high-side sensing). The load return goes to the supply negative. The ESP32 reads the INA219 via I²C. The OLED is connected to the same I²C bus. ESP32 GND, INA219 GND, OLED GND, and the 5V supply negative must share a common reference.

See `../hardware/connection-diagram.png` and `../hardware/system-block-diagram.png`.

## 7. Proposed wiring

### Power path

- 5V supply positive → INA219 VIN+.
- INA219 VIN− → load positive.
- Load negative → 5V supply negative.
- 5V supply negative → ESP32 GND.

### Logic and I²C path

- INA219 VCC → ESP32 3V3.
- INA219 GND → ESP32 GND.
- OLED VCC → ESP32 3V3, if the selected OLED module supports 3.3V supply.
- OLED GND → ESP32 GND.
- INA219 SDA and OLED SDA → ESP32 GPIO21.
- INA219 SCL and OLED SCL → ESP32 GPIO22.

Power ESP32 via laptop USB during early tests. Do not connect the 5V load supply to the ESP32 3V3 pin. Verify module pin labels and logic-level requirements before connection.

## 8. Software design

The firmware is written for the Arduino framework on ESP32. It initializes I²C, initializes the SSD1306 display, and (in hardware mode) initializes the INA219 library. At a regular update interval, it obtains voltage and current, calculates power, prints the values to Serial, and refreshes the OLED.

Two modes are provided:

- **Simulation mode:** generated values for testing the ESP32/OLED display flow on a laptop simulator. It does not measure a real circuit.
- **Hardware mode:** reads the actual INA219 sensor. This mode should only be selected after connecting the physical sensor and checking the breakout's shunt calibration and rating.

## 9. Laptop-only simulation

Wokwi supports ESP32 development boards and SSD1306 OLED displays. Its published standard hardware list does not include INA219 as a built-in sensor part. Therefore the supplied Wokwi setup uses synthetic values to test the screen layout and firmware flow only. It cannot prove INA219 accuracy or the real power-path wiring.

## 10. Testing and validation plan

The following tests are planned after hardware is available:

1. Confirm ESP32 uploads and prints to Serial.
2. Confirm OLED is detected at its actual I²C address.
3. Run an I²C scanner to check OLED and INA219 addresses.
4. With the power source OFF, inspect polarity and continuity.
5. Start with a regulated 5V supply and a low-current load within the breakout rating.
6. Compare bus voltage with a multimeter.
7. Compare current with a suitable multimeter connection or known series reference method.
8. Verify calculated power against `V × I`.
9. Repeat with a second load only after the first test is stable.
10. Record test conditions, component markings, errors, and genuine photos.

No test results are reported in this document because the physical prototype has not yet been built.

## 11. Applications

- Learning DC power measurement and sensor interfacing.
- Monitoring small DC electronic loads.
- Testing low-voltage embedded prototypes.
- Demonstrating I²C communication and OLED data presentation.
- Educational battery-powered project monitoring, subject to appropriate voltage/current ratings and calibration.

## 12. Limitations

- The accuracy depends on the INA219 grade, breakout shunt resistor, calibration, wiring, and measurement conditions.
- The 26V bus capability in the INA219 IC datasheet is not a safe operating guarantee for every breakout board or connected load.
- The OLED address and supply requirements vary across modules.
- The current project monitors instantaneous DC readings; energy (Wh) would require integrating power over time and careful timekeeping.
- The initial Wokwi demo uses synthetic values and does not simulate the INA219.

## 13. Safety precautions

- Never connect AC mains to the prototype.
- Use only a regulated low-voltage DC source for initial tests.
- Check the INA219 breakout's stated shunt/current limit; do not infer it from the IC datasheet alone.
- Begin with a low-current load and a current-limited supply.
- Switch off power before changing wiring.
- Observe correct VIN+ / VIN− polarity and common ground.
- Keep power resistors ventilated; they may become hot.

## 14. Conclusion

The proposed ESP32 DC Power Monitor is a practical learning project combining DC measurement, embedded programming, I²C sensor interfacing, power calculation, and local display output. The next milestone is a display-only simulation, followed by component procurement, careful assembly, and verification against a multimeter. The repository will be updated with real measured results only after those tests have been completed.

## References

1. Texas Instruments, [INA219 datasheet](https://www.ti.com/lit/ds/symlink/ina219.pdf).
2. Espressif, [Arduino-ESP32 I²C documentation](https://docs.espressif.com/projects/arduino-esp32/en/latest/api/i2c.html).
3. Adafruit, [INA219 Arduino library](https://github.com/adafruit/Adafruit_INA219).
4. Adafruit, [SSD1306 Arduino library](https://github.com/adafruit/Adafruit_SSD1306).
5. Wokwi, [Supported hardware](https://docs.wokwi.com/getting-started/supported-hardware) and [SSD1306 reference](https://docs.wokwi.com/parts/board-ssd1306).
