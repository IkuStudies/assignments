import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Extract data for scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x, y)

    # Perform linear regression for the first line of best fit
    res = linregress(x, y)

    # Generate x-values for the line of best fit
    prediction_x = pd.Series(range(1880, 2051))
    prediction_y = res.slope * prediction_x + res.intercept

    # Plot the first line of best fit
    ax.plot(prediction_x, prediction_y, 'r', label='Line of Best Fit')

    # Filter data for the second line of best fit
    recent_data = df[df['Year'] >= 2000]
    x_recent = recent_data['Year']
    y_recent = recent_data['CSIRO Adjusted Sea Level']

    # Perform linear regression for the second line of best fit
    res_recent = linregress(x_recent, y_recent)

    # Generate x-values for the second line of best fit
    prediction_x_recent = pd.Series(range(2000, 2051))
    prediction_y_recent = res_recent.slope * prediction_x_recent + res_recent.intercept

    # Plot the second line of best fit
    ax.plot(prediction_x_recent, prediction_y_recent, 'g', label='Line of Best Fit (2000 onwards)')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Add legend
    ax.legend()

    # Save plot and return the axis object for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return ax
