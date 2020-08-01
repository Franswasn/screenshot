from PIL import Image,ImageGrab
import time
#action = input ('Take screenshot y/n ?: ')
def takeScreenshot ():
    image = ImageGrab.grab()
    image.show()
    
if __name__ == "__main__":
    time.sleep(2)
    takeScreenshot()
