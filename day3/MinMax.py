''' This function outputs the minimum and the maximum number in a list '''
def MinMax(ListNum):
   
   if type(ListNum) is list:
      '''checks whether the minmum number and the maximum are equal'''
      if (min(ListNum)==max(ListNum)):         
         return [min(ListNum)]
      else:
         return [min(ListNum),max(ListNum)]  
   else:
       return None
