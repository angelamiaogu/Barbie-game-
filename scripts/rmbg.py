from PIL import Image


img = Image.open("pinkButterfly.jpg")
new_img = img
small_img = new_img.resize((100, 100))
rotate_30_degree = small_img.rotate(-30)
rotate_30_degree.save("small_butterfly.jpg")