from pathlib import Path
from typing import Tuple

import pandas as pd


def load_example_dataset() -> pd.DataFrame:
    """Load a tiny built-in example dataset.

    This is just a placeholder to show structure.
    Contributors are encouraged to replace this with
    a real phishing dataset loader or a downloader.
    """

    data = {
        "text": [
            "Hey, are we still meeting for lunch today?",
            "URGENT: Your account has been compromised, click here to reset your password now!",
            "Reminder: your package will be delivered tomorrow.",
            "Congratulations, you have won a free prize, click this link!",
        ],
        "label": [0, 1, 0, 1],
    }
    return pd.DataFrame(data)


def load_csv(path: Path) -> pd.DataFrame:
    """Load a CSV with `text` and `label` columns.

    Parameters
    ----------
    path: Path
        Path to a CSV file. Must contain `text` and `label` columns.
    """

    df = pd.read_csv(path)
    if "text" not in df.columns or "label" not in df.columns:
        raise ValueError("CSV must contain 'text' and 'label' columns")
    return df
