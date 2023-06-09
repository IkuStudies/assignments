import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = (df['weight']/((df['height']/100)**2) > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df['cholesterol']==1, 'cholesterol'] = 0
df.loc[df['cholesterol']>1, 'cholesterol'] = 1
df.loc[df['gluc']==1, 'gluc'] = 0
df.loc[df['gluc']>1, 'gluc'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat['total'] = 1
    df_cat = df_cat.groupby(['cardio' , 'variable' , 'value'] , as_index = False).count()

    # Draw the catplot with 'sns.catplot()'
    graph = sns.catplot(x='variable', y="total", hue="value", kind="bar", col='cardio',data=df_cat)
    
    # Get the figure for the output
    fig = graph.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[
        (df["ap_hi"] >= df["ap_lo"]) &
        (df["height"] >= df["height"].quantile(0.025)) &
        (df["height"] <= df["height"].quantile(0.975)) &
        (df["weight"] >= df["weight"].quantile(0.025)) &
        (df["weight"] <= df["weight"].quantile(0.975))
  ]
    # Calculate the correlation matrix
    corr = df_heat.corr()
    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    # Create a mask for the upper triangle of the correlation matrix
    mask[np.triu_indices_from(mask)] = True

# Set the plotting style to white
    with sns.axes_style("white"):
    # Create a figure and axis object
        f, fig = plt.subplots(figsize=(12, 7))
    
    # Plot the heatmap with specific parameters
        fig = sns.heatmap(corr,
                          vmin=0,
                          vmax=0.25,
                          square=True,
                          annot=True,
                          linewidths=0.5,
                          fmt=".1f",
                          mask=mask)
            
    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (14 , 14))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr , linewidths = 1 , annot = True , square = True , mask = mask, fmt = '.1f', center = 0.08 , cbar_kws = {'shrink':0.5})

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
