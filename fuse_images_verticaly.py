import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import random
import scipy.misc
# from scipy.misc import imsave
#from scipy.misc.pilutil import imsave
# from imageio import imsave
import PIL
from PIL import Image



def fuse_images_vertically(im2, im1, im_shape):

    fused_image = np.zeros((im_shape[0], im_shape[1], im_shape[2]))
    fused_image[0 : int(im_shape[1] / 2), :] = im1[0 : int(im_shape[1] / 2), :]
    fused_image[int(im_shape[1] / 2) : , :] = im2[int(im_shape[1] / 2) : , :]

    return fused_image


def main():
    images_path = "D:\\OneDrive - Philips\\Desktop\\output_for_creating_halves"
    path_to_save = 'D:\\OneDrive - Philips\\Desktop\\final_halves'
    all_images = os.listdir(images_path)

    image_names = set([image.split("_")[0] for image in all_images])
    image_names = list(image_names)

    for image in image_names:
        for upper_index in range(0,10):
                image_num = int(image)
                upper_name = ("%04d" % image_num) + "_" + str(upper_index) + '.png'
                if upper_name in all_images:

                    im1 = mpimg.imread(os.path.join(images_path, upper_name))
                    im_shape = im1.shape

                    for lower_index in range(0,10):
                            lower_name = ("%04d" % image_num) + "_" + str(lower_index) + '.png'
                            if lower_name in all_images:
                                im2 = mpimg.imread(os.path.join(images_path, lower_name))


                                fused_image_1 = fuse_images_vertically(im1, im2, im_shape)
                                fused_image_1_name = upper_name + '_' + lower_name
                                fused_image_2 = fuse_images_vertically(im2, im1, im_shape)
                                fused_image_2_name = lower_name + '_' + upper_name

                                fused_image_1 = Image.fromarray(np.uint8((fused_image_1) * 255))
                                fused_image_2 = Image.fromarray(np.uint8((fused_image_2) * 255))

                                fused_image_1.save(os.path.join(path_to_save, fused_image_1_name), "PNG")
                                fused_image_2.save(os.path.join(path_to_save, fused_image_2_name), "PNG")


        # img_num1 = random.randint(0, 10000)
        # im1_name = 'img' + ("%08d" % img_num1) + '.png'

        # while(im1_name not in all_images):
        #     img_num1 = random.randint(0, 10000)
        #     im1_name = 'img' + ("%08d" % img_num1) + '.png'
        #
        # img_num2 = random.randint(0, 10000)
        # im2_name = 'img' + ("%08d" % img_num2) + '.png'
        #
        # while (im2_name not in all_images):
        #     img_num2 = random.randint(0, 10000)
        #     im2_name = 'img' + ("%08d" % img_num2) + '.png'



        # im2 = mpimg.imread(os.path.join(images_path,im2_name))




        #mpimg.imsave(os.path.join(path_to_save,fused_image_1_name), fused_image_1, vmin=None, vmax=None, cmap=None, format='png', origin=None, dpi=100)
        #mpimg.imsave(os.path.join(path_to_save,fused_image_2_name), fused_image_2, vmin=None, vmax=None, cmap=None, format='png', origin=None, dpi=100)

        # scipy.misc.toimage(fused_image_1).save(os.path.join(path_to_save,fused_image_1_name))
        # scipy.misc.toimage(fused_image_2).save(os.path.join(path_to_save, fused_image_2_name))

        # imsave(os.path.join(path_to_save,fused_image_1_name), fused_image_1)
        # imsave(os.path.join(path_to_save,fused_image_2_name), fused_image_2)

        #fused_image_1 = image(fused_image_1)


        print("")



if __name__ == "__main__":
    main()
