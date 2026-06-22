"""
Task 15 — MLOps: Experiment Tracking with MLflow
Starter Template
Author: Mussa Khan (@musagithub1)

This file is intentionally minimal. Treat it as scaffolding — fill in
TODOs and refactor freely. The mentor team is more interested in your
*decisions* than in adherence to this template.
"""

from __future__ import annotations

import argparse
import logging
import random
from pathlib import Path

import numpy as np
import pandas as pd

# ----------------------------- Config ---------------------------------
RANDOM_SEED = 42
DATA_DIR = Path("DATASETS/raw")
FIG_DIR = Path("figures")
REPORT_DIR = Path("reports")

FIG_DIR.mkdir(exist_ok=True, parents=True)
REPORT_DIR.mkdir(exist_ok=True, parents=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger(__name__)


def set_seed(seed: int = RANDOM_SEED) -> None:
    """Set seeds for reproducibility."""
    random.seed(seed)
    np.random.seed(seed)
    # If you use torch / tensorflow, also seed them here.


# ----------------------------- Data -----------------------------------
def load_data(path: Path) -> pd.DataFrame:
    """Load raw data. TODO: implement schema validation."""
    logger.info("Loading data from %s", path)
    df = pd.read_csv(path)
    logger.info("Loaded shape=%s", df.shape)
    return df


def basic_eda(df: pd.DataFrame) -> None:
    """Print a quick sanity-check summary."""
    print("Shape:", df.shape)
    print("Dtypes:\n", df.dtypes)
    print("Missing %:\n", (df.isna().mean() * 100).round(2))
    print("Head:\n", df.head())


# ----------------------------- Modeling -------------------------------
def train_model(X: pd.DataFrame, y: pd.Series):
    """TODO: implement training logic for Task 15."""
    raise NotImplementedError("Fill me in — Task 15: MLOps: Experiment Tracking with MLflow")


def evaluate(model, X_test, y_test) -> dict:
    """TODO: return a dict of metrics relevant to this task."""
    raise NotImplementedError


# ----------------------------- Main -----------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(description="Task 15: MLOps: Experiment Tracking with MLflow")
    parser.add_argument("--data", type=Path, default=DATA_DIR / "input.csv")
    args = parser.parse_args()

    set_seed()
    df = load_data(args.data)
    basic_eda(df)
    # TODO: split, train, evaluate, save figures + report


if __name__ == "__main__":
    main()
