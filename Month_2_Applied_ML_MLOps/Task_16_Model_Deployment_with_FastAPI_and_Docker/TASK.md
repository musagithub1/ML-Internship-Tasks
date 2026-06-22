# 📋 TASK 16 — Model Deployment with FastAPI and Docker

| Attribute | Value |
|-----------|-------|
| Difficulty | ⭐⭐⭐⭐ Advanced |
| Estimated Time | 6-7 days |
| Prerequisites | Tasks 10, 15 |
| Key Skills | FastAPI (endpoints, request/response models, validation), Docker (Dockerfile, multi-stage builds), health checks, input validation, error handling, API testing, load testing basics |

---

## 🎯 Learning Objectives
After completing this task, you should be able to:
1. Understand the core principles of model deployment with fastapi and docker
2. Apply the relevant tools and techniques to a real-world dataset
3. Interpret the results in a business context
4. Document and communicate your findings effectively
5. Defend your technical decisions

---

## 🏢 Business Scenario
Data science team has 3 models stuck in notebooks. Product team has been waiting 4 months for a prediction API. You need to deploy a model as a REST API that handles 100 requests/second with <200ms latency.

---

## 📐 Detailed Requirements

### 1. Data Processing
- [ ] Load the dataset: **Iris (reuse) + Custom trained model**
- [ ] Perform appropriate data cleaning and preprocessing
- [ ] Document all transformations and justify them

### 2. Implementation
- [ ] Implement the core solution using app/main.py with FastAPI scaffold AND a Dockerfile AND docker-compose.yml
- [ ] Follow best practices for Model Deployment with FastAPI and Docker
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
**Name:** Iris (reuse) + Custom trained model
See `DATASETS/dataset_info.md` for full details and alternative sources.
