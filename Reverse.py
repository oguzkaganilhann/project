yeniliste=[]
def listeçevir(x):
    for i in x:
        if isinstance(i,list):
            i =i[::-1]
            yeniliste.append(i)
        else:
            i = i[::-1]
            yeniliste.append(i)
    return yeniliste[::-1]
