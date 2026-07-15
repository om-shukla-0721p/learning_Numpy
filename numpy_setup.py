import numpy as np

arr=np.array([[["a","b","c"],
              ["a","b","c"],
              ["a","b","c"]] for i in range(3)])

print(arr.ndim)

word=arr[0,0,0]+arr[0,1,1]+arr[0,2,2]
print(word)

