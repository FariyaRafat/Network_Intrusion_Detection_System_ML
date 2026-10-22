
import joblib
import numpy as np
import pandas as pd

MODEL_PATH = "rf_model.pkl"


def main():
    # Load the latest trained Random Forest model
    try:
        model = joblib.load(MODEL_PATH)
    except FileNotFoundError:
        print(f"Error: {MODEL_PATH} not found.")
        print("Run the notebook training and model-saving cells first.")
        return

    # Retrieve the exact feature names and order used during training
    if not hasattr(model, "feature_names_in_"):
        print("Error: The model does not contain feature names.")
        print("Retrain and save the model using a pandas DataFrame.")
        return

    features = list(model.feature_names_in_)
    expected_count = len(features)

    print("\nNETWORK INTRUSION DETECTION SYSTEM")
    print("=" * 45)
    print(f"Model: Random Forest")
    print(f"Expected number of features: {expected_count}")
    print("\nEnter values in the following exact order:\n")

    for i, feature in enumerate(features, start=1):
        print(f"{i:2}. {feature}")

    print("\nEnter all values separated by commas or spaces.")
    print(f"You must enter exactly {expected_count} numeric values.")

    user_input = input("\nInput: ").strip()

    try:
        # Accept either comma-separated or space-separated values
        values = [
            float(value)
            for value in user_input.replace(",", " ").split()
        ]
    except ValueError:
        print("Error: All feature values must be numeric.")
        return

    # Validate the input length
    if len(values) != expected_count:
        print(
            f"Error: Expected {expected_count} values, "
            f"but received {len(values)}."
        )
        return

    # Reject NaN and infinite values
    if not np.isfinite(values).all():
        print("Error: Values must be finite numbers.")
        return

    # Construct the input DataFrame in the model's exact feature order
    input_df = pd.DataFrame([values], columns=features)

    # Predict class: 0 = Benign, 1 = Attack
    prediction = int(model.predict(input_df)[0])

    print("\n" + "=" * 45)
    print("PREDICTION RESULT")
    print("=" * 45)

    if prediction == 0:
        print("Result: BENIGN TRAFFIC")
    else:
        print("Result: ATTACK DETECTED")

    # Display estimated class probabilities
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(input_df)[0]

        print("\nModel-estimated probabilities:")

        for class_label, probability in zip(
            model.classes_, probabilities
        ):
            class_name = (
                "Benign" if class_label == 0 else "Attack"
            )
            print(f"{class_name}: {probability:.4%}")

    print("\nNote: Prediction quality depends on valid input features.")
    print("These probabilities are model estimates, not guarantees.")


if __name__ == "__main__":
    main()
