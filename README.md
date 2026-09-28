# 🚗 Car Price Prediction API

A machine learning project that predicts the selling price of used cars using a Random Forest Regressor trained on a CarDekho dataset.

The project provides a FastAPI REST API for predictions and a Streamlit web interface for user-friendly interaction.

---
## 🔗 Live Demo

| Component | Link |
|-----------|------|
| 🖥️ Streamlit App | https://carpricepredictionapi-nveywf4w8c9woudaooyh97.streamlit.app/ |
| ⚙️ FastAPI Backend (Render) | https://car-price-prediction-api-9wpe.onrender.com |
| 📄 API Docs (Swagger) | https://car-price-prediction-api-9wpe.onrender.com/docs |

- ⏳ The backend runs on Render's free tier, so the first request after inactivity can take 30–60 seconds while it wakes up.

--- 
## 📌 Features

- Used-car price prediction using Machine Learning
- Random Forest Regression
- Categorical feature encoding with One-Hot Encoding
- FastAPI REST API
- Swagger API documentation
- Streamlit prediction interface
- Input validation using Pydantic
- Saved ML model using Joblib

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Pydantic
- Streamlit
- Joblib

---

## 📂 Project Structure

```text
car_price_api/
│
├── app/
│   ├── main.py
│   ├── model.py
│   ├── schema.py
│   └── streamlit_app.py
│
├── cardekho_dataset.csv
├── feature_columns.pkl
├── random_forest_models.pkl
├── train.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📊 Dataset

The model uses a CarDekho used-car dataset containing features such as:

- Car Name
- Brand
- Model
- Vehicle Age
- Kilometers Driven
- Seller Type
- Fuel Type
- Transmission Type
- Mileage
- Engine
- Max Power
- Seats

**Target:** `selling_price`

---

## 🤖 Machine Learning Pipeline

```text
CarDekho Dataset
       ↓
Data Preprocessing
       ↓
Categorical Encoding
       ↓
Train/Test Split
       ↓
Random Forest Regressor
       ↓
Model Evaluation
       ↓
Saved Model (.pkl)
       ↓
FastAPI Prediction API
       ↓
Streamlit Interface
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Gargik283/car_price_api.git
cd car_price_api
```

### 2. Create and activate virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the model

```bash
python train.py
```

This generates:

```text
feature_columns.pkl
random_forest_models.pkl
```

### 5. Start FastAPI

```bash
uvicorn app.main:app --reload
```

API:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

### 6. Start Streamlit

Open another terminal:

```bash
streamlit run app/streamlit_app.py
```

---

## 🔮 API Endpoint

### POST `/predict`

Example request:

```json
{
  "car_name": "Maruti Alto",
  "brand": "Maruti",
  "model": "Alto",
  "vehicle_age": 5,
  "km_driven": 50000,
  "seller_type": "Dealer",
  "fuel_type": "Petrol",
  "transmission_type": "Manual",
  "mileage": 19.7,
  "engine": 1197,
  "max_power": 82.0,
  "seats": 5
}
```

Example response:

```json
{
  "prediction_price": 123456.78
}
```

---

## 📈 Model Evaluation

The model is evaluated using:

- **MAE** — Mean Absolute Error
- **RMSE** — Root Mean Squared Error
- **R² Score** — Coefficient of Determination

The evaluation metrics are printed automatically when `train.py` is executed.

---

## 👩‍💻 Author

**Gargi Kundu**

Data Science & Analytics | Python | SQL | Power BI | Machine Learning

GitHub: https://github.com/Gargik283
