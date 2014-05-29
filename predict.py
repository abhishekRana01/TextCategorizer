from imports import *

def predict(X,batchsize):
    with open('my_dumped_classifier.pkl', 'rb') as fid:
        clf = cPickle.load(fid)
    count0 = 0
    count1 = batchsize
    prediction = []
    max = shape(X)[0]
    if(batchsize >= max):
        X_test = np.array(X.todense())
        prediction.append(clf.predict(X_test).tolist())
        return list(itertools.chain.from_iterable(prediction))
    else:
        while(count1 <= max):
            X_test = np.array(X[count0:count1].todense())
            prediction.append (clf.predict(X_test).tolist())
            count0 = count1
            count1 += batchsize
    return list(itertools.chain.from_iterable(prediction))
