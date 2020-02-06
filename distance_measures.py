import numpy as np
from math import sqrt

# Euclidean distance
def euclidean(x, y):
    distance = 0
    for a, b in zip(x, y):
        distance += (sum([(pow((a-b),2))]))
    return sqrt(distance)
print("Euclidean Distance:",euclidean([1,3,4,1],[3,2,1,1]))

# Manhattan distance
def manhattan(x, y):
    distance=0
    for a,b in zip(x,y):
        distance += sum([abs(a-b)])
    return distance
print("Manhattan Distance:",manhattan([1,3,4,1],[3,2,1,1]))

#chebyshev distance
def chebyshev(x,y):
    distance = []
    for a,b in zip(x,y):
        distance.append(abs(a-b))
    return max(distance)
print("Chebyshev Distance:",chebyshev([1,3,4,1],[3,2,1,1]))

#hamming distance
def hamming(x,y):
    distance = 0
    for a,b in zip(x,y):
        if a != b:
            distance += 1
    return distance
print("Hamming Distance:",hamming("hello world","hallo warld"))

#cosine_similarity
def cosine_similarity(x,y):
    numerator = 0
    sum_x = 0
    sum_y = 0
    for a,b in zip(x,y):
        numerator += sum([a * b])
        sum_x += sum([a**2])
        sum_y += sum([b**2])
    denominator = round(sqrt(sum_x) * sqrt(sum_y))
    return numerator / denominator
print("Cosine Similarity:", cosine_similarity([1,3,4,1],[3,2,1,1]))

#jaccard
def jaccard_similarity(x,y):
    intersection = len(set(x).intersection(set(y)))
    union = len(set(x).union(set(y)))
    return (intersection / union)
print("Jaccard Similarity:",jaccard_similarity([0,1,2,5,6], [0,2,3,4,5,7,9]))
print("Jaccard Distance:", 1-jaccard_similarity([0,1,2,5,6],[0,2,3,4,5,7,9]))