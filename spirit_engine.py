import numpy as np

animals = {
    "Shadow Owl 🦉": {
        "vector": [80, 30, 60, 40, 70],
        "description": "Silent strategist. Night-driven focus and analytical dominance."
    },
    "Lone Wolf 🐺": {
        "vector": [75, 60, 50, 85, 65],
        "description": "Independent yet socially aware. Balanced power."
    },
    "Neon Tiger 🐯": {
        "vector": [90, 50, 70, 40, 80],
        "description": "Aggressive drive. High performance predator."
    },
    "Silver Fox 🦊": {
        "vector": [60, 70, 75, 55, 50],
        "description": "Emotionally adaptive and clever."
    },
    "Crimson Phoenix 🔥": {
        "vector": [85, 55, 80, 50, 90],
        "description": "High intensity rebirth energy. Thrives under pressure."
    },
    "Void Raven 🐦‍⬛": {
        "vector": [65, 40, 85, 45, 70],
        "description": "Emotionally perceptive observer."
    },
    "Frost Dragon 🐉": {
        "vector": [95, 60, 75, 55, 85],
        "description": "Dominant presence. High control and power."
    }
}


def find_spirit(user_vector):
    min_distance = float("inf")
    best_match = None
    
    for name, data in animals.items():
        animal_vector = np.array(data["vector"])
        distance = np.linalg.norm(np.array(user_vector) - animal_vector)
        
        if distance < min_distance:
            min_distance = distance
            best_match = (name, data["description"])
    
    return best_match
