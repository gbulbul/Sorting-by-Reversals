# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 14:27:09 2024

@author: gbulb
"""
class sorting_by_reversals:
    def find_reverses(perm1,perm2):
        tuples=()
        counter=0
        for k in range(len(perm1)):
            for m in range(len(perm1)):
                for i,j in enumerate(zip(perm1,perm2)):
                    if j[0]!=j[1] and perm1[k]==perm2[i] and perm1[i]==perm2[m] and k!=m and k!=i and i!=m:
                       if perm2[i] not in tuples and perm1[i] not in tuples:
                          tuples+=(perm2[i],perm1[i])
        return tuples
    def organize_output(tup):
        dict_={1: [tup[0],tup[2]],2: [tup[1],tup[3]] }
        df = pd.DataFrame(dict_,index=['', ''])
        df.columns = df.iloc[0,:].values
        df = df.tail(-1)
        print(len(dict_.keys()))
        print(df)
    
if __name__=="__main__":    
    perm1,perm2=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[1, 8, 9, 3, 2, 7, 6, 5, 4, 10]
    tup=sorting_by_reversals.find_reverses(perm1,perm2)
    import pandas as pd
    sorting_by_reversals.organize_output(tup)
    
       
        


