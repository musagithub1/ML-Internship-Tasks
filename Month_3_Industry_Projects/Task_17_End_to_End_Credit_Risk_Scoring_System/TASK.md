# 📋 TASK 17 — End-to-End Credit Risk Scoring System

| Attribute | Value |
|-----------|-------|
| Difficulty | ⭐⭐⭐⭐ Advanced |
| Estimated Time | 7-8 days |
| Prerequisites | Tasks 02, 03, 06, 11, 12 |
| Key Skills | Full end-to-end pipeline: data ingestion → cleaning → feature engineering → model training → evaluation → interpretability → report. Handle multiple related tables (application, bureau, previous_application). Scorecard development. |

---

## 🎯 Learning Objectives
After completing this task, you should be able to:
1. Understand the core principles of end-to-end credit risk scoring system
2. Apply the relevant tools and techniques to a real-world dataset
3. Interpret the results in a business context
4. Document and communicate your findings effectively
5. Defend your technical decisions

---

## 🏢 Business Scenario
Consumer lending company processes 2,000 loan applications/day. Current manual review takes 48 hours. False negative (approve defaulter) costs $15,000 in losses. False positive (reject good borrower) costs $200 in lost origination fees. Build a credit scoring system that automates 80% of decisions.

---

## 📐 Detailed Requirements

### 1. Data Processing
- [ ] Load the dataset: **Home Credit Default Risk (Kaggle)**
- [ ] Perform appropriate data cleaning and preprocessing
- [ ] Document all transformations and justify them

### 2. Implementation
- [ ] Implement the core solution using multi-table data loading, feature aggregation pipeline scaffold, scorecard conversion functions, model evaluation with business metrics
- [ ] Follow best practices for End-to-End Credit Risk Scoring System
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
**Name:** Home Credit Default Risk (Kaggle)
See `DATASETS/dataset_info.md` for full details and alternative sources.
