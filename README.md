# Priced Out: predicting Bay Area rent spikes

8th Annual Datathon for Social Good

Bay Area rent keeps climbing, and low-income renters can't see the next hike coming. We combine housing
costs, wages, and access to everyday services for 293 Bay Area zip codes, and train a model that
predicts which zip codes are likely to see a rent spike.

## What's in this repo

| Folder | What it holds | Write-up |
|---|---|---|
| `datathon/anna_upload/` | Access to essential services: distance from homes to groceries, pharmacies, doctors, banks, transit and food banks; access score per zip | [anna_essential_services.md](datathon/anna_upload/docs/anna_essential_services.md) |
| `housing_costs/` | Housing costs per zip: typical rent and home value, change since 2019, income needed for rent | [albert_housing_costs.md](housing_costs/docs/albert_housing_costs.md) |
| `wages_and_affordability/` | Wages and housing affordability: advertised pay by job and city compared with local rent | [wages_and_affordability.md](wages_and_affordability/docs/wages_and_affordability.md) |
| `rent-vs-reach-map/` | Interactive map of rent, jobs, service reviews and access by zip (`index.html`; data built by `scripts/build_data.py`) | |
| `src/`, `run.py`, `tests/` | One-command modeling pipeline: cleaning, logged joins, a seeded train/validation/test split, models scored next to baselines, subgroup and failure analysis | |

Each write-up documents its data sources, cleaning steps, joins, hand checks and known biases.

## Data

Provided by the datathon (most via Bright Data / The Bright Initiative): Zillow Housing listings,
Google Maps Places and Reviews, Indeed job postings. External: Zillow Research rent (ZORI) and home value
(ZHVI) indexes, BLS wage data, and Census ZIP code boundaries for the map.

Raw datathon files are not committed. Put them in `data/raw/` (read-only; never edited).

## Reproduce the pipeline

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run.py all      # or: make all
python run.py final    # run once, after features are frozen: scores the held-out test set
python run.py check    # checks -> outputs/check_report.md
```

| Step | Command | Writes |
|---|---|---|
| data | `run.py data` | `data/interim/*.parquet`, `01_dataset_summary.csv` |
| features | `run.py features` | `data/processed/master.parquet`, `02_join_audit.csv` |
| split | `run.py split` | `data/processed/split_ids.parquet` (seeded, once) |
| train | `run.py train` | `outputs/models/*.joblib` + metadata json |
| predict | `run.py predict` | validation predictions (test only in `run.py final`) |
| eval | `run.py eval` | `03_model_vs_baseline`, `04_subgroup_performance`, `05_failure_examples` |
| tables | `run.py tables` | `06_hand_check_sample`, `07_key_findings` |
| figures | `run.py figures` | `outputs/figures/*.png/svg` |

The test set is never used for training or tuning: it is predicted only by `run.py final`, and
`tests/test_leakage.py` checks that no test IDs appear in training or validation.

## Ethics

Results are reported at zip-code level only, never for individual addresses or listings. Large
landlords already price with commercial software, so the larger risk is that a public list of likely
spikes draws investors, and wrong predictions either leave renters unprepared or stigmatize a
neighborhood. Areas with thin data are shown as having no data rather than estimated. Each write-up
lists its own known biases.
