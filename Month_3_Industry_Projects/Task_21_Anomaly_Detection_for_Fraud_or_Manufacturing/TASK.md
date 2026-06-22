# 📋 TASK 21 — Anomaly Detection for Fraud or Manufacturing

| Attribute | Value |
|-----------|-------|
| Difficulty | ⭐⭐⭐⭐ Advanced |
| Estimated Time | 7-8 days |
| Prerequisites | Tasks 06, 08, 12 |
| Key Skills | Isolation Forest, One-Class SVM, Autoencoders for anomaly detection, LOF, handling extreme imbalance (0.17% positive), precision-recall tradeoff in rare events, alert threshold calibration |

---

## 🎯 Learning Objectives
After completing this task, you should be able to:
1. Understand the core principles of anomaly detection for fraud or manufacturing
2. Apply the relevant tools and techniques to a real-world dataset
3. Interpret the results in a business context
4. Document and communicate your findings effectively
5. Defend your technical decisions

---

## 🏢 Business Scenario
Payment processor handles 500K transactions/day. Fraud rate is 0.17%. Each undetected fraud costs $2,500 average. Each false alert costs $15 in manual review. Current rule-based system catches 65% of fraud with 3% false positive rate. You need >85% detection with <1% false positive.

---

## 📐 Detailed Requirements

### 1. Data Processing
- [ ] Load the dataset: **Credit Card Fraud Detection (Kaggle)**
- [ ] Perform appropriate data cleaning and preprocessing
- [ ] Document all transformations and justify them

### 2. Implementation
- [ ] Implement the core solution using anomaly detection algorithm comparison, threshold calibration, cost-sensitive evaluation, PyOD integration
- [ ] Follow best practices for Anomaly Detection for Fraud or Manufacturing
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
**Name:** Credit Card Fraud Detection (Kaggle)
See `DATASETS/dataset_info.md` for full details and alternative sources.
