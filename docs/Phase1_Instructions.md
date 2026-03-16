# Phase 1 Project Instructions: Student Success Prediction

**Foundations of Artificial Intelligence — Fall 2025**

**Phase 1 Duration:** ~1 week

**Repo Path:** `docs/Phase1_Instructions.md`

**Group Size:** 1–2 students

---

## Goal

In Phase 1, you will:

* Debug and complete a baseline ML pipeline
* Fix data preprocessing and a Gradient Boosting pipeline
* Implement a **Random Forest from scratch** (no sklearn trees)
* Evaluate your models using real metrics (F1, ROC-AUC)

This phase simulates working in an applied ML team: you inherit code, fix it, and make it work correctly and reliably.

---

## Deliverables

| Deliverable                         | File                                   |
| ----------------------------------- | -------------------------------------- |
| Core implementation                 | `student_project/student_project.py` |
| (Optional) Notebook for exploration | `notebooks/phase1_experiments.ipynb` |
| Must pass tests              | `pytest tests/test_phase_1.py` |

---

## Files Provided

<pre class="overflow-visible!" data-start="1145" data-end="1374"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>student_project/
├── student_project.py  </span><span># starter code with intentional bugs</span><span>
datasets/
├── student-mat.csv  </span><span># Full UCI dataset</span><span>
├── student-mat-mini.csv  </span><span># ~10% stratified sample of UCI dataset</span><span>
tests/
├── conftest.py
├── test_phase_1.py
docs/
├── Phase1_FAQs.md
└── Phase1_Instructions.md (this file)
</span></span></code></div></div></pre>

---

## What You're Building

You are training models to flag students **at risk of failing** :

<pre class="overflow-visible!" data-start="1475" data-end="1512"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>at_risk</span><span> = </span><span>1</span><span> if G3 < </span><span>10</span><span> else </span><span>0</span><span>
</span></span></code></div></div></pre>

(turning it into a **binary classification task)**

You will:

### 1) Preprocess the data

* Remove missing values
* Encode categoricals
* Scale numeric columns to `[0,1]`
* Return a clean DataFrame with **no object dtypes**

### 2) Fix the Gradient Boosting pipeline

* Use `sklearn.Pipeline` with preprocessor + classifier
* Train and evaluate on a validation split

### 3) Build Random Forest from scratch

* `DecisionTree.fit/predict`
* `RandomForest.fit/predict` with bootstrapping + majority vote
* **No sklearn tree or RF APIs**

---

## Evaluation Metrics

You must report:

* **F1 score**
* **ROC-AUC**

Minimum expected performance on the mini dataset:

| Model                   | Requirement                                                    |
| ----------------------- | -------------------------------------------------------------- |
| Gradient Boosting       | F1 ≥ 0.40 **OR** F1_model ≥ (F1_dummy + 0.10)          |
| Random Forest (scratch) | F1 ≥ 0.30 **OR** F1 ≥ (F1_gradient_boosting − 0.15) |
| Either model            | ROC-AUC > 0.50                                                 |

We give slack because hand-built trees are simpler — but they must meaningfully outperform random guessing.

---

## Library & API Rules

Allowed:

* `pandas`, `numpy`
* `sklearn` (only for GradientBoosting + preprocessing tools)
* `pytest`

Forbidden in Phase 1:

* `sklearn.RandomForest*`
* `sklearn.DecisionTree*`
* XGBoost / LightGBM / CatBoost
* AutoML libraries

If we detect these, tests will fail.

---

## Testing

Run tests locally:

<pre class="overflow-visible!" data-start="2796" data-end="2842"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>pytest tests/test_phase_1.py
</span></span></code></div></div></pre>

Tests check:

* I/O and core functionality
* No leakage (G1/G2/G3 not directly fed to models)
* Data fully numeric and scaled
* Correct class names + methods
* Bootstrapped trees actually created
* Metric thresholds
* Verify structure, correctness, and quality

---

## Code Requirements

Your code **must implement** these classes/methods:

<pre class="overflow-visible!" data-start="3231" data-end="3543"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>class</span><span></span><span> DecisionTree</span><span>:
    </span><span>def</span><span></span><span>__init__</span><span>(</span><span>self, max_depth=None</span><span>): ...
    </span><span>def</span><span></span><span>fit</span><span>(</span><span>self, X, y</span><span>): ...
    </span><span>def</span><span></span><span>predict</span><span>(</span><span>self, X</span><span>): ...

</span><span>class</span><span></span><span> RandomForest</span><span>:
    </span><span>def</span><span></span><span>__init__</span><span>(</span><span>self, n_estimators=10</span><span>, max_depth=</span><span>None</span><span>, sample_size=</span><span>None</span><span>, random_state=</span><span>42</span><span>): ...
    </span><span>def</span><span></span><span>fit</span><span>(</span><span>self, X, y</span><span>): ...
    </span><span>def</span><span></span><span>predict</span><span>(</span><span>self, X</span><span>): ...
</span></span></code></div></div></pre>

We check for:

* Bootstrapping
* Recursive splits or stumps
* Majority voting

---

## Suggested Workflow

| Step | Task                                            |
| ---- | ----------------------------------------------- |
| 1    | Run public tests → see failures                |
| 2    | Fix `load_data` + target creation             |
| 3    | Implement preprocessing pipeline                |
| 4    | Debug Gradient Boosting pipeline                |
| 5    | Implement DecisionTree + test small input       |
| 6    | Build RandomForest + verify `trees` populated |
| 7    | Run metrics on mini dataset                     |
| 8    | Pass all tests                           |

---

## Tips

* Start simple: shallow trees, clear splits
* Stratified train/validation split
* Use `random_state=42`
* Debug printed shapes, dtypes, and class balance

Common mistakes to avoid:

* Data leakage
* Forgetting to scale numeric columns
* Incorrect majority voting
* Predicting wrong shape (must match X rows)
* Only reporting training accuracy — **not acceptable**

---

## Phase 1 Rubric
We have 18 tests in total; passing each test will be rewarded with 1 point.

## After Phase 1

You will move to  **Phase 2** :

* Improve models
* Add planning / optimization
* Optional: uncertainty modeling (Bayesian, HMMs)

But for now — focus on **making the baseline pipeline correct and measurable.**

Good luck, and have fun — you're building a real ML pipeline, not a toy script.
