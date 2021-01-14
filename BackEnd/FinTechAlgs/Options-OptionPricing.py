import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
import scipy.interpolate as ip
from mpl_toolkits.mplot3d import Axes3D


def optionPricing():
    # parameter
    mu = 0.15
    sigma = 0.30
    Delta_t = 0.192  # 1/52 years = 1 week
    T = 1000
    S = np.zeros((T, 1))
    Delta_S = np.zeros((T, 1))

    # loop
    for s in range(2, T):
        var_eps = np.random.randn()
        Delta_S[s] = mu * Delta_t * S[s] + sigma * math.sqrt(Delta_t) * var_eps
        S[s] = S[s - 1] + Delta_S[s]

    # plot
    plt.figure(1)
    plt.subplot(2, 1, 1)
    plt.plot(S)
    plt.subplot(2, 1, 2)
    plt.plot(Delta_S)

    M = 1000
    S = np.zeros((T, M))
    Delta_S = np.zeros((T, M))
    for m in range(1, M):
        for s in range(2, T):
            var_eps = np.random.randn()
            Delta_S[s, m] = (
                mu * Delta_t * S[s, m] + sigma * math.sqrt(Delta_t) * var_eps
            )
            S[s, m] = S[s - 1, m] + Delta_S[s, m]
    plt.figure(2)
    plt.subplot(2, 1, 1)
    plt.plot(S)
    plt.subplot(2, 1, 2)
    plt.plot(Delta_S)


def VolatilitySurface():
    # PLOT VOLATILITY SURFACE
    dates = ["1016", "1018", "1021", "1023", "1025", "1028", "1030", "1031"]
    dates_full = [
        "10/16/2019",
        "10/18/2019",
        "10/21/2019",
        "10/23/2019",
        "10/25/2019",
        "10/28/2019",
        "10/30/2019",
        "10/31/2019",
    ]
    STRIKE = {}
    IMPLIED_VOL = {}

    for i in range(8):
        data1 = pd.read_excel("Options.xlsx", sheet_name=dates[i])
        data_call = data1.loc[data1["Type"] == "C"]
        STRIKE[dates[i]] = data_call["Strike"]
        IMPLIED_VOL[dates[i]] = data_call["Implied Volatility"]

    # IMPLIED VOL SMILE
    plt.figure(1)
    for j in range(8):
        plt.subplot(2, 4, j + 1)
        plt.scatter(STRIKE[dates[j]], IMPLIED_VOL[dates[j]])
        plt.title(dates_full[j])

    # IMPLIED VOL SURFACE
    STRIKE_vec = set()
    for col in STRIKE.values():
        for cell in col:
            STRIKE_vec.add(cell)
    STRIKE_vec = list(STRIKE_vec)
    STRIKE_vec.sort()

    # MODEL 1: STRIKE = STRIKE_vec
    # MODEL 2: STRIKE = Interpolate 1000 points within range of STRIKE_vec
    # STRIKE2 = np.linspace(min(STRIKE_vec),max(STRIKE_vec),1000)

    VOL_SMILE = {}
    for d in dates:
        STRIKE2 = np.linspace(min(STRIKE[d]), max(STRIKE[d]), 1000)
        f = ip.interp1d(STRIKE[d], IMPLIED_VOL[d], kind="cubic")
        VOL_SMILE[d] = f(STRIKE2)
    # vec = np.linspace(601,800,200)
    VOL_SMILE2 = []
    for data in VOL_SMILE.values():
        VOL_SMILE2.append(data[601:801])
    fig = plt.figure(2)
    ax = Axes3D(fig)
    X, Y = np.meshgrid(range(len(VOL_SMILE2)), range(len(VOL_SMILE2[0])))
    ax.plot_surface(X, Y, np.array(VOL_SMILE2).T)
    plt.xticks(
        np.linspace(1, 8, 8),
        ["10/16", "10/18", "10/21", "10/23", "10/25", "10/28", "10/30", "10/31"],
    )
    plt.yticks([1, 50, 100, 150, 200], [601, 650, 700, 750, 800])


def STATE_PRICE_DENSITY(c, strike, st):
    strike = np.array(strike)
    n = len(c)
    p = np.zeros((n, 1))
    for i in range(0, n):
        if i == 0:
            p[0] = 1 - (st - c[0]) / strike[0]
        else:
            p[i] = 1 - (c[i] - c[i - 1]) / (strike[i] - strike[i - 1])
    p[n - 1] = 1 - sum(p[n - 2])
    p.sort()
    SPD = np.divide((p[2:n] - p[1 : n - 1]), (strike[2:n] - strike[1 : n - 1]))
    SPD = SPD[3:-1]
    return SPD


def RND():
    # ESTIMATE RISK-NEUTRAL DENSITY (STATE-PRICE DENSITY)
    # SPX PRICE
    St = 2966.15
    dates = ["1016", "1018", "1021", "1023", "1025", "1028", "1030", "1031"]
    dates_full = [
        "10/16/2019",
        "10/18/2019",
        "10/21/2019",
        "10/23/2019",
        "10/25/2019",
        "10/28/2019",
        "10/30/2019",
        "10/31/2019",
    ]
    STRIKE = {}
    IMPLIED_VOL = {}
    BID = {}
    ASK = {}
    C = {}
    SPD = {}

    for i in range(8):
        data1 = pd.read_excel("Options.xlsx", sheet_name=dates[i])
        data_call = data1.loc[data1["Type"] == "C"]
        STRIKE[dates[i]] = data_call["Strike"]
        IMPLIED_VOL[dates[i]] = data_call["Implied Volatility"]
        BID[dates[i]] = np.array(
            [0 if data == "-" else data for data in data_call["Bid"]]
        )
        ASK[dates[i]] = data_call["Ask"]
        C[dates[i]] = [(a + b) / 2 for b, a in zip(BID[dates[i]], ASK[dates[i]].values)]
        SPD[dates[i]] = STATE_PRICE_DENSITY(C[dates[i]], STRIKE[dates[i]], St)
    plt.figure(3)
    for i in range(4):
        plt.subplot(2, 2, i + 1)
        plt.plot(SPD[dates[i]])
        plt.title(dates_full[i])


if __name__ == "__main__":
    optionPricing()
    VolatilitySurface()
    RND()
