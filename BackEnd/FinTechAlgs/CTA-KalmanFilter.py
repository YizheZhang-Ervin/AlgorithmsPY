import numpy as np
import pandas as pd
import pyflux as pf
from scipy.optimize import minimize
from pandas_datareader import DataReader
from datetime import datetime
import matplotlib.pyplot as plt


def Kalman_Filter(param, *args):
    S = Y.shape[0]
    S = S + 1
    #  Initialize Params:
    T = param[0]
    H = param[1]
    Q = param[2]
    #  Kalman Filter Starts:
    u_predict = np.zeros(S)
    u_update = np.zeros(S)
    P_predict = np.zeros(S)
    P_update = np.zeros(S)
    v = np.zeros(S)
    F = np.zeros(S)
    KF_Dens = np.zeros(S)
    for s in range(1, S):
        if s == 1:
            P_update[s] = 1000
            P_predict[s] = T * P_update[1] * np.transpose(T) + Q
        else:
            F[s] = X[s - 1] * P_predict[s - 1] * np.transpose(X[s - 1]) + H
            v[s] = Y[s - 1] - X[s - 1] * u_predict[s - 1]
            u_update[s] = (
                u_predict[s - 1]
                + P_predict[s - 1] * np.transpose(X[s - 1]) * (1 / F[s]) * v[s]
            )
            u_predict[s] = T * u_update[s]
            P_update[s] = (
                P_predict[s - 1]
                - P_predict[s - 1]
                * np.transpose(X[s - 1])
                * (1 / F[s])
                * X[s - 1]
                * P_predict[s - 1]
            )
            P_predict[s] = T * P_update[s] * np.transpose(T) + Q
            KF_Dens[s] = (
                (1 / 2) * np.log(2 * np.pi)
                + (1 / 2) * np.log(abs(F[s]))
                + (1 / 2) * np.transpose(v[s]) * (1 / F[s]) * v[s]
            )
            Likelihood = np.sum(KF_Dens[1:-1])
            return Likelihood


def Kalman_Smoother(params, Y, X):
    S = Y.shape[0]
    S = S + 1
    # Initialize Params:
    T = params[0]
    H = params[1]
    Q = params[2]

    # Kalman Filter Starts:
    u_predict = np.zeros(S)
    u_update = np.zeros(S)
    P_predict = np.zeros(S)
    P_update = np.zeros(S)
    v = np.zeros(S)
    F = np.zeros(S)
    for s in range(1, S):
        if s == 1:
            P_update[s] = 1000
            P_predict[s] = T * P_update[1] * np.transpose(T) + Q
        else:
            F[s] = X[s - 1] * P_predict[s - 1] * np.transpose(X[s - 1]) + H
            v[s] = Y[s - 1] - X[s - 1] * u_predict[s - 1]
            u_update[s] = (
                u_predict[s - 1]
                + P_predict[s - 1] * np.transpose(X[s - 1]) * (1 / F[s]) * v[s]
            )
            u_predict[s] = T * u_update[s]
            P_update[s] = (
                P_predict[s - 1]
                - P_predict[s - 1]
                * np.transpose(X[s - 1])
                * (1 / F[s])
                * X[s - 1]
                * P_predict[s - 1]
            )
            P_predict[s] = T * P_update[s] * np.transpose(T) + Q

            u_smooth = np.zeros(S)
            P_smooth = np.zeros(S)
            u_smooth[S - 1] = u_update[S - 1]
            P_smooth[S - 1] = P_update[S - 1]
    for t in range(S - 1, 0, -1):
        u_smooth[t - 1] = u_update[t] + P_update[t] * np.transpose(T) / P_predict[t] * (
            u_smooth[t] - T * u_update[t]
        )
        P_smooth[t - 1] = (
            P_update[t]
            + P_update[t]
            * np.transpose(T)
            / P_predict[t]
            * (P_smooth[t] - P_predict[t])
            / P_predict[t]
            * T
            * P_update[t]
        )
    u_smooth = u_smooth[1:]
    return u_smooth


if __name__ == "__main__":
    SPY = DataReader("SPY", "yahoo", datetime(2019, 1, 1), datetime(2019, 8, 31))
    TQQQ = DataReader("TQQQ", "yahoo", datetime(2019, 1, 1), datetime(2019, 8, 31))

    Y = SPY["Adj Close"].values
    X = TQQQ["Adj Close"].values
    T = Y.shape[0]
    param0 = np.array([3.5, 4.8, 10])
    param_star = minimize(
        Kalman_Filter, param0, method="BFGS", options={"xtol": 1e-8, "disp": True}
    )
    beta_update = Kalman_Smoother(param_star.x, Y, X)
    timevec = np.linspace(1, T, T)
    plt.figure(figsize=(15, 5))
    plt.plot(timevec, beta_update, "r")
    plt.ylabel("beta(t)")
    plt.title("Dynamic Direct Hedge Ratios")

    # REAL-TIME TRADING SIGNALS
    k = 60
    eps = np.zeros(T - k)
    beta = np.zeros(T - k)
    for t in range(k + 1, T):
        Y = SPY["Adj Close"].values[t - k : t]
        X = TQQQ["Adj Close"].values[t - k : t]
        param_star = minimize(
            Kalman_Filter, param0, method="BFGS", options={"xtol": 1e-8, "disp": True}
        )
        beta_update = Kalman_Smoother(param_star.x, Y, X)
        beta[t - k] = beta_update[-1]
        eps[t - k] = Y[-1] - X[-1] * beta[t - k]
        expected_eps = np.mean(eps[0 : t - k])

    # Long the spread eps when the movement is negatively far from the expected value
    # Short the spread when the movement is positively far from the expected value.

    timevec = np.linspace(1, T - k - 1, T - k - 1)
    plt.figure(figsize=(15, 5))
    plt.plot(timevec, eps[1:], "b")
    plt.ylabel("eps(t)")
    plt.title("Crush Spread")
