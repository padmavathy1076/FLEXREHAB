"""
=============================================================================
  FLEXREHAB: AI-Based Smart Hand Rehabilitation System
  Model Training, Multi-Algorithm Benchmark & Evaluation Pipeline
=============================================================================
Inputs:
  - finger_angle (degrees): Range of motion (10° to 90°)
  - time_seconds (sec): Active exercise duration (10s to 120s)
  - repetitions: Number of successful finger movements (5 to 50)
  - movement_speed: Execution cadence (1=Slow, 2=Medium/Optimal, 3=Fast)
  - session_number: Chronological therapy progression (1 to 20)

Target:
  - recovery_score (%): Functional motor recovery (0.0% to 100.0%)
  - therapy_level: Beginner (<40%), Intermediate (40-70%), Advanced (>70%)
=============================================================================
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import joblib
import os


# =============================================================================
# 1. SYNTHETIC REHABILITATION DATA GENERATION
# =============================================================================
def generate_rehab_dataset(n_samples: int = 650, random_state: int = 42) -> pd.DataFrame:
    """
    Generates realistic clinical hand rehabilitation data based on sensor readings
    from the ESP32 exoskeleton glove (5x SG90 servos + flex sensors).
    """
    np.random.seed(random_state)
    
    # Generate realistic clinical input distributions
    session_number = np.random.randint(1, 21, size=n_samples)
    finger_angle = np.clip(15 + session_number * 3.2 + np.random.normal(0, 6.5, n_samples), 10, 90)
    repetitions = np.clip(8 + session_number * 1.6 + np.random.normal(0, 4.0, n_samples), 5, 50).astype(int)
    time_seconds = np.clip(repetitions * 2.2 + np.random.normal(0, 7.0, n_samples), 10, 120)
    
    # Speed: 1=Slow, 2=Medium (Optimal cadence), 3=Fast
    movement_speed = np.random.choice([1, 2, 3], size=n_samples, p=[0.25, 0.55, 0.20])
    speed_efficiency = np.where(movement_speed == 2, 1.0, 0.85)

    # Biomechanical recovery formula correlating sensor features to functional recovery %
    base_recovery = (
        0.35 * (finger_angle / 90.0 * 100) +
        0.25 * (repetitions / 50.0 * 100) +
        0.20 * (session_number / 20.0 * 100) +
        0.10 * (time_seconds / 120.0 * 100) +
        0.10 * (speed_efficiency * 100)
    )
    
    # Add clinical measurement noise
    noise = np.random.normal(0, 2.5, n_samples)
    recovery_score = np.clip(base_recovery + noise, 5.0, 98.0)
    
    # Categorize clinical therapy stage
    therapy_level = pd.cut(
        recovery_score,
        bins=[-np.inf, 40.0, 70.0, np.inf],
        labels=['Beginner', 'Intermediate', 'Advanced']
    )

    df = pd.DataFrame({
        'finger_angle': np.round(finger_angle, 1),
        'time_seconds': np.round(time_seconds, 1),
        'repetitions': repetitions,
        'movement_speed': movement_speed,
        'session_number': session_number,
        'recovery_score': np.round(recovery_score, 1),
        'therapy_level': therapy_level
    })
    
    return df


# =============================================================================
# 2. MODEL EVALUATION & BENCHMARKING (5 ALGORITHMS)
# =============================================================================
def evaluate_all_models(X_train, X_test, y_train, y_test) -> pd.DataFrame:
    """
    Trains and compares 5 machine learning regressors on R², MAE, and RMSE.
    """
    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(max_depth=5, random_state=42),
        "Random Forest": RandomForestRegressor(n_estimators=100, max_depth=6, random_state=42),
        "K-Nearest Neighbors (KNN)": KNeighborsRegressor(n_neighbors=5),
        "Support Vector Regressor (SVR)": SVR(kernel='rbf', C=10.0, epsilon=0.2)
    }

    results = []

    for name, model in models.items():
        # Train
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Performance Metrics
        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))

        # 5-Fold Cross Validation
        kfold = KFold(n_splits=5, shuffle=True, random_state=42)
        cv_scores = cross_val_score(model, X_train, y_train, cv=kfold, scoring='r2')

        results.append({
            "Model": name,
            "R² Score": round(r2, 4),
            "MAE (%)": round(mae, 2),
            "RMSE (%)": round(rmse, 2),
            "5-Fold CV R² (Mean)": round(cv_scores.mean(), 4),
            "CV Std Dev": round(cv_scores.std(), 4)
        })

    return pd.DataFrame(results).sort_values(by="R² Score", ascending=False)


# =============================================================================
# 3. SINGLE PATIENT INFERENCE FUNCTION
# =============================================================================
def predict_patient_recovery(model, finger_angle: float, time_seconds: float, 
                             repetitions: int, movement_speed: int, session_number: int) -> dict:
    """
    Predicts functional recovery score and assigns therapy recommendations.
    """
    input_data = pd.DataFrame([{
        'finger_angle': finger_angle,
        'time_seconds': time_seconds,
        'repetitions': repetitions,
        'movement_speed': movement_speed,
        'session_number': session_number
    }])

    pred_score = float(model.predict(input_data)[0])
    pred_score = round(max(0.0, min(100.0, pred_score)), 1)

    if pred_score < 40.0:
        therapy_level = "Beginner"
        recommendation = "Focus on passive finger stretching, gentle fist clench, and spasticity relief (8-9 exercises)."
    elif pred_score <= 70.0:
        therapy_level = "Intermediate"
        recommendation = "Progress to active tendon gliding, wall finger walking, and pinch grip strength (5 exercises)."
    else:
        therapy_level = "Advanced"
        recommendation = "Focus on rapid finger coordination, fine motor piano taps, and vocational readiness (1-2 exercises)."

    # Estimate remaining sessions needed to achieve clinical discharge benchmark (85.0%)
    target_score = 85.0
    if pred_score >= target_score:
        sessions_needed = 0
    else:
        # Typical progression velocity is ~4.5% to 6.5% per session
        sessions_needed = int(np.ceil((target_score - pred_score) / 5.2))

    return {
        "predicted_recovery_score": f"{pred_score}%",
        "therapy_level": therapy_level,
        "recommended_action": recommendation,
        "estimated_sessions_to_discharge": sessions_needed
    }


# =============================================================================
# 4. MAIN PIPELINE EXECUTION
# =============================================================================
if __name__ == "__main__":
    print("=" * 70)
    print("  1. Generating Rehabilitation Dataset (650 Clinical Sessions)...")
    print("=" * 70)
    df = generate_rehab_dataset(n_samples=650)
    print(df.head())
    print("\nDataset Summary Statistics:")
    print(df.describe())

    # Features and Target
    feature_cols = ['finger_angle', 'time_seconds', 'repetitions', 'movement_speed', 'session_number']
    X = df[feature_cols]
    y = df['recovery_score']

    # Train / Test Split (80% Train, 20% Test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

    print("\n" + "=" * 70)
    print("  2. Training & Benchmarking 5 Machine Learning Algorithms...")
    print("=" * 70)
    comparison_df = evaluate_all_models(X_train, X_test, y_train, y_test)
    print(comparison_df.to_string(index=False))

    print("\n" + "=" * 70)
    print("  3. Final Model Training & Feature Importance (Linear Regression)...")
    print("=" * 70)
    final_model = LinearRegression()
    final_model.fit(X_train, y_train)

    # Display Learned Feature Weights
    importance_df = pd.DataFrame({
        'Feature': feature_cols,
        'Coefficient (Weight)': np.round(final_model.coef_, 4)
    }).sort_values(by='Coefficient (Weight)', ascending=False)
    print(importance_df.to_string(index=False))
    print(f"\nModel Intercept: {round(final_model.intercept_, 4)}")

    # Save model artifact into ml/data directory
    os.makedirs("ml/data", exist_ok=True)
    model_save_path = os.path.join("ml", "data", "rehab_model.joblib")
    joblib.dump(final_model, model_save_path)
    print(f"\n[SUCCESS] Trained model saved as: '{model_save_path}'")

    print("\n" + "=" * 70)
    print("  4. Running Sample Test Patient Inference...")
    print("=" * 70)
    # Sample Patient Input:
    # Finger Angle: 60°, Time: 30s, Repetitions: 15, Speed: Medium (2), Session: 3
    sample_prediction = predict_patient_recovery(
        model=final_model,
        finger_angle=60.0,
        time_seconds=30.0,
        repetitions=15,
        movement_speed=2,
        session_number=3
    )

    for key, value in sample_prediction.items():
        print(f"  • {key.replace('_', ' ').title()}: {value}")
    print("=" * 70)
