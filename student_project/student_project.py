# student_project/student_project.py
"""
Student starter (broken by design) for CS5100 Phase 1.
This file is intentionally TODO-heavy. Students must implement the functions
below to pass the tests.

Design goals:
- Clear error messages (NotImplementedError) instead of silent wrong types.
- Helpful guidance in docstrings about expected behavior.
- Safe to import (no heavy compute at import time).
"""
import os

import pandas
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


# -------------------------
# Section A: Data Loading
# -------------------------
def load_data(path=None):
    """
    Load the student dataset.

    Behavior expected by autograder / tests:
    - If path is None:
        prefer "student-mat-mini.csv" in repo root (fast), else
        prefer "datasets/student-mat-mini.csv", else
        fall back to "datasets/student-mat.csv" or "student-mat.csv".
    - Return: pandas.DataFrame

    NOTE TO STUDENTS: Implement this to read CSV using the correct separator
    (UCI full dataset uses ';'). If you don't have the full dataset locally,
    run the provided generator script to create the mini CSV.

    Currently this function is left as a TODO for you to implement.
    """
    # Helpful explicit error rather than returning None
    # Students should implement the loading logic described above.

    # if there is no path given, try one of the alternate paths.
    alternate_paths = [
        "student-mat-mini.csv",
        "datasets/student-mat-mini.csv",
        "datasets/student-mat.csv",
        "student-mat.csv"
    ]

    # when submitting, use current_path
    current_path = os.getcwd()
    parent_path = os.path.dirname(current_path)

    while path is None:
        for i in range(len(alternate_paths)):
            path = parent_path + os.sep + alternate_paths[i]
            if os.path.exists(path):
                break
            else:
                print("File not found in ", path)
                continue

    print(f"File found in {path},\nloading...")
    df = pd.read_csv(path, sep=None, engine='python')
    return df

# -------------------------
# Section B: Exploratory / Preprocessing helpers
# -------------------------
def summary_stats():
    """
    Return a dictionary of summary statistics, e.g.:
        {"mean_G3": ..., "median_absences": ...}
    """
    df = load_data()
    summary = dict()
    summary["F_count"] = df["sex"].str.count("F").count()

    summary["mean_G1"] = df["G1"].mean()
    summary["mean_G2"] = df["G2"].mean()
    summary["mean_G3"] = df["G3"].mean()
    summary["median_absences"] = df["absences"].median()

    return summary

def compute_correlations():
    """
    Compute and return a pandas DataFrame of correlations (df.corr()) for numeric columns.
    """
    df = load_data()
    return df.corr()

def preprocess_data(df: pd.DataFrame):
    """
    Preprocess the provided DataFrame and return a processed DataFrame ready for modeling.

    Expected contract (must meet autograder checks):
    - Create target column 'at_risk' as: (df['G3'] < 10).astype(int)
    - Drop grade columns (G1, G2, G3) from the feature matrix to avoid leakage
    - Encode categorical variables (one-hot or similar) so NO object dtypes remain
    - Impute missing values
    - Scale numeric columns to [0,1] range
    - Return a pandas DataFrame that includes 'at_risk' and only numeric columns otherwise

    NOTE: Tests assert target is exactly (G3 < 10) and will fail if you change it.
    """

    # fill missing values with 0
    df = df.fillna(0)

    # create target column
    df["at_risk"] = (df["G3"] < 10).astype(int)

    # drop grade columns
    df.drop(columns=["G1"], inplace=True)
    df.drop(columns=["G2"], inplace=True)
    df.drop(columns=["G3"], inplace=True)

    # encode boolean features
    boolean_features = [
        "schoolsup", "famsup", "paid", "activities", "nursery", "higher",
        "internet", "romantic"
    ]
    for feature in boolean_features:
        df[feature] = np.where(df[feature] == "yes", np.float64(1), np.float64(0))

    # scale numeric values
    df = scale_numeric_values(df)

    # encode categorical features
    df = one_hot_encode(df)

    return df

def one_hot_encode(df):
    """ One hot encode categorical features in pandas DataFrame """
    categorical_features = (df.select_dtypes(include=["object"])
                            .columns.tolist())
    encoder = OneHotEncoder(sparse_output=False)
    one_hot_encoded = encoder.fit_transform(df[categorical_features])
    one_hot_df = pd.DataFrame(
        one_hot_encoded,
        columns=encoder.get_feature_names_out(categorical_features))
    df_encoded = pd.concat([one_hot_df, df], axis=1)
    df_encoded = df_encoded.drop(categorical_features, axis=1)

    return df_encoded

def scale_numeric_values(df):
    """ Scale numeric features in pandas DataFrame into [0,1] range """
    # get names of numeric features
    numeric_features = df.select_dtypes(include=["number"]).columns.tolist()
    numeric_features.remove("at_risk")

    # take the max value from dataset, scale each value with it by division
    df_scaled = df[numeric_features] / df[numeric_features].max()
    df[numeric_features] = df_scaled[numeric_features]

    return df

# -------------------------
# Section B: Gradient Boosting Pipeline (Broken starter)
# -------------------------
def train_gb_pipeline(X_train=None, y_train=None):
    """
    Build and fit a sklearn Pipeline that includes:
      ("preprocessor", ColumnTransformer(...)) and ("classifier", GradientBoostingClassifier)

    - Must return a fitted sklearn-like pipeline with .predict() and preferably .predict_proba()
    - Tests expect a named step "preprocessor" to exist (if you return a Pipeline)
    """
    try:
        from sklearn.pipeline import Pipeline
        from sklearn.ensemble import GradientBoostingClassifier
    except Exception:
        raise NotImplementedError("sklearn not available in the environment; install dependencies.")

    preprocessor = ColumnTransformer(transformers=[], remainder="passthrough")

    model = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("classifier", GradientBoostingClassifier())
    ])

    model.fit(X_train, y_train)
    return model

# -------------------------
# Section C: Random Forest (From Scratch) skeleton
# -------------------------

class Tree():
    def __init__(self, X, y, features:pandas.Index, depth=0, track_feature_importance=False, feature_importances=None):
        self.X = X
        self.y = y
        self.features = features
        self.left = None
        self.right = None
        self.is_leaf = False
        self.depth = depth
        self.track_feature_importance = track_feature_importance
        self.feature_importances = feature_importances if feature_importances is not None else {}

    def is_leaf(self):
        return len(self.y.unique()) == 1

    def build_tree(self, X, y, features, depth=0):
        # Check if we have features to split on
        if len(self.features) == 0:
            print(f"No features left at depth {self.depth}, stopping.")
            self.is_leaf = True
            return

        feature = find_best_feature(X, y, self.features)

        # If no valid feature found (shouldn't happen but check for safety)
        if feature is None:
            print(f"No valid feature found at depth {self.depth}, stopping.")
            self.is_leaf = True
            return

        new_features = self.features.drop(feature)
        print(f"Splitting tree with: {feature}")

        # Track feature importance if enabled
        if self.track_feature_importance:
            reduction = calculate_gini_reduction(X, y, feature)
            if feature in self.feature_importances:
                self.feature_importances[feature] += reduction
            else:
                self.feature_importances[feature] = reduction

        # if categorical, right subtree is true samples
        if is_categorical_feature(X, feature):
            left_X = X[X[feature] == 0]
            right_X = X[X[feature] == 1]

        # if numeric, right subtree is more than mean
        else:
            mean = X[feature].mean()
            left_X = X[X[feature] <= mean]
            right_X = X[X[feature] > mean]
        print(f"left_X: {len(left_X)}\t right_X: {len(right_X)}")

        # build tree from left and right X
        left_y = y[y.index.isin(left_X.index)]
        right_y = y[y.index.isin(right_X.index)]
        self.left = Tree(left_X, left_y, new_features, self.depth + 1, self.track_feature_importance, self.feature_importances)
        self.right = Tree(right_X, right_y, new_features, self.depth + 1, self.track_feature_importance, self.feature_importances)

        # determine if any of the subtree contains homogenous y value
        if len(left_y.unique()) == 1:
            print(f"Left node is leaf (indices: {left_y.index.tolist()})")
            self.left.is_leaf = True
        if len(right_y.unique()) == 1:
            print(f"Right node is leaf (indices: {right_y.index.tolist()})")
            self.right.is_leaf = True

        # recursively call build_leaf() until leaf is reached
        # Also check if there are features left to continue building
        if not self.left.is_leaf and len(new_features) > 0:
            print(f"\nBuilding left subtree at depth {self.left.depth}")
            self.left.build_tree(left_X, left_y, new_features, self.left.depth)
        elif not self.left.is_leaf and len(new_features) == 0:
            print(f"Left subtree at depth {self.left.depth} has no features left, marking as leaf")
            self.left.is_leaf = True

        if not self.right.is_leaf and len(new_features) > 0:
            print(f"\nBuilding right subtree at depth {self.right.depth}")
            self.right.build_tree(right_X, right_y, new_features, self.right.depth)
        elif not self.right.is_leaf and len(new_features) == 0:
            print(f"Right subtree at depth {self.right.depth} has no features left, marking as leaf")
            self.right.is_leaf = True

class DecisionTree:
    def __init__(self, X:pd.DataFrame, y:pd.Series, features, max_depth=np.isinf, track_feature_importance=False):
        """
        Simple DecisionTree skeleton. Students may implement any reasonable tree
        representation (tuple/dict/class with 'predict' method).
        """
        self.X = X  # complete dataset
        self.y = y
        self.features = features  # list of features in dataset
        self.left = None
        self.right = None

        self.max_depth = max_depth
        self.track_feature_importance = track_feature_importance
        self.feature_importances = {}
        self.tree = Tree(self.X, self.y, self.features, 0, track_feature_importance, self.feature_importances)

    def fit(self, X, y):
        """Student: implement recursive split building and store in self.tree"""
        # raise NotImplementedError("DecisionTree.fit not implemented (student task)")

        criteria = find_best_feature(X, y, self.features)
        self.criteria = criteria
        # select best feature, exclude it from new features
        new_features = self.features.drop(criteria)
        print(f"Splitting tree with: {criteria}")

        # Track feature importance if enabled
        if self.track_feature_importance:
            reduction = calculate_gini_reduction(X, y, criteria)
            if criteria in self.feature_importances:
                self.feature_importances[criteria] += reduction
            else:
                self.feature_importances[criteria] = reduction

        # if categorical, right subtree is true samples
        if is_categorical_feature(X, criteria):
            left_X = X[X[criteria] == 0]
            right_X = X[X[criteria] == 1]

        # if numeric, right subtree is more than mean
        else:
            mean = X[criteria].mean()
            left_X = X[X[criteria] <= mean]
            right_X = X[X[criteria] > mean]

        print(f"left_X: {len(left_X)}\t right_X: {len(right_X)}")

        # build tree from left and right X
        left_y = y[y.index.isin(left_X.index)]
        right_y = y[y.index.isin(right_X.index)]
        self.tree.left = Tree(left_X, left_y, new_features, self.tree.depth + 1, self.track_feature_importance, self.feature_importances)
        self.tree.right = Tree(right_X, right_y, new_features, self.tree.depth + 1, self.track_feature_importance, self.feature_importances)

        # determine if any of the subtree contains homogenous y value
        if len(left_y.unique()) == 1:
            print(f"Left node is leaf (indices: {left_y.index.tolist()})")
            self.tree.left.is_leaf = True
        if len(right_y.unique()) == 1:
            print(f"Right node is leaf (indices: {right_y.index.tolist()})")
            self.tree.right.is_leaf = True

        # recursively call build_leaf() until leaf is reached
        if not self.tree.left.is_leaf:
            print(f"Building left subtree in depth {self.tree.left.depth}")
            self.tree.left.build_tree(left_X, left_y, new_features, self.tree.left.depth)
        if not self.tree.right.is_leaf:
            print(f"Building right subtree in depth {self.tree.right.depth}")
            self.tree.right.build_tree(right_X, right_y, new_features, self.tree.right.depth)

    def predict(self, X):
        """Student: implement prediction traversal using self.tree"""
        # raise NotImplementedError("DecisionTree.predict not implemented (student task)")
        predictions = []
        for idx in X.index:
            prediction = self._predict_single(X.loc[idx], self.tree)
            predictions.append(prediction)
        return np.array(predictions)

    def _predict_single(self, sample, node):
        """Helper method to predict a single sample by traversing the tree"""
        # If we reached a leaf node, return the majority class
        if node.is_leaf or node.left is None or node.right is None:
            return node.y.mode()[0] if len(node.y) > 0 else 0

        # Get the feature value for this node's criteria
        feature = find_best_feature(node.X, node.y, node.features)
        feature_value = sample[feature]

        # Decide whether to go left or right
        if is_categorical_feature(node.X, feature):
            # For categorical: left = 0, right = 1
            if feature_value == 0:
                return self._predict_single(sample, node.left)
            else:
                return self._predict_single(sample, node.right)
        else:
            # For numeric: left <= mean, right > mean
            mean = node.X[feature].mean()
            if feature_value <= mean:
                return self._predict_single(sample, node.left)
            else:
                return self._predict_single(sample, node.right)

class RandomForest:
    def __init__(self, n_estimators=10, max_depth=None, sample_size=None, random_state=42,
                 track_feature_importance=False):
        """
        RandomForest skeleton (bagging). Students must implement fit/predict.
        The autograder expects:
         - fit(X, y): populates self.trees (list of DecisionTree instances)
         - predict(X): returns a list/array of labels (same length as X)
        """
        self.n_estimators = int(n_estimators)
        self.max_depth = max_depth
        self.sample_size = sample_size
        self.random_state = random_state
        self.track_feature_importance = track_feature_importance
        self.trees = []
        self.feature_importances = None

    def fit(self, X, y):
        """Student: implement bagging + DecisionTree training"""
        # raise NotImplementedError("RandomForest.fit not implemented (student task)")
        np.random.seed(self.random_state)

        # Convert to pandas if numpy arrays are passed
        if isinstance(X, np.ndarray):
            X = pd.DataFrame(X)
        if isinstance(y, np.ndarray):
            y = pd.Series(y)

        # Default sample size to full dataset if not specified
        sample_size = self.sample_size if self.sample_size is not None else len(X)

        for i in range(self.n_estimators):
            print(f"\nTRAINING TREE {i + 1}/{self.n_estimators}")
            bootstrap_indices = np.random.choice(X.index, size=sample_size, replace=True)

            # bootstrap
            X_bootstrap = X.loc[bootstrap_indices]
            y_bootstrap = y.loc[bootstrap_indices]

            # train and add decision tree to self.tree
            tree = DecisionTree(X_bootstrap, y_bootstrap, X.columns, self.max_depth, self.track_feature_importance)
            tree.fit(X_bootstrap, y_bootstrap)
            self.trees.append(tree)

        print(f"TRAINING COMPLETE WITH A TOTAL OF {len(self.trees)} TREES.")

        # Calculate feature importances if tracking is enabled
        if self.track_feature_importance:
            self._compute_feature_importances()

    def predict(self, X):
        """Student: implement majority-vote across self.trees"""
        # raise NotImplementedError("RandomForest.predict not implemented (student task)")

        # Convert to pandas if numpy array is passed
        if isinstance(X, np.ndarray):
            X = pd.DataFrame(X)

        # store predictions from each training tree
        all_predictions = []
        for tree in self.trees:
            predictions = tree.predict(X)
            all_predictions.append(predictions)

        # Convert list to numpy array for easier indexing
        all_predictions = np.array(all_predictions)

        # Majority Vote
        y = []
        for i in range(len(X)):
            sample_predictions = all_predictions[:, i]
            unique, counts = np.unique(sample_predictions, return_counts=True)
            majority_vote = unique[np.argmax(counts)]
            y.append(majority_vote)

        return np.array(y)

    def _compute_feature_importances(self):
        """ Aggregate feature importances from all trees and normalize. """
        # Aggregate importances from all trees
        total_importances = {}
        for tree in self.trees:
            for feature, importance in tree.feature_importances.items():
                if feature in total_importances:
                    total_importances[feature] += importance
                else:
                    total_importances[feature] = importance

        # Normalize to sum to 1
        total_sum = sum(total_importances.values())
        if total_sum > 0:
            self.feature_importances = {
                feature: importance / total_sum
                for feature, importance in total_importances.items()
            }
        else:
            self.feature_importances = total_importances

    def get_feature_importances(self):
        """
        Return feature importances as a dictionary.
        Returns None if track_feature_importance was not enabled during training.
        """
        if not self.track_feature_importance:
            return None
        return self.feature_importances

    def select_top_k_features(self, k):
        """
        Select the top K most important features based on feature importance.

        Args:
            k: Number of top features to select

        Returns:
            List of top K feature names, sorted by importance (descending)
            Returns None if track_feature_importance was not enabled during training.

        Example:
            rf = RandomForest(track_feature_importance=True)
            rf.fit(X_train, y_train)
            top_features = rf.select_top_k_features(10)
            X_train_reduced = X_train[top_features]
            X_test_reduced = X_test[top_features]
        """
        if not self.track_feature_importance:
            print("Warning: feature importance tracking was not enabled during training.")
            return None

        if self.feature_importances is None:
            print("Warning: no feature importances available. Train the model first.")
            return None

        # Sort features by importance (descending)
        sorted_features = sorted(
            self.feature_importances.items(),
            key=lambda x: x[1],
            reverse=True
        )

        # Return top K feature names
        top_k = min(k, len(sorted_features))
        return [feature for feature, _ in sorted_features[:top_k]]


# --------------------------------------------------
# UTILITY FUNCTIONS
# --------------------------------------------------
def is_categorical_feature(df, column):
    unique_values = df[column].unique()
    return unique_values.shape[0] == 2 and 1 in unique_values and 0 in unique_values


def find_best_feature(X:pd.DataFrame, y:pd.Series, features:pd.Index):
    """ Find the best feature to split the decision tree. """
    best_feature = None
    gini = float("inf")
    for f in features:
        current_gini = get_gini(X, y, f)
        if current_gini < gini:
            best_feature, gini = f, current_gini

    return best_feature


def get_gini(X:pd.DataFrame, y:pd.Series, feature):
    """
    Gets Gini Impurity value of a feature split.
    For numeric values, determine using mean value.
    Returns the weighted Gini impurity after splitting on the feature.
    """
    # Split data based on feature type
    if is_categorical_feature(X, feature):
        left_mask = X[feature] == 0
        right_mask = X[feature] == 1
    else:
        mean = X[feature].mean()
        left_mask = X[feature] <= mean
        right_mask = X[feature] > mean

    # Get target values for each split
    left_y = y[left_mask]
    right_y = y[right_mask]

    total_count = len(y)
    left_count = len(left_y)
    right_count = len(right_y)

    # Handle edge case where split puts all samples on one side
    if left_count == 0 or right_count == 0:
        return float("inf")

    # Calculate Gini impurity for left subset
    left_gini = 1.0
    for class_val in left_y.unique():
        p = (left_y == class_val).sum() / left_count
        left_gini -= p ** 2

    # Calculate Gini impurity for right subset
    right_gini = 1.0
    for class_val in right_y.unique():
        p = (right_y == class_val).sum() / right_count
        right_gini -= p ** 2

    # Return weighted average of Gini impurities
    weighted_gini = (left_count / total_count) * left_gini + (right_count / total_count) * right_gini
    return weighted_gini


def calculate_gini_reduction(X:pd.DataFrame, y:pd.Series, feature):
    """
    Calculate the Gini reduction (importance) for a feature split.
    Gini reduction = parent_gini - weighted_child_gini
    """
    # Calculate parent Gini impurity
    total_count = len(y)
    parent_gini = 1.0
    for class_val in y.unique():
        p = (y == class_val).sum() / total_count
        parent_gini -= p ** 2

    # Get the weighted child Gini (this is what get_gini returns)
    weighted_child_gini = get_gini(X, y, feature)

    # If the split is invalid, return 0
    if weighted_child_gini == float("inf"):
        return 0

    # Gini reduction is the decrease in impurity
    gini_reduction = parent_gini - weighted_child_gini
    return gini_reduction
