import json
import random
import os

def make_json(input_dir="./", output_dir="test/"):
    with open(input_dir + "train_all.json", 'r') as f:
        dict_data = json.load(f)

    frames = dict_data["frames"]

    for num_image in [25, 50]:
        # get images randomly
        modified_frames = random.sample(frames, num_image)

        dict_data["frames"] = modified_frames

        with open(output_dir + f"train_all_{num_image}_random.json", "w") as f:
            json.dump(dict_data, f)
            #json.dump(dict_data, f, indent=4)



path = "/home/ccl/Datasets/NeRF/ScanNerf/"
scene_list = sorted(os.listdir(path))

for scene in scene_list:
    input_dir = f"{path}{scene}/"


    # new_dir_path = f"./train_all_25_50_scenes/{scene}"
    # if not os.path.exists(new_dir_path):
    #     os.mkdir(new_dir_path)
    # new_dir = new_dir_path + "/"

    # new_dir = f"{path}{scene}/" 

    make_json(input_dir, new_dir)

