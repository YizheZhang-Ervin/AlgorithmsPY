import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from pandas_datareader import DataReader
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt


def CTA():
    dt1 = DataReader("MA", "yahoo", datetime(2020, 1, 1), datetime(2020, 8, 31))
    DATA1 = pd.DataFrame(dt1["Adj Close"].values)
    dt2 = DataReader("V", "yahoo", datetime(2020, 1, 1), datetime(2020, 8, 31))
    DATA2 = pd.DataFrame(dt2["Adj Close"].values)

    y = np.array(DATA1)
    # y = y.reshape(-1,1)
    x = np.array(DATA2)
    # x = x.reshape(-1,1)
    T = DATA1.shape[0]
    k = 90
    Beta = np.zeros(T - k)
    z_score = np.zeros(T - k)
    for t in range(k, T):
        Y = y[t - k : t]
        X = x[t - k : t]
        # OLS REGRESSION STARTS: ROLLING WINDOW APPROACH
        # LINEAR REGRESSION of Y: T x 1 on
        # Regressors X: T x N
        # OLS_estimates for coefficents: X x 1
        invXX = np.linalg.inv(X.transpose() @ X)
        Beta[t - k] = invXX @ X.transpose() @ Y
        Spread = Y - X * Beta[t - k]
        "k x 1"
        mu = np.mean(Spread)
        sigma = np.std(Spread)
        z_score[t - k] = (Spread[-1] - mu) / sigma

    # Long: if z-score <= - predetermined threshold,
    # Short: if z-score >= pre-determined threshold.
    # Exit: |z-score| <= an additional threshold.

    timevec = np.linspace(1, T - k - 1, T - k - 1)
    plt.figure(figsize=(15, 5))
    plt.plot(timevec, z_score[1:], "b")
    plt.ylabel("z_score(t)")
    plt.title("Z-score")

    plt.plot(timevec, Beta[1:], "r")


if __name__ == "__main__":
    CTA()