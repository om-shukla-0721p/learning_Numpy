import numpy as np
rng=np.random.default_rng(seed=10)
# seed is a specific code saved one seed has one fixed value of genearation

arr=rng.integers(low=1,high=101,size=(4,4))

print(arr)

np.random.seed(seed=1)

print(np.random.uniform(low=-1,high=1))


# shuffling arrays
rng=np.random.default_rng()

arr=[1,2,3,4,5]
rng.shuffle(arr)

print(arr)



fruits=np.array(["apple","banana","orange","pineapple","strawberry"])
fruits=rng.choice(fruits,size=(3,3))

print(fruits)