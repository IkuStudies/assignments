import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
df = df[
        (df["value"] >= df["value"].quantile(0.025)) &
        (df["value"] <= df["value"].quantile(0.975))
    ]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(32, 10))
    ax.plot(df.index, df['value'], color='indianred', linewidth=3)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019", fontsize=24)
    ax.set_xlabel("Date", fontsize=20)
    ax.set_ylabel("Page Views", fontsize=20)
    ax.yaxis.set_tick_params(labelsize=20)
    ax.xaxis.set_tick_params(labelsize=20)
    

    # Save image and return fig (don't change this part)
    plt.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    df_bar = df_bar.groupby(['year', 'month']).mean().reset_index()

    # Pivot the data to have months as columns and years as rows
    df_pivot = df_bar.pivot(index='year', columns='month', values='value')

    # Define the order of months
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Reindex the columns of the pivot DataFrame based on the month order
    df_pivot = df_pivot.reindex(columns=month_order)
  
    # Define the color palette for the bars
    colors = sns.color_palette('Set2', len(df_pivot.columns))

    # Create the bar plot
    fig, ax = plt.subplots(figsize=(15, 13))
    df_pivot.plot(kind='bar', ax=ax, color=colors)
    ax.set_xlabel('Years', fontsize=18)
    ax.set_ylabel('Average Page Views', fontsize=18)
    ax.yaxis.set_tick_params(labelsize=18)
    ax.xaxis.set_tick_params(labelsize=18)

    # Add legend for the months
    month_labels = df_pivot.columns.tolist()
    ax.legend(labels=month_labels, title='Months', fontsize=18)

    # Save image and return fig (don't change this part)
    plt.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(20, 7))

    sns.boxplot(x='year', y='value', data=df_box, ax=ax[0])
    ax[0].set_title('Year-wise Box Plot (Trend)', fontsize=12)
    ax[0].set_xlabel('Year', fontsize=10)
    ax[0].set_ylabel('Page Views', fontsize=10)
    ax[0].yaxis.set_tick_params(labelsize=10)
    ax[0].xaxis.set_tick_params(labelsize=10)

    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(x='month', y='value', data=df_box, ax=ax[1], order=month_order)
    ax[1].set_title('Month-wise Box Plot (Seasonality)', fontsize=12)
    ax[1].set_xlabel('Month', fontsize=10)
    ax[1].set_ylabel('Page Views', fontsize=10)
    ax[1].yaxis.set_tick_params(labelsize=10)
    ax[1].xaxis.set_tick_params(labelsize=10)

    # Save image and return fig (don't change this part)
    plt.savefig('box_plot.png')
    return fig
