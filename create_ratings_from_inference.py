import os
import numpy as np
path = "D:\\OneDrive - Philips\\Desktop\\"
folder = os.path.join(path,"final_halves")
images = os.listdir(folder)
image_filenames = sorted(images)
number_of_means = 4
beauty_rates_halves = np.zeros((len(image_filenames), number_of_means))
for i, image_file_name in enumerate(image_filenames):
    upper_rate = int(image_file_name.split(".")[0].split("_")[1]) / 10
    lower_rate = int(image_file_name.split(".")[1].split("_")[2]) / 10
    beauty_rates_halves[i,0] = upper_rate
    beauty_rates_halves[i,1] = upper_rate

    beauty_rates_halves[i, 2] = lower_rate
    beauty_rates_halves[i, 3] = lower_rate

csv_new_rates_name = "latest_ratings.csv"
np.savetxt(os.path.join(path,csv_new_rates_name), beauty_rates_halves, delimiter=",")




