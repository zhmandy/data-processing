# 利用KNN分类算法进行分类
from sklearn import neighbors , datasets
iris = datasets.load_iris()
knn = neighbors.KNeighborsClassifier()
# 从已有数据中学习
knn.fit(iris.data, iris.target)
# 利用分类模型进行未知数据的预测（确定标签）
knn.predict([[5.0, 3.0, 5.0, 2.0]])