import json
import numpy as np

with open("./" + "train_all.json", 'r') as f:
    dict_data = json.load(f)

frames = dict_data["frames"]

selected_points = {}
selected_frames = {}
equator_threshold = -0.4
count = 0

for frame in frames:
    transform_matrix = frame["transform_matrix"]
    c2w = np.array(transform_matrix)

    if c2w[1,3] <= equator_threshold: # TODO > <= ??
        continue

    camera_pos = c2w[:3, 3]

print(count)