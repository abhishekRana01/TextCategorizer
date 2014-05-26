def prcntagaccurcy(pred,Y):
    j = 0
    for i in range(len(pred)):
        if(pred[i] == Y[i]):
            j +=1
    return (j/float(len(pred)))*100
