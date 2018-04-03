import matplotlib.pyplot as plt
import numpy as np
import time

from PIL import Image


imgF = Image.open('BW_photo1.jpg')
imgBW = imgF.convert('LA')
img = np.array(list(imgBW.getdata(band=0)), float)
img.shape = (imgBW.size[1], imgBW.size[0])
img = np.matrix(img)
plt.imshow(img, cmap='gray');
plt.show()

u, s, v = np.linalg.svd(img)
print "U: \n", u.shape
print "sigma: \n", s.shape
print "V: \n", v.shape


# Image size is 960*1280
# for 8:1
i=80
rImg = np.matrix(u[:, :i]) * np.diag(s[:i]) * np.matrix(v[:i, :])
plt.imshow(rImg, cmap='gray')
title = "n = %s" % i
plt.title(title)
plt.show()

# for 4:1
i=160
rImg = np.matrix(u[:, :i]) * np.diag(s[:i]) * np.matrix(v[:i, :])
plt.imshow(rImg, cmap='gray')
title = "n = %s" % i
plt.title(title)
plt.show()

# for 2:1
i=320
rImg = np.matrix(u[:, :i]) * np.diag(s[:i]) * np.matrix(v[:i, :])
plt.imshow(rImg, cmap='gray')
title = "n = %s" % i
plt.title(title)
plt.show()