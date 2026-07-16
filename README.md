# Lupin MEE Energy & Steam Efficiency Analysis

Analysis of shift-log data from a Multiple Effect Evaporator (MEE) system at Lupin Pharmaceuticals, Bhopal, collected during a process engineering internship (May 2026). The project applies Python and SQL to compute process efficiency KPIs and flag instrumentation anomalies from raw shift-log readings.

## Objective

Convert raw plant instrumentation readings (temperature, vacuum, steam flow, feed/product rates) into actionable process performance metrics — steam economy, concentration factor, and condensate recovery — and validate them against theoretical benchmarks for a 4-effect evaporator system.

## Data Source

Manually logged shift data from plant DCS/field instruments across 3 operating days, covering:
- Effect-wise temperature and vacuum readings (VS-01 to VS-04, RP-02 to RP-04)
- Cooling water inlet/outlet temperatures
- Steam pressure, flow, and totalizer readings
- Feed rate, condensate rate, product rate
- Feed and product concentration (%)

## Repository Structure

```
├── data/
│   ├── LUPIN_DATASET_original.xlsx     Raw shift-log data
│   ├── cleaned_mee_data.csv            Cleaned dataset with anomaly flags
│   ├── kpi_summary.csv                 Calculated KPIs
│   └── powerbi_ready_data.xlsx         Formatted for Power BI import
├── scripts/
│   ├── 01_data_cleaning.py             Load, clean, flag anomalies
│   ├── 02_kpi_calculations.py          Steam economy, concentration factor, condensate recovery
│   ├── 03_vacuum_profile_chart.py      Effect-wise vacuum profile
│   ├── 04_steam_economy_chart.py       Steam economy by day
│   └── 05_concentration_trend_chart.py Feed vs product concentration
├── sql/
│   ├── mee_analysis.sql                Query set for the same analysis in SQL
│   └── mee_database.db                 SQLite database of the cleaned dataset
└── visuals/
    ├── vacuum_profile.png
    ├── steam_economy.png
    └── concentration_trend.png
```

## Tools Used

Python (pandas, matplotlib, numpy), SQL

## Key Findings

- Steam flow reading on Day 1 (132 kg/hr) is inconsistent with Days 2–3 (1318–1700 kg/hr), producing an implausible steam economy of ~56. Flagged as a likely instrumentation/logging error rather than averaged in blindly.
- Excluding the flagged reading, average steam economy across reliable readings is **~5.0 kg vapor/kg steam**, with Day 3 (4.35) closest to the theoretical maximum of 4.0 for a 4-effect evaporator.
- Concentration factor (product % / feed %) is consistent across all three days (8.5–8.8x), indicating stable process control despite the steam flow anomaly.


