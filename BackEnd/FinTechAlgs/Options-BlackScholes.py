import numpy as np
from scipy.stats import norm

# norm.cdf(x,mu,sigma)


def blackScholes(S, X, T, r, sigma, option="call"):
    """
    S: spot price
    X: strike price
    T: time to maturity
    r: risk-free interest rate
    sigma: standard deviation of price of underlying asset
    """
    d1 = (np.log(S / X) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / X) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    if option == "call":
        p = S * norm.cdf(d1, 0.0, 1.0) - X * np.exp(-r * T) * norm.cdf(d2, 0.0, 1.0)
    elif option == "put":
        p = X * np.exp(-r * T) * norm.cdf(-d2, 0.0, 1.0) - S * norm.cdf(-d1, 0.0, 1.0)
    else:
        return None
    return p


if __name__ == "__main__":
    S = 50
    X = 100
    T = 1
    r = 0.05
    sigma = 0.25
    arr1 = np.array([S, X, T, r, sigma])
    rst1 = blackScholes(*arr1, option="call")
    rst2 = blackScholes(*arr1, option="put")
    print(rst1, rst2)
    print(arr1)