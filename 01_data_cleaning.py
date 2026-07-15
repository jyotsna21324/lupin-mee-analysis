import pandas as pd
import numpy as np
import sqlite3

COLS = ['DATE','SET_TEMP_C','TIC_507_C','TI_508_C','VS01_C','RP02_C','VS02_C',
        'RP03_C','VS03_C','RP04_C','VS04_C','CW_IN_C','CW_OUT_C','TVR_mmHg',
        'VAC_VS01_mmHg','VAC_VS02_mmHg','VAC_VS03_mmHg','VAC_VS04_mmHg',
        'VT04_OVERALL_VACUUM_mmHg','STEAM_PRESSURE_kgcm2','STEAM_FLOW_kghr',
        'STEAM_TOTALIZER_kghr','FEED_RATE_kLhr','CONDENSATE_RATE_kLhr',
        'PRODUCT_RATE_kghr','FEED_CONC_PCT','PRODUCT_CONC_PCT']

def load_raw(path):
    raw = pd.read_excel(path, header=None, skiprows=5, nrows=3)
    raw.columns = COLS
    return raw

def flag_anomalies(df):
    df = df.copy()
    econ_est = (df['FEED_RATE_kLhr']*1000 - df['PRODUCT_RATE_kghr']) / df['STEAM_FLOW_kghr']
    df['STEAM_ECONOMY_RAW'] = econ_est
    df['ANOMALY_FLAG'] = np.where((econ_est > 10) | (econ_est < 1), 'CHECK_INSTRUMENT', 'OK')
    return df

def build_clean_dataset(path):
    df = load_raw(path)
    df = flag_anomalies(df)
    numeric_cols = [c for c in df.columns if c not in ('DATE','ANOMALY_FLAG')]
    for c in numeric_cols:
        df[c] = pd.to_numeric(df[c], errors='coerce')
    return df

def export(df, csv_path, db_path):
    df.to_csv(csv_path, index=False)
    conn = sqlite3.connect(db_path)
    df.to_sql('mee_readings', conn, if_exists='replace', index=False)
    conn.close()

if __name__ == '__main__':
    clean = build_clean_dataset('../data/LUPIN_DATASET_original.xlsx')
    export(clean, '../data/cleaned_mee_data.csv', '../sql/mee_database.db')
    print(clean)
