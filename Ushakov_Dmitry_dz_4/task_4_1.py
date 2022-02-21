# 1. Проверить, установлен ли пакет pillow в глобальном окружении.
from PIL import Image

image = Image.open('01.jpg')
image.show()
image = Image.open('02.jpg')
image.show()
image = Image.open('03.jpg')
image.show()
image = Image.open('04.jpg')
image.show()
