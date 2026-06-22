# 📈 EXAMPLES — Task 19: NLP Project: Transformer Fine-Tuning

This folder contains **illustrative example outputs** so you know what "good" looks like. Do not copy them — use them as a target quality bar.

---

## Example Output Structure

```
EXAMPLES/
├── example_report.md       # A skeleton report with the right tone
├── example_metrics.json    # Sample metrics dump
└── example_figure.txt      # Description of what a "great" chart looks like (image generated at runtime)
```

---

## Example Executive Summary (target tone)

> "We trained 3 candidate models on 7,043 customer records. The XGBoost model achieved a recall of 0.81 on the churn class at a precision of 0.62, beating logistic regression by 14 recall points. Tenure, contract type, and monthly charges are the dominant drivers (SHAP). We recommend deploying the XGBoost model behind a 0.35 probability threshold, which is projected to recover ~$220K/quarter in retained revenue. Limitations: the dataset is from a single region and 2 years old — we recommend a quarterly retraining cadence."

5 bullets. No jargon. Numbers everywhere. Recommendation explicit.

---

## Example Figure Quality Checklist

- [ ] Title in plain English (not `df.column_name`)
- [ ] Axes labeled with units
- [ ] Legend if multiple series
- [ ] Colorblind-safe palette (`viridis`, `cividis`)
- [ ] Source / data caveat in a small caption
- [ ] Saved at ≥150 DPI
