# 📤 SUBMISSION GUIDELINES — Task 18: Computer Vision: Image Classification Project

---

## 📁 Required Files

Your submission folder **must** contain:

```
Task_18_Computer_Vision_Image_Classification_Project/
├── README.md                  # Your task-specific summary
├── notebook.ipynb             # Main solution notebook
├── src/                       # Modular helper code
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   └── modeling.py
├── figures/                   # All generated charts (.png)
├── reports/
│   └── REPORT.md              # Written report
├── requirements.txt           # Pinned dependencies
└── .gitignore                 # Standard Python .gitignore
```

---

## 🐙 GitHub Structure

Your **single** internship repository must be:

> **https://github.com/musagithub1/ML-Internship-Tasks**

With this top-level layout:

```
ML-Internship-Tasks/
├── README.md                  # Repo-level introduction + task index
├── Month_1_Foundations/
│   ├── Task_01_.../
│   ├── Task_02_.../
│   └── ...
├── Month_2_Applied_ML_MLOps/
│   ├── Task_09_.../
│   └── ...
└── Month_3_Industry_Projects/
    ├── Task_17_.../
    └── ...
```

---

## 🏷️ Naming Conventions

| Element | Convention | Example |
|---------|-----------|---------|
| Folders | `Task_NN_PascalCaseUnderscored` | `Task_03_Feature_Engineering_Mastery` |
| Branches | `feat/task-NN-short-name` | `feat/task-03-feature-engineering` |
| Commits | Conventional Commits | `feat(task-03): add target encoding pipeline` |
| Notebooks | `notebook.ipynb` or `01_eda.ipynb` etc. | — |
| Variables | `snake_case` | `train_features`, `final_model` |
| Classes | `PascalCase` | `FeaturePipeline` |
| Constants | `UPPER_SNAKE_CASE` | `RANDOM_SEED = 42` |

---

## 📝 Report Format (`REPORT.md`)

```markdown
# Task 18 — Computer Vision: Image Classification Project — Report
Author: Mussa Khan (@musagithub1)
Date: YYYY-MM-DD

## 1. Executive Summary (≤5 bullets)
## 2. Business Problem & Framing
## 3. Data Overview
## 4. Methodology
## 5. Results & Key Visualizations
## 6. Limitations & Risks
## 7. Recommendation / Next Steps
## 8. References
```

---

## ⏰ Submission Deadline

| Item | Deadline |
|------|----------|
| Code pushed to GitHub | End of assigned week, Sunday 23:59 (your local time) |
| Report finalized      | Same as above |
| Mentor review request | Open a GitHub Issue titled `Review: Task 18` |

---

## ✅ Submission Checklist

- [ ] All required files present
- [ ] Notebook runs top-to-bottom without errors on a fresh kernel
- [ ] `requirements.txt` is pinned (`package==version`)
- [ ] No data files >100MB committed (use `.gitignore` + dataset link instead)
- [ ] No API keys, secrets, or credentials committed
- [ ] Report has Executive Summary
- [ ] At least 5 figures saved in `figures/`
- [ ] Commit history shows incremental progress (≥5 meaningful commits)
- [ ] GitHub Issue opened for review
