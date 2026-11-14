"""Step `split`: THE one train/val/test split (CLAUDE.md §5). Fixed seed; saved to
data/processed/split_ids.parquet with columns [<id_col>, split]. Optional group split
(config split.group_col) keeps every row of a group in a single split to prevent leakage.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.model_selection import GroupShuffleSplit, train_test_split

from src.utils import load_config, split_path


def make_split(df: pd.DataFrame, cfg: dict) -> pd.DataFrame:
    t, s, seed = cfg["task"], cfg["split"], cfg["seed"]
    ids = df[t["id_col"]].to_numpy()
    test_size, val_size = s["test_size"], s["val_size"]
    val_frac_of_rest = val_size / (1 - test_size)
    idx = np.arange(len(df))

    if s.get("group_col"):
        groups = df[s["group_col"]].to_numpy()
        gss = GroupShuffleSplit(n_splits=1, test_size=test_size, random_state=seed)
        rest_idx, test_idx = next(gss.split(idx, groups=groups))
        gss2 = GroupShuffleSplit(n_splits=1, test_size=val_frac_of_rest, random_state=seed)
        tr, va = next(gss2.split(rest_idx, groups=groups[rest_idx]))
        train_idx, val_idx = rest_idx[tr], rest_idx[va]
    else:
        y = df[t["target_col"]].to_numpy()
        strat = t["type"] == "classification" and s.get("stratify", True)
        rest_idx, test_idx = train_test_split(idx, test_size=test_size, random_state=seed,
                                              stratify=y if strat else None)
        train_idx, val_idx = train_test_split(rest_idx, test_size=val_frac_of_rest, random_state=seed,
                                              stratify=y[rest_idx] if strat else None)

    split = np.empty(len(df), dtype=object)
    split[train_idx], split[val_idx], split[test_idx] = "train", "val", "test"
    return pd.DataFrame({t["id_col"]: ids, "split": split})


def main() -> None:
    cfg = load_config()
    df = pd.read_parquet(cfg["features"]["master_table"])
    out = make_split(df, cfg)
    out.to_parquet(split_path(cfg), index=False)
    print("split sizes:", out["split"].value_counts().to_dict())


if __name__ == "__main__":
    main()
