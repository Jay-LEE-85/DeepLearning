# Load library

import numpy as np
import matplotlib.pyplot as plt

# custom function

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

def relu(x):
  return np.maximum(0, x)