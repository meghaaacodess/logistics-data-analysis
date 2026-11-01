"""
Week 1 Task: Strategic Planning and Data Exploration in Logistics

This beginner-friendly script demonstrates how a logistics analyst could:
1. Load a delivery dataset
2. Inspect and clean basic data
3. Calculate example KPIs
4. Train a baseline regression model for delivery duration

IMPORTANT:
- This is a template for learning and planning.
- Replace "deliveries.csv" and the column names with those in your actual dataset.
- No results should be reported until the code is run on a real dataset.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error


def main():
    # 1. Load the dataset (place deliveries.csv in the same folder as this script).
    df = pd.read_csv("deliveries.csv")

    # 2. Inspect the data.
    print("\nFirst five rows:")
    print(df.head())
    print("\nDataset shape:", df.shape)
    print("\nMissing values per column:")
    print(df.isnull().sum())

    # 3. Remove exact duplicate rows.
    df = df.drop_duplicates()

    # 4. Create delivery duration if the required timestamp columns exist.
    required_times = {"dispatch_time", "delivery_time"}
    if required_times.issubset(df.columns):
        df["dispatch_time"] = pd.to_datetime(
            df["dispatch_time"], errors="coerce"
        )
        df["delivery_time"] = pd.to_datetime(
            df["delivery_time"], errors="coerce"
        )
        df["duration_minutes"] = (
            df["delivery_time"] - df["dispatch_time"]
        ).dt.total_seconds() / 60

        # Keep records with positive delivery duration.
        df = df[df["duration_minutes"] > 0].copy()
        df["dispatch_hour"] = df["dispatch_time"].dt.hour
        df["weekday"] = df["dispatch_time"].dt.dayofweek

        print("\nAverage delivery duration (minutes):",
              round(df["duration_minutes"].mean(), 2))

        # 5. Calculate on-time delivery rate only if a promised time is available.
        if "promised_delivery_time" in df.columns:
            df["promised_delivery_time"] = pd.to_datetime(
                df["promised_delivery_time"], errors="coerce"
            )
            valid = df.dropna(
                subset=["delivery_time", "promised_delivery_time"]
            )
            if len(valid) > 0:
                on_time_rate = (
                    valid["delivery_time"] <= valid["promised_delivery_time"]
                ).mean() * 100
                print("On-time delivery rate (%):",
                      round(on_time_rate, 2))

        # 6. Train a simple baseline regression model if usable features exist.
        possible_features = ["dispatch_hour", "weekday", "distance_km"]
        features = [col for col in possible_features if col in df.columns]

        if features and df["duration_minutes"].notna().sum() >= 5:
            model_data = df[features + ["duration_minutes"]].dropna(
                subset=["duration_minutes"]
            )
            X = model_data[features]
            y = model_data["duration_minutes"]

            if len(model_data) >= 5:
                X_train, X_test, y_train, y_test = train_test_split(
                    X, y, test_size=0.2, random_state=42
                )
                model = make_pipeline(
                    SimpleImputer(strategy="median"),
                    LinearRegression()
                )
                model.fit(X_train, y_train)
                predictions = model.predict(X_test)

                mae = mean_absolute_error(y_test, predictions)
                rmse = np.sqrt(mean_squared_error(y_test, predictions))
                print("\nBaseline regression model")
                print("Features used:", features)
                print("Mean Absolute Error (minutes):", round(mae, 2))
                print("Root Mean Squared Error (minutes):", round(rmse, 2))
            else:
                print("\nNot enough rows to train a model.")
        else:
            print(
                "\nModel skipped: add suitable feature columns such as "
                "dispatch_hour, weekday, or distance_km."
            )
    else:
        print(
            "\nDuration and modelling steps skipped because the dataset "
            "must contain dispatch_time and delivery_time columns."
        )
        print("Expected example columns: dispatch_time, delivery_time, "
              "distance_km, promised_delivery_time (optional).")


if __name__ == "__main__":
    main()
