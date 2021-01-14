import math
import numpy as np
import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt


class NSCurveFamily:
    """
    The class fit data into Nelson Siegel and Nelson Siegel Svensson Models.
    Parsimonious Modeling of Yield Curves
    Charles Nelson and Andrew F Siegel
    The Journal of Business, 1987, vol. 60, issue 4, 473-89
    """

    def __init__(self, useNSS=False):
        """initialised with True if use Nelson Siegel Svensson Model
        initialised with False if use Nelson Siegel Model
        """
        self.useNSS = useNSS
        self.HasEstParam = False

    def fitNSModel(self, tau, t_seq, zr_seq):
        t_to_tau = [t / tau for t in t_seq]
        xterm1 = [(1.0 - math.exp(-tt)) / tt for tt in t_to_tau]
        xterm2 = [(1.0 - math.exp(-tt)) / tt - math.exp(-tt) for tt in t_to_tau]
        x = np.array([xterm1, xterm2]).T
        x = sm.add_constant(x)
        wt = np.append(t_seq[0], np.diff(t_seq))
        # Use the weighted OLS with the weight proportional to the tenor between data points
        # This intends to give equal wt to the full yield curve rather than overweight the portion with a lot of samples
        res = sm.WLS(zr_seq, x, wt).fit()
        return (res.params, res.rsquared)

    def fitNSSModel(self, tau1, tau2, t_seq, zr_seq):
        t_to_tau1 = [t / tau1 for t in t_seq]
        t_to_tau2 = [t / tau2 for t in t_seq]

        xterm1 = [(1.0 - math.exp(-tt)) / tt for tt in t_to_tau1]
        xterm2 = [(1.0 - math.exp(-tt)) / tt - math.exp(-tt) for tt in t_to_tau1]
        xterm3 = [(1.0 - math.exp(-tt)) / tt - math.exp(-tt) for tt in t_to_tau2]

        x = np.array([xterm1, xterm2, xterm3]).T
        x = sm.add_constant(x)
        wt = np.append(t_seq[0], np.diff(t_seq))
        # Use the weighted OLS with the weight proportional to the tenor between data points
        # This intends to give equal wt to the full yield curve rather than overweight the portion with a lot of samples
        res = sm.WLS(zr_seq, x, wt).fit()
        return (res.params, res.rsquared)

    def estNSParam(self, t_seq, zr_seq):
        # for yield curve estimation the search space in time is not likely to be outside front part of the curve
        tau_univ = [0.1, 0.15, 0.2, 0.3, 0.5, 0.75, 1, 1.5, 2, 3, 5, 7.5, 10]
        rsq_univ = [self.fitNSModel(tau, t_seq, zr_seq)[1] for tau in tau_univ]
        opt_tau = tau_univ[np.argmax(rsq_univ)]
        opt_param, opt_rsqr = self.fitNSModel(opt_tau, t_seq, zr_seq)
        return (opt_param, opt_tau, opt_rsqr)

    def estNSSParam(self, t_seq, zr_seq):
        # for yield curve estimation the search space in time is not likely to be outside  front part of the curve
        tau_univ = [0.1, 0.15, 0.2, 0.3, 0.5, 0.75, 1, 1.5, 2, 3, 5, 7.5, 10]
        nTau = len(tau_univ)
        rsq_univ = np.array(
            [
                self.fitNSSModel(tau0, tau1, t_seq, zr_seq)[1]
                for tau0 in tau_univ
                for tau1 in tau_univ
            ]
        )
        rsq_univ = rsq_univ.reshape((nTau, nTau))
        maxidx = np.argmax(rsq_univ)
        opt_tau0, opt_tau1 = tau_univ[maxidx // nTau], tau_univ[maxidx % nTau]
        opt_param, opt_rsqr = self.fitNSSModel(opt_tau0, opt_tau1, t_seq, zr_seq)
        return (opt_param, opt_tau0, opt_tau1, opt_rsqr)

    def estimateParam(self, t_seq, zr_seq):
        """Estimate model parameters by grid search
        t_seq: pandas series, time in year
        zr_seq: pandas series, spot rate
        """
        if self.useNSS:
            param, tau0, tau1, rsqr = self.estNSSParam(t_seq, zr_seq)
            self.beta0, self.beta1, self.beta2, self.beta3 = param
            self.tau0, self.tau1, self.rsqr = tau0, tau1, rsqr
        else:
            param, tau, rsqr = self.estNSParam(t_seq, zr_seq)
            self.beta0, self.beta1, self.beta2 = param
            self.tau0, self.rsqr = tau, rsqr
            self.tau1, self.beta3 = float("nan"), float("nan")
        self.HasEstParam = True

    def getSpot(self, t_seq):
        """Return the spot rate based upon the estimated parameters
        t_seq: pandas series, time in year
        """
        if self.HasEstParam == False:
            raise Exception("Parameters are not available")
        if self.useNSS:
            t_to_tau1 = [t / self.tau0 for t in t_seq]
            t_to_tau2 = [t / self.tau1 for t in t_seq]
            xterm1 = [(1.0 - math.exp(-tt)) / tt for tt in t_to_tau1]
            xterm2 = [(1.0 - math.exp(-tt)) / tt - math.exp(-tt) for tt in t_to_tau1]
            xterm3 = [(1.0 - math.exp(-tt)) / tt - math.exp(-tt) for tt in t_to_tau2]
            param = [self.beta0, self.beta1, self.beta2, self.beta3]
            x = np.array([xterm1, xterm2, xterm3]).T
            x = sm.add_constant(x)
        else:
            t_to_tau = [t / self.tau0 for t in t_seq]
            xterm1 = [(1.0 - math.exp(-tt)) / tt for tt in t_to_tau]
            xterm2 = [(1.0 - math.exp(-tt)) / tt - math.exp(-tt) for tt in t_to_tau]
            param = [self.beta0, self.beta1, self.beta2]
            x = np.array([xterm1, xterm2]).T
            x = sm.add_constant(x)
        return x.dot(param)

    def getFwdRate(self, t_seq):
        """Return the forward rate based upon the estimated parameters
        t_seq: pandas series, time in year
        """
        if self.HasEstParam == False:
            raise Exception("Parameters are not available")
        if self.useNSS:
            t_to_tau1 = [t / self.tau0 for t in t_seq]
            t_to_tau2 = [t / self.tau1 for t in t_seq]
            xterm1 = [math.exp(-tt) for tt in t_to_tau1]
            xterm2 = [tt * math.exp(-tt) for tt in t_to_tau1]
            xterm3 = [tt * math.exp(-tt) for tt in t_to_tau2]
            param = [self.beta0, self.beta1, self.beta2, self.beta3]
            x = np.array([xterm1, xterm2, xterm3]).T
            x = sm.add_constant(x)
        else:
            t_to_tau = [t / self.tau0 for t in t_seq]
            xterm1 = [math.exp(-tt) for tt in t_to_tau]
            xterm2 = [tt * math.exp(-tt) for tt in t_to_tau]
            param = [self.beta0, self.beta1, self.beta2]
            x = np.array([xterm1, xterm2]).T
            x = sm.add_constant(x)
        return x.dot(param)


def plotNSmodel(tenor, nsm, y):
    plt.figure(figsize=(12, 5))
    plt.subplot(121)
    plt.plot(tenor, nsm.getSpot(tenor), "o--", label="NS Model")
    plt.plot(tenor, y, "o-", label="Input Data")
    plt.title("Data fit to NS Model")
    plt.xlabel("t(Yr)")
    plt.ylabel("spot rate(%)")
    plt.legend()
    plt.subplot(122)
    plt.plot(tenor, nsm.getFwdRate(tenor), "o-", label="NS Model")
    plt.title("Forward rate from NS Model")
    plt.xlabel("t(Yr)")
    plt.ylabel("forward rate(%)")
    plt.show()


def getData():
    colHdr = ["Tenor", "EURAAA_20191111"]
    zrdata = [
        [0.25, -0.602],
        [0.333, -0.6059],
        [0.417, -0.6096],
        [0.5, -0.613],
        [0.75, -0.6215],
        [1, -0.6279],
        [1.5, -0.6341],
        [2, -0.6327],
        [3, -0.6106],
        [4, -0.5694],
        [5, -0.5161],
        [6, -0.456],
        [7, -0.3932],
        [8, -0.3305],
        [9, -0.2698],
        [10, -0.2123],
        [12, -0.1091],
        [15, 0.0159],
        [17, 0.0818],
        [20, 0.1601],
        [25, 0.2524],
        [30, 0.315],
    ]
    data = pd.DataFrame(zrdata, columns=colHdr)
    tIdxName, rateColName = "Tenor", "EURAAA_20191111"
    tenor, y = data[tIdxName], data[rateColName]
    return tenor, y


def run(modelType):
    tenor, y = getData()
    if modelType == "NS":
        print("This is NS Model")
        nsm = NSCurveFamily(False)
        nsm.estimateParam(tenor, y)
        print("Best fit param: (RSqr=%.3f)" % nsm.rsqr)
        print(
            "tau=%.2f intercept=%.3f beta1=%.3f beta2=%.3f"
            % (nsm.tau0, nsm.beta0, nsm.beta1, nsm.beta2)
        )
        plotNSmodel(tenor, nsm, y)
    elif modelType == "NSS":
        print("This is NSS Model")
        nssm = NSCurveFamily(True)
        nssm.estimateParam(tenor, y)
        print("Best fit param: (RSqr=%.3f)" % nssm.rsqr)
        print(
            "tau1=%.2f tau2=%.2f intercept=%.3f beta1=%.3f beta2=%.3f beta3=%.3f"
            % (nssm.tau0, nssm.tau1, nssm.beta0, nssm.beta1, nssm.beta2, nssm.beta3)
        )
        plotNSmodel(tenor, nssm, y)


if __name__ == "__main__":
    run("NS")
    run("NSS")