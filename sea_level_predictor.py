import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    #print(df)
    #print(df.dtypes)
    # Create scatter plot
    plt.subplots(figsize=(15,10))
    df.plot.scatter(x='Year',y='CSIRO Adjusted Sea Level')
    # Create first line of best fit
    linReg1 = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    x1 = np.arange(df['Year'].min(),2050,1)
    y1 = x1 * linReg1.slope + linReg1.intercept
    plt.plot(x1,y1,'r')
    # Create second line of best fit
    dfAdj = df[df['Year'] >= 2000]
    linReg2 = linregress(dfAdj['Year'],dfAdj['CSIRO Adjusted Sea Level'])
    x2 = np.arange(2000,2050,1)
    y2 = x2 * linReg2.slope + linReg2.intercept
    plt.plot(x2,y2,'purple')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()