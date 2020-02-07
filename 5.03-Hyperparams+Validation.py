# Don't just blindly throw ML at things. Consider carefully the following related points:
#   Choice of HyperParams     (your 'priors')
#   Choice of Model
# To be reasonably sure our model is doing what we want, have to perform Validation on it.

### Model Validation: A Poor approach.
# load in iris data
from sklearn.datasets import load_iris
iris = load_iris()
x = iris.data
y = iris.target
# choose k-neighbors model
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=1)

