import pytesseract
from PIL import ImageOps, ImageEnhance
import pyscreenshot


def separate_text(img):
    pix = img.load()
    w, h = img.size
    threshold = 200
    for i in range(0, w):
        for j in range(0, h):
            try:
                r, g, b = img.getpixel((i, j))
                if r > threshold or g > threshold or b > threshold:
                    pix[i, j] = (255, 255, 255)
            except:
                return "nope"
    return img


def get_image_text(img):
    img = separate_text(img)
    return pytesseract.image_to_string(img, lang="eng")


def get_question_and_answers():
    question = get_image_text(pyscreenshot.grab(bbox=(75, 200, 400, 350)))
    answers = {
        0: get_image_text(pyscreenshot.grab(bbox=(85, 360, 400, 410))),
        1: get_image_text(pyscreenshot.grab(bbox=(85, 425, 400, 475))),
        2: get_image_text(pyscreenshot.grab(bbox=(85, 490, 400, 540)))
    }
    return question, answers
