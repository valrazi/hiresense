import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(vec1, vec2):

    v1 = np.array(vec1).reshape(1, -1)
    v2 = np.array(vec2).reshape(1, -1)

    similarity = cosine_similarity(v1, v2)[0][0]

    return float(similarity)