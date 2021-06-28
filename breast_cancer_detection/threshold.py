import numpy as np
def selectThreshold(yval,pval):

    bestEpsilon = 0
    bestF1 =0
    F1 =0
    tp=0
    fp=0
    fn=0
    for  epsilon in np.linspace(1.01*min(pval),max(pval)):
        var = (pval<epsilon)
        for i in range(yval.size):
          
            temp = (yval[i]==var[i])
            if(temp==1):
                if(var[i]==1):
                    
                    tp+=1
            else:
                if(var[i] ==1):
                    fp+=1
                else:
                    fn+=1
            
        if(tp==0):
                continue
        else:
            prec = (tp)/(tp+fp)
            rec = (tp)/(tp+fn)
            F1 = (2*prec*rec)/(prec+rec)
        if F1>bestF1:
            bestF1 = F1
            bestEpsilon = epsilon
        tp=0
        fp=0
        fn=0
            
            
            
            
        
    return bestEpsilon,bestF1