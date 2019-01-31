import os
import csv
import numpy as np
from numpy import genfromtxt

def load_csv(dataset_folder,name_to_save,csv_to_read):
    path = 'D:\OneDrive - Philips\Desktop'
    destination_folder = 'survey&model_400_All_Ratings'
    # Dictionary to load dataset
    # key: image name
    # value: list of 60 beauty rates from raters
    dataset_dict = {}

    # csv will be stored in the parent folder
    csv_folder = os.path.dirname(dataset_folder)

    # read raters csv file
    with open(os.path.join(path,destination_folder, csv_to_read), 'r') as csvfile:

        raw_dataset = csv.reader(csvfile, delimiter=',', quotechar='|')
        for i, row in enumerate(raw_dataset):
            row = ','.join(row)
            row = row.split(',')

            # create list of rates for each image
            if row[1] in dataset_dict:
                dataset_dict[row[1]][0].append(float(row[2]))
            else:
                dataset_dict[row[1]] = [[float(row[2])]]

    beauty_rates_list = []

    # move dict to lists, convert beauty rates to numpy ranged in [0,1]
    keylist = dataset_dict.keys()
    for key in sorted(keylist):
        beauty_rates_list.append(dataset_dict[key])

    # convert dataset_dict to a numpy of beauty rates in shape of [images,1]
    print("")
    beauty_rates_np = (np.array(beauty_rates_list, dtype=np.float32) / 5.0)

    # change shape from [images,1,60] to [images,60]
    beauty_rates_np = np.squeeze(beauty_rates_np, axis=1)

    np.savetxt(os.path.join(path,destination_folder,name_to_save), beauty_rates_np, delimiter=",")

    return beauty_rates_np


def main():
    path = 'D:\OneDrive - Philips\Desktop'
    destination_folder = 'survey&model_400_All_Ratings'
    name_to_save = 'beauty_rates_model_dean.csv'
    #name_to_save = 'beauty_rates_model.csv'
    csv_to_read = 'All_Ratings_model_dean.csv'
    #csv_to_read = 'All_Ratings_model.csv'

    dataset_folder = os.path.join(path,destination_folder)
    load_csv(dataset_folder,name_to_save,csv_to_read)
    # tfrecord_dir = '/home/deanir/datasets/Halves_from_inference/'
    # image_dir = '/home/deanir/datasets/Halves_from_inference/img/'
    # shuffle = True
    # create_from_images_cond_continuous(tfrecord_dir, image_dir, shuffle)
#----------------------------------------------------------------------------

if __name__ == "__main__":
    # execute_cmdline(sys.argv)
    main()
#--------------------------------------