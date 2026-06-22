# ⚙️ Month 2 — Applied Machine Learning & MLOps

> **Weeks 5–8** | Move beyond single-model experiments. Learn advanced modeling techniques, production pipelines, experiment tracking, and your first model deployment.

---

## 🎯 Learning Objectives

By the end of Month 2, you will be able to:

1. **Systematically tune hyperparameters** — grid search, random search, Bayesian optimization with Optuna, and AutoML exploration
2. **Build reproducible ML pipelines** — Scikit-learn `Pipeline` + `ColumnTransformer` that go from raw data to predictions in one `.predict()` call
3. **Design and train ensemble models** — bagging, boosting (XGBoost, LightGBM), and stacking to squeeze out the last 1–2% of accuracy
4. **Explain model predictions to stakeholders** — SHAP force plots, waterfall charts, and LIME explanations for individual predictions
5. **Forecast time series data** — decomposition, stationarity testing, ARIMA, Prophet, and walk-forward validation
6. **Build NLP classification pipelines** — text preprocessing, TF-IDF, word embeddings, and training a text classifier end-to-end
7. **Track ML experiments rigorously** — MLflow for logging parameters, metrics, artifacts, and comparing experiment runs
8. **Deploy a trained model as a REST API** — FastAPI endpoint, containerized with Docker, tested with automated requests

---

## 📅 Expected Timeline

| Week | Tasks | Focus |
|------|-------|-------|
| Week 5 | Task 09 + Task 10 | Hyperparameter Tuning → Pipeline Engineering |
| Week 6 | Task 11 + Task 12 | Ensembles → Model Interpretation |
| Week 7 | Task 13 + Task 14 | Time Series → NLP |
| Week 8 | Task 15 + Task 16 | MLflow Tracking → FastAPI Deployment |

**Pace:** 2 tasks per week, ~3–4 working days per task.

---

## 🔑 Key Skills Gained

- Optuna hyperparameter optimization and search spaces
- Scikit-learn Pipeline & ColumnTransformer design patterns
- XGBoost, LightGBM, and model stacking
- SHAP & LIME model explainability
- Time series decomposition, stationarity testing, and forecasting
- NLP preprocessing (tokenization, TF-IDF, embeddings)
- MLflow experiment tracking and model registry
- FastAPI REST API development
- Docker containerization and deployment
- Production-quality code: type hints, docstrings, unit tests

---

## 📝 Task List

| # | Task | Description | Difficulty |
|---|------|-------------|------------|
| 09 | [Hyperparameter Tuning & AutoML](./Task_09_Hyperparameter_Tuning_and_AutoML/) | Tune a model with grid search, random search, and Optuna — compare efficiency and final performance | ⭐⭐ |
| 10 | [Pipeline Engineering with Scikit-Learn](./Task_10_Pipeline_Engineering_with_Scikit_Learn/) | Build a full preprocessing + modeling pipeline that's serializable, testable, and production-ready | ⭐⭐ |
| 11 | [Ensemble Methods: Bagging, Boosting & Stacking](./Task_11_Ensemble_Methods_Bagging_Boosting_Stacking/) | Implement Random Forest, XGBoost, LightGBM, and a stacked ensemble — analyze when ensembles help vs. overfit | ⭐⭐⭐ |
| 12 | [Model Interpretation with SHAP & LIME](./Task_12_Model_Interpretation_with_SHAP_and_LIME/) | Generate global and local explanations for a black-box model — create a stakeholder-ready explanation report | ⭐⭐ |
| 13 | [Time Series Forecasting](./Task_13_Time_Series_Forecasting/) | Forecast a real-world time series with ARIMA, Prophet, and ML models — use walk-forward validation | ⭐⭐⭐ |
| 14 | [NLP Foundations: Text Classification](./Task_14_NLP_Foundations_Text_Classification/) | Build a text classifier from TF-IDF baseline to word embeddings — evaluate with precision/recall/F1 | ⭐⭐⭐ |
| 15 | [MLOps: Experiment Tracking with MLflow](./Task_15_MLOps_Experiment_Tracking_with_MLflow/) | Log, compare, and register ML experiments with MLflow — serve a model from the registry | ⭐⭐ |
| 16 | [Model Deployment: FastAPI + Docker](./Task_16_Model_Deployment_with_FastAPI_and_Docker/) | Deploy a trained model as a FastAPI endpoint inside a Docker container with health checks and input validation | ⭐⭐⭐ |

---

## ✅ Month 2 Completion Checklist

- [ ] Task 09 — Hyperparameter Tuning & AutoML
- [ ] Task 10 — Pipeline Engineering with Scikit-Learn
- [ ] Task 11 — Ensemble Methods: Bagging, Boosting & Stacking
- [ ] Task 12 — Model Interpretation with SHAP & LIME
- [ ] Task 13 — Time Series Forecasting
- [ ] Task 14 — NLP Foundations: Text Classification
- [ ] Task 15 — MLOps: Experiment Tracking with MLflow
- [ ] Task 16 — Model Deployment: FastAPI + Docker

> 🎉 **Month 2 complete?** You can now build, explain, track, and deploy ML models. Time for the real thing — [Month 3 — Industry Projects](../Month_3_Industry_Projects/).
