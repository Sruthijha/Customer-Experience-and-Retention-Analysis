"""Statistical test helpers for the customer retention analysis project."""

from __future__ import annotations

RANDOM_STATE = 42


def explain_test_choice(test_name: str, context: str) -> str:
    """Return a brief plain-language explanation for a statistical test."""
    if test_name == "chi_square":
        return f"Use a chi-square test for {context} because the outcome is categorical and we compare observed counts across groups."
    if test_name == "welch_t":
        return f"Use Welch's t-test for {context} because the means are compared across groups without assuming equal variances."
    if test_name == "mann_whitney":
        return f"Use the Mann-Whitney U test for {context} when the outcome is ordinal or the distribution is not approximately normal."
    return f"Use {test_name} to evaluate {context} in a consistent, reproducible way."
