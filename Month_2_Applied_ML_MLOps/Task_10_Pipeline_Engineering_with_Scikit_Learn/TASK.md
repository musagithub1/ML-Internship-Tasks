# 📋 TASK 10 — Pipeline Engineering with Scikit-Learn

| Attribute | Value |
|-----------|-------|
| Difficulty | ⭐⭐⭐ Intermediate-Advanced |
| Estimated Time | 4-5 days |
| Prerequisites | Tasks 02, 03, 05 |
| Key Skills | sklearn Pipeline, ColumnTransformer, custom transformers, FeatureUnion, pipeline serialization (joblib), preventing leakage through pipelines |

---

## 🎯 Learning Objectives
After completing this task, you should be able to:
1. Understand the core principles of pipeline engineering with scikit-learn
2. Apply the relevant tools and techniques to a real-world dataset
3. Interpret the results in a business context
4. Document and communicate your findings effectively
5. Defend your technical decisions

---

## 🏢 Business Scenario
Data science team has 12 notebooks with inconsistent preprocessing. Models break in production because training and inference preprocessing diverge. You need to build ONE reproducible pipeline that handles everything from raw data to predictions.

---

## 📐 Detailed Requirements

### 1. Data Processing
- [ ] Load the dataset: **Titanic (Kaggle)**
- [ ] Perform appropriate data cleaning and preprocessing
- [ ] Document all transformations and justify them

### 2. Implementation
- [ ] Implement the core solution using ColumnTransformer scaffold, custom transformer class template, Pipeline construction, joblib serialization
- [ ] Follow best practices for Pipeline Engineering with Scikit-Learn
- [ ] Ensure the solution is reproducible and modular

### 3. Evaluation
- [ ] Evaluate the solution using relevant metrics
- [ ] Compare with a simple baseline
- [ ] Analyze the results and potential shortcomings

---

## 🗺️ Suggested Approach
### Phase 1: Exploration & Setup (Day 1)
- Understand the business problem and dataset
- Set up your environment and initial scripts

### Phase 2: Core Implementation (Day 2-3)
- Build the main pipeline or model
- Iterate and refine the approach

### Phase 3: Evaluation & Polishing (Day 4+)
- Evaluate the results and finalize the code
- Write the final report and ensure reproducibility

---

## ⛔ Constraints
- Code must be modular and documented
- No data leakage allowed
- Must run locally with the provided requirements.txt

---

## 📦 Deliverables
- Solution notebook or scripts (`.ipynb` or `.py`)
- Modular helpers in `src/` directory
- Written report in `REPORT.md`
- Any relevant visualizations or configuration files

---

## ✅ Success Criteria
- The solution addresses the specific business problem outlined above.
- Code is clean, well-structured, and passes linting.
- The report clearly explains the methodology and business impact.
- The repository can be cloned and run seamlessly.

---

## 🧭 Dataset
**Name:** Titanic (Kaggle)
See `DATASETS/dataset_info.md` for full details and alternative sources.
