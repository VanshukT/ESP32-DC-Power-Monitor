# GitHub Upload Guide — Hinglish

## Repository name

`ESP32-DC-Power-Monitor`

## Short description

`ESP32-based DC voltage, current and power monitor using INA219 and an SSD1306 OLED. Current status: design and display simulation; physical build pending.`

## Browser se upload karne ke steps

1. GitHub par login kar.
2. **New repository** par click kar.
3. Repository name `ESP32-DC-Power-Monitor` rakh.
4. Public visibility select kar, agar portfolio mein dikhana hai.
5. Agar local folder ka README already bana hua hai, toh GitHub par naya README auto-generate mat kar; blank repository create karna easiest rahega.
6. Repository open kar aur **Add file → Upload files** select kar.
7. Extracted `ESP32_DC_Power_Monitor` folder ke **andar ka saara content** upload kar. Folder ke andar ke folders (`src`, `docs`, `hardware`, `images`, `simulation`, `tests`) ko bhi preserve karna.
8. Commit message likh: `Add initial project documentation and simulation firmware`.
9. Commit changes kar.

GitHub web uploader mein folder drag/drop kabhi browser ke hisaab se vary kar sakta hai. Agar nested folders upload na ho rahe hon, toh GitHub Desktop ya Git CLI use kar; ek-ek file ko alag-alag root mein mat daalna, warna relative image links break honge.

## Repository ke About section mein

- Description: upar wali short description.
- Topics: `esp32`, `ina219`, `i2c`, `oled`, `embedded-systems`, `electronics`, `dc-power-monitor`.

## Pinned repo / profile mein kya show karein

Project ko tab pin kar sakta hai jab initial README, code, diagrams aur simulation instructions upload ho jayein. README mein project status clearly likha rehna chahiye.

## Very important — genuine portfolio

- `concept-render-not-built-prototype.png` AI-generated concept render hai. Isko concept image hi label karna.
- `connection-diagram.png` proposed wiring diagram hai, actual hardware photograph nahi.
- OLED mockup aur simulation outputs illustrative/demo hain.
- Physical prototype build hone ke baad apni asli photos aur actual readings add karna. Fake “I built this” evidence mat upload karna; honest project stage recruiters ke liye bhi better hai.
