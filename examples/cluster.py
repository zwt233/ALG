import numpy as np
import torch

 
def newCent(L):

    centroids = []
    label_list = np.unique(L[:,-1])
    for i in label_list:
        L_i = L[(L[:,-1])==i]
        cent_i = np.mean(L_i,0)
        centroids.append(cent_i[:-1])
    return np.array(centroids) 

def semi_kMeans(L, U, initial_centriod=newCent):

    dataSet = np.vstack((L[:,:-1],U))
    label_list = np.unique(L[:,-1])
    k = len(label_list)          
    m = np.shape(U)[0]
    n = np.shape(L)[0]
    
    clusterAssment = np.zeros(n+m)
    clusterAssment[:n] = L[:,-1] 
    centroids = initial_centriod(L)
    clusterChanged = True

    while clusterChanged:
        clusterChanged = False
        distance=torch.cdist(torch.Tensor(dataSet[n:]),torch.Tensor(centroids)).numpy()
        idx=np.argmin(distance,axis=1)
        if not ((clusterAssment[n:]==idx).all()):
            clusterChanged = True       
                
        clusterAssment[n:]=idx
         
        for cent in range(k):
            
            ptsInClust = dataSet[np.nonzero(clusterAssment==cent)[0]] 

            centroids[cent,:] = np.mean(ptsInClust, axis=0) 

    return clusterAssment,centroids