# 📋 TASK 06 — Classification Algorithms Comparison

---

## 🏢 Business Problem

You have just joined the **Data Science team at a mid-sized company**. Your manager has assigned you a problem that — while it may look academic from the outside — mirrors a real responsibility you would own as a Junior ML Engineer.

**Scenario:**
The business needs a defensible, data-driven approach to **classification algorithms comparison**. Decisions made downstream (pricing, targeting, risk approval, hiring) will rely on the quality of your work. A wrong call costs the company money, reputation, or compliance penalties.

Your job is **not** to "get good accuracy." Your job is to:

- Understand the business cost of being wrong.
- Choose the right method (not the trendiest one).
- Defend your choices with evidence.
- Communicate the result clearly to non-technical stakeholders.

---

## 📐 Detailed Requirements

### 1. Problem Framing
- [ ] Restate the business problem in your own words.
- [ ] Define the ML problem type (regression / classification / clustering / etc.).
- [ ] Define the **target metric** and justify it (why F1 instead of accuracy? why MAE instead of RMSE?).
- [ ] Identify at least **2 risks or assumptions**.

### 2. Data
- [ ] Use the recommended dataset: **Pima Indians Diabetes**.
- [ ] Document its schema, size, and source.
- [ ] Identify potential data quality issues *before* modeling.

### 3. Methodology
- [ ] Implement the core technique(s) required for **Classification Algorithms Comparison**.
- [ ] Compare at least **2 approaches** (baseline vs. improved).
- [ ] Use proper validation — no leakage, no peeking at test data.
- [ ] Reproducibility: set seeds, log versions.

### 4. Analysis
- [ ] Produce at least **5 publication-quality visualizations**.
- [ ] Explain what each chart tells the business — not just what it shows.
- [ ] Quantify uncertainty where applicable (confidence intervals, error bars).

### 5. Communication
- [ ] Write a `REPORT.md` with: Problem → Approach → Results → Recommendation.
- [ ] Include a 5-bullet **Executive Summary** at the top of the report.
- [ ] Tag every chart with a 1–2 sentence business takeaway.

### 6. Engineering
- [ ] Code organized in functions / modules — no 500-line monolithic notebooks.
- [ ] `requirements.txt` pinned with versions.
- [ ] `README.md` inside your task folder with how to run it.
- [ ] Commit history shows incremental progress (not one giant "final commit").

---

## ⛔ Constraints

1. **No copy-pasting Kaggle notebooks.** Reference them, don't steal them. Cite every source.
2. **No premature modeling.** You must do EDA before fitting anything.
3. **No data leakage.** Splits happen before transformations that learn from the data.
4. **No "black box submissions."** Every model decision must be explainable.
5. **Reproducibility required.** A reviewer should be able to clone your repo and reproduce results within 10 minutes.

---

## 📦 Deliverables

| # | Deliverable | Format |
|---|-------------|--------|
| 1 | Solution notebook | `.ipynb` |
| 2 | Modular helpers | `src/` folder with `.py` files |
| 3 | Written report | `REPORT.md` |
| 4 | Visualizations | `figures/*.png` |
| 5 | Requirements file | `requirements.txt` |
| 6 | README | `README.md` inside your task folder |
| 7 | (Optional) Recorded walkthrough | Loom / YouTube unlisted link |

---

## ✅ Success Criteria

Your submission is considered **successful** if:

- A senior engineer can clone your repo and reproduce your results in **≤ 10 minutes**.
- Your report can be read by a **non-technical manager** and they walk away knowing what you did and why.
- Your visualizations would survive a **screenshot in a stakeholder meeting** without embarrassment.
- Your code passes basic linting (`flake8` / `ruff`) and uses meaningful function names.
- You can defend every modeling decision in a **15-minute mock interview**.

---

## 🧭 Dataset

**Name:** Pima Indians Diabetes
**Description:** 768 diagnostic records used to predict diabetes onset based on 8 medical predictor variables.
**Source:** [https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

See [`DATASETS/dataset_info.md`](./DATASETS/dataset_info.md) for full details and alternative sources.
