#!/usr/bin/env python

SNOW_FILE = '~/gits/gads_26/datasets/snowfall_2.tsv'
RAYLEIGH_FILE = '~/gits/gads_26/datasets/rayleigh.tsv'
MAUNA_LOA_FILE = '~/gits/gads_26/datasets/mauna_loa.tsv'

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def box():

    k = pd.read_csv(RAYLEIGH_FILE, sep='\t')
    k['oxygen'] = k.origin.apply(lambda k: k == 'Air')
    ax = sns.boxplot(x='oxygen', y='weight', data=k)
    plt.show()

def scatter():

    k = pd.read_csv(MAUNA_LOA_FILE, sep='\t')
    grid = sns.JointGrid(k.dec_date, k.avg, space=0, size=6, ratio=50)
    grid.plot_joint(plt.scatter, color="g")
    plt.show()

if __name__ == '__main__':
    scatter()
