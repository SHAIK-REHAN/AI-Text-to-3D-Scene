scene = {
    "objects": ["boy", "football"],
    "actions": ["playing"],
    "environment": ["park"]
}

# Mapping dictionary
object_map = {
    "boy": "human_model",
    "football": "ball_model"
}

environment_map = {
    "park": "park_scene"
}

action_map = {
    "playing": "play_animation"
}

# Convert to 3D instructions
mapped_scene = {
    "models": [object_map.get(obj, obj) for obj in scene["objects"]],
    "environment": [environment_map.get(env, env) for env in scene["environment"]],
    "actions": [action_map.get(act, act) for act in scene["actions"]]
}

print(mapped_scene)