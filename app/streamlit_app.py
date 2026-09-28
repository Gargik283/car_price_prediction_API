import streamlit as st
import requests
import os

# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="centered"
)


# ---------------------------------------------------------
# Title
# ---------------------------------------------------------

st.title("🚗 Car Price Prediction")

st.write(
    "Enter the car details below to predict its estimated selling price."
)


# ---------------------------------------------------------
# API URL
# ---------------------------------------------------------

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/predict")

# ---------------------------------------------------------
# Input fields
# ---------------------------------------------------------

car_name = st.text_input(
    "Car Name",
    value="Maruti Alto"
)

brand = st.text_input(
    "Brand",
    value="Maruti"
)

model = st.text_input(
    "Model",
    value="Alto"
)


vehicle_age = st.number_input(
    "Vehicle Age (years)",
    min_value=0,
    max_value=50,
    value=5,
    step=1
)


km_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    max_value=1000000,
    value=50000,
    step=1000
)


seller_type = st.selectbox(
    "Seller Type",
    [
        "Dealer",
        "Individual"
    ]
)


fuel_type = st.selectbox(
    "Fuel Type",
    [
        "Petrol",
        "Diesel",
        "CNG",
        "LPG",
        "Electric"
    ]
)


transmission_type = st.selectbox(
    "Transmission",
    [
        "Manual",
        "Automatic"
    ]
)


mileage = st.number_input(
    "Mileage (km/l)",
    min_value=1.0,
    max_value=100.0,
    value=19.7,
    step=0.1
)


engine = st.number_input(
    "Engine (cc)",
    min_value=1,
    max_value=10000,
    value=1197,
    step=1
)


max_power = st.number_input(
    "Max Power (bhp)",
    min_value=1.0,
    max_value=2000.0,
    value=82.0,
    step=0.1
)


seats = st.number_input(
    "Number of Seats",
    min_value=1,
    max_value=20,
    value=5,
    step=1
)


# ---------------------------------------------------------
# Prediction button
# ---------------------------------------------------------

if st.button(
    "Predict Car Price",
    use_container_width=True
):

    data = {

        "car_name": car_name,

        "brand": brand,

        "model": model,

        "vehicle_age": vehicle_age,

        "km_driven": km_driven,

        "seller_type": seller_type,

        "fuel_type": fuel_type,

        "transmission_type": transmission_type,

        "mileage": mileage,

        "engine": engine,

        "max_power": max_power,

        "seats": seats
    }


    try:

        response = requests.post(
            API_URL,
            json=data,
            timeout=60
        )


        if response.status_code == 200:

            result = response.json()

            predicted_price = result[
                "prediction_price"
            ]


            st.success(
                "Prediction generated successfully!"
            )


            st.metric(
                "Estimated Selling Price",
                f"₹{predicted_price:,.0f}"
            )


        else:

            st.error(
                f"API Error: {response.text}"
            )


    except requests.exceptions.ConnectionError:

        st.error(
            "Could not connect to the FastAPI server. "
            "Please start FastAPI first."
        )


    except requests.exceptions.Timeout:

        st.error(
            "The API request timed out."
        )


    except Exception as e:

        st.error(
            f"Something went wrong: {e}"
        )
