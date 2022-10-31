# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 22:20:05 2022

@author: nicol
"""

# Pagina oficial de Seaborn
# https://seaborn.pydata.org/tutorial/introduction


# Scatterplots
import _pandas as pnd
import seaborn as sns

sns.scatterplot(data = pnd.df_jacarandas, x = 'diametro', y = 'altura_tot')