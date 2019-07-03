from cv2 import cv2
import numpy as np
import pytesseract
from PIL import Image


path = "C://Users//HHS//Desktop//ScanIt//"
imgPath = path + "form.jpg"
img = cv2.imread(imgPath)

def preprocess(path, imgPath):
    gray = cv2.imread(imgPath, 0)
    inverted = 255 - gray
    kernel = np.ones((2,2), np.uint8)
    dilated = cv2.dilate(inverted, kernel)
    cv2.imwrite(path+"sample//dilated.jpg",dilated)

    ret, thres = cv2.threshold(dilated, 0, 255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imwrite(path+"sample//threshold.jpg",thres)
    
    kernel = np.ones((1,16), np.uint8)
    blobs = cv2.morphologyEx(thres, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite(path+"sample//blobs.jpg",blobs)
    
    return blobs

def identifyChunks(blobs, padding=2):
    contours, hierarchy = cv2.findContours(blobs.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # create mask layer with black background
    mask = np.zeros(blobs.shape, np.uint8)
    
    i = 0
    for contour in range(len(contours)):
            i = i +1
            (x, y, w, h) = cv2.boundingRect(contours[contour])

            # mask around bounding rectangle
            mask[y:y+h, x:x+w] = 0
            
            # white fill to bounding rectangle area
            cv2.drawContours(mask, contours, contour, (255, 255, 255), -1)
            cv2.imwrite(path+"sample//result" + str(i) + ".jpg",mask)

            
            # calculate ratio of non-black
            ratio = float(cv2.countNonZero(mask[y:y+h, x:x+w])) / (w * h)
            
            if  w > 5 and h > 5:
                cv2.rectangle(img, (x-padding, y-padding), (x+w+padding, y+h+padding), (0, 0, 255), 2)
                # textExtract(img[y-3:y+h+3, x-3:x+w+3])
                
    cv2.imwrite(path+"sample//result.jpg",img)

    return img

def textExtract(img):
    img = Image.fromarray(img, 'RGB')
    # img.show()
    # cv2.waitKey(0)
    text = pytesseract.image_to_string(img)
    if(text == ""):
        imgArray.append(img)
    else:
        textArray.append(text)

if __name__ == '__main__':
    textArray = []
    imgArray = []

    blobs = preprocess(path, imgPath)
    img = identifyChunks(blobs)
    
    print(textArray)
    print(imgArray)