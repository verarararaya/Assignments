# Assessed exercises for week 8 -qq plots

# It is often the case that we wish to decide which distribution is the best fit
# to a single variable. For example, we might want to see whether the residuals
# of a linear regression are approximately normally distributed. QQ-plots are 
# one of the best ways to do this. They are often superior to drawing histograms
# as it's easier to assess whether the tails of the distribution fit.

# In this assessed exercise we're going to create some QQ-plots. The steps to create 
# a qqplot to compare a chosen probability distribution with a single variable x are:
# 1. Calculate the empirical cdf (ecdf) of x
# 2. Simulate a large number of observations from the chosen probability distribution
# 3. Find the quantiles of the distribution at the probabilities defined by the ecdf
# If the two data sets match, a plot of the quantiles and the original data should 
# fall on a straight line. For more detail, see e.g. http://onlinestatbook.com/2/advanced_graphs/q-q_plots.html

# In this exercises we will use four data sets which come from four unknown probability 
# distributions. One of them comes from a N(0,1) distribution, another a t_5 distribution
# another a Exp(1) distribution, and finally a Chi-squared(1) distribution. The files 
# are labelled qq1 to qq4.txt and are all of different lengths. We're going to use 
# QQ-plots to find which data set matches to which probability distribution

# 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import numpy.random as npr
import statsmodels.api as sm
from pandas import Series, DataFrame

# First you will need to load in the data sets
path = '/path/to/files/'
qq1 = pd.read_csv('qq1.txt',header=None)
qq2 = pd.read_csv('qq2.txt',header=None)
qq3 = pd.read_csv('qq3.txt',header=None)
qq4 = pd.read_csv('qq4.txt',header=None)

# Q1 For the first part of the task, we need to create the empirical cumulative distribution
# function (ecdf). This is defined as:
# Number of observations z less than or equal to z_i / Number of observations, for every z_i in z
# Write a function called which takes a set of observations z and produces the empirical cdf
# If you are unfamiliar with empirical cdfs, you may want to read the following article:
# https://towardsdatascience.com/what-why-and-how-to-read-empirical-cdf-123e2b922480
def exercise1(z):
    dataset = []
    for i in range(len(z)):
        dataset.append(z.iloc[i,0])
    ecdf = sm.distributions.ECDF(dataset)
    print(ecdf)
    x = dataset
    y = ecdf(x)
    return y
plt.subplot(2,2,1)
plt.xlabel('qq1')
plt.ylabel('ecdf')
plt.plot(qq1.iloc[:,0],exercise1(qq1),'go')
plt.title('qq1')
plt.subplot(2,2,2)
plt.xlabel('qq2')
plt.ylabel('ecdf')
plt.plot(qq2.iloc[:,0],exercise1(qq2),'go')
plt.title('qq2')
plt.subplot(2,2,3)
plt.xlabel('qq3')
plt.ylabel('ecdf')
plt.plot(qq3.iloc[:,0],exercise1(qq3),'go')
plt.title('qq3')
plt.subplot(2,2,4)
plt.xlabel('qq4')
plt.ylabel('ecdf')
plt.plot(qq4.iloc[:,0],exercise1(qq4),'go')
plt.title('qq4')
plt.suptitle('Q1')
plt.show()
# plt.savefig("Q1.png")
# Plot each of the variables qq1, qq2, etc. versus their ecdf, as subplots in a single figure window. 
# Save your figure and include it in your submission.


# Q2 For the next part we need to create the quantiles of a chosen probability distribution
# Write a function which takes an ecdf created by your function in Q2
# and simulates 10,000 observations from a normal(0,1) distribution. Then calculate
# the quantiles of these simulations at the probabilities defined by the ecdf
def exercise2(ecdf):
    z = np.random.normal(0, 1, 10000)
    output = []
    for i in range(len(ecdf)):
        x = np.percentile(z,ecdf[i])
        output.append(x)
    return output
plt.subplot(2,2,1)
plt.xlabel('quantiles')
plt.ylabel('qq1')
plt.plot(exercise2(exercise1(qq1)),qq1.iloc[:,0],'go')
plt.title('qq1')
plt.subplot(2,2,2)
plt.xlabel('quantiles')
plt.ylabel('qq2')
plt.plot(exercise2(exercise1(qq2)),qq2.iloc[:,0],'go')
plt.title('qq2')
plt.subplot(2,2,3)
plt.xlabel('quantiles')
plt.ylabel('qq3')
plt.plot(exercise2(exercise1(qq3)),qq3.iloc[:,0],'go')
plt.title('qq3')
plt.subplot(2,2,4)
plt.xlabel('quantiles')
plt.ylabel('qq4')
plt.plot(exercise2(exercise1(qq4)),qq4.iloc[:,0],'go')
plt.title('qq4')
plt.suptitle('Q2')
plt.show()
# plt.savefig("Q2.png")
# Create a scatter plot of the theoretical quantiles from your new function (x-axis) against qq1 (y-axis). Repeat 
# this for each dataset, creating each plot as a subplot on the same figure. Save your figure and include it in your
# submission. If the two distributions match, the points should lie on a straight line - this is a QQ-plot. Which of
# the datasets is normally distributed variable?

# Ans: 
#     Q4 would be more possible.


# Q3 Create a new function that takes two arguments. The first argument should be your data Series and the second
# argument should be a set of simulations from some probability distribution. It should use these samples to calculate
# the theoretical quantiles. This function should the computed theoretical quantiles
def exercise3(y,d):
    dataset = exercise1(y)
    output = []
    for i in range(len(dataset)):
        a = np.percentile(d, dataset[i])
        output.append(a)
    return output
# Q4 Run your function for each of the datasets, with
# - d = Series(npr.randn(10000)) (normal distribution)
# - d = Series(npr.exponential(1,10000)) (exponential distribution)
# - d = Series(npr.standard_t(5,10000)) (t_5 distribution)
# - d = Series(npr.chisquare(1,10000)) (chi-squared distribution)
# Plot empirical data versus the theoretical quantiles returned by exercise3 to determine which 
# data set matches to which probability distribution
# Complete the quiz 'W8 - Assessed exercises Q4' to submit your answer for this question.
d1 = Series(npr.randn(10000))
d2 = Series(npr.exponential(1,10000))
d3 = Series(npr.standard_t(5,10000))
d4 = Series(npr.chisquare(1,10000))
plt.clf()
plt.suptitle('normal')
plt.subplot(2,2,1)
t = np.arange(-4,-2, 0.02)
plt.plot(t,t)
plt.plot(exercise3(qq1,d1),qq1.iloc[:,0],'go')
plt.title('qq1')
plt.subplot(2,2,2)
plt.plot(exercise3(qq2,d1),qq2.iloc[:,0],'go')
t = np.arange(-4,-1, 0.02)
plt.plot(t,t)
plt.title('qq2')
plt.subplot(2,2,3)
plt.plot(exercise3(qq3,d1),qq3.iloc[:,0],'go')
t = np.arange(-4,-1, 0.02)
plt.plot(t,t)
plt.title('qq3')
plt.subplot(2,2,4)
plt.plot(exercise3(qq4,d1),qq4.iloc[:,0],'go')
t = np.arange(-4,-1, 0.02)
plt.plot(t,t)
plt.title('qq4')
plt.show()
plt.clf()
plt.suptitle('exponential')
plt.subplot(2,2,1)
plt.plot(exercise3(qq1,d2),qq1.iloc[:,0],'go')
t = np.arange(0,0.01, 0.0002)
plt.plot(t,t)
plt.title('qq1')
plt.subplot(2,2,2)
plt.plot(exercise3(qq2,d2),qq2.iloc[:,0],'go')
t = np.arange(0,0.01, 0.0002)
plt.plot(t,t)
plt.title('qq2')
plt.subplot(2,2,3)
plt.plot(exercise3(qq3,d2),qq3.iloc[:,0],'go')
t = np.arange(0,0.01, 0.0002)
plt.plot(t,t)
plt.title('qq3')
plt.subplot(2,2,4)
plt.plot(exercise3(qq4,d2),qq4.iloc[:,0],'go')
t = np.arange(0,0.01, 0.0002)
plt.plot(t,t)
plt.title('qq4')
plt.show()
plt.clf()
plt.suptitle('t_5')
plt.subplot(2,2,1)
plt.plot(exercise3(qq1,d3),qq1.iloc[:,0],'go')
t = np.arange(-10,-2, 0.0002)
plt.plot(t,t)
plt.title('qq1')
plt.subplot(2,2,2)
plt.plot(exercise3(qq2,d3),qq2.iloc[:,0],'go')
t = np.arange(-10,-2, 0.0002)
plt.plot(t,t)
plt.title('qq2')
plt.subplot(2,2,3)
plt.plot(exercise3(qq3,d3),qq3.iloc[:,0],'go')
t = np.arange(-10,-2, 0.0002)
plt.plot(t,t)
plt.title('qq3')
plt.subplot(2,2,4)
plt.plot(exercise3(qq4,d3),qq4.iloc[:,0],'go')
t = np.arange(-10,-2, 0.0002)
plt.plot(t,t)
plt.title('qq4')
plt.show()
plt.clf()
plt.suptitle('Chi-squared')
plt.subplot(2,2,1)
plt.plot(exercise3(qq1,d4),qq1.iloc[:,0],'go')
t = np.arange(0,0.0002, 0.0000002)
plt.plot(t,t)
plt.title('qq1')
plt.subplot(2,2,2)
plt.plot(exercise3(qq2,d4),qq2.iloc[:,0],'go')
t = np.arange(0,0.0002, 0.0000002)
plt.plot(t,t)
plt.title('qq2')
plt.subplot(2,2,3)
plt.plot(exercise3(qq3,d4),qq3.iloc[:,0],'go')
t = np.arange(0,0.0002, 0.0000002)
plt.plot(t,t)
plt.title('qq3')
plt.subplot(2,2,4)
plt.plot(exercise3(qq4,d4),qq4.iloc[:,0],'go')
t = np.arange(0,0.0002, 0.0000002)
plt.plot(t,t)
plt.title('qq4')
plt.show()