Problem Statement :
===================        
        Find the length of the given integer array. Don't use the len() function.
Input :
=======
        Integer Array 
Output :
========
        Integer - Lenght of the array
      
Code :
=======        
        
def lenght(array):
    count = 0
    iterator = 0
    array.append("+-*/")
    while(array[i]!="+-*/"):
        count += 1
        iterator+=1
    return count 
