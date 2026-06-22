# 📊 Dataset — Task 06: Classification Algorithms Comparison

---

## Primary Dataset

**Name:** Pima Indians Diabetes
**Source:** [https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

**Description:**
768 diagnostic records used to predict diabetes onset based on 8 medical predictor variables.

---

## Download Instructions

### Option A — Kaggle CLI (recommended)

```bash
pip install kaggle
# place your kaggle.json in ~/.kaggle/
kaggle datasets download -d <owner>/<dataset-slug>
# or for competitions:
kaggle competitions download -c <competition-slug>
unzip *.zip -d ./data/raw/
```

### Option B — Manual Download

1. Visit the source link above.
2. Sign in to Kaggle (free).
3. Click **Download** and unzip into `./data/raw/`.

---

## Folder Convention

```
DATASETS/
├── raw/           # untouched original files (git-ignored)
├── interim/       # cleaned but not feature-engineered
└── processed/     # ready-to-model
```

**Do NOT commit raw data files to GitHub.** Use `.gitignore`:

```
DATASETS/raw/
DATASETS/interim/
DATASETS/processed/
*.csv
*.parquet
```

---

## Alternative / Backup Datasets

If the primary dataset becomes unavailable, you may substitute with:

- [UCI ML Repository](https://archive.ics.uci.edu/datasets)
- [OpenML](https://www.openml.org/search?type=data)
- [Hugging Face Datasets](https://huggingface.co/datasets)
- [Google Dataset Search](https://datasetsearch.research.google.com/)

> ⚠️ If you switch datasets, document the reason in your `REPORT.md` and update `DATASETS/dataset_info.md`.

---

## Ethics & Licensing

- Confirm the dataset license permits academic/educational use.
- Never re-distribute datasets in your GitHub repo without permission.
- Strip any personally identifiable information (PII) you encounter.
