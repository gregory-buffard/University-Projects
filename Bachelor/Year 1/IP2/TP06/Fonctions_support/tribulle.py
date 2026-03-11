def tribulle(L : list[int]) -> None :    
    for k in range(len(L)-1):
        permutation = False
        for pos in range(len(L)-1):           
            if L[pos+1]< L[pos] :
                temp=L[pos+1]
                L[pos+1]=L[pos]
                L[pos]=temp                         
        print(f"  L={L} ")
L = [9,7,3,8,1]
tribulle(L)