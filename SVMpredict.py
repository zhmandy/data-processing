from sklearn import svm, datasets

iris = datasets.load_iris()
svc = svm.LinearSVC()
svc.fit(iris.data, iris.target) # 学习
svc.predict([[ 5.0, 3.0, 5.0, 2.0]])  # 预测