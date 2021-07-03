import numpy as np
import matplotlib.pylab as plt
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

# 加载数据集 （numpy版本问题，故加上‘allow_pickle=True’）
data = np.load(r'G:\\Five_Flower.npy', allow_pickle=True)

# for img in data:
#     img1 = img * 255
#     img2 = array_to_img(img1,scale=False)     # 图像类型为<class 'PIL.Image.Image'>
#     plt.imshow(img2)
#     plt.show()

# 取出数据，应该有更好方法
train_x = np.array(data[0])
train_y = np.array(data[1])
validation_x = np.array(data[2])
validation_y = np.array(data[3])
test_x = np.array(data[4])
test_y = np.array(data[5])


# 检查是否正常
print(test_y)
image = validation_x[0]
print(validation_y[0])
plt.imshow(image)
plt.show()
