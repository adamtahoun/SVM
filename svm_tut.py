from sklearn import svm

X = [[0,0],[0,1],[1,1]]
y = [0,1,1]
clf = svm.SVC()
clf.fit(X,y)
pred = clf.predict([[1,0]])
print(pred)
