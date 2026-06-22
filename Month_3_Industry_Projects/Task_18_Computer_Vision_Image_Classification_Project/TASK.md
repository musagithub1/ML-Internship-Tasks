# 📋 TASK 18 — Computer Vision Image Classification Project

| Attribute | Value |
|-----------|-------|
| Difficulty | ⭐⭐⭐⭐ Advanced |
| Estimated Time | 7-8 days |
| Prerequisites | Tasks 08, 09 |
| Key Skills | CNN architecture (build from scratch + transfer learning), data augmentation (Albumentations), learning rate scheduling, grad-CAM visualization, training loop from scratch, model comparison (custom CNN vs. pretrained ResNet/EfficientNet) |

---

## 🎯 Learning Objectives
After completing this task, you should be able to:
1. Understand the core principles of computer vision image classification project
2. Apply the relevant tools and techniques to a real-world dataset
3. Interpret the results in a business context
4. Document and communicate your findings effectively
5. Defend your technical decisions

---

## 🏢 Business Scenario
Manufacturing company inspects 10,000 products/day on assembly line. Manual inspection catches 92% of defects, costs $500K/year in labor. Build a CV model that achieves 97%+ accuracy to reduce inspection cost by 70%.

---

## 📐 Detailed Requirements

### 1. Data Processing
- [ ] Load the dataset: **CIFAR-10 or Intel Image Classification (Kaggle)**
- [ ] Perform appropriate data cleaning and preprocessing
- [ ] Document all transformations and justify them

### 2. Implementation
- [ ] Implement the core solution using PyTorch Dataset class, DataLoader setup, CNN architecture scaffold, training loop with logging, Albumentations transforms, Grad-CAM visualization
- [ ] Follow best practices for Computer Vision Image Classification Project
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
**Name:** CIFAR-10 or Intel Image Classification (Kaggle)
See `DATASETS/dataset_info.md` for full details and alternative sources.
