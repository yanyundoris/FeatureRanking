# FeatureRanking

## What is FeatureRankingTool

FeatureRankingTool is a python package which can help you ranking and analysis your features if you want to train a learning model. Currently it support these functions:

1. Ranking your features by linear coefficience (For linear model only)
2. Ranking your features by feature importance (For tree model only)
3. Find misclassified data point (For classification problem only)
4. Find correlation coefficience among features and label.

## You are welcome to:

1. Report bug for this project, and
2. Add new function which we will frequently use when we train a model

## What dependencies you need to install


1. sklearn
2. pandas
3. numpy
4. random

## How to install it

`pip install FeatureRankingTool --upgrade`


## How to use it - a demo using iris dataset from sklearn

### Prepare your dataset:

```python
from sklearn import datasets
import pandas as pd
import numpy as np

# Load iris data
iris = datasets.load_iris()

# Get features and target 
feature = iris.data
target = np.array(iris.target)
target = target.reshape(len(target),1)

# Merge features and target into a DataFrame
data = np.concatenate((feature,target),axis=1)
data = pd.DataFrame(data,columns=['sepal_length','sepal_width','petal_length','petal_width','target'])

```

### Choose a model you need to use, like, linear-svm:
```python
from sklearn.svm import SVC
from FeatureRankingTool import RankingTool

feature_columns = ['sepal_length','sepal_width','petal_length','petal_width']
target_name = 'target'

classif = SVC(kernel='linear')
result = RankingTool.RankingFeature(data,classif,feature_columns,target_name,modeltype='linear',use_cv=5)

```
### Or, you can use tree-based model instead:

```python
from sklearn.ensemble import RandomForestRegressor
from FeatureRankingTool import RankingTool

feature_columns = ['sepal_length','sepal_width','petal_length','petal_width']
target_name = 'target'

classif = RandomForestRegressor()
result = RankingTool.RankingFeature(data,classif,feature_columns,target_name,modeltype='tree',use_cv=5)

```

### For feature & target correlation, you can use:

```python
RankingTool.GetFeatureCoef(data,feature_columns,target_name)

```


## Version

1.0.9

## Function description

## License

MIT
