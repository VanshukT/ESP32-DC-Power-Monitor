# Components and Purchase Checklist

This list is for the **physical prototype**. The user currently has no hardware parts, so nothing in this list is marked as owned.

| # | Item to buy | What to check before ordering | Priority |
|---:|---|---|---|
| 1 | ESP32 DevKit V1 (classic ESP32) | USB connector type, board layout, accessible GPIO21/GPIO22, 3V3 and GND pins. | Essential |
| 2 | INA219 I²C breakout | Confirm it is an INA219 board; check VIN+/VIN− terminals, shunt marking/value, stated current rating, supply/logic requirements, and included terminal block. | Essential |
| 3 | 0.96-inch SSD1306 OLED, 128×64, I²C, 4-pin | Confirm controller is SSD1306, interface is I²C, pin labels are GND/VCC/SCL/SDA, supply works at 3.3V, and address if listed. | Essential |
| 4 | Half-size breadboard | Standard solderless breadboard. | Essential |
| 5 | Jumper wires | Male-to-male; male-to-female if the modules use pin headers. | Essential |
| 6 | Regulated 5V DC supply | Stable regulated output; current limit preferred. Do not use a variable supply until its setting is checked. | Essential |
| 7 | 100Ω, 1W resistor | Predictable initial test load: about 50mA and 0.25W at 5V. It can become warm; keep ventilated. | Recommended first load |
| 8 | Small 5V DC fan | Optional visual load. Check rated and start-up/stall current against the supply and INA219 breakout ratings. | Optional |
| 9 | USB data cable | Must support data, not charging only; match the ESP32 board connector (Micro-USB or USB-C). | Essential |
| 10 | Digital multimeter | For independent voltage/current checks and continuity/polarity inspection. | Strongly recommended |

## Do not order blindly

- Do not assume every INA219 module can safely carry 2A or 3A. The breakout shunt, PCB traces, connectors, and cooling determine its practical limit.
- Do not assume every OLED board accepts 5V on VCC. The selected module must be safe with 3.3V supply/logic, or the wiring must be adjusted using its datasheet.
- Confirm the exact ESP32 board before relying on pin labels.
- Use a current-limited 5V source where possible. Do not connect the project to AC mains.

## First purchase order

A practical first order is: ESP32 DevKit + INA219 breakout + 0.96-inch I²C OLED + half breadboard + jumper wire kit + 5V regulated source + 100Ω 1W resistor + data USB cable. Add the fan after verifying its current rating.
