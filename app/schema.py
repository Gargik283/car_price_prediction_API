from pydantic import BaseModel, Field
from enum import Enum


class SellerType(str, Enum):
    dealer = "Dealer"
    individual = "Individual"


class FuelType(str, Enum):
    petrol = "Petrol"
    diesel = "Diesel"
    cng = "CNG"
    lpg = "LPG"
    electric = "Electric"


class TransmissionType(str, Enum):
    manual = "Manual"
    automatic = "Automatic"


class CarFeatures(BaseModel):
    car_name: str = Field(..., example="Maruti Alto")
    brand: str = Field(..., example="Maruti")
    model: str = Field(..., example="Alto")

    vehicle_age: int = Field(..., ge=0, example=5)
    km_driven: int = Field(..., ge=0, example=50000)

    seller_type: SellerType
    fuel_type: FuelType
    transmission_type: TransmissionType

    mileage: float = Field(..., gt=0, example=19.7)
    engine: int = Field(..., gt=0, example=796)
    max_power: float = Field(..., gt=0, example=46.3)
    seats: int = Field(..., gt=0, example=5)


class PredictionResponse(BaseModel):
    prediction_price: float