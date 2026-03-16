# At Risk Student Prediction ML Pipeline

## 1. Use Full Dataset

This stage involves comparing F1 score of the Random Forest Classifier in Phase 1 using two datasets `student-mat.csv` and `student-mat-mini.csv`. The result was a **40% boost** in F1 score when training the classifier with `student-mat.csv`, which is the larger dataset.

## 2. Reduced Dataset Dimensionality with Feature Selection
This stage involves reducing the dimensionality of the dataset using feature importance approach. When calculating Gini impurity, we globally track the value for each node in the decision tree, providing the information of how each criterion is of more importance in terms of selecting the best feature to split. Then, we pick $k$ features with the highest importance to build the random forest classifier.

As a result, the best $k$ was 30, and the dataset with reduced dimensionality suffered 26.14% F1 score decrease but the elapsed time decreased 55.23%. This approach would be appropriate if runtime is prioritized than accuracy of the model.

## 3. Stacking

In this stage, the following base models will be trained.
* Logistic Regression (sklearn library)
* Support Vector Machines (sklearn library)
* Random Forest (implemented in phase 1)

Then, the predictions made by the three base models will be augmented into the dataset, with which the meta model (Random Forest in this case) will be trained on.

The result was a 34% boost in F1 score compared to baseline Random Forest classifier.

## Reflection
### What was your favorite/least favorite part of the project?
My most AND least favorite part of the project was building the decision tree from scratch. Implementing a data structure is one of my most favorite approach in studying, and I learned a lot from implementing decision trees. The reason why it was the least favorite was because when I moved onto implementing Random Forest classifiers I constantly had to restructure the whole class to make the classifier work, which was very challenging and time-consuming.

### On what topic from the course did your perspective change the most from before to after the project? Did your opinion of the usefulness of this topic go up or down after working with it within the context of the project?
Supervised learning was definitely had the most perspective change before and after the project, since it was the main topic of the final project. I had some experience in supervised learning when I was taking natural language processing, but I did not favor the approach due to excessive preprocessing it needs to accurately fit and predict. But for datasets similar to what we have dealt with the final project, I realized the advantages of supervised learning in terms of high accuracy and clear result.

### If you had more time, which scope item (or item from phase 1) that you implemented would you wish to improve the implementation of further and how might you try to do this?
If I had more time, I would have focused more on pseudocoding the decision tree and random forest implementation before diving into python code, which is a common mistake I make when I am coding. I opened up a Jupyter notebook and implemented as I go, but now I realize this was the wrong turn to take.

### If you had more time, what new scope item/ techniques would you like to try to apply and why?
I would have tried applying transformers. I skimmed through some readings describing what they were during Natural Language Processing course, but have not had the chance to actually implement one myself.

### Any recommendations to improve the project experience for future students? (optional)
Code reviews could be one of the ways the class would benefit from the project experience. Even if the code works, I was often unsure if this was the right way to write it and was curious about ways to improve it. And I am not saying that we should only receive reviews; I believe if students could have a peer review between themselves it would be a great experience.

### Roughly how many hours did you spend one phase 1 and phase 2 of the project respectively? This can be a 1 sentences answer and will not impact grade (optional)
* Phase 1: ~30 hours
* Phase 2: ~20 hours
