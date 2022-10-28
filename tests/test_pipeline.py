from sklearn.pipeline import Pipeline
from src.preprocess.transformers import RainfallInitialPreprocess

def test_rainfall_initial_preprocess(rainfall_data):
    pipeline = Pipeline(
        [
            ('RainfallInitialPreprocess', RainfallInitialPreprocess())
        ]
    )

    transformed = pipeline.transoform(rainfall_data)
    head = transform.head(1)
    tail = transform.tail(1)

    assert 'mes' in transformed.columns
    assert 'ano' in transformed.columns
    assert head.date.item() < tail.date.item()

    