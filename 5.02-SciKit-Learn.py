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