"""Integration checks for the Advanced Track requirements. Prints PASS / FAIL / MANUAL per item and writes
outputs/check_report.md. `run.py check` runs `all` + pytest first, so item 1-3 reflect that run."""
from __future__ import annotations

import sys

import pandas as pd

from src.utils import ROOT, load_config, split_path


def check(cfg) -> list[tuple[str, str, str]]:
    T = cfg["paths"]["tables"]
    R = []

    def tbl(name):
        p = T / name
        return pd.read_csv(p) if p.exists() else None

    # 1. make all (this process only runs after `all` succeeded in run.py check)
    master = cfg["features"]["master_table"]
    R.append(("1 make all end-to-end", "PASS" if master.exists() else "FAIL",
              "pipeline ran in this checkout; run `python run.py clean-clone-check` for a true clean clone"))

    # 2. schemas — covered by pytest tests/test_schemas.py (run.py check aborts if it fails)
    n_interim = len(list(cfg["paths"]["interim"].glob("*.parquet")))
    R.append(("2 schema tests", "PASS" if n_interim else "FAIL",
              f"{n_interim} interim parquet(s) validated by tests/test_schemas.py"))

    # 3. leakage
    sp = split_path(cfg)
    if sp.exists():
        s = pd.read_parquet(sp)
        idc = cfg["task"]["id_col"]
        test_ids = set(s.loc[s.split == "test", idc])
        overlap = test_ids & set(s.loc[s.split != "test", idc])
        R.append(("3 no test leakage", "FAIL" if overlap else "PASS", f"{len(overlap)} overlapping ids"))
    else:
        R.append(("3 no test leakage", "FAIL", "no split_ids.parquet"))

    # 4. baseline + test metrics
    mvb = tbl("03_model_vs_baseline.csv")
    if mvb is None:
        R.append(("4 baseline + test metrics", "FAIL", "03 missing"))
    else:
        has_base = (mvb["role"] == "baseline").any()
        on_test = (mvb["test"].astype(str) != "LOCKED").all()
        status = "PASS" if has_base and on_test else "FAIL"
        R.append(("4 baseline + test metrics", status,
                  f"baseline rows: {has_base}; test metrics: {'yes' if on_test else 'LOCKED (run `run.py final` once)'}"))

    # 5. subgroups + failures
    sg, fe = tbl("04_subgroup_performance.csv"), tbl("05_failure_examples.csv")
    n_groups = 0 if sg is None else len(sg)
    n_fail = 0 if fe is None else len(fe)
    R.append(("5 >=3 subgroups + failure examples", "PASS" if n_groups >= 3 and n_fail > 0 else "FAIL",
              f"{n_groups} subgroup rows, {n_fail} failure examples"))

    # 6. data decisions: documented in each analysis write-up; hand-check results in 06
    hc = tbl("06_hand_check_sample.csv")
    n_hc = 0 if hc is None else len(hc)
    R.append(("6 data decisions + hand-check", "PASS" if n_hc else "MANUAL",
              f"{n_hc} hand-check(s) in 06_hand_check_sample.csv; data decisions live in each analysis write-up"))

    # 7. README verified by a human
    R.append(("7 README repro verified", "MANUAL", "follow README from a fresh clone on a teammate's laptop"))

    # 8. slide numbers vs 07 (the deck lives in Google Slides, outside the repo)
    kf = tbl("07_key_findings.csv")
    R.append(("8 slide numbers match 07", "MANUAL",
              f"compare the deck's numbers with 07_key_findings.csv ({0 if kf is None else len(kf)} findings)"))

    return R


def main() -> None:
    cfg = load_config()
    rows = check(cfg)
    lines = ["| check | status | detail |", "|---|---|---|"] + [f"| {a} | {b} | {c} |" for a, b, c in rows]
    report = "\n".join(lines)
    print(report)
    (ROOT / "outputs" / "check_report.md").write_text("# Integration check report\n\n" + report + "\n",
                                                      encoding="utf-8")
    if any(s == "FAIL" for _, s, _ in rows):
        sys.exit(1)


if __name__ == "__main__":
    main()
