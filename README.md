# Laptop-only Display Simulation (Wokwi)

This simulation is for practicing the ESP32 + SSD1306 OLED software/display flow while the physical components are not yet available.

## Important limitation

The published Wokwi standard supported-hardware catalogue lists ESP32 boards and SSD1306 OLEDs, but does not list INA219 as a standard built-in part. The included simulation therefore runs the sketch with `SIMULATION_MODE = 1` and generates demonstration readings in software. It does **not** measure voltage/current and does **not** validate the INA219 circuit.

## Run it

1. Open https://wokwi.com/ and create a new ESP32 project.
2. Replace the starter sketch with `../src/esp32_dc_power_monitor.ino`.
3. Add a `diagram.json` using the file in this folder.
4. Add `libraries.txt` with the two OLED libraries listed in this folder.
5. Keep `SIMULATION_MODE = 1`.
6. Start simulation. The OLED and Serial Monitor should show clearly labelled demo values.

## When real hardware is available

1. Install Adafruit INA219 Library in Arduino IDE.
2. Assemble the physical circuit using `../hardware/connection-diagram.png` and the wiring table in the root README.
3. Check the module shunt/current rating, pinout, polarity and common ground.
4. Change `SIMULATION_MODE` from `1` to `0` only after the physical INA219 is connected.
5. Upload to the physical ESP32 and validate the readings against a multimeter.
