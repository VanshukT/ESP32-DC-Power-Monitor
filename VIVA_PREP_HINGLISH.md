# Viva / Professor Explanation — Hinglish

## 30-second introduction

“Sir, my project is called ESP32 DC Power Monitor. Iska objective kisi low-voltage DC load ka voltage, current aur power monitor karna hai. Isme INA219 sensor DC bus voltage aur shunt current measure karta hai. ESP32 I²C communication ke through sensor se readings leta hai, power calculate karta hai aur 0.96-inch OLED display par voltage, current aur power show karta hai. Serial Monitor par bhi readings milti hain.”

## Simple working explanation

1. “5V regulated DC supply load ko power deti hai.”
2. “INA219 sensor supply ke positive path mein series mein laga hota hai, isliye load ka current shunt resistor se pass hota hai.”
3. “INA219 shunt voltage drop aur bus voltage read karta hai.”
4. “ESP32 I²C ke through sensor se data receive karta hai.”
5. “Firmware `P = V × I` se power calculate karta hai.”
6. “OLED par voltage, current aur power display hote hain.”

## Viva questions and answers

**Q1. ESP32 ka role kya hai?**  
ESP32 main controller hai. Ye INA219 aur OLED ke saath I²C communication karta hai, readings process karta hai, aur display/Serial Monitor update karta hai.

**Q2. INA219 kyun use kiya?**  
INA219 ek I²C-based current/power monitor hai jo shunt voltage aur bus voltage measure karta hai. Isse current sensing ke liye alag analog amplifier design karne ki zarurat nahi padti.

**Q3. Shunt resistor kya hota hai?**  
Ye low-value resistor hota hai. Iske across chhota voltage drop measure karke current calculate hota hai: `I = Vshunt / Rshunt`.

**Q4. Power ka formula kya hai?**  
`P = V × I`, jahan voltage volt mein aur current ampere mein hota hai. Power watt mein milti hai.

**Q5. I²C kya hai?**  
I²C ek two-wire serial communication protocol hai. SDA data line hai aur SCL clock line hai. ESP32 master hai; INA219 aur OLED slave devices hain.

**Q6. INA219 aur OLED same SDA/SCL pins share kaise kar sakte hain?**  
I²C bus par multiple devices connect ho sakte hain, agar unke addresses alag hon. INA219 commonly 0x40 aur OLED commonly 0x3C hota hai, lekin actual addresses scan karke confirm karenge.

**Q7. VIN+ aur VIN− ka order kyun important hai?**  
Supply positive VIN+ par aur load positive VIN− par lagta hai. Is direction se current positive sign mein read hona chahiye. Reverse wiring se negative current ya wrong readings aa sakti hain.

**Q8. Common ground kyun chahiye?**  
ESP32, sensor, OLED aur external DC supply ko ek common voltage reference chahiye, tabhi I²C logic levels correctly interpret honge.

**Q9. Kya project AC mains measure kar sakta hai?**  
Nahi. Ye low-voltage DC monitor hai. Is project ko AC mains se connect nahi karna chahiye.

**Q10. Kya Wokwi simulation actual INA219 ko test karti hai?**  
Nahi. Supplied Wokwi setup ESP32 aur OLED ko test karta hai. INA219 standard Wokwi parts list mein included nahi hai, isliye demo mode generated sample values use karta hai. Real sensor readings sirf physical hardware test ke baad milengi.

**Q11. Energy (Wh) bhi show kar sakte hain?**  
Haan, future upgrade mein power ko time ke saath integrate karke energy Wh calculate ki ja sakti hai. Current version instantaneous power show karta hai.

**Q12. Accuracy kis par depend karegi?**  
INA219 IC grade, breakout shunt resistor, calibration, wiring, supply stability, temperature aur multimeter reference par.

## Honesty line for current stage

“Sir, abhi project design and simulation-preparation stage mein hai. Physical hardware assemble aur test hone ke baad hi actual measured readings aur final results add karunga.”
