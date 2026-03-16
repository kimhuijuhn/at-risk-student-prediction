## FAQ (Phase 1)

**Q1. What exactly is the target label? Can I change it?**

**A.** The label is  **hard-coded** :

<pre class="overflow-visible!" data-start="317" data-end="362"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>at_risk = </span><span>1</span><span></span><span> if</span><span> G3 < </span><span>10</span><span></span><span> else </span><span></span><span>0</span><span>
</span></span></code></div></div></pre>

Do **not** change this. The autograder **fails** if the rule is different, missing, or created elsewhere.

---

**Q2. Do I have to use your function/class names?**

**A.** Yes. We autograde structure. Implement these **exact** names:

<pre class="overflow-visible!" data-start="598" data-end="973"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>def </span><span></span><span>preprocess_data</span><span>(</span><span>df</span><span>): ...
</span><span>def</span><span></span><span> train_gb_pipeline</span><span>(</span><span>X, y</span><span>): ...

</span><span>class</span><span></span><span> DecisionTree</span><span>:
    </span><span>def</span><span></span><span>__init__</span><span>(</span><span>self, max_depth=None</span><span>): ...
    </span><span>def</span><span></span><span>fit</span><span>(</span><span>self, X, y</span><span>): ...
    </span><span>def</span><span></span><span>predict</span><span>(</span><span>self, X</span><span>): ...

</span><span>class</span><span></span><span> RandomForest</span><span>:
    </span><span>def</span><span></span><span>__init__</span><span>(</span><span>self, n_estimators=10</span><span>, max_depth=</span><span>None</span><span>, sample_size=</span><span>None</span><span>, random_state=</span><span>42</span><span>): ...
    </span><span>def</span><span></span><span>fit</span><span>(</span><span>self, X, y</span><span>): ...
    </span><span>def</span><span></span><span>predict</span><span>(</span><span>self, X</span><span>): ...
</span></span></code></div></div></pre>

---

**Q3. Which libraries can I use?**

**A.** Allowed: `pandas`, `numpy`, `scikit-learn` (preprocessing + **GradientBoostingClassifier** only), `pytest`.

Forbidden in Phase 1: `sklearn.RandomForest*`, `sklearn.DecisionTree*`, `xgboost`, `lightgbm`, `catboost`, AutoML.

We run a policy check; using banned APIs **fails** the tests.

---

**Q4. Do I need deep learning in Phase 1?**

**A.** No. Phase 1 is classical ML + your **from-scratch** Random Forest. Deep models (RNN/Transformer) can be explored in Phase 2.

---

**Q5. How are models evaluated? What are the minimums?**

**A.** Report **F1** and **ROC-AUC** on the validation split. You pass the metric gate if:

* **Gradient Boosting:** `F1 ≥ 0.40` **or** `F1 ≥ (dummy_F1 + 0.10)`; and preferably `ROC-AUC > 0.50`.
* **Random Forest (scratch):** `F1 ≥ 0.30` **or** `F1 ≥ (GB_F1 − 0.15)`; and preferably `ROC-AUC > 0.50`.

  These thresholds acknowledge class imbalance and hand-built trees.

---

**Q6. What is the “dummy baseline”? How do I compute it?**

**A.** A trivial classifier (e.g., always predicts the majority class). We’ll compute and compare to its **F1** so your model must beat it by **≥ 0.10** (for GB case).

---

**Q7. Train/validation split rules?**

**A.** Use a **stratified** split with a fixed seed (`random_state=42`). Don’t leak labels; don’t scale/fit encoders on the validation set.

---

**Q8. What counts as data leakage here?**

**A.** Feeding `G3` (final grade) directly into features, or creating `at_risk` **after** any transformation/split. Also avoid using `G2` in ways that implicitly reveal `G3`. Our tests check for leakage.

---

**Q9. How big is the dataset I should use locally?**

**A.** We provide a **mini dataset (~10% stratified)** for fast iteration. Tests may use the full UCI file. Your code must generalize (no hard-coded row counts).

---

**Q10. Can I tune hyperparameters?**

**A.** Yes—**but keep runtime reasonable** on the mini dataset (≤ ~30s). Prioritize correctness and clean structure over heavy tuning.

---

**Q11. My Random Forest is worse than Gradient Boosting—am I failing?**

**A.** Not necessarily. You pass if `F1_RF ≥ 0.30` **or** `F1_RF ≥ (F1_GB − 0.15)`. Your implementation must be structurally correct (bootstrapping + majority vote).

---

**Q12. Do I need to normalize to [0,1]?**

**A.** Yes. After `preprocess_data`, there should be **no object dtypes** and numeric features should be scaled to **[0,1]** (tolerance for tiny float error).

---

**Q13. Can I change file names or move functions into a notebook?**

**A.** No. Keep required code in `student_project/student_project.py`. We import these symbols in the autograder.

---

**Q14. What should my short report include?**

**A.** 1–2 pages: preprocessing summary, model configs, F1/ROC-AUC table, brief error analysis (what fails and why), and one takeaway.

---

**Q15. Common failure causes?**

* Not creating `at_risk` correctly (or at all)
* Leaving categorical columns unencoded
* Not scaling numerics
* Using banned APIs (sklearn RF/DT)
* Random Forest missing bootstrapping or majority vote
* Reporting only training accuracy
