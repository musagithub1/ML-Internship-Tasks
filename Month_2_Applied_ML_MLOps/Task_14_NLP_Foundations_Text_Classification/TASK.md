# 📋 TASK 14 — NLP Foundations — Text Classification

| Attribute | Value |
|-----------|-------|
| Difficulty | ⭐⭐⭐ Intermediate-Advanced |
| Estimated Time | 5-6 days |
| Prerequisites | Tasks 06, 10 |
| Key Skills | Text preprocessing (tokenization, stemming, lemmatization, stopwords), BoW, TF-IDF, word embeddings (Word2Vec/GloVe), text classification with traditional ML, confusion matrix per class |

---

## 🎯 Learning Objectives
After completing this task, you should be able to:
1. Understand the core principles of nlp foundations — text classification
2. Apply the relevant tools and techniques to a real-world dataset
3. Interpret the results in a business context
4. Document and communicate your findings effectively
5. Defend your technical decisions

---

## 🏢 Business Scenario
E-commerce platform receives 50K product reviews/day. Manual moderation costs $200K/year. You need to build an automated sentiment classifier that's 90%+ accurate to flag negative reviews for urgent response (within 2 hours).

---

## 📐 Detailed Requirements

### 1. Data Processing
- [ ] Load the dataset: **IMDB Reviews OR 20 Newsgroups (sklearn)**
- [ ] Perform appropriate data cleaning and preprocessing
- [ ] Document all transformations and justify them

### 2. Implementation
- [ ] Implement the core solution using text preprocessing pipeline, TF-IDF vectorization, multiple classifier comparison, text-specific evaluation
- [ ] Follow best practices for NLP Foundations — Text Classification
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
**Name:** IMDB Reviews OR 20 Newsgroups (sklearn)
See `DATASETS/dataset_info.md` for full details and alternative sources.
