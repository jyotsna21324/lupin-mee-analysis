import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
kpi = pd.read_csv(BASE_DIR / 'kpi_summary.csv')
colors = ['#d62728' if flag == 'CHECK_INSTRUMENT' else '#2ca02c' for flag in kpi['ANOMALY_FLAG']]

fig, ax = plt.subplots(figsize=(7, 5))
bars = ax.bar(kpi['DATE'], kpi['STEAM_ECONOMY'], color=colors)
ax.axhline(4.0, color='black', linestyle='--', linewidth=1, label='Theoretical benchmark (4-effect)')

for bar, value in zip(bars, kpi['STEAM_ECONOMY']):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5, round(value, 2), ha='center')

ax.set_ylabel('Steam Economy (kg vapor / kg steam)')
ax.set_title('Steam Economy by Day (Red = Flagged Anomaly)')
ax.legend()
plt.tight_layout()
plt.savefig(BASE_DIR / 'steam_economy.png', dpi=200)
