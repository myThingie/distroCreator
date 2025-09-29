import scipy
import numpy

class distroCreator():
    # Maybe some good other comments make more sense to the reader. let's add them here!
    def __init__(self):
        self.distro = None
        self._alpha_param = None
        self._beta_param = None
        self._mu = 0
        self._sigma = 0.1
        self._normalDistroSampleSize = 1000000

    def _getAlphaBetaValues(self):
        return [self._alpha_param, self._beta_param]

    def _setAlphaBetaParam(self, alphaParam, betaParam):
        self._alpha_param = alphaParam
        self._beta_param = betaParam

    def _setNormalDistroParams(self, mu, sigma, N):
        self._mu = mu
        self._sigma = sigma
        self._normalDistroSampleSize = N

    def _getNormalDistroParams(self):
        return [self._mu, self._sigma]


    def createNormal(self, mu=0, sigma=0.1, size=N):
        _getNormalDistroParams()
        if self._mu!=None & self._sigma!=None & self._normalDistroSampleSize!=None:
            _setNormalDistroParams(mu, sigma, N)
        self.distro = np.random.normal(mu, sigma, N=1000)
        return self.distro

    def createBeta(alpha, beta):
        self._alpha_param, self._beta_param = _getAlphaBetaValues()
        if self._alpha_param == None & self._beta_param == None:
            _setAlphaBetaParam(alpha, beta)
            from scipy.stats import beta
            self.distro = beta(self._alpha_param, self._beta_param)
        return self.distro

