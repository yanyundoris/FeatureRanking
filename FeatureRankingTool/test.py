from sklearn import datasets
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
import random
from sklearn.datasets import make_multilabel_classification
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from FeatureRankingTool import RankingTool


iris = datasets.load_iris()

X = iris.data
Y = np.array(iris.target)
Y = Y.reshape(len(Y),1)

XY = np.concatenate((X,Y),axis=1)

print XY.shape

XY = pd.DataFrame(XY,columns=['sepal_length','sepal_width','petal_length','petal_width','target'])

print XY
#classif = SVC(kernel='linear')
classif = RandomForestRegressor()

classifier = OneVsRestClassifier(SVC(kernel='linear', probability=True))
classifier.fit(X, Y.ravel())

result = RankingTool.GetLearningResult(XY,classif,['sepal_length','sepal_width','petal_length','petal_width'],'target',modeltype='tree',use_cv=5)

print result