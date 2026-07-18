import numpy as np

array=np.array([[["a","b","c"],
              ["a","b","c"],
              ["a","b","c"]] for i in range(3)])

print(array.ndim)

word=array[0,0,0]+array[0,1,1]+array[0,2,2]
print(word)
# what


arr=        [[1, 2 ,3 ,4],
             [5, 6 ,7 ,8],
             [9, 10,11,12],
             [13,14,15,16]]

print(arr[row[0:2]] for row in range(0,2))

