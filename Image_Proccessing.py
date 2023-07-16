from PIL import Image, ImageFilter
img = Image.open('my.png.jpg')
# img.show()

b_image = img.filter(ImageFilter.BLUR)
# b_image.show()

g_image = img.convert('L')
# g_image .show()

p_image = img.filter(ImageFilter.FIND_EDGES)
# p_image.show()
