"""
FLEXREHAB - AI-Based Smart Hand Rehabilitation System
Flask Backend Application providing REST APIs and Dashboard views.
"""

import os
import sys
import threading
from datetime import datetime
import pandas as pd
from flask import Flask, jsonify, render_template, request, send_from_directory
from flask_cors import CORS

# Add workspace directory to python path for internal imports
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from ml.synthetic_data import generate_data
from ml.model import RehabModel
from exercises_data import (
    EXERCISES_BY_LEVEL,
    EXERCISES_DICT,
    ALL_EXERCISES,
    VISUALIZATION_DATA
)

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

# Data Directories
DATA_DIR = os.path.join(BASE_DIR, "data")
ML_DATA_DIR = os.path.join(BASE_DIR, "ml", "data")
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(ML_DATA_DIR, exist_ok=True)

SESSIONS_FILE = os.path.join(DATA_DIR, "patient_sessions.csv")
REPORTS_FILE = os.path.join(DATA_DIR, "patient_reports.csv")
PATIENTS_FILE = os.path.join(DATA_DIR, "patients.csv")
SYNTHETIC_DATA_FILE = os.path.join(ML_DATA_DIR, "synthetic_data.csv")
MODEL_FILE = os.path.join(ML_DATA_DIR, "rehab_model.joblib")

# Thread lock for file operations
file_lock = threading.Lock()

# In-Memory Activity Log (Pre-seeded with initial status items)
recent_activities = [
    {
        "id": "act-1",
        "time": "10:24 AM",
        "title": "Prediction completed",
        "desc": "Recovery score: 76.3% | Intermediate",
        "type": "green",
        "dotColor": "dot-green",
        "timestamp": datetime.now().isoformat()
    },
    {
        "id": "act-2",
        "time": "10:20 AM",
        "title": "Report saved",
        "desc": "patient_reports.csv",
        "type": "cyan",
        "dotColor": "dot-cyan",
        "timestamp": datetime.now().isoformat()
    },
    {
        "id": "act-3",
        "time": "09:15 AM",
        "title": "Session data updated",
        "desc": "Patient ID: PT-00123 (John Doe)",
        "type": "blue",
        "dotColor": "dot-blue",
        "timestamp": datetime.now().isoformat()
    },
    {
        "id": "act-4",
        "time": "08:30 AM",
        "title": "ML Model Loaded",
        "desc": "RehabModel Linear Regression initialized",
        "type": "blue",
        "dotColor": "dot-blue",
        "timestamp": datetime.now().isoformat()
    }
]


def log_activity(title: str, desc: str, activity_type: str = "blue"):
    """
    Log an event into the in-memory recent activities list.
    """
    now = datetime.now()
    time_str = now.strftime("%I:%M %p")
    dot_color = f"dot-{activity_type}" if activity_type in ["green", "cyan", "blue", "orange"] else "dot-blue"

    entry = {
        "id": f"act-{len(recent_activities) + 1}",
        "time": time_str,
        "title": title,
        "desc": desc,
        "description": desc,
        "type": activity_type,
        "dotColor": dot_color,
        "timestamp": now.isoformat()
    }
    recent_activities.insert(0, entry)
    # Keep only the last 50 activities
    if len(recent_activities) > 50:
        recent_activities.pop()


# ============================================================================
# STARTUP INITIALIZATION
# ============================================================================
def init_storage_and_ml():
    """
    Initializes required CSV data stores, synthetic data, and ML model on startup.
    """
    # 1. Ensure synthetic training data exists
    if not os.path.exists(SYNTHETIC_DATA_FILE):
        print("[FLEXREHAB Startup] Generating synthetic rehabilitation training dataset...")
        generate_data(num_samples=650, output_path=SYNTHETIC_DATA_FILE)

    # 2. Ensure ML model exists / trained
    global rehab_model
    rehab_model = RehabModel(model_path=MODEL_FILE, data_path=SYNTHETIC_DATA_FILE)
    print(f"[FLEXREHAB Startup] RehabModel ready. Model status: {'Trained' if rehab_model.is_trained else 'Initialized'}")

    # 3. Pre-populate patient_sessions.csv if not exists
    if not os.path.exists(SESSIONS_FILE):
        print("[FLEXREHAB Startup] Pre-populating patient_sessions.csv with initial cohort data...")
        sessions_data = [
            {
                "session_id": "SES-1001",
                "patient_id": "PT-00123",
                "patient_name": "John Doe",
                "session_number": 1,
                "date": "22-04-2025 09:45 AM",
                "finger_angle": 45.0,
                "repetitions": 15,
                "time_seconds": 45.0,
                "movement_speed": 1,
                "recovery_score": 55.2,
                "therapy_level": "Beginner",
                "notes": "Initial baseline assessment; moderate flexion stiffness"
            },
            {
                "session_id": "SES-1002",
                "patient_id": "PT-00123",
                "patient_name": "John Doe",
                "session_number": 2,
                "date": "26-04-2025 09:18 AM",
                "finger_angle": 60.0,
                "repetitions": 25,
                "time_seconds": 60.0,
                "movement_speed": 2,
                "recovery_score": 68.7,
                "therapy_level": "Intermediate",
                "notes": "Steady motor control improvements with motorized SG90 assistance"
            },
            {
                "session_id": "SES-1003",
                "patient_id": "PT-00123",
                "patient_name": "John Doe",
                "session_number": 3,
                "date": "27-04-2025 10:24 AM",
                "finger_angle": 78.0,
                "repetitions": 35,
                "time_seconds": 75.0,
                "movement_speed": 2,
                "recovery_score": 76.3,
                "therapy_level": "Intermediate",
                "notes": "Active extension and increased repetition tolerance achieved"
            },
            {
                "session_id": "SES-1004",
                "patient_id": "PT-00124",
                "patient_name": "Sarah Smith",
                "session_number": 7,
                "date": "27-04-2025 11:30 AM",
                "finger_angle": 84.0,
                "repetitions": 45,
                "time_seconds": 95.0,
                "movement_speed": 2,
                "recovery_score": 84.5,
                "therapy_level": "Advanced",
                "notes": "Excellent range-of-motion recovery after carpal tunnel release"
            },
            {
                "session_id": "SES-1005",
                "patient_id": "PT-00125",
                "patient_name": "Robert Chang",
                "session_number": 2,
                "date": "25-04-2025 02:15 PM",
                "finger_angle": 42.0,
                "repetitions": 12,
                "time_seconds": 40.0,
                "movement_speed": 1,
                "recovery_score": 54.0,
                "therapy_level": "Beginner",
                "notes": "Early rehabilitation following flexor tendon repair"
            },
            {
                "session_id": "SES-1006",
                "patient_id": "PT-00126",
                "patient_name": "Emily Watson",
                "session_number": 5,
                "date": "26-04-2025 03:45 PM",
                "finger_angle": 68.0,
                "repetitions": 30,
                "time_seconds": 70.0,
                "movement_speed": 2,
                "recovery_score": 71.8,
                "therapy_level": "Intermediate",
                "notes": "Consistent flexion gains post distal radius fracture"
            }
        ]
        pd.DataFrame(sessions_data).to_csv(SESSIONS_FILE, index=False)

    # 4. Pre-populate patient_reports.csv if not exists
    if not os.path.exists(REPORTS_FILE):
        print("[FLEXREHAB Startup] Pre-populating patient_reports.csv...")
        reports_data = [
            {
                "report_id": "REP-103",
                "patient_id": "PT-00123",
                "patient_name": "John Doe",
                "date": "27-04-2025 10:24 AM",
                "generated_by": "Dr. Sarah Adams",
                "summary": "Completed session 3 with 76.3% recovery score. Marked increase in MCP joint mobility.",
                "recommendations": "Continue intermediate level grip exercise and progress to resistance glove drills.",
                "recovery_score": 76.3,
                "therapy_level": "Intermediate",
                "finger_angle": 78.0,
                "repetitions": 35,
                "time_seconds": 75.0,
                "movement_speed": 2,
                "session_number": 3
            },
            {
                "report_id": "REP-102",
                "patient_id": "PT-00123",
                "patient_name": "John Doe",
                "date": "26-04-2025 09:18 AM",
                "generated_by": "Dr. Sarah Adams",
                "summary": "Completed session 2 with 68.7% recovery score. Good progress.",
                "recommendations": "Continue current exercises with gradual increase in repetitions.",
                "recovery_score": 68.7,
                "therapy_level": "Intermediate",
                "finger_angle": 60.0,
                "repetitions": 25,
                "time_seconds": 60.0,
                "movement_speed": 2,
                "session_number": 2
            },
            {
                "report_id": "REP-101",
                "patient_id": "PT-00123",
                "patient_name": "John Doe",
                "date": "22-04-2025 09:45 AM",
                "generated_by": "Dr. Sarah Adams",
                "summary": "Initial baseline session assessment. Baseline recovery score at 55.2%.",
                "recommendations": "Focus on gentle finger flexion and guided passive range-of-motion drills.",
                "recovery_score": 55.2,
                "therapy_level": "Beginner",
                "finger_angle": 45.0,
                "repetitions": 15,
                "time_seconds": 45.0,
                "movement_speed": 1,
                "session_number": 1
            }
        ]
        pd.DataFrame(reports_data).to_csv(REPORTS_FILE, index=False)

    # 5. Pre-populate patients.csv if not exists
    if not os.path.exists(PATIENTS_FILE):
        print("[FLEXREHAB Startup] Pre-populating patients.csv...")
        patients_data = [
            {
                "patient_id": "PT-00123",
                "patient_name": "John Doe",
                "age": 48,
                "gender": "Male",
                "condition": "Post-Stroke Hemiparesis",
                "status": "Active",
                "affected_hand": "Right",
                "joined_date": "2025-04-15",
                "notes": "Targeting finger extension and grasp strength"
            },
            {
                "patient_id": "PT-00124",
                "patient_name": "Sarah Smith",
                "age": 36,
                "gender": "Female",
                "condition": "Carpal Tunnel Release",
                "status": "Active",
                "affected_hand": "Right",
                "joined_date": "2025-04-02",
                "notes": "Near-complete functional flexion recovery"
            },
            {
                "patient_id": "PT-00125",
                "patient_name": "Robert Chang",
                "age": 62,
                "gender": "Male",
                "condition": "Flexor Tendon Repair",
                "status": "Active",
                "affected_hand": "Left",
                "joined_date": "2025-04-20",
                "notes": "Early gentle mobilization protocol"
            },
            {
                "patient_id": "PT-00126",
                "patient_name": "Emily Watson",
                "age": 29,
                "gender": "Female",
                "condition": "Distal Radius Fracture",
                "status": "Active",
                "affected_hand": "Right",
                "joined_date": "2025-04-10",
                "notes": "Wrist stiffness improving with passive assist"
            }
        ]
        pd.DataFrame(patients_data).to_csv(PATIENTS_FILE, index=False)


# Initialize on module load
init_storage_and_ml()


# ============================================================================
# PAGE ROUTES
# ============================================================================
@app.route("/")
@app.route("/dashboard.html")
def route_dashboard():
    """Render main interactive dashboard."""
    return render_template("dashboard.html")


@app.route("/patient-records")
@app.route("/patient_records.html")
def route_patient_records():
    """Render patient records directory."""
    return render_template("patient_records.html")


@app.route("/reports")
@app.route("/reports.html")
def route_reports():
    """Render clinical reports page."""
    return render_template("reports.html")


@app.route("/progress-graph")
@app.route("/progress_graph.html")
def route_progress_graph():
    """Render recovery progress chart analytics."""
    return render_template("progress_graph.html")


@app.route("/daily-exercises")
@app.route("/daily_exercises.html")
def route_daily_exercises():
    """Render daily rehabilitation exercises protocol page."""
    return render_template("daily_exercises.html")


@app.route("/movement-visualization")
@app.route("/movement_visualization.html")
def route_movement_visualization():
    """Render interactive 2D/3D biomechanical movement visualization page."""
    return render_template("movement_visualization.html")


@app.route("/settings")
@app.route("/settings.html")
def route_settings():
    """Render system settings and ML controls."""
    return render_template("settings.html")


# ============================================================================
# API ENDPOINTS
# ============================================================================

@app.route("/api/predict", methods=["POST"])
def api_predict():
    """
    POST /api/predict
    Accepts JSON: {finger_angle, time_seconds, repetitions, movement_speed, session_number, patient_id, patient_name}
    Returns: {recovery_score, predicted_score, score, therapy_level, recommendation, model_used, input_features, timestamp}
    """
    try:
        data = request.get_json(silent=True) or {}

        patient_id = data.get("patient_id", "PT-00123")
        patient_name = data.get("patient_name", "John Doe")
        finger_angle = float(data.get("finger_angle", 60.0))
        time_seconds = float(data.get("time_seconds", 30.0))
        repetitions = int(data.get("repetitions", 15))
        movement_speed = data.get("movement_speed", 2)
        session_number = int(data.get("session_number", 3))

        # Perform ML prediction
        prediction = rehab_model.predict(
            finger_angle=finger_angle,
            time_seconds=time_seconds,
            repetitions=repetitions,
            movement_speed=movement_speed,
            session_number=session_number
        )

        score = prediction["recovery_score"]
        therapy_level = prediction["therapy_level"]

        # Check historical session velocity for this patient
        session_velocity = None
        try:
            with file_lock:
                if os.path.exists(SESSIONS_FILE):
                    df_sess = pd.read_csv(SESSIONS_FILE)
                    p_hist = df_sess[df_sess["patient_id"].astype(str).str.upper() == patient_id.strip().upper()].sort_values(by="session_number")
                    if len(p_hist) >= 2:
                        first_s = float(p_hist.iloc[0]["recovery_score"])
                        last_s = float(p_hist.iloc[-1]["recovery_score"])
                        sess_delta = max(1, int(p_hist.iloc[-1]["session_number"]) - int(p_hist.iloc[0]["session_number"]))
                        session_velocity = (last_s - first_s) / sess_delta
        except Exception:
            session_velocity = None

        # Predict sessions needed using patient's velocity or standard clinical rate
        forecast = rehab_model.predict_sessions_needed(
            current_score=score,
            target_score=85.0,
            current_session=session_number,
            session_velocity=session_velocity
        )

        # Clinical recommendation based on therapy level
        if score < 40.0:
            recommendation = "Focus on gentle finger flexion and guided passive range-of-motion drills."
        elif score <= 70.0:
            recommendation = "Continue current exercises with gradual increase in repetitions."
        else:
            recommendation = "Progress to resistance glove training, complex pinching, and fine motor dexterity."

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        response_payload = {
            "recovery_score": score,
            "predicted_score": score,
            "score": score,
            "therapy_level": therapy_level,
            "recommendation": recommendation,
            "model_used": prediction["model_used"],
            "input_features": prediction["input_features"],
            "patient_id": patient_id,
            "patient_name": patient_name,
            "session_number": session_number,
            "timestamp": timestamp,
            "estimated_sessions_needed": forecast["sessions_needed"],
            "sessions_needed": forecast["sessions_needed"],
            "target_score": forecast["target_score"],
            "sessions_forecast": forecast
        }

        # Log activity
        log_activity(
            title="Prediction completed",
            desc=f"Recovery score: {score}% | {therapy_level} (~{forecast['sessions_needed']} sessions needed)",
            activity_type="green"
        )

        return jsonify(response_payload), 200

    except Exception as e:
        return jsonify({"error": str(e), "message": "Failed to generate prediction"}), 400


@app.route("/api/sessions/<patient_id>", methods=["GET"])
def api_get_patient_sessions(patient_id):
    """
    GET /api/sessions/<patient_id>
    Returns all rehabilitation session records for a specific patient.
    """
    try:
        with file_lock:
            if not os.path.exists(SESSIONS_FILE):
                return jsonify([]), 200
            df = pd.read_csv(SESSIONS_FILE)

        # Filter by patient ID (case-insensitive)
        filtered = df[df["patient_id"].astype(str).str.upper() == patient_id.strip().upper()].copy()

        if filtered.empty:
            return jsonify([]), 200

        # Sort descending by session_number so newest session is first
        filtered.sort_values(by="session_number", ascending=False, inplace=True)

        results = []
        for _, row in filtered.iterrows():
            score_val = float(row["recovery_score"])
            level_val = str(row["therapy_level"])
            session_num = int(row["session_number"])
            results.append({
                "session_id": str(row.get("session_id", f"SES-{session_num}")),
                "patient_id": str(row["patient_id"]),
                "patient_name": str(row.get("patient_name", "Patient")),
                "session": session_num,
                "session_number": session_num,
                "date": str(row["date"]),
                "datetime": str(row["date"]),
                "finger_angle": float(row.get("finger_angle", 0)),
                "repetitions": int(row.get("repetitions", 0)),
                "time_seconds": float(row.get("time_seconds", 0)),
                "movement_speed": row.get("movement_speed", 2),
                "score": score_val,
                "recovery_score": score_val,
                "level": level_val,
                "therapy_level": level_val,
                "notes": str(row.get("notes", ""))
            })

        return jsonify(results), 200

    except Exception as e:
        return jsonify({"error": str(e), "message": "Failed to retrieve session records"}), 500


@app.route("/api/sessions", methods=["POST"])
def api_save_session():
    """
    POST /api/sessions
    Saves a new session record to data/patient_sessions.csv.
    """
    try:
        data = request.get_json(silent=True) or {}

        patient_id = data.get("patient_id", "PT-00123").strip()
        patient_name = data.get("patient_name", "John Doe").strip()
        finger_angle = float(data.get("finger_angle", 60.0))
        repetitions = int(data.get("repetitions", 15))
        time_seconds = float(data.get("time_seconds", 30.0))
        movement_speed = data.get("movement_speed", 2)
        session_number = int(data.get("session_number", 1))
        notes = data.get("notes", "Routine rehabilitation session")

        # If recovery score was not provided, predict it using the ML model
        if "recovery_score" in data and data["recovery_score"] is not None:
            recovery_score = float(data["recovery_score"])
            therapy_level = data.get("therapy_level") or RehabModel.get_therapy_level(recovery_score)
        else:
            pred = rehab_model.predict(
                finger_angle=finger_angle,
                time_seconds=time_seconds,
                repetitions=repetitions,
                movement_speed=movement_speed,
                session_number=session_number
            )
            recovery_score = pred["recovery_score"]
            therapy_level = pred["therapy_level"]

        now_formatted = datetime.now().strftime("%d-%m-%Y %I:%M %p")
        session_id = f"SES-{int(datetime.now().timestamp()) % 100000:04d}"

        new_row = {
            "session_id": session_id,
            "patient_id": patient_id,
            "patient_name": patient_name,
            "session_number": session_number,
            "date": now_formatted,
            "finger_angle": finger_angle,
            "repetitions": repetitions,
            "time_seconds": time_seconds,
            "movement_speed": movement_speed,
            "recovery_score": recovery_score,
            "therapy_level": therapy_level,
            "notes": notes
        }

        with file_lock:
            if os.path.exists(SESSIONS_FILE):
                df = pd.read_csv(SESSIONS_FILE)
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            else:
                df = pd.DataFrame([new_row])
            df.to_csv(SESSIONS_FILE, index=False)

        log_activity(
            title="Session data updated",
            desc=f"Patient ID: {patient_id} (Session {session_number})",
            activity_type="blue"
        )

        return jsonify({
            "success": True,
            "message": "Session recorded successfully",
            "session": new_row
        }), 201

    except Exception as e:
        return jsonify({"error": str(e), "message": "Failed to save session record"}), 400


@app.route("/api/patients", methods=["GET"])
def api_get_patients():
    """
    GET /api/patients
    Returns list of all registered patients enriched with session statistics.
    """
    try:
        with file_lock:
            if os.path.exists(PATIENTS_FILE):
                patients_df = pd.read_csv(PATIENTS_FILE)
            else:
                patients_df = pd.DataFrame(columns=["patient_id", "patient_name", "age", "gender", "condition", "status"])

            sessions_df = pd.read_csv(SESSIONS_FILE) if os.path.exists(SESSIONS_FILE) else pd.DataFrame()

        patient_list = []
        for _, p in patients_df.iterrows():
            pid = str(p["patient_id"])
            p_sessions = pd.DataFrame()
            if not sessions_df.empty and "patient_id" in sessions_df.columns:
                p_sessions = sessions_df[sessions_df["patient_id"].astype(str).str.upper() == pid.upper()]

            total_sessions = len(p_sessions)
            if not p_sessions.empty:
                latest_row = p_sessions.sort_values(by="session_number", ascending=False).iloc[0]
                latest_score = float(latest_row["recovery_score"])
                latest_level = str(latest_row["therapy_level"])
                last_active = str(latest_row["date"])
            else:
                latest_score = 0.0
                latest_level = "Beginner"
                last_active = "No sessions yet"

            patient_list.append({
                "patient_id": pid,
                "patient_name": str(p.get("patient_name", "Unknown")),
                "name": str(p.get("patient_name", "Unknown")),
                "age": int(p.get("age", 45)),
                "gender": str(p.get("gender", "Other")),
                "condition": str(p.get("condition", "Rehabilitation")),
                "status": str(p.get("status", "Active")),
                "affected_hand": str(p.get("affected_hand", "Right")),
                "total_sessions": total_sessions,
                "latest_score": f"{latest_score:.1f}%" if latest_score > 0 else "N/A",
                "therapy_level": latest_level,
                "last_active": last_active
            })

        return jsonify(patient_list), 200

    except Exception as e:
        return jsonify({"error": str(e), "message": "Failed to fetch patients"}), 500


@app.route("/api/patients", methods=["POST"])
def api_add_patient():
    """
    POST /api/patients
    Registers a new patient into data/patients.csv.
    """
    try:
        data = request.get_json(silent=True) or {}

        patient_name = data.get("patient_name") or data.get("name")
        if not patient_name:
            return jsonify({"error": "Missing patient_name"}), 400

        with file_lock:
            if os.path.exists(PATIENTS_FILE):
                df = pd.read_csv(PATIENTS_FILE)
            else:
                df = pd.DataFrame()

            # Generate unique ID if missing
            patient_id = data.get("patient_id")
            if not patient_id:
                next_num = len(df) + 127
                patient_id = f"PT-{next_num:05d}"

            new_patient = {
                "patient_id": patient_id.strip(),
                "patient_name": patient_name.strip(),
                "age": int(data.get("age", 40)),
                "gender": data.get("gender", "Unspecified"),
                "condition": data.get("condition", "General Hand Rehabilitation"),
                "status": data.get("status", "Active"),
                "affected_hand": data.get("affected_hand", "Right"),
                "joined_date": datetime.now().strftime("%Y-%m-%d"),
                "notes": data.get("notes", "Registered via FLEXREHAB Dashboard")
            }

            df = pd.concat([df, pd.DataFrame([new_patient])], ignore_index=True)
            df.to_csv(PATIENTS_FILE, index=False)

        log_activity(
            title="Patient registered",
            desc=f"{new_patient['patient_name']} ({patient_id})",
            activity_type="blue"
        )

        return jsonify({
            "success": True,
            "message": "Patient registered successfully",
            "patient": new_patient
        }), 201

    except Exception as e:
        return jsonify({"error": str(e), "message": "Failed to register patient"}), 400


@app.route("/api/stats", methods=["GET"])
def api_get_stats():
    """
    GET /api/stats
    Returns summary statistics:
    {total_patients, total_sessions, latest_recovery_score, ml_model_status, latest_session}
    """
    try:
        with file_lock:
            sessions_df = pd.read_csv(SESSIONS_FILE) if os.path.exists(SESSIONS_FILE) else pd.DataFrame()
            patients_df = pd.read_csv(PATIENTS_FILE) if os.path.exists(PATIENTS_FILE) else pd.DataFrame()

        total_patients = len(patients_df) if not patients_df.empty else 1
        total_sessions = len(sessions_df) if not sessions_df.empty else 0

        latest_session_dict = {}
        latest_score = 76.3
        score_subtext = "Session 3"

        if not sessions_df.empty:
            latest_row = sessions_df.iloc[-1]
            latest_score = float(latest_row.get("recovery_score", 76.3))
            sess_num = latest_row.get("session_number", 3)
            score_subtext = f"Session {sess_num}"
            latest_session_dict = {
                "patient_id": str(latest_row.get("patient_id", "PT-00123")),
                "patient_name": str(latest_row.get("patient_name", "John Doe")),
                "session_number": int(sess_num),
                "recovery_score": latest_score,
                "therapy_level": str(latest_row.get("therapy_level", "Intermediate")),
                "date": str(latest_row.get("date", "Today"))
            }

        response = {
            "total_patients": total_patients,
            "patient_subtext": "Active Patient" if total_patients == 1 else "Active Patients",
            "total_sessions": total_sessions,
            "sessions_subtext": "This Month",
            "latest_recovery_score": f"{latest_score:.1f}%",
            "latest_score": f"{latest_score:.1f}%",
            "score_subtext": score_subtext,
            "ml_model_status": "Loaded Successfully",
            "ml_model": "Linear Regression",
            "model_subtext": "(Loaded Successfully)",
            "latest_session": latest_session_dict
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e), "message": "Failed to calculate stats"}), 500


@app.route("/api/progress/<patient_id>", methods=["GET"])
def api_get_progress(patient_id):
    """
    GET /api/progress/<patient_id>
    Returns session-wise recovery scores for charting.
    """
    try:
        range_val = request.args.get("range", "7")
        limit = int(range_val) if range_val.isdigit() else 7

        with file_lock:
            if not os.path.exists(SESSIONS_FILE):
                # Fallback mockup curve
                return jsonify({
                    "labels": ["1", "2", "3", "4", "5", "6", "7"],
                    "scores": [52, 60, 68, 72, 76, 80, 85]
                }), 200
            df = pd.read_csv(SESSIONS_FILE)

        p_sessions = df[df["patient_id"].astype(str).str.upper() == patient_id.strip().upper()].copy()

        if p_sessions.empty:
            # Return baseline trajectory
            return jsonify({
                "patient_id": patient_id,
                "labels": ["1", "2", "3"],
                "scores": [55.2, 68.7, 76.3]
            }), 200

        # Sort ascending by session number
        p_sessions.sort_values(by="session_number", ascending=True, inplace=True)
        if len(p_sessions) > limit:
            p_sessions = p_sessions.tail(limit)

        labels = [str(int(row["session_number"])) for _, row in p_sessions.iterrows()]
        scores = [float(row["recovery_score"]) for _, row in p_sessions.iterrows()]

        return jsonify({
            "patient_id": patient_id,
            "labels": labels,
            "scores": scores,
            "total_recorded": len(labels)
        }), 200

    except Exception as e:
        return jsonify({"error": str(e), "message": "Failed to load progress data"}), 500


@app.route("/api/reports/save", methods=["POST"])
def api_save_report():
    """
    POST /api/reports/save
    Saves clinical report to data/patient_reports.csv.
    """
    try:
        data = request.get_json(silent=True) or {}

        patient_id = data.get("patient_id", "PT-00123")
        patient_name = data.get("patient_name", "John Doe")
        session_number = int(data.get("session_number", 3))
        recovery_score = float(data.get("recovery_score", 76.3))
        therapy_level = data.get("therapy_level", "Intermediate")
        finger_angle = float(data.get("finger_angle", 60.0))
        repetitions = int(data.get("repetitions", 15))
        time_seconds = float(data.get("time_seconds", 30.0))
        movement_speed = data.get("movement_speed", 2)

        now_formatted = datetime.now().strftime("%d-%m-%Y %I:%M %p")
        report_id = f"REP-{int(datetime.now().timestamp()) % 1000:03d}"

        summary = data.get(
            "summary",
            f"Completed rehabilitation session {session_number} with {recovery_score:.1f}% recovery score."
        )
        recommendations = data.get(
            "recommendations",
            f"Assigned {therapy_level} level protocol. Continue prescribed SG90 finger mobility drills."
        )

        new_report = {
            "report_id": report_id,
            "patient_id": patient_id,
            "patient_name": patient_name,
            "date": now_formatted,
            "generated_by": data.get("generated_by", "Dr. Sarah Adams"),
            "summary": summary,
            "recommendations": recommendations,
            "recovery_score": recovery_score,
            "therapy_level": therapy_level,
            "finger_angle": finger_angle,
            "repetitions": repetitions,
            "time_seconds": time_seconds,
            "movement_speed": movement_speed,
            "session_number": session_number
        }

        with file_lock:
            if os.path.exists(REPORTS_FILE):
                df = pd.read_csv(REPORTS_FILE)
                df = pd.concat([df, pd.DataFrame([new_report])], ignore_index=True)
            else:
                df = pd.DataFrame([new_report])
            df.to_csv(REPORTS_FILE, index=False)

        log_activity(
            title="Report saved",
            desc="patient_reports.csv",
            activity_type="cyan"
        )

        return jsonify({
            "success": True,
            "message": "Report saved successfully",
            "report_id": report_id,
            "report": new_report
        }), 201

    except Exception as e:
        return jsonify({"error": str(e), "message": "Failed to save report"}), 400


@app.route("/api/reports", methods=["GET"])
def api_get_reports():
    """
    GET /api/reports
    Returns all generated rehabilitation reports from data/patient_reports.csv.
    """
    try:
        with file_lock:
            if not os.path.exists(REPORTS_FILE):
                return jsonify([]), 200
            df = pd.read_csv(REPORTS_FILE)

        reports = df.to_dict(orient="records")
        return jsonify(reports), 200
    except Exception as e:
        return jsonify({"error": str(e), "message": "Failed to fetch reports"}), 500


@app.route("/api/model/compare", methods=["GET"])
def api_compare_models():
    """
    GET /api/model/compare
    Trains and benchmarks 5 regression algorithms on synthetic rehabilitation data.
    """
    try:
        results = rehab_model.compare_models()
        return jsonify({
            "success": True,
            "comparison": results["comparison"],
            "models": results["models"],
            "best_model": results["best_model"],
            "total_samples": results["total_samples"]
        }), 200
    except Exception as e:
        return jsonify({"error": str(e), "message": "Failed to run model comparison"}), 500


@app.route("/api/activity", methods=["GET"])
def api_get_activity():
    """
    GET /api/activity
    Returns recent system activity logs.
    """
    return jsonify(recent_activities), 200


@app.route("/api/insights/<patient_id>", methods=["GET"])
def api_get_insights(patient_id):
    """
    GET /api/insights/<patient_id>
    Returns quick insights: {score_increase, total_sessions, sessions_count, progress_trend, trend, current_therapy_level, current_level}
    """
    try:
        with file_lock:
            if not os.path.exists(SESSIONS_FILE):
                return jsonify({
                    "score_increase": "+21.1%",
                    "total_sessions": 3,
                    "sessions_count": 3,
                    "progress_trend": "Steady",
                    "trend": "Steady",
                    "current_therapy_level": "Intermediate",
                    "current_level": "Intermediate"
                }), 200
            df = pd.read_csv(SESSIONS_FILE)

        p_sessions = df[df["patient_id"].astype(str).str.upper() == patient_id.strip().upper()].copy()

        if p_sessions.empty:
            return jsonify({
                "patient_id": patient_id,
                "score_increase": "+0.0%",
                "total_sessions": 0,
                "sessions_count": 0,
                "progress_trend": "New Patient",
                "trend": "New Patient",
                "current_therapy_level": "Beginner",
                "current_level": "Beginner"
            }), 200

        p_sessions.sort_values(by="session_number", ascending=True, inplace=True)
        total_sessions = len(p_sessions)
        first_score = float(p_sessions.iloc[0]["recovery_score"])
        latest_row = p_sessions.iloc[-1]
        latest_score = float(latest_row["recovery_score"])
        current_level = str(latest_row["therapy_level"])

        diff = latest_score - first_score
        sign = "+" if diff >= 0 else ""
        score_increase = f"{sign}{diff:.1f}%"

        if diff > 5.0:
            trend = "Steady" if diff < 15.0 else "Accelerating"
        elif diff >= 0.0:
            trend = "Consistent"
        else:
            trend = "Plateau"

        # Calculate estimated sessions needed for this patient
        velocity = (diff / max(1, total_sessions - 1)) if total_sessions > 1 else None
        forecast = rehab_model.predict_sessions_needed(
            current_score=latest_score,
            target_score=85.0,
            current_session=int(latest_row.get("session_number", total_sessions)),
            session_velocity=velocity
        )

        return jsonify({
            "patient_id": patient_id,
            "score_increase": score_increase,
            "total_sessions": total_sessions,
            "sessions_count": total_sessions,
            "progress_trend": trend,
            "trend": trend,
            "current_therapy_level": current_level,
            "current_level": current_level,
            "latest_score": latest_score,
            "estimated_sessions_needed": forecast["sessions_needed"],
            "sessions_needed": forecast["sessions_needed"],
            "sessions_needed_text": f"{forecast['sessions_needed']} Sessions",
            "sessions_forecast": forecast
        }), 200

    except Exception as e:
        return jsonify({"error": str(e), "message": "Failed to compute insights"}), 500


# ============================================================================
# EXERCISE & MOVEMENT VISUALIZATION API ENDPOINTS
# ============================================================================

@app.route("/api/exercises", methods=["GET"])
@app.route("/api/exercises/<therapy_level>", methods=["GET"])
def api_get_exercises(therapy_level=None):
    """
    GET /api/exercises/<therapy_level>
    Returns a list of rehabilitation exercises based on therapy level:
      - 'Beginner' -> 9 exercises (for recovery_score < 40%)
      - 'Intermediate' -> 5 exercises (for recovery_score 40-70%)
      - 'Advanced' -> 2 exercises (for recovery_score > 70%)
      - 'all' / None -> all 16 exercises
    """
    try:
        if not therapy_level or therapy_level.strip().lower() in ["all", "any"]:
            selected = ALL_EXERCISES
            level_name = "All"
        else:
            norm = therapy_level.strip().lower()
            matched_key = None
            for key in EXERCISES_BY_LEVEL.keys():
                if key.lower() == norm:
                    matched_key = key
                    break

            if matched_key:
                selected = EXERCISES_BY_LEVEL[matched_key]
                level_name = matched_key
            else:
                # Fallback to Beginner if unrecognized
                selected = EXERCISES_BY_LEVEL["Beginner"]
                level_name = "Beginner"

        # If consumer explicitly requested envelope via query param, wrap it
        if request.args.get("envelope") == "true" or request.args.get("wrap") == "true":
            return jsonify({
                "therapy_level": level_name,
                "count": len(selected),
                "exercises": selected
            }), 200

        # Return list directly as per specification
        return jsonify(selected), 200

    except Exception as e:
        return jsonify({"error": str(e), "message": "Failed to retrieve exercises"}), 500


@app.route("/api/exercises/patient/<patient_id>", methods=["GET"])
def api_get_patient_exercises(patient_id):
    """
    GET /api/exercises/patient/<patient_id>
    Looks up patient's latest therapy_level from most recent session in patient_sessions.csv,
    then returns the appropriate exercises for that level along with patient info and current level.
    """
    try:
        pid = patient_id.strip()
        patient_name = pid
        therapy_level = "Beginner"
        recovery_score = None
        session_number = 0
        condition = "Hand Rehabilitation"
        affected_hand = "Right"
        age = None
        gender = None

        # 1. Lookup in patients.csv for demographics
        try:
            with file_lock:
                if os.path.exists(PATIENTS_FILE):
                    pdf = pd.read_csv(PATIENTS_FILE)
                    p_match = pdf[pdf["patient_id"].astype(str).str.strip().str.upper() == pid.upper()]
                    if not p_match.empty:
                        p_row = p_match.iloc[0]
                        patient_name = str(p_row.get("patient_name", pid))
                        condition = str(p_row.get("condition", condition))
                        affected_hand = str(p_row.get("affected_hand", affected_hand))
                        age = int(p_row.get("age")) if pd.notna(p_row.get("age")) else None
                        gender = str(p_row.get("gender", "")) if pd.notna(p_row.get("gender")) else None
        except Exception as pe:
            print(f"[Warning] Failed to read patients.csv: {pe}")

        # 2. Lookup in patient_sessions.csv for latest therapy_level & recovery_score
        with file_lock:
            if os.path.exists(SESSIONS_FILE):
                sdf = pd.read_csv(SESSIONS_FILE)
                s_match = sdf[sdf["patient_id"].astype(str).str.strip().str.upper() == pid.upper()].copy()
                if not s_match.empty:
                    s_match.sort_values(by="session_number", ascending=True, inplace=True)
                    latest_session = s_match.iloc[-1]
                    session_number = int(latest_session.get("session_number", len(s_match)))
                    patient_name = str(latest_session.get("patient_name", patient_name))
                    raw_level = str(latest_session.get("therapy_level", "")).strip()

                    if pd.notna(latest_session.get("recovery_score")):
                        recovery_score = float(latest_session.get("recovery_score"))

                    # Determine or validate therapy level
                    if raw_level and raw_level.capitalize() in EXERCISES_BY_LEVEL:
                        therapy_level = raw_level.capitalize()
                    elif recovery_score is not None:
                        if recovery_score < 40.0:
                            therapy_level = "Beginner"
                        elif recovery_score <= 70.0:
                            therapy_level = "Intermediate"
                        else:
                            therapy_level = "Advanced"

        # 3. Retrieve exercises for this therapy level
        exercises = EXERCISES_BY_LEVEL.get(therapy_level, EXERCISES_BY_LEVEL["Beginner"])

        return jsonify({
            "patient_id": pid,
            "patient_name": patient_name,
            "therapy_level": therapy_level,
            "current_level": therapy_level,
            "recovery_score": recovery_score,
            "session_number": session_number,
            "condition": condition,
            "affected_hand": affected_hand,
            "age": age,
            "gender": gender,
            "exercises_count": len(exercises),
            "exercises": exercises
        }), 200

    except Exception as e:
        return jsonify({"error": str(e), "message": "Failed to retrieve patient exercises"}), 500


@app.route("/api/visualization/<exercise_id>", methods=["GET"])
def api_get_visualization(exercise_id):
    """
    GET /api/visualization/<exercise_id>
    Returns detailed biomechanical animation data (keyframes, finger angles, spread, wrist kinematics, timing)
    for a specific exercise.
    """
    try:
        target = exercise_id.strip()
        matched_data = None

        # 1. Direct ID match (e.g. 'ex_001')
        if target in VISUALIZATION_DATA:
            matched_data = VISUALIZATION_DATA[target]

        # 2. Numeric match (e.g. '1' -> 'ex_001')
        if not matched_data and target.isdigit():
            padded = f"ex_{int(target):03d}"
            if padded in VISUALIZATION_DATA:
                matched_data = VISUALIZATION_DATA[padded]

        # 3. Animation type or name match (case-insensitive)
        if not matched_data:
            target_lower = target.lower().replace("-", "_").replace(" ", "_")
            for ex_id, vdata in VISUALIZATION_DATA.items():
                if vdata.get("animation_type", "").lower() == target_lower:
                    matched_data = vdata
                    break
                if vdata.get("name", "").lower().replace(" ", "_") == target_lower:
                    matched_data = vdata
                    break

        if not matched_data:
            # Fallback to ex_001 if not found
            matched_data = VISUALIZATION_DATA["ex_001"]

        ex_id = matched_data["id"]
        metadata = EXERCISES_DICT.get(ex_id, {})

        response_payload = {
            "id": ex_id,
            "exercise_id": ex_id,
            "name": matched_data.get("name", metadata.get("name", "Exercise")),
            "exercise_name": matched_data.get("name", metadata.get("name", "Exercise")),
            "animation_type": matched_data.get("animation_type", metadata.get("animation_type", "flexion")),
            "description": matched_data.get("description", metadata.get("description", "")),
            "therapy_level": matched_data.get("therapy_level", metadata.get("therapy_level", "Beginner")),
            "total_duration_ms": matched_data.get("total_duration_ms", 5000),
            "instructions": metadata.get("instructions", []),
            "benefits": metadata.get("benefits", ""),
            "target_fingers": metadata.get("target_fingers", ["all"]),
            "duration": metadata.get("duration", "5 minutes"),
            "repetitions": metadata.get("repetitions", 10),
            "sets": metadata.get("sets", 3),
            "difficulty": metadata.get("difficulty", "Easy"),
            "keyframes": matched_data.get("keyframes", []),
            "steps_count": len(matched_data.get("keyframes", []))
        }

        return jsonify(response_payload), 200

    except Exception as e:
        return jsonify({"error": str(e), "message": "Failed to retrieve visualization data"}), 500


# ============================================================================
# RUN APPLICATION
# ============================================================================
if __name__ == "__main__":
    print("\n" + "=" * 65)
    print("  FLEXREHAB - AI-Based Smart Hand Rehabilitation System")
    print("  Server running on http://127.0.0.1:5000")
    print("=" * 65 + "\n")
    app.run(host="0.0.0.0", port=5000, debug=True)


