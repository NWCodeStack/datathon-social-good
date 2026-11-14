"""Model + baseline factories. Every pipeline uses the same preprocessing so comparisons are fair."""
from __future__ import annotations

from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier, DummyRegressor
from sklearn.ensemble import (HistGradientBoostingClassifier, HistGradientBoostingRegressor,
                              RandomForestClassifier, RandomForestRegressor)
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def preprocessor(num_cols: list[str], cat_cols: list[str]) -> ColumnTransformer:
    return ColumnTransformer([
        ("num", make_pipeline(SimpleImputer(strategy="median"), StandardScaler()), num_cols),
        ("cat", make_pipeline(SimpleImputer(strategy="most_frequent"),
                              OneHotEncoder(handle_unknown="ignore", min_frequency=5)), cat_cols),
    ])


def estimator(name: str, task: str, seed: int, params: dict | None = None):
    params = params or {}
    clf = task == "classification"
    table = {
        "dummy": (lambda: DummyClassifier(strategy="most_frequent")) if clf else (lambda: DummyRegressor()),
        "linear": (lambda: LogisticRegression(max_iter=2000, class_weight="balanced"))
                  if clf else (lambda: LinearRegression()),
        "logistic": lambda: LogisticRegression(max_iter=2000, random_state=seed, **params),
        "ridge": lambda: Ridge(random_state=seed, **params),
        "hist_gb": (lambda: HistGradientBoostingClassifier(random_state=seed, **params)) if clf
                   else (lambda: HistGradientBoostingRegressor(random_state=seed, **params)),
        "random_forest": (lambda: RandomForestClassifier(random_state=seed, n_jobs=-1, **params)) if clf
                         else (lambda: RandomForestRegressor(random_state=seed, n_jobs=-1, **params)),
    }
    if name not in table:
        raise ValueError(f"unknown model {name!r}; options: {sorted(table)}")
    return table[name]()


def build_pipeline(name: str, cfg: dict, num_cols: list[str], cat_cols: list[str]) -> Pipeline:
    t = cfg["task"]
    params = cfg["model"].get("params") if name == cfg["model"]["name"] else None
    return Pipeline([("prep", preprocessor(num_cols, cat_cols)),
                     ("est", estimator(name, t["type"], cfg["seed"], params))])
