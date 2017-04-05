
def MinMax(ListNum):
   
    if type(ListNum) is list:
       if (min(ListNum)==max(ListNum)):
           return [min(ListNum)]
       else:
           return [min(ListNum),max(ListNum)]  
    else:
       return None
