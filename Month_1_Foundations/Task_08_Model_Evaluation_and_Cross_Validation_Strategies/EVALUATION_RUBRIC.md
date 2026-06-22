# 🧪 EVALUATION RUBRIC — Task 08: Model Evaluation & Cross-Validation Strategies

> **Total: 100 marks** | Pass: 60 | Distinction: 85+

---

## 📊 Grading Breakdown

| Category | Max Marks | What's Evaluated |
|----------|-----------|------------------|
| 1. Problem Framing & Business Understanding | 10 | Did you translate business → ML correctly? Did you justify the target metric? |
| 2. Data Understanding & EDA | 15 | Depth of exploration, schema documentation, identified data issues |
| 3. Methodology & Technical Correctness | 20 | Right algorithms, no leakage, proper splits, sound assumptions |
| 4. Code Quality & Reproducibility | 15 | Modularity, naming, `requirements.txt`, seed control, runnable end-to-end |
| 5. Experimentation & Comparison | 10 | ≥2 approaches compared with fair evaluation |
| 6. Model Evaluation & Interpretation | 10 | Correct metrics, error analysis, interpretability (SHAP/feature importance where relevant) |
| 7. Visualizations | 10 | ≥5 clear, labeled, business-meaningful charts |
| 8. Report & Communication | 5 | Clear writing, exec summary, non-technical readability |
| 9. GitHub Hygiene | 5 | Commit history, structure, README, no secrets, no >100MB blobs |
| **TOTAL** | **100** | |

---

## 🎯 Detailed Criteria

### 1. Problem Framing (10)
- 0–3: No framing or restates the brief verbatim.
- 4–6: Restates problem, identifies ML problem type.
- 7–8: Adds metric justification and assumptions.
- 9–10: Adds business cost analysis and risk discussion.

### 2. Data Understanding & EDA (15)
- 0–4: Just `.describe()` and `.info()`.
- 5–9: Univariate + bivariate analysis.
- 10–12: Adds multivariate, missingness, outliers, target relationship.
- 13–15: Hypothesis-driven EDA with statistical backing.

### 3. Methodology (20)
- 0–6: Plug-and-chug, leakage present, or wrong split.
- 7–12: Clean splits, basic correct method.
- 13–17: Strong validation strategy, multiple baselines.
- 18–20: Reproducible, principled, defensible, addresses edge cases.

### 4. Code Quality & Reproducibility (15)
- 0–4: One messy notebook, no requirements.
- 5–9: Some functions, requirements present.
- 10–12: Modular `src/`, seeds set, runs top-to-bottom.
- 13–15: Production-grade: type hints, docstrings, linted.

### 5. Experimentation (10)
- 0–3: Single model.
- 4–6: Two models, no fair comparison.
- 7–8: Multiple models with shared CV.
- 9–10: Statistical comparison (significance/CI).

### 6. Evaluation & Interpretation (10)
- 0–3: Accuracy on imbalanced data only.
- 4–6: Correct metrics, confusion matrix / residuals.
- 7–8: Error analysis on failure cases.
- 9–10: SHAP / partial dependence / feature importance with business reading.

### 7. Visualizations (10)
- 0–3: Default matplotlib, no titles/axes.
- 4–6: Labeled but cluttered.
- 7–8: Clean, colorblind-safe, captioned.
- 9–10: Storytelling charts you could put in a board meeting.

### 8. Report (5)
- 0–1: Bullet points only.
- 2–3: Full sections but jargon-heavy.
- 4–5: Exec summary + accessible to non-technical readers.

### 9. GitHub Hygiene (5)
- 0–1: Single commit, no README.
- 2–3: Multiple commits, basic README.
- 4–5: Conventional commits, clean PR/Issue trail, badge-style README.

---

## 🏅 Bonus (up to +5)

- Solving the [`BONUS_CHALLENGE.md`](./BONUS_CHALLENGE.md)
- Recording a Loom/YouTube walkthrough
- Writing a LinkedIn / Medium / Dev.to post about your work
- Contributing improvements to the internship template repo

---

## ❌ Automatic Fails

- Plagiarized notebook (uncited copy of a Kaggle kernel)
- Data leakage in core methodology
- Committed credentials, API keys, or PII
- Submission cannot be reproduced from a fresh clone
