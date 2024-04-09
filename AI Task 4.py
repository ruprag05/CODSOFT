import numpy as np
from scipy.spatial.distance import cosine
from sklearn.metrics.pairwise import cosine_similarity

class RecommendationSystem:
    def __init__(self, user_preferences):
        self.user_preferences = user_preferences
        self.item_similarity = cosine_similarity(user_preferences)

    def recommend(self, user_id, num_recommendations=1):
        user_preferences = self.user_preferences[user_id]
        item_similarity = self.item_similarity[user_id]

        item_similarity[user_preferences.nonzero()] = 0

        top_indices = np.argsort(item_similarity)[::-1][:num_recommendations]
        return top_indices
user_preferences = np.array([
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 1, 1],
])

recommendation_system = RecommendationSystem(user_preferences)

recommended_items = recommendation_system.recommend(0)
print("Recommended items for user 0:", recommended_items)
