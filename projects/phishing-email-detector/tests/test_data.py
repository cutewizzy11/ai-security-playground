from projects.phishing_email_detector.src.data import load_example_dataset


def test_load_example_dataset_shape():
    df = load_example_dataset()
    assert "text" in df.columns
    assert "label" in df.columns
    assert len(df) >= 1
