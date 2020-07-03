
from PIL import Image, ImageFont, ImageDraw

def resize(img,width,high):
    img = img.resize((width, high), Image.ANTIALIAS)
    return img

def add_image(back,front,place):
    front=front.convert("RGBA")

    back.paste(front, place, mask=front)


def characteristic_img(characteristic):
    if characteristic.currentText() == "Ą":
        die1 = "Templates/Symbology and Misc/melee-white.png"
    if characteristic.currentText() == "ą":
        die1 = "Templates/Symbology and Misc/ranged-white.png"
    if characteristic.currentText() == "Ć":
        die1 = "Templates/Symbology and Misc/indirect-white.png"
    if characteristic.currentText() == "ć":
        die1 = "Templates/Symbology and Misc/shield-white.png"
    if characteristic.currentText() == "Ĉ":
        die1 = "Templates/Symbology and Misc/resource-white.png"
    if characteristic.currentText() == "ĉ":
        die1 = "Templates/Symbology and Misc/disrupt-white.png"
    if characteristic.currentText() == "Ċ":
        die1 = "Templates/Symbology and Misc/discard-white.png"
    if characteristic.currentText() == "ċ":
        die1 = "Templates/Symbology and Misc/focus-white.png"
    if characteristic.currentText() == "Č":
        die1 = "Templates/Symbology and Misc/special-white.png"
    if characteristic.currentText() == "č":
        die1 = "Templates/Symbology and Misc/Blank Die Fill.png"

    return die1

def costs_img(characteristic):
    die1 = ""
    if characteristic.currentText() == "Ą":
        die1 = "Templates/Symbology and Misc/melee-yellow.png"
    if characteristic.currentText() == "ą":
        die1 = "Templates/Symbology and Misc/ranged-yellow.png"
    if characteristic.currentText() == "Ć":
        die1 = "Templates/Symbology and Misc/indirect-yellow.png"
    if characteristic.currentText() == "ć":
        die1 = "Templates/Symbology and Misc/shield-yellow.png"
    if characteristic.currentText() == "Ĉ":
        die1 = "Templates/Symbology and Misc/resource-yellow.png"
    if characteristic.currentText() == "ĉ":
        die1 = "Templates/Symbology and Misc/disrupt-yellow.png"
    if characteristic.currentText() == "Ċ":
        die1 = "Templates/Symbology and Misc/discard-yellow.png"
    if characteristic.currentText() == "ċ":
        die1 = "Templates/Symbology and Misc/focus-yellow.png"
    if characteristic.currentText() == "Č":
        die1 = "Templates/Symbology and Misc/special-white.png"
    if characteristic.currentText() == "č":
        die1 = "Templates/Symbology and Misc/Blank Die Fill.png"

    return die1

