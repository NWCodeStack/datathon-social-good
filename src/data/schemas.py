"""Data contract: expected schema of every data/interim/<name>.parquet.

Each cleaner's output must match its SCHEMA here (tests/test_schemas.py).
dtype strings are pandas dtype *kinds*: "int", "float", "string", "bool", "datetime", "category".
Document every entry in the dataset's write-up (name, dtype, meaning, null handling).

Example (adapt once datasets are chosen):

SCHEMAS["places"] = {
    "place_id": {"dtype": "string", "nullable": False, "unique": True},
    "name":     {"dtype": "string", "nullable": True},
    "category": {"dtype": "string", "nullable": False},
    "lat":      {"dtype": "float",  "nullable": False},
    "lon":      {"dtype": "float",  "nullable": False},
    "zip":      {"dtype": "string", "nullable": True},
}
"""
from __future__ import annotations

SCHEMAS: dict[str, dict[str, dict]] = {}
