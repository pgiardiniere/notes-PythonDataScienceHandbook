# Scikit-Learn provides efficient versions of a large number of common algorithms
# It's relatively uniform API and good docs make it very popular

##############################
### Data Representation in Scikit-Learn

## Data as a table:
# a basic table is a 2D grid of data, rows representing elements, cols qtys related to it

# example: Iris dataset
import seaborn as sns
iris = sns.load_dataset('iris')
iris.head()

# refer to rows of our matrix as samples, num rows as n_samples
# similarly, cols refer to features, num cols is n_features


## Features Matrix
# 

## Target Array:
# Lable/Target arrays usually called 'y'.
# Generally they're 1D, with len = n_samples, and generally contained
# in NP arrs or PD Series.

# Per naming convention as 'y', these would generally contain the qty 
# we aim to predict from our data (our dependent variable, in stats-land)

# Example: visualizing data in SeaBorn
%matplotlib inline
import seaborn as sns; sns.set()
sns.pairplot(iris, hue='species', size=1.5)
# For use in Scikit-Learn, we will extract features matrix and target arr from DF

X_iris = iris.drop('species', axis=1)
X_iris.shape

y_iris = iris['species']
y_iris.shape
# now we have properly formatted data to use.

### Scikit-Learn Estimator API
# See the Scikit-Learn API paper (linked below) for details on general rules
# http://arxiv.org/abs/1309.0238

## basics of the API
# 

## Supervised learning example: Simple Linear Regression
# Fitting a line to (x, y) data
import matplotlib.pyplot as plt 
import numpy as np

rng = np.random.RandomState(42)
x = 10 * rng.rand(50)
y = 2 * x - 1 + rng.randn(50)
plt.scatter(x, y)

# Now, with some data in place, can walk through fitting line

##   1) Choose a class of model
# Recall, every class of model is represented by a Python class.
# General list of Regresssion models: http://scikit-learn.org/stable/modules/linear_model.html

# for our linear regression model, import LinearRegression class:
from sklearn.linear_model import LinearRegression

##  2) Choose model hyperparameters
model = LinearRegression(fit_intercept=True)
model