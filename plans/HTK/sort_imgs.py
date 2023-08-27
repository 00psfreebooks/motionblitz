# make sure images are numberd in order
# ex: 10.png
# ex: 10_tmp.png

import os
import shutil

imgs_dir = "./"
img_ext = ".png"

imgs_names = []
new_image_names = []

name_appends = [
    "_tmp",
]

# get number of files in directory
num_files = len([f for f in os.listdir(imgs_dir)if os.path.isfile(os.path.join(imgs_dir, f))])

for i in range(1, num_files+1):
    imgs_names.append(str(i) + img_ext)

# check if file names have name appends and remove them
for file in os.listdir(imgs_dir):
    for append in name_appends:
        if file.__contains__(append):
            newfile = file.replace(append, "")
            # write to new file
            if newfile.__contains__(img_ext):
                os.rename(imgs_dir + file, imgs_dir + newfile)
            else:
                os.rename(imgs_dir + file, imgs_dir + newfile + img_ext)
            



# for every 7 images, append the wk number and the day of the week to the day of the week
for i in range(1, num_files + 1, 7):
    for j in range(1, 8):
        new_image_names.append("w" + str((i // 7) + 1) + "-d" + str(j) + img_ext)

# copy new names to new files
for i in range(len(imgs_names)):
    shutil.copyfile(os.path.join(imgs_dir, imgs_names[i]), os.path.join(imgs_dir, new_image_names[i]))

