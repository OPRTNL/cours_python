from PIL import ImageGrab

capture = ImageGrab.grab()
capture.save("capture.png", "PNG")