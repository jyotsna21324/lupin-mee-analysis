import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
df = pd.read_csv(BASE_DIR / 'cleaned_mee_data.csv')
x = np.arange(len(df))
width = 0.35

fig, ax = plt.subplots(figsize=(7, 5))
ax.bar(x - width / 2, df['FEED_CONC_PCT'], width, label='Feed Conc %')
ax.bar(x + width / 2, df['PRODUCT_CONC_PCT'], width, label='Product Conc %')

ax.set_xticks(x)
ax.set_xticklabels(df['DATE'])
ax.set_ylabel('Concentration (%)')
ax.set_title('Feed vs Product Concentration')
ax.legend()
plt.tight_layout()
plt.savefig(BASE_DIR / 'concentration_trend.png', dpi=200)
