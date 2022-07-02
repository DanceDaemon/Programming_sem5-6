"""4.2. Разработать фрагмент программы с использованием библиотеки pyqrcode, позволяющей создавать изображение QR-кода на основе переданной в программу текстовой строки."""

import pyqrcode, random

code = pyqrcode.create("This QR-code is for exersise 4.2")
code.svg("QR-code.svg", scale=4, background="white")

"""4.3. Реализовать модификацию изображения генерируемого QR-кода: раскрасить фрагменты изображения в несколько случайно определяемых цветов."""

colors = ['white', 'blue', 'red', 'green', 'orange', 'black', 'yellow', 'purple', 'grey']
moduleColor1 = colors[random.randint(0, 8)]
moduleColor2 = colors[random.randint(0, 8)]
backgroundColor1 = colors[random.randint(0, 8)]
backgroundColor2 = colors[random.randint(0, 8)]

code.svg("4.3_QR-code_first.svg", scale=4, module_color=moduleColor1, background=backgroundColor1)
code.svg("4.3_QR-code_second.svg", scale=4, module_color=moduleColor2, background=backgroundColor2)