import numpy as np
import pyflux as pf
import pandas as pd
from pandas_datareader import DataReader
from datetime import datetime
import matplotlib.pyplot as plt


def Garch():
    # PRELIMINARY ANALYSIS
    dt = DataReader("V", "yahoo", datetime(2019, 1, 1), datetime(2019, 8, 31))
    returns = pd.DataFrame(np.diff(np.log(dt["Adj Close"].values)))
    returns.index = dt.index.values[1 : dt.index.values.shape[0]]
    returns.columns = ["Visa Returns"]

    plt.figure(figsize=(15, 5))
    plt.plot(returns.index, returns)
    plt.ylabel("Returns")
    plt.title("Visa Returns")

    plt.figure(figsize=(15, 5))
    plt.plot(returns.index, np.abs(returns))
    plt.ylabel("Absolute Returns")
    plt.title("Visa Absolute Returns")

    model = pf.GARCH(returns, p=1, q=1)
    x = model.fit()
    x.summary()

    # REAL-TIME TRADING SIGNALS
    T = returns.shape[0]
    k = 60
    y_GARCH = returns.loc[returns.index[k]]
    y_ARIMA = returns.loc[returns.index[k]]
    for t in range(k + 1, T):
        model_garch = pf.GARCH(returns[t - k : t], p=1, q=1)
        x = model_garch.fit()
        y_tplus1 = model_garch.predict(1, intervals=False)
        y_GARCH.loc[returns.index[t - k]] = y_tplus1

        model = pf.ARIMA(
            returns[t - k : t], ar=2, ma=2, target="Visa Returns", family=pf.Normal()
        )
        x = model.fit("MLE")
        y_tplus1 = model.predict(1, intervals=False)
        y_ARIMA.loc[returns.index[t - k]] = y_tplus1

        """
        If y_ARIMA/GARCH > 0, long 5 contracts
        If y_ARIMA/GARCH < 0, short 5 contracts
        """


if __name__ == "__main__":
    Garch()