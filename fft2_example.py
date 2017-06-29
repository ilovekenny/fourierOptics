from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# open an 8bpp indexed image
img = Image.open('circles.bmp')
# as array
img_data = np.asarray(img)
# perform fft2
fourier = np.fft.fft2(img_data)
# fftshift
fourier = np.fft.fftshift(fourier)
# abs
fourier = np.abs(fourier)
# log10
fourier = np.log10(fourier)
# lowest
lowest = np.nanmin(fourier)
# highest
highest = np.nanmax(fourier)
# contrast
original_range = highest - lowest
# normalize
norm_fourier = (fourier - lowest) / original_range * 255
# convert to image
norm_fourier_img = Image.fromarray(norm_fourier)
# display and save
fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax1.imshow(img,cmap='gray')
ax2.imshow(norm_fourier_img)
ax1.title.set_text('Original image')
ax2.title.set_text('Fourier image')
plt.show()