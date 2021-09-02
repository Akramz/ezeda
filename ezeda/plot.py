"""Plotting utilities."""
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


def corr(df):
    """Visualizes the correlation matrix between dataframe features.

    # Params
        df (pd.DataFrame): the dataframe containing the features of interest.
    """
    # Compute the correlation matrix
    correlations = df.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(correlations, dtype=bool))

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))

    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(230, 20, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(correlations, mask=mask, cmap=cmap, vmin=-1., vmax=1., center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})
