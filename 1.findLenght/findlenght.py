#. Find the length of the given integer array. Don't use the len() function.

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