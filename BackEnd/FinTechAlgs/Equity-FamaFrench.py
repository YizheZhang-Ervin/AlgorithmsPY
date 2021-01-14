import numpy as np
import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import math
import matplotlib.pyplot as plt
import os


def collectData():
    # parameters

    # stock list
    LIST = [
        "JILL",
        "ELTK",
        "ONVO",
        "UAVS",
        "AEY",
        "OBLN",
        "XRF",
        "MLSS",
        "MICT",
        "SOLY",
        "NMRD",
        "SINA",
        "INUV",
        "VTGN",
        "VIPS",
        "SOHU",
        "MTSL",
        "DXR",
        "QADA",
        "MYOV",
        "BOSC",
        "APTO",
        "PESI",
        "TITN",
        "EYEG",
        "CAPR",
        "UROV",
        "APDN",
        "TTPH",
        "ECOR",
        "WYND",
        "ZN",
        "OSN",
        "HDSN",
        "BDR",
        "TBLT",
        "PLM",
        "DMRC",
        "MOV",
        "PVH",
        "TLYS",
        "CPAH",
        "CNXT",
        "QQQ",
        "GLD",
        "IYZ",
        "SSO",
        "FAS",
        "XLE",
        "SPY",
        "LINX",
        "PCRFY",
        "GO",
        "CRRFY",
        "WSTL",
        "KEYS",
        "DBI",
        "AVD",
        "DIS",
        "PG",
        "KO",
        "GE",
        "NKE",
        "CAJ",
        "CTVA",
        "CVX",
        "RIO",
        "CAT",
        "COP",
        "AEP",
        "UNP",
        "TM",
        "HMC",
        "SIRI",
        "XOM",
        "F",
        "JNJ",
        "CMCSA",
        "CREG",
        "V",
        "TCCO",
        "AAMC",
        "OXBR",
        "ANCN",
        "BCRX",
        "ALRN",
        "RTW",
        "LTBR",
        "WWR",
        "SBUX",
        "VTVT",
        "MACK",
        "NDRA",
        "CBON",
        "JPM",
        "YY",
        "RENN",
        "BEST",
        "TSM",
        "CHNR",
        "CHA",
        "SNP",
        "SHI",
        "CEA",
        "ZNH",
        "LFC",
        "EDU",
        "JOBS",
        "BIDU",
        "NTES",
    ]
    T = 44
    N = len(LIST)  # columns
    PORTFOLIO = np.zeros((T, N))

    # loop for stocks data
    start = dt.datetime(2019, 6, 28)
    end = dt.datetime(2019, 8, 31)
    for n in range(N):
        try:
            STOCK = web.DataReader(LIST[n], "yahoo", start, end)
            PRICE = (STOCK.Open.values + STOCK.Close.values) / 2
            RETURN = np.log(PRICE[1:] / PRICE[:-1])
            PORTFOLIO[:, n - 1] = RETURN
        except Exception:
            continue
    # save file
    pd.DataFrame(PORTFOLIO).to_csv("portfolio.csv")
    return PORTFOLIO


def famaFrench():
    # check if file exists
    if not os.path.isfile("portfolio.csv"):
        PORTFOLIO = collectData()
    else:
        PORTFOLIO = pd.read_csv("portfolio.csv")

    # FAMA-FRENCH 3 FACTORS
    FAMA_FRENCH_3 = pd.read_csv("Equity.csv", skiprows=4)
    FAMA_FRENCH_3 = FAMA_FRENCH_3.loc[24517:24560]
    MKT = FAMA_FRENCH_3[["Mkt-RF"]].values - FAMA_FRENCH_3[["RF"]].values
    SMB = FAMA_FRENCH_3[["SMB"]].values
    HML = FAMA_FRENCH_3[["HML"]].values

    F = np.concatenate([np.ones((T, 1)), MKT, SMB, HML], axis=1)
    K = len(F[0])

    # Step 1. RUN TIME-SREIS REGRESSION FOR EACH STOCK
    beta = np.zeros((K, N))
    for n in range(N):
        y = PORTFOLIO[:, n]  # T x 1
        x = F  # T x K
        beta[:, n] = np.matmul(np.dot(np.linalg.inv(np.dot(x.T, x)), x.T), y)  # K x 1

    # Step 2. RUN CROSS-SECTIONAL REGRESSION
    # ACTIVE RETURNS
    alpha = np.zeros((N, T))
    sigma = np.zeros((N, N, T))
    for t in range(T):
        y = PORTFOLIO[t, :].T  # N x 1
        x = beta.T  # N x K
        lambdaa = np.matmul(
            np.matmul(np.linalg.inv(np.matmul(x.T, x)), x.T), y
        )  # (KxN)(NxK)(KxN)(Nx1)  = (Kx1)
        alpha[:, t] = y - np.matmul(x, lambdaa)  # (Nx1) - (NxK)(Kx1)
        sigma[:, :, t] = np.matmul(alpha[:, t], (alpha[:, t].T))

    ALPHA = np.mean(alpha, axis=1)  # N x 1
    SIGMA = np.mean(sigma, axis=2)  # N x N

    plt.figure(1)
    plt.title("Active Returns of Portfolio")
    plt.stem(ALPHA)


if __name__ == "__main__":
    famaFrench()