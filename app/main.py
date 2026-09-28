from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.schema import (
    CarFeatures,
    PredictionResponse
)

from app.model import (
    predict_price,
    load_artifacts
)


app = FastAPI(
    title="Car Price Prediction API",
    description="Machine Learning API for predicting used car prices.",
    version="1.0"
)


# ---------------------------------------------------------
# Startup
# ---------------------------------------------------------

@app.on_event("startup")
def startup_event():

    load_artifacts()


# ---------------------------------------------------------
# Root route
# ---------------------------------------------------------

@app.get("/")
def test():

    return JSONResponse(
        status_code=200,
        content={
            "success": True,
            "message": "Car Price Prediction API is running!"
        }
    )


# ---------------------------------------------------------
# Health check
# ---------------------------------------------------------

@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "model_loaded": True
    }


# ---------------------------------------------------------
# Prediction endpoint
# ---------------------------------------------------------

@app.post(
    "/predict",
    response_model=PredictionResponse
)
def predict(
    features: CarFeatures
):

    price = predict_price(
        features.model_dump()
    )

    return PredictionResponse(
        prediction_price=round(price, 2)
    )