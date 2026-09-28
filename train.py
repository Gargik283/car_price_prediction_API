import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ---------------------------------------------------------
# 1. Load dataset
# ---------------------------------------------------------

DATA_PATH = "cardekho_dataset.csv"

df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)


# ---------------------------------------------------------
# 2. Remove unnecessary column
# ---------------------------------------------------------

if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])


# ---------------------------------------------------------
# 3. Define target and features
# ---------------------------------------------------------

TARGET = "selling_price"

X = df.drop(columns=[TARGET])
y = df[TARGET]

print("\nFeatures:")
print(X.columns.tolist())

print("\nTarget:")
print(TARGET)


# ---------------------------------------------------------
# 4. Identify categorical and numerical columns
# ---------------------------------------------------------

categorical_columns = [
    "car_name",
    "brand",
    "model",
    "seller_type",
    "fuel_type",
    "transmission_type"
]

numerical_columns = [
    "vehicle_age",
    "km_driven",
    "mileage",
    "engine",
    "max_power",
    "seats"
]


# ---------------------------------------------------------
# 5. Save feature columns
# ---------------------------------------------------------

feature_columns = X.columns.tolist()

joblib.dump(
    feature_columns,
    "feature_columns.pkl"
)

print("\nFeature columns saved successfully!")


# ---------------------------------------------------------
# 6. Train-test split
# ---------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# ---------------------------------------------------------
# 7. Preprocessing
# ---------------------------------------------------------

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        ),
        (
            "numerical",
            "passthrough",
            numerical_columns
        )
    ]
)


# ---------------------------------------------------------
# 8. Random Forest model
# ---------------------------------------------------------

random_forest = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1,
    max_features="sqrt"
)


# ---------------------------------------------------------
# 9. Create complete pipeline
# ---------------------------------------------------------

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("random_forest", random_forest)
    ]
)


# ---------------------------------------------------------
# 10. Train model
# ---------------------------------------------------------

print("\nTraining Random Forest model...")

model.fit(X_train, y_train)

print("Training completed!")


# ---------------------------------------------------------
# 11. Make predictions
# ---------------------------------------------------------

y_pred = model.predict(X_test)


# ---------------------------------------------------------
# 12. Evaluate model
# ---------------------------------------------------------

mae = mean_absolute_error(y_test, y_pred)

rmse = mean_squared_error(
    y_test,
    y_pred
) ** 0.5

r2 = r2_score(
    y_test,
    y_pred
)


print("\n-----------------------------")
print("MODEL PERFORMANCE")
print("-----------------------------")

print(f"MAE  : ₹{mae:,.2f}")
print(f"RMSE : ₹{rmse:,.2f}")
print(f"R²   : {r2:.4f}")


# ---------------------------------------------------------
# 13. Save trained model
# ---------------------------------------------------------

joblib.dump(
    model,
    "random_forest_models.pkl"
)

print("\nModel saved successfully!")
print("File: random_forest_models.pkl")
print("File: feature_columns.pkl")