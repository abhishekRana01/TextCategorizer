from imports import *

def predict(X,Y,batchsize):
    with open('my_dumped_classifier.pkl', 'rb') as fid:
        clf = cPickle.load(fid)
    count0 = 0
    count1 = batchsize
    prediction = []
    if(batchsize >= len(Y)):
        X_test = np.array(X.todense())
        Y_test = np.array(Y)
        prediction.append(clf.predict(X_test).tolist())
        return list(itertools.chain.from_iterable(prediction))
    else:
        while(count1 <= len(Y)):
            X_test = np.array(X[count0:count1].todense())
            Y_test = np.array(Y[count0:count1])
            prediction.append (clf.predict(X_test).tolist())
            count0 = count1
            count1 += batchsize
    return list(itertools.chain.from_iterable(prediction))
