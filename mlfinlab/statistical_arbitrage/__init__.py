"""
Module for Statistical Arbitrage.
"""

from mlfinlab.statistical_arbitrage.stationarity import calc_adfuller, calc_kpss
from mlfinlab.statistical_arbitrage.cointegration import calc_engle_granger, calc_johansen
from mlfinlab.statistical_arbitrage.pairs_regression import calc_rolling_pairs_regression, calc_all_pairs_regression
from mlfinlab.statistical_arbitrage.eigenportfolio import calc_all_eigenportfolio, calc_pca
