import numpy as np
from numpy import genfromtxt
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image


path = "D:\\OneDrive - Philips\\Desktop"
beaty_rates_name = "beauty_rates_easy.csv"
celebs_dir = "img"

k = 50
new_directory_ugliest_name = 'celeba_top_'+str(k)+'_ugliest'
new_directory_beautiest_name = 'celeba_top_'+str(k)+'_beautiest'

if not os.path.exists(os.path.join(path,new_directory_ugliest_name)):
    os.mkdir(os.path.join(path,new_directory_ugliest_name))
if not os.path.exists(os.path.join(path,new_directory_beautiest_name)):
    os.mkdir(os.path.join(path,new_directory_beautiest_name))


beauty_rates = genfromtxt(os.path.join(path,beaty_rates_name), delimiter=',')
print(beauty_rates.shape)

means = np.zeros((30000,1))
indices_top_k_ugliest = []
indices_top_k_beautiest = []
for i, row in enumerate(beauty_rates):
    mean =np.mean(row)
    means[i] = mean

sorted = np.sort(means, axis=0)
for i in range(k):
    itemindex_ugly = np.where(means == sorted[i])
    indices_top_k_ugliest.append(itemindex_ugly[0][0])

    itemindex_beauty = np.where(means == sorted[beauty_rates.shape[0] - 1 - i])
    indices_top_k_beautiest.append(itemindex_beauty[0][0])

print("ugliest are:")
print(indices_top_k_ugliest)
print("with scores:")
print(means[indices_top_k_ugliest])


for ugly in indices_top_k_ugliest:
    celeb_name = 'img' + ("%08d" % (ugly)) + '.png'
    celeb_img = mpimg.imread(os.path.join(path, celebs_dir,celeb_name))
    celeb_img = Image.fromarray(np.uint8((celeb_img) * 255))
    celeb_img.save(os.path.join(path,new_directory_ugliest_name, celeb_name), "PNG")
    # plt.imshow(celeb_img)
    # plt.show()

print("beautiest are:")
print(indices_top_k_beautiest)
print("with scores:")
print(means[indices_top_k_beautiest])

for beauty in indices_top_k_beautiest:
    celeb_name = 'img' + ("%08d" % (beauty)) + '.png'
    celeb_img = mpimg.imread(os.path.join(path, celebs_dir,celeb_name))
    celeb_img = Image.fromarray(np.uint8((celeb_img) * 255))
    celeb_img.save(os.path.join(path, new_directory_beautiest_name, celeb_name), "PNG")
    # plt.imshow(celeb_img)
    # plt.show()





