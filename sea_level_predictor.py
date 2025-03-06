import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

ddef draw_plot():
    # Read data from the provided CSV file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # Create first line of best fit using all data (1880-2050)
    slope_all, intercept_all, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create a line of best fit for all years (1880-2050)
    years_all = range(1880, 2051)
    line_all = [slope_all * year + intercept_all for year in years_all]
    plt.plot(years_all, line_all, label='Best Fit Line (1880 - 2050)', color='red')

    # Create second line of best fit using data from 2000 onward
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    # Create a line of best fit for 2000-2050
    years_recent = range(2000, 2051)
    line_recent = [slope_recent * year + intercept_recent for year in years_recent]
    plt.plot(years_recent, line_recent, label='Best Fit Line (2000 - 2050)', color='green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
