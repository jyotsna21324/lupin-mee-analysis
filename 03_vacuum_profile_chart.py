import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/cleaned_mee_data.csv')
effects = ['VAC_VS01_mmHg','VAC_VS02_mmHg','VAC_VS03_mmHg','VAC_VS04_mmHg']
labels = ['Effect 1','Effect 2','Effect 3','Effect 4']

fig, ax = plt.subplots(figsize=(8,5))
for i, row in df.iterrows():
    values = [row[c] for c in effects]
    ax.plot(labels, values, marker='o', linewidth=2, label=row['DATE'])

ax.set_ylabel('Vacuum (mmHg)')
ax.set_xlabel('Evaporator Effect')
ax.set_title('Effect-wise Vacuum Profile')
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('../visuals/vacuum_profile.png', dpi=200)
