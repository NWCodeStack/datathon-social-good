"""Builds the master analytic table from data/interim/*.parquet.

Not implemented yet: Model 1's feature table plugs in here.
Contract: return ONE row per prediction unit with columns
  config.task.id_col (unique), config.task.target_col, features, and config.task.subgroup_cols.
Use audited_merge for every join.
"""
from __future__ import annotations

import pandas as pd

from src.features.joins import audited_merge  # noqa: F401  (use for every join)


def build(cfg: dict) -> pd.DataFrame:
    raise NotImplementedError(
        "build_features.build() not implemented yet. "
        "Load data/interim/*.parquet here, join with audited_merge, and return the master table."
    )
