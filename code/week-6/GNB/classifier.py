import numpy as np
import random
from math import sqrt, pi, exp

def gaussian_prob(obs, mu, sig):
    # Calculate Gaussian probability given
    # - observation
    # - mean
    # - standard deviation
    num = (obs - mu) ** 2
    denum = 2 * sig ** 2
    norm = 1 / sqrt(2 * pi * sig ** 2)
    return norm * exp(-num / denum)

# Gaussian Naive Bayes class
class GNB():
    # Initialize classification categories
    def __init__(self):
        self.classes = ['left', 'keep', 'right']

    # Given a set of variables, preprocess them for feature engineering.
    def process_vars(self, vars):
        # The following implementation simply extracts the four raw values
        # given by the input data, i.e. s, d, s_dot, and d_dot.
        s, d, s_dot, d_dot = vars
        return s, d, s_dot, d_dot

    # Train the GNB using a combination of X and Y, where
    # X denotes the observations (here we have four variables for each) and
    # Y denotes the corresponding labels ("left", "keep", "right").
    def train(self, X, Y):
        '''
        Collect the data and calculate mean and standard variation
        for each class. Record them for later use in prediction.
        '''
        # TODO: implement code.
        r_v = [[0.], [0.], [0.], [0.]]
        l_v = [[0.], [0.], [0.], [0.]]
        k_v = [[0.], [0.], [0.], [0.]]


        proc_x = [list(self.process_vars(x)) for x in X]

        for val, label in zip(proc_x, Y):
            if label == "right":
                for i, r in enumerate(val):
                    r_v[i].append(r)
            elif label == "left":
                for i, l in enumerate(val):
                    l_v[i].append(l)
            elif label == "keep":
                for i, k in enumerate(val):
                    k_v[i].append(k)

        r_v = np.array(r_v)
        self.r_m = [v.mean() for v in r_v]
        self.r_std = [v.std() for v in r_v]

        l_v = np.array(l_v)
        self.l_m = [v.mean() for v in l_v]
        self.l_std = [v.std() for v in l_v]

        k_v = np.array(k_v)
        self.k_m = [v.mean() for v in k_v]
        self.k_std = [v.std() for v in k_v]

    # Given an observation (s, s_dot, d, d_dot), predict which behaviour
    # the vehicle is going to take using GNB.
    def predict(self, observation):
        '''
        Calculate Gaussian probability for each variable based on the
        mean and standard deviation calculated in the training process.
        Multiply all the probabilities for variables, and then
        normalize them to get conditional probabilities.
        Return the label for the highest conditional probability.
        '''
        # TODO: implement code.

        r_pr = l_pr = k_pr = 1.
        r_norm = l_norm = k_norm = 0.

        for i, obs in enumerate(observation):
            r_pr = r_pr * gaussian_prob(obs,self.r_m[i], self.r_std[i])
            r_norm = r_norm + gaussian_prob(obs,self.r_m[i], self.r_std[i])

            l_pr = l_pr * gaussian_prob( obs,self.l_m[i], self.l_std[i])
            l_norm = l_norm + gaussian_prob( obs,self.l_m[i], self.l_std[i])

            k_pr = k_pr * gaussian_prob( obs,self.k_m[i], self.k_std[i])
            k_norm = k_norm + gaussian_prob(obs, self.k_m[i], self.k_std[i])

        r_pr = r_pr / r_norm
        l_pr = l_pr / l_norm
        k_pr = k_pr / k_norm

        idx = np.argmax([l_pr , k_pr, r_pr])

        return self.classes[idx]
