"""
Utility functions for the support vector machine classifier.

@copyright: The Broad Institute of MIT and Harvard 2015
"""

import numpy as np
import pandas as pd
import pickle

"""Return a function that gives a prediction from a design matrix row
"""
def gen_predictor(params_filename="./data/svm-params"):
    clf = pickle.load(open(params_filename, "rb" ) )

    def predictor(X):
        scores = clf.predict_proba(X)
        probs = [x[1] for x in scores]
        return probs

    return predictor