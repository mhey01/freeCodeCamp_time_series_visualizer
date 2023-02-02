import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10,5))

    plt.scatter(
        x = df['Year'],
        y = df['CSIRO Adjusted Sea Level']
    )

    # Create first line of best fit
    r = linregress(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])
    m = r[0]
    c = r[1]

    line_years = np.arange(1880, 2051, 1)
    predicted_sea_level = (m * line_years) + c

    lobf = pd.DataFrame({
        'line_year': line_years,
        'line_sea_level': predicted_sea_level
    })

    # Plotting line of best fit

    plt.plot(
        lobf['line_year'],
        lobf['line_sea_level'],
        color='red'
    )

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]

    # Create second line of best fit
    r = linregress(x = df_2000['Year'], y = df_2000['CSIRO Adjusted Sea Level'])
    m = r[0]
    c = r[1]

    line_years = np.arange(2000, 2051, 1)
    predicted_sea_level = (m * line_years) + c

    lobf = pd.DataFrame({
        'line_year': line_years,
        'line_sea_level': predicted_sea_level
    })

    lobf[lobf['line_year'] == 2050]

    plt.plot(
        lobf['line_year'],
        lobf['line_sea_level'],
        color='purple'
    )

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()