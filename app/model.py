import os
import joblib
import pandas as pd


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "random_forest_models.pkl"
)

FEATURE_PATH = os.path.join(
    BASE_DIR,
    "feature_columns.pkl"
)


model = None
feature_columns = None


def load_artifacts():

    global model
    global feature_columns

    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model file not found: {MODEL_PATH}"
        )

    if not os.path.exists(FEATURE_PATH):
        raise FileNotFoundError(
            f"Feature file not found: {FEATURE_PATH}"
        )

    model = joblib.load(MODEL_PATH)

    feature_columns = joblib.load(
        FEATURE_PATH
    )

    print("Model loaded successfully!")
    print("Feature columns loaded successfully!")


def predict_price(features):

    global model
    global feature_columns

    if model is None or feature_columns is None:
        load_artifacts()

    # Convert input dictionary to DataFrame
    input_data = pd.DataFrame(
        [features]
    )

    # Make sure columns are in the same order
    input_data = input_data[
        feature_columns
    ]

    # Prediction
    prediction = model.predict(
        input_data
    )[0]

    return float(prediction)