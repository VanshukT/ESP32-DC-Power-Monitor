/*
  Project: ESP32 DC Power Monitor
  Purpose: Read DC bus voltage and load current with INA219, calculate power,
           and display the values on a 0.96-inch SSD1306 I2C OLED.

  IMPORTANT:
  - SIMULATION_MODE = 1 uses generated demonstration values (no sensor measurement).
  - SIMULATION_MODE = 0 enables the physical INA219 sensor.
  - Do not describe simulated values as real test results.
  - Verify the INA219 breakout's shunt/current rating and wiring before use.
*/

#define SIMULATION_MODE 1  // Change to 0 only after connecting the real INA219 hardware.

#include <Wire.h>
#include <math.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#if SIMULATION_MODE == 0
  #include <Adafruit_INA219.h>
  Adafruit_INA219 ina219;
#endif

// Generic ESP32 DevKit defaults. Confirm these pins on your exact board.
constexpr uint8_t I2C_SDA_PIN = 21;
constexpr uint8_t I2C_SCL_PIN = 22;
constexpr uint8_t OLED_ADDRESS = 0x3C;  // Some OLED modules use 0x3D.

constexpr int SCREEN_WIDTH = 128;
constexpr int SCREEN_HEIGHT = 64;
constexpr int OLED_RESET = -1;
constexpr unsigned long UPDATE_INTERVAL_MS = 500;

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
unsigned long lastUpdateMs = 0;
bool oledReady = false;

struct PowerReadings {
  float voltageV;
  float currentA;
  float powerW;
};

void showError(const char *line1, const char *line2) {
  Serial.println(line1);
  if (oledReady) {
    display.clearDisplay();
    display.setTextColor(SSD1306_WHITE);
    display.setTextSize(1);
    display.setCursor(0, 8);
    display.println(line1);
    display.println(line2);
    display.display();
  }
}

bool readPowerReadings(PowerReadings &reading) {
#if SIMULATION_MODE == 1
  // Demonstration data for laptop/Wokwi display testing only.
  // These values are generated in software and are NOT sensor measurements.
  const float t = millis() / 1000.0f;
  reading.voltageV = 5.00f + 0.03f * sinf(t * 0.70f);
  reading.currentA = 0.10f + 0.01f * sinf(t * 1.10f);
  reading.powerW = reading.voltageV * reading.currentA;
  return true;
#else
  // Physical mode: INA219 measures the bus voltage and shunt current.
  reading.voltageV = ina219.getBusVoltage_V();
  reading.currentA = ina219.getCurrent_mA() / 1000.0f;
  reading.powerW = reading.voltageV * reading.currentA;
  return true;
#endif
}

void updateDisplay(const PowerReadings &reading) {
  display.clearDisplay();
  display.setTextColor(SSD1306_WHITE);

  display.setTextSize(1);
  display.setCursor(0, 0);
  display.println(F("DC POWER MONITOR"));
  display.drawLine(0, 11, SCREEN_WIDTH - 1, 11, SSD1306_WHITE);

  display.setCursor(0, 17);
  display.print(F("Voltage: "));
  display.print(reading.voltageV, 2);
  display.println(F(" V"));

  display.setCursor(0, 31);
  display.print(F("Current: "));
  display.print(reading.currentA, 3);
  display.println(F(" A"));

  display.setCursor(0, 45);
  display.print(F("Power:   "));
  display.print(reading.powerW, 3);
  display.println(F(" W"));

#if SIMULATION_MODE == 1
  display.setCursor(0, 57);
  display.print(F("DEMO VALUES ONLY"));
#endif

  display.display();
}

void printToSerial(const PowerReadings &reading) {
  Serial.print(F("Voltage: "));
  Serial.print(reading.voltageV, 3);
  Serial.print(F(" V | Current: "));
  Serial.print(reading.currentA, 3);
  Serial.print(F(" A | Power: "));
  Serial.print(reading.powerW, 3);
  Serial.println(F(" W"));
}

void setup() {
  Serial.begin(115200);
  delay(200);

  Wire.begin(I2C_SDA_PIN, I2C_SCL_PIN);

  oledReady = display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDRESS);
  if (!oledReady) {
    Serial.println(F("OLED not detected. Check address and I2C wiring."));
    while (true) {
      delay(1000);
    }
  }

  display.clearDisplay();
  display.setTextColor(SSD1306_WHITE);
  display.setTextSize(1);
  display.setCursor(0, 10);
  display.println(F("DC POWER MONITOR"));
#if SIMULATION_MODE == 1
  display.println(F("Starting demo mode..."));
#else
  display.println(F("Starting sensor mode..."));
#endif
  display.display();

#if SIMULATION_MODE == 0
  if (!ina219.begin()) {
    showError("INA219 not detected", "Check I2C connections");
    while (true) {
      delay(1000);
    }
  }
  // The library's default calibration is intended for common 32V/2A-class
  // Adafruit boards. A clone or different shunt may need calibration changes.
  // Verify your specific breakout documentation before trusting measurements.
#endif

  Serial.println();
  Serial.println(F("ESP32 DC Power Monitor"));
#if SIMULATION_MODE == 1
  Serial.println(F("MODE: SIMULATION - generated demo values, not real measurements"));
#else
  Serial.println(F("MODE: HARDWARE - INA219 sensor readings"));
#endif
}

void loop() {
  const unsigned long now = millis();
  if (now - lastUpdateMs >= UPDATE_INTERVAL_MS) {
    lastUpdateMs = now;

    PowerReadings reading{};
    if (readPowerReadings(reading)) {
      updateDisplay(reading);
      printToSerial(reading);
    } else {
      showError("Read failed", "Check the sensor");
    }
  }
}
