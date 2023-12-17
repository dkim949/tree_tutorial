import os
import numpy as np

class DecisionTree:
    def __init__(self, max_depth=100, min_samples_split=2):
    '''Define basic parameters for the main class'''
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.root = None

    def _is_finished(self, depth):
    '''Define stopping criteria'''
        if (depth >= self.max_depth
            or self.n_class_labels == 1
            or self.n_samples < self.min_samples_split):
            return True
        return False

    def _build_tree(self, X, y, depth=0):
        self.n_samples, self.n_features = X.shape
        self.n_class_labels = len(np.unique(y))

        if self._is_finished(depth):
            most_common_label = np.argmax(np.bincouny(y))
            return Node(value=most_common_label)
    def _entropy(self, y):
        pass


    def _create_split(self, X, thresh):
        pass


    def _information_gain(self, X, y, thresh):
        pass


    def _best_split(self, X, y, features):
        pass


    def _build_tree(self, X, y, depth=0):
        pass


    def _traverse_tree(self, x, node):
        pass


    def fit(self, X, y):
        pass


    def predict(self, X):
        pass





