"""§8.3: no test-set ids (or groups, when group-splitting) appear in train/val."""
from __future__ import annotations

import pandas as pd
import pytest

from src.models.split import make_split
from src.utils import load_config, split_path
from tests.conftest import synthetic_master


def _assert_disjoint(s: pd.DataFrame, col: str):
    test = set(s.loc[s["split"] == "test", col])
    other = set(s.loc[s["split"] != "test", col])
    assert not (test & other), f"{len(test & other)} {col} values leak between test and train/val"


def test_synthetic_split_is_disjoint_and_grouped(synth_cfg):
    synth_cfg(group_col="place_id")
    cfg = load_config()
    df = synthetic_master()
    s = make_split(df, cfg).merge(df[["id", "place_id"]], on="id")
    _assert_disjoint(s, "id")
    _assert_disjoint(s, "place_id")
    assert set(s["split"]) == {"train", "val", "test"}


def test_split_is_deterministic(synth_cfg):
    synth_cfg()
    cfg = load_config()
    df = synthetic_master()
    pd.testing.assert_frame_equal(make_split(df, cfg), make_split(df, cfg))


def test_project_split_has_no_leakage():
    cfg = load_config()
    p = split_path(cfg)
    if not p.exists():
        pytest.skip("no data/processed/split_ids.parquet yet (run `run.py split`)")
    s = pd.read_parquet(p)
    _assert_disjoint(s, cfg["task"]["id_col"])
    g = cfg["split"].get("group_col")
    if g:
        master = pd.read_parquet(cfg["features"]["master_table"], columns=[cfg["task"]["id_col"], g])
        _assert_disjoint(s.merge(master, on=cfg["task"]["id_col"]), g)
