---
layout: page
title: Activity coefficient
---

```python
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from scipy import stats
import numpy as np

%matplotlib inline

file = pd.read_excel("E3_Aktivitätskoeffizient.xlsx","For_Plot",usecols=[0,2,3,4])

X = file['sqrt(Konzentration)']
Y = file['A']


#fig, ax = plt.subplots()
#ax.plot(X,Y,'o',color='#D73D4B')
#ax.grid(True, which='major', axis='both', color='#F19211', linestyle='-')
#ax.grid(True, which='minor', axis='both', color='#F19211', linestyle='--')
#ax.spines['left'].set_position('zero')
#ax.spines['right'].set_color('none')
#ax.spines['bottom'].set_position('zero')
#ax.spines['top'].set_color('none')
#ax.legend(loc='upper center', frameon=True)

#major & minor ticks
#ax.xaxis.set_major_locator(MultipleLocator(0.05))
#ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
#ax.xaxis.set_minor_locator(MultipleLocator(0.01))

#ax.yaxis.set_major_locator(MultipleLocator(0.01))
#ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))
#ax.yaxis.set_minor_locator(MultipleLocator(0.001))

x1 = X.values.reshape(-1,1)
y1 = Y.values.reshape(-1,1)

ransac = linear_model.RANSACRegressor()
ransac.fit(x1,y1)
inlier_mask = ransac.inlier_mask_
outlier_mask = np.logical_not(inlier_mask)
line_y1_ransac = ransac.predict(x1)
a1 = ransac.estimator_.intercept_
m1 = ransac.estimator_.coef_[0]

def lsqfity(X, Y):
    """
    Calculate a "MODEL-1" least squares fit.

    The line is fit by MINIMIZING the residuals in Y only.

    The equation of the line is:     Y = my * X + by.

    Equations are from Bevington & Robinson (1992)
    Data Reduction and Error Analysis for the Physical Sciences, 2nd Ed."
    pp: 104, 108-109, 199.

    Data are input and output as follows:

    my, by, ry, smy, sby = lsqfity(X,Y)
    X     =    x data (vector)
    Y     =    y data (vector)
    my    =    slope
    by    =    y-intercept
    ry    =    correlation coefficient
    smy   =    standard deviation of the slope
    sby   =    standard deviation of the y-intercept

    """

    X, Y = map(np.asanyarray, (X, Y))

    # Determine the size of the vector.
    n = len(X)

    # Calculate the sums.

    Sx = np.sum(X)
    Sy = np.sum(Y)
    Sx2 = np.sum(X ** 2)
    Sxy = np.sum(X * Y)
    Sy2 = np.sum(Y ** 2)

    # Calculate re-used expressions.
    num = n * Sxy - Sx * Sy
    den = n * Sx2 - Sx ** 2

    # Calculate my, by, ry, s2, smy and sby.
    my = num / den
    by = (Sx2 * Sy - Sx * Sxy) / den
    ry = num / (np.sqrt(den) * np.sqrt(n * Sy2 - Sy ** 2))

    diff = Y - by - my * X

    s2 = np.sum(diff * diff) / (n - 2)
    smy = np.sqrt(n * s2 / den)
    sby = np.sqrt(Sx2 * s2 / den)

    return my, by, ry, smy, sby    

#plt.plot(x1, line_y1_ransac, color='#D73D4B')


#plt.xlabel(r'$\sqrt{c(HCl)}$')
#plt.ylabel(r'$E + 2\cdot \frac{RT}{F} \cdot \ln(c_{HCl})$')
#plt.savefig('Nico.pdf')
print("Der y-Achsenabschnitt ist:",a1)
print("Die Steigung ist:",m1)
print ('Die Standardabweichung der Steigung ist:',lsqfity(X,Y)[3])
print ('Die Standardabweichung des y-Achsenabschnitts ist:',lsqfity(X,Y)[4])

```

    y-intercept is: [0.20920238]
    Slope is: [0.04574559]
    Standard deviation of the slope: 0.038651730321567004
    Standard deviation of the Y-intercept: 0.005678428996995362



```python
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from scipy import stats
import numpy as np

%matplotlib inline

file = pd.read_excel("E3_Aktivitätskoeffizient.xlsx","For_Plot",usecols=[0,4])

X = file['Konzentration(mol/L)']
Y = file['f+-']

#fig, ax = plt.subplots()
#ax.plot(X,Y,'o',color='#D73D4B')
#ax.grid(True, which='major', axis='both', color='#F19211', linestyle='-')
#ax.grid(True, which='minor', axis='both', color='#F19211', linestyle='--')
#ax.spines['left'].set_position('zero')
#ax.spines['right'].set_color('none')
#ax.spines['bottom'].set_position('zero')
#ax.spines['top'].set_color('none')
#ax.legend(loc='upper center', frameon=True)

#major & minor ticks
#ax.xaxis.set_major_locator(MultipleLocator(0.01))
#ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
#ax.xaxis.set_minor_locator(MultipleLocator(0.001))

#ax.yaxis.set_major_locator(MultipleLocator(0.2))
#ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))
#ax.yaxis.set_minor_locator(MultipleLocator(0.02))

x1 = X.values.reshape(-1,1)
y1 = Y.values.reshape(-1,1)

ransac = linear_model.RANSACRegressor()
ransac.fit(x1,y1)
inlier_mask = ransac.inlier_mask_
outlier_mask = np.logical_not(inlier_mask)
line_y1_ransac = ransac.predict(x1)
a1 = ransac.estimator_.intercept_
m1 = ransac.estimator_.coef_[0]

#plt.plot(x1, line_y1_ransac, color='#D73D4B')

#plt.xlabel(r'$c(HCl)$')
#plt.ylabel(r'$\gamma\pm$')
#plt.savefig('Nico.pdf')
#print("y-intercept is:",a1)
#print("Slope is:",m1)
#plt.savefig('Nico1.pdf')


```
