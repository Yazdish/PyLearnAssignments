import os
import imageio


# result = os.listdir("../assignment3")
# print(result)

file_list = sorted(os.listdir("image2"))
print(file_list)
images = []
for file_name in file_list:
    file_path = "image2/" + file_name
    image = imageio.imread(file_path)
    images.append(image)

imageio.mimsave("result2.gif", images)
