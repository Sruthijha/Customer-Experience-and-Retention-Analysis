"""Modeling helpers for the customer retention analysis project."""

from __future__ import annotations

RANDOM_STATE = 42


def model_summary_template() -> dict:
    """Return a template for model reporting."""
    return {
        "model_name": None,
        "train_size": None,
        "test_size": None,
        "roc_auc": None,
        "pr_auc": None,
        "precision": None,
        "recall": None,
        "f1": None,
        "notes": "Interpret with caution because the data are observational.",
    }
