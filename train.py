from imports import *

clf = svm.LinearSVC()

def train(X,Y,batchsize):
    count0 = 0
    count1 = batchsize
    if ( batchsize >= len(Y) ):
        X_train = np.array(X.todense())
        Y_train = np.array(Y)
        clf.fit(X_train,Y_train)
    else:
        while(count1 <= len(Y)):
            X_train = np.array(X[count0:count1].todense())
            Y_train = np.array(Y[count0:count1])
            clf.fit(X_train,Y_train)
            count0 = count1
            count1 += batchsize
    with open('my_dumped_classifier.pkl', 'wb') as fid:
        cPickle.dump(clf, fid)
