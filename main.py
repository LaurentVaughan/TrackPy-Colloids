import numpy as np
import pandas as pd
from pandas import DataFrame, Series  # for convenience

import pims
import trackpy as tp


def f(x):
    y = np.exp(x)
    return y


print(f(0))
