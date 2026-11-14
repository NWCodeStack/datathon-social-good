# ⚠️ Project name — 8th Annual Datathon for Social Good

**Pitch (one paragraph):** ⚠️ TODO — cause, who is affected, what we predict, why it helps.

**Results summary:** ⚠️ TODO — filled from `outputs/tables/07_key_findings.csv` after final eval.

Advanced Track evidence: [docs/checklist.md](docs/checklist.md) · Ethics: [docs/ethics.md](docs/ethics.md) ·
Data decisions: [docs/data_decisions.md](docs/data_decisions.md)

## Reproduce

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
# put the shared-drive dataset folders in data/raw/ (read-only; never edited)
make all          # or: python run.py all
make final        # ONCE, after features are frozen: test-set predictions + final tables
make check        # integration checks -> outputs/check_report.md
```

| step | command | writes |
|---|---|---|
| data | `run.py data` | `data/interim/*.parquet`, `01_dataset_summary.csv` |
| features | `run.py features` | `data/processed/master.parquet`, `02_join_audit.csv` |
| split | `run.py split` | `data/processed/split_ids.parquet` (seeded, once) |
| train | `run.py train` | `outputs/models/*.joblib` + metadata json |
| predict | `run.py predict` | val predictions (test only when `final_eval` / `run.py final`) |
| eval | `run.py eval` | `03_model_vs_baseline`, `04_subgroup_performance`, `05_failure_examples` |
| tables | `run.py tables` | `06_hand_check_sample`, `07_key_findings` |
| figures | `run.py figures` | `outputs/figures/*.png/svg` |

No `make` on Windows? Every target works as `python run.py <target>`.

## How to plug in your part (teammates)
1. **Cleaner**: copy `src/data/clean_TEMPLATE.py` to `clean_<name>.py`, add `<name>` to
   `config.yaml: datasets`, and ask the Integrator to add its schema to `src/data/schemas.py`.
2. **Features**: implement `build()` in `src/features/build_features.py`; use
   `src.features.joins.audited_merge` for every join.
3. **Task**: set `task.*` (target, id, subgroup columns) and `split.group_col` in `config.yaml`.
4. **Hand checks**: drop `docs/hand_checks/<name>.csv` (`item_id, auto_value, checked_value, checker`).
5. Notebooks go in `notebooks/NN_owner_topic.ipynb`, outputs stripped. Reported numbers must come from `run.py`.

## Repo layout
See `CLAUDE.md` §4.
