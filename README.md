# FLEXREHAB: Smart Hand Rehabilitation System

FLEXREHAB is an IoT and Machine Learning-assisted hand rehabilitation system developed to support patients recovering from post-stroke hemiparesis, carpal tunnel syndrome, tendon repair surgeries, and arthritis.

The project pairs an ESP32-based sensor glove with an interactive web dashboard. It measures finger bending angles, movement speed, repetition cadence, and duration during rehabilitation exercises, then uses machine learning to estimate a recovery score and suggest level-appropriate physical therapy exercises.

---

## System Overview

The system consists of two major components:
1. **Hardware Glove (ESP32):**
   - Flex sensors placed along the dorsal side of the fingers to capture deflection angles.
   - Microcontroller (ESP32) reading analog voltage changes through voltage divider circuits and transmitting data over Serial/USB.
   - Servo actuators (optional assistive glove module) to guide active-assisted finger motion.

2. **Web Dashboard & AI Model (Flask + Scikit-Learn):**
   - Live clinical dashboard displaying patient vitals, session logs, and recovery progress curves over time.
   - Trained regression and classification models estimating functional recovery percentage based on joint mobility, time elapsed, and repetition counts.
   - Prescribed daily exercise plans (Beginner, Intermediate, Advanced) with completion checklists.
   - Biomechanical hand animation providing visual exercise guidance.

---

## Machine Learning Pipeline

- **Features used for prediction:**
  - `finger_angle`: Active joint angle achieved in degrees (0° - 120°)
  - `time_seconds`: Total duration of the movement session
  - `repetitions`: Total repetition count completed
  - `movement_speed`: Motion cadence (Categorical: Slow, Medium, Fast)
  - `session_number`: Longitudinal progression index
- **Target Output:**
  - `recovery_score`: Functional score (0% to 100%)
  - `therapy_level`: Recommended exercise tier (Beginner < 50%, Intermediate 50–79%, Advanced ≥ 80%)
- **Algorithms Evaluated:**
  - Linear Regression (Baseline)
  - Random Forest Regressor
  - Support Vector Regressor (SVR)
  - K-Nearest Neighbors (KNN)
  - Gradient Boosting

The models were evaluated and serialized using joblib into `ml/data/rehab_model.joblib`.

---

## Project Structure

```
FLEXREHAB/
├── app.py                      # Main Flask application and REST API endpoints
├── exercises_data.py           # Exercise database and servo angle coordinates
├── train_and_evaluate.py       # ML training and evaluation script
├── FLEXREHAB_ML_Pipeline.ipynb # Jupyter notebook for exploratory data analysis
├── data/
│   ├── patients.csv            # Patient registry
│   ├── patient_sessions.csv    # Logged session telemetry
│   └── patient_reports.csv     # Clinical reports history
├── ml/
│   ├── model.py                # Model loader and inference helper
│   ├── synthetic_data.py       # Dataset generation utilities
│   └── data/                   # Saved .joblib model weights and datasets
├── static/
│   ├── css/                    # Custom CSS styling (style.css)
│   └── js/                     # Frontend client logic and Chart.js integration
├── templates/
│   ├── dashboard.html          # Main clinical dashboard view
│   ├── patient_records.html    # Patient directory and registration
│   ├── reports.html            # Session reports & CSV export
│   ├── progress_graph.html     # Historical recovery tracking curves
│   ├── daily_exercises.html    # Prescribed exercises & checklist
│   ├── movement_visualization.html # 2D biomechanical motion guide
│   └── settings.html           # ESP32 COM port and ML settings
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## Setup and Installation

### Prerequisites
- Python 3.10 or higher
- Git (optional, for cloning)

### 1. Clone or Download the Repository
```bash
git clone https://github.com/padmavathy1076/FLEXREHAB.git
cd FLEXREHAB
```

### 2. Create a Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```

Once started, open your web browser and navigate to:
```
http://127.0.0.1:5000/
```

---

## Notes on Hardware Connection (Optional)
If running with an ESP32 hardware glove connected:
1. Connect the ESP32 to your PC via USB.
2. In the dashboard, navigate to **Settings**.
3. Select your active COM Port (e.g., `COM3` on Windows) and set the Baud Rate to `115200`.
4. Click **Connect to ESP32** to begin streaming real-time sensor telemetry into the dashboard.

---

## Authors & Acknowledgments
- Project developed for biomedical engineering research and hands-on capstone demonstration.
- Team: TechStrix
