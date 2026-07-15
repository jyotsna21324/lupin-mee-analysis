import pandas as pd

df = pd.read_csv('../data/cleaned_mee_data.csv')

def evaporation_load(row):
    return row['FEED_RATE_kLhr']*1000 - row['PRODUCT_RATE_kghr']

def steam_economy(row):
    return evaporation_load(row) / row['STEAM_FLOW_kghr']

def concentration_factor(row):
    return row['PRODUCT_CONC_PCT'] / row['FEED_CONC_PCT']

def condensate_recovery_ratio(row):
    return (row['CONDENSATE_RATE_kLhr']*1000) / row['STEAM_FLOW_kghr']

def cw_delta_t(row, in_col='CW_IN_C', out_col='CW_OUT_C'):
    return row[out_col] - row[in_col]

kpi = pd.DataFrame({
    'DATE': df['DATE'],
    'EVAPORATION_LOAD_kghr': df.apply(evaporation_load, axis=1),
    'STEAM_ECONOMY': df.apply(steam_economy, axis=1),
    'CONCENTRATION_FACTOR': df.apply(concentration_factor, axis=1),
    'CONDENSATE_RECOVERY_RATIO': df.apply(condensate_recovery_ratio, axis=1),
    'CW_DELTA_T': df.apply(cw_delta_t, axis=1),
    'ANOMALY_FLAG': df['ANOMALY_FLAG']
})

reliable = kpi[kpi['ANOMALY_FLAG'] == 'OK']
benchmark_economy = 4.0
avg_reliable_economy = reliable['STEAM_ECONOMY'].mean()
gap_pct = ((benchmark_economy - avg_reliable_economy) / benchmark_economy) * 100

kpi.to_csv('../data/kpi_summary.csv', index=False)

print(kpi)
print('Average steam economy (reliable readings only):', round(avg_reliable_economy, 2))
print('Gap vs theoretical 4-effect benchmark:', round(gap_pct, 2), '%')
