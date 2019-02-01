#. Find the length of the given integer array. Don't use the len() function.
#algorithm :
        #1. I have added a string to the list and iterated the 
        # list item untill the string is found using while Loop 
        #I have used while loop because where we can't predict when the list get ends
        
def len(array):
    count = 0
    i = 0
    array.append("+-*/")
    while(array[i]!="+-*/"):
        count += 1
        i+=1
    return count 


array = [1,2,3,4,5,6]
print(len(array))