import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
from matplotlib.lines import Line2D
from pathlib import Path

OUT = Path(__file__).parent / 'hardware'
OUT.mkdir(exist_ok=True)

# Palette
NAVY = '#12304A'
BLUE = '#2878B5'
CYAN = '#12A6A6'
RED = '#D94C4C'
BLACK = '#263238'
GREEN = '#328A59'
GOLD = '#D49A25'
LIGHT = '#F4F7FA'
MUTED = '#5B6B78'


def box(ax, xy, w, h, title, subtitle='', fc='white', ec=NAVY, title_fs=14, sub_fs=10):
    x, y = xy
    patch = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.03,rounding_size=0.14',
                           linewidth=1.8, edgecolor=ec, facecolor=fc)
    ax.add_patch(patch)
    ax.text(x+w/2, y+h*0.62, title, ha='center', va='center', fontsize=title_fs,
            fontweight='bold', color=NAVY)
    if subtitle:
        ax.text(x+w/2, y+h*0.30, subtitle, ha='center', va='center', fontsize=sub_fs,
                color=MUTED, wrap=True)
    return patch

# 1) Connection diagram
fig, ax = plt.subplots(figsize=(16, 10), dpi=180)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set_xlim(0, 16)
ax.set_ylim(0, 10)
ax.axis('off')
ax.text(8, 9.62, 'ESP32 DC POWER MONITOR', ha='center', va='center', fontsize=25,
        fontweight='bold', color=NAVY)
ax.text(8, 9.20, 'Conceptual wiring diagram • Low-voltage 5V DC test setup', ha='center',
        fontsize=12, color=MUTED)

# Power path row
box(ax, (0.55, 6.95), 2.55, 1.25, '5V DC SUPPLY', 'regulated source', fc='#FFF7E8', ec=GOLD, title_fs=14)
box(ax, (6.15, 6.95), 3.15, 1.25, 'INA219 MODULE', 'VIN+  |  VIN−  |  I²C', fc='#EAF4FB', ec=BLUE, title_fs=14)
box(ax, (12.75, 6.95), 2.65, 1.25, '5V DC LOAD', 'small fan / rated load', fc='#F1F8F3', ec=GREEN, title_fs=14)
ax.add_patch(FancyArrowPatch((3.10, 7.68), (6.15, 7.68), arrowstyle='-|>', mutation_scale=18,
                             linewidth=2.6, color=RED))
ax.text(4.62, 7.93, 'Supply + → VIN+', ha='center', color=RED, fontsize=10.5, fontweight='bold')
ax.add_patch(FancyArrowPatch((9.30, 7.68), (12.75, 7.68), arrowstyle='-|>', mutation_scale=18,
                             linewidth=2.6, color=RED))
ax.text(11.03, 7.93, 'VIN− → Load +', ha='center', color=RED, fontsize=10.5, fontweight='bold')
# Load return path
ax.plot([14.08, 14.08, 1.82, 1.82], [6.95, 5.95, 5.95, 6.95], color=BLACK, linewidth=2.6)
ax.add_patch(FancyArrowPatch((1.82, 6.45), (1.82, 6.95), arrowstyle='-|>', mutation_scale=15,
                             linewidth=2.6, color=BLACK))
ax.text(8.0, 5.72, 'Load − → Supply − (common 0V return)', ha='center', fontsize=10.5,
        color=BLACK, fontweight='bold')

# Controller and display
box(ax, (2.30, 2.85), 3.45, 1.35, 'ESP32 DEVKIT', 'USB-powered from laptop', fc='#EEF3FF', ec=BLUE, title_fs=15)
box(ax, (10.20, 2.85), 3.40, 1.35, '0.96-inch OLED', 'SSD1306 • I²C • usually 0x3C', fc='#F4F0FF', ec='#7655A5', title_fs=15)

# Shared I2C bus callout
box(ax, (6.05, 2.82), 3.85, 1.38, 'SHARED I²C BUS',
    'GPIO21 SDA → INA219 + OLED\nGPIO22 SCL → INA219 + OLED\nESP32 is the bus master',
    fc='#F0FAFA', ec=CYAN, title_fs=12.5, sub_fs=9.1)

# Logic supply / ground detail panel
box(ax, (0.60, 2.70), 1.30, 1.65, '3.3V', 'ESP32 → INA219 VCC\nESP32 → OLED VCC', fc='#F1F8F3', ec=GREEN, title_fs=14, sub_fs=8.6)
box(ax, (14.15, 2.70), 1.30, 1.65, 'GND', 'ESP32, INA219, OLED\nand supply negative\nshare common ground', fc='#F4F6F8', ec='#80909D', title_fs=14, sub_fs=8.4)

ax.text(8, 1.80, 'IMPORTANT', ha='center', fontsize=12, color=RED, fontweight='bold')
ax.text(8, 1.43, 'Power the ESP32 via USB during initial tests. Tie the 5V supply negative to ESP32 GND.',
        ha='center', fontsize=10.2, color=BLACK)
ax.text(8, 1.05, 'Never connect the 5V load supply to the ESP32 3V3 pin. Do not use AC mains.',
        ha='center', fontsize=10.2, color=RED)
ax.text(8, 0.55, 'Check the actual breakout labels, shunt/current rating, polarity and I²C address before powering on.',
        ha='center', fontsize=9.3, color=MUTED)
plt.tight_layout(pad=0.8)
fig.savefig(OUT/'connection-diagram.png', bbox_inches='tight', facecolor='white')
fig.savefig(OUT/'connection-diagram.svg', bbox_inches='tight', facecolor='white')
plt.close(fig)

# 2) System block diagram
fig, ax = plt.subplots(figsize=(15, 7), dpi=180)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set_xlim(0, 15)
ax.set_ylim(0, 7)
ax.axis('off')
ax.text(7.5, 6.52, 'SYSTEM BLOCK DIAGRAM', ha='center', fontsize=24, fontweight='bold', color=NAVY)
ax.text(7.5, 6.12, 'Measurement path and display/data path', ha='center', fontsize=12, color=MUTED)

box(ax, (0.45, 3.7), 2.35, 1.15, '5V DC SOURCE', 'low-voltage input', fc='#FFF7E8', ec=GOLD)
box(ax, (4.0, 3.7), 2.65, 1.15, 'INA219 SENSOR', 'bus voltage + shunt current', fc='#EAF4FB', ec=BLUE)
box(ax, (8.0, 3.7), 2.35, 1.15, 'ESP32', 'reads and processes data', fc='#EEF3FF', ec=BLUE)
box(ax, (11.65, 4.55), 2.75, 1.05, 'OLED DISPLAY', 'voltage • current • power', fc='#F4F0FF', ec='#7655A5')
box(ax, (11.65, 2.60), 2.75, 1.05, 'SERIAL MONITOR', 'debugging / laptop output', fc='#F1F8F3', ec=GREEN)
box(ax, (4.0, 1.35), 2.65, 1.05, 'DC LOAD', 'small 5V fan / test load', fc='#F1F8F3', ec=GREEN)

# Power path arrows
ax.add_patch(FancyArrowPatch((2.8, 4.28), (4.0, 4.28), arrowstyle='-|>', mutation_scale=18, color=RED, linewidth=2.6))
ax.add_patch(FancyArrowPatch((5.33, 3.7), (5.33, 2.4), arrowstyle='-|>', mutation_scale=18, color=RED, linewidth=2.6))
ax.text(3.38, 4.58, 'DC +', ha='center', fontsize=10, color=RED, fontweight='bold')
ax.text(5.58, 2.98, 'measured load path', ha='left', fontsize=9.5, color=RED, rotation=90, va='center')
# I2C sensor to ESP
ax.add_patch(FancyArrowPatch((6.65, 4.25), (8.0, 4.25), arrowstyle='<|-|>', mutation_scale=18, color=CYAN, linewidth=2.5))
ax.text(7.33, 4.56, 'I²C', ha='center', fontsize=10, color=CYAN, fontweight='bold')
# ESP to displays
ax.add_patch(FancyArrowPatch((10.35, 4.35), (11.65, 5.0), arrowstyle='-|>', mutation_scale=18, color='#7655A5', linewidth=2.5))
ax.add_patch(FancyArrowPatch((10.35, 4.0), (11.65, 3.15), arrowstyle='-|>', mutation_scale=18, color=GREEN, linewidth=2.5))
ax.text(7.5, 0.65, 'Power calculation:  P (W) = V (V) × I (A)', ha='center', fontsize=16, fontweight='bold', color=NAVY)
ax.text(7.5, 0.25, 'OLED shows live readings; Serial Monitor provides a second output for testing.', ha='center', fontsize=10, color=MUTED)
plt.tight_layout(pad=0.8)
fig.savefig(OUT/'system-block-diagram.png', bbox_inches='tight', facecolor='white')
fig.savefig(OUT/'system-block-diagram.svg', bbox_inches='tight', facecolor='white')
plt.close(fig)

print('Created diagrams:', *[p.name for p in OUT.iterdir()])
