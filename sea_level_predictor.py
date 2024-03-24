import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress




def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Scatter plot
    plt.figure(figsize=(12,8))
    plt.scatter(data=df,x='Year',y='CSIRO Adjusted Sea Level',label='CSIRO Adjusted Sea Level Observations: Late 19th Century - 21st Century')
    
    # First line of best fit. Line predicts sea level until year 2050 based on data up from years 1880 - 2000.
    df_recent = df[df['Year'] >=2000]
    df_future = pd.DataFrame({'Year' : [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 
                                     2022, 2023, 2024, 2025, 2026, 2027,2028, 2029, 2030, 2031, 2032, 
                                     2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 
                                     2044, 2045, 2046, 2047, 2048, 2049, 2050]})

    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    years = np.arange(1880, 2051) 
    line_regress = linregress(x, y)
    y0 = line_regress.intercept + line_regress.slope * years
    plt.plot(years, y0, color='green', linewidth=2, label='Past trend')

    # Second line of best fit. Line predicts sea level until year 2050 based on sea level from years 2000 - 2013.
    x2 = df_recent['Year']
    y2 = df_recent['CSIRO Adjusted Sea Level']
    line_reg_to_2050 = linregress(x2, y2)
    x1 = np.arange(2000, 2051)
    y1 = line_reg_to_2050.intercept + line_reg_to_2050.slope * x1
    df_rec_fut = pd.concat([df_recent,df_future])
    plt.scatter(x2, y2, label='Recent Observations (Years 2000 - 2013)')
    plt.plot(df_rec_fut['Year'], y1, color='red', label='Prediction')

    # Chart labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Saves plot and returns data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()
draw_plot()
