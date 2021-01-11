import matplotlib.pyplot as plt
import numpy as np
import pickle
import math
from scipy.stats import fisk
from scipy.stats import norm
from mpl_toolkits import mplot3d

def E_Step(X,Logistic,Gaussian):
    for i in range(len(Logistic)):
        p1=Logistic[i]
        p2=Gaussian[i]
        p=p1+p2
        Logistic[i]=p1/p
        Gaussian[i]=p2/p
    return


def gauss(x, p): # p[0]==mean, p[1]==stdev, p[2]==height                 
    a = p[2]
    mu = p[0]
    sig = p[1]
    return a * np.exp(-1.0 * ((x - mu)**2.0) / (2.0 * sig**2.0))

def M_Step(Partition1,Partition2):
    return

def NormalLikelihood(Samples):
    std=[1,2,3,4,5,6,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12]
    mu=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    maximumLikelihood=float('-inf')
    n=len(Samples)
    for m in mu:
        #plt.title("Maximum Likelihood")
        #plt.tight_layout()
        Likelihood=[]
        Sum=0
        for sample in Samples:
            Sum+=(sample-m)**2
        for s in std:
            num=(1/(np.pi*2*s**2))**(n/2)
            likelihood= num* np.exp(-(1/(2*s**2))*(Sum))
            Likelihood.append(likelihood)
            if likelihood > maximumLikelihood :
                RetStd=s
                Retmu=m
                maximumLikelihood=likelihood
        #plt.plot(std,Likelihood,lw=3,alpha=2.5,label="mu="+str(m))
        #plt.legend()
    return RetStd,Retmu

def LogLogisticLikelihood(Samples):
    p1=[1,1.5,2,3]
    p2=[15,16,17,18,19,20,21,22]
    p3=[30,40,50,60,70,80,90.100]
    maximumLikelihood=float('-inf')
    #ax = plt.axes(projection='3d')
    for a in p1:
        # plt.title("Maximum Likelihood")
        # plt.tight_layout()
        for b in p2:
            Likelihood=[]
            for c in p3:
                Logistic=fisk.pdf(Samples,a,loc=b,scale=c)
                likelihood=0
                for p in Logistic:
                    likelihood+=np.log(p)
                Likelihood.append(likelihood[0])
                if(likelihood > maximumLikelihood):
                    RetA=a
                    RetB=b
                    RetC=c
                    maximumLikelihood=likelihood  
        #ax.plot3D(p3, p2, Likelihood,label='a='+str(a))
        #plt.plot(p3,Likelihood,lw=3,alpha=2.5,label="b="+str(b))
        #plt.legend()
    return RetA,RetB,RetC

with open("RunTimes.pkl",'rb') as f:
    Runtimes,Probs,RuntimesRep=pickle.load(f)
RuntimesRep=np.array(RuntimesRep).reshape(-1,1)
Runtimes=np.array(Runtimes).reshape(-1,1)
RuntimesRep=RuntimesRep[:,0]
RuntimesRep=np.sort(RuntimesRep)

#sigma,mu=NormalLikelihood(Runtimes[0:22])
#gaussian=gauss(Runtimes[0:22],[mu,sigma,0.02])
# fig=plt.figure()
# plt.plot(Runtimes[0:22],gaussian,lw=3,alpha=2.5)
# plt.xscale('log',base=2)

#a,b,c=LogLogisticLikelihood(Runtimes[22:])
#logistic=fisk.pdf(Runtimes[22:],a,loc=b,scale=c)
# fig=plt.figure()
# plt.plot(Runtimes[22:],logistic,lw=3,alpha=2.5)
# plt.xscale('log',base=2)

#initialize the distributions
# dist=[]
# for i in range(len(gauss1)):
#     dist.append((logistic[i]+gauss1[i])/2)
 
# fig = plt.figure()
gauss1=gauss(Runtimes[0:21],[1,0.865,0.02])
logistic=fisk.pdf(Runtimes[21:],1,loc=7.4859,scale=0.8139)
plt.subplot(2, 1, 1)
plt.plot(Runtimes[0:21], gauss1, lw=3, alpha=2.5)
plt.xscale('log',base=2)

plt.subplot(2, 1, 2)
plt.plot(Runtimes[21:], logistic, lw=3, alpha=2.5)
plt.xscale('log',base=2)
plt.tight_layout()
plt.show()

#dist=np.concatenate((gaussian,logistic))
# plt.title("the two distributions")
# plt.xscale('log',base=2)
# plt.tight_layout()
# plt.plot(Runtimes,dist,lw=3,alpha=2.5)
# plt.plot(Runtimes,Probs,lw=3,alpha=2.5)