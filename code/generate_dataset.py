"""
generate_dataset.py
Creates a synthetic medical dataset for KPI analysis and dashboard development.
"""

import numpy as np
import pandas as pd

np.random.seed(42)

n = 1000

departments = ["Emergency", "Cardiology", "Oncology", "Surgery", "Pediatrics"]
discharge_statuses = ["Home", "Transfer", "AMA", "Deceased"]

df = pd.DataFrame({
    "patient_id": np.arange(1, n+1),
    "visit_date": pd.to_datetime(
        np.random.choice(pd.date_range("2025-01-01", "2025-12-31"), n)
    ),
    "department": np.random.choice(departments, n, p=[0.45, 0.15, 0.15, 0.15, 0.10]),
    "wait_time_minutes": np.random.normal(42, 12, n).clip(5, 180),
    "length_of_stay_days": np.random.exponential(2.5, n).clip(0.1, 20),
    "readmission_30d": np.random.binomial(1, 0.11, n),
    "medication_errors": np.random.poisson(0.03, n),
    "provider_id": np.random.choice([f"P{i}" for i in range(1, 21)], n),
    "triage_level": np.random.choice([1, 2, 3, 4, 5], n, p=[0.05, 0.15, 0.45, 0.25, 0.10]),
    "discharge_status": np.random.choice(discharge_statuses, n, p=[0.92, 0.05, 0.02, 0.01])
})

df.to_csv("../data/synthetic_medical_log.csv", index=False)
