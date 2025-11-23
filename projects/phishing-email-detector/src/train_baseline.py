"""Baseline phishing email detector training script.

This script is intentionally simple. It shows one way to:
- Load a small dataset
- Split into train/test
- Train a classical ML model
- Print basic metrics

Contributors can extend or replace this with more advanced approaches.
"""

from typing import Optional

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline

from data import load_example_dataset


def train_baseline(test_size: float = 0.3, random_state: int = 42) -> None:
    df = load_example_dataset()

    X_train, X_test, y_train, y_test = train_test_split(
        df["text"],
        df["label"],
        test_size=test_size,
        random_state=random_state,
        stratify=df["label"],
    )

    model = make_pipeline(
        CountVectorizer(),
        LogisticRegression(max_iter=1000),
    )

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("Test texts:", list(X_test))
    print("True labels:", list(y_test))
    print("Predicted labels:", list(y_pred))
    print()
    print(classification_report(y_test, y_pred, zero_division=0))


if __name__ == "__main__":
    train_baseline()
