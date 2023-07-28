import cv2 as cv
import numpy as np 
import pyautogui
import time 

#images 
cookie = cv.imread("C:/Users/jamie/Desktop/Code/Projects/Cookie Clicker Bot/cookie.png", cv.IMREAD_GRAYSCALE)
cursor = cv.imread("C:/Users/jamie/Desktop/Code/Projects/Cookie Clicker Bot/additionalcursor.png", cv.IMREAD_GRAYSCALE)
gran = cv.imread("C:/Users/jamie/Desktop/Code/Projects/Cookie Clicker Bot/gran.png", cv.IMREAD_GRAYSCALE)
farm = cv.imread("C:/Users/jamie/Desktop/Code/Projects/Cookie Clicker Bot/farm.png", cv.IMREAD_GRAYSCALE)
mine = cv.imread("C:/Users/jamie/Desktop/Code/Projects/Cookie Clicker Bot/mine.png", cv.IMREAD_GRAYSCALE)
factory = cv.imread("C:/Users/jamie/Desktop/Code/Projects/Cookie Clicker Bot/factory.png", cv.IMREAD_GRAYSCALE)
bank = cv.imread("C:/Users/jamie/Desktop/Code/Projects/Cookie Clicker Bot/bank.png", cv.IMREAD_GRAYSCALE)
cookie_screen = cv.imread("C:/Users/jamie/Desktop/Code/Projects/Cookie Clicker Bot/cookie screen.png", cv.IMREAD_GRAYSCALE)


def find(haystack, needle, threshhold=0.5,click=False, debug=False):
    result = cv.matchTemplate(haystack, needle, cv.TM_CCOEFF_NORMED)
    
    w = needle.shape[1]
    h = needle.shape[0]
    
    locs = np.where(result >= threshhold)
    locs = list(zip(*locs[::-1]))

    rectangles = []
    for loc in locs:
        rect = [loc[0], loc[1], w, h]
        rectangles.append(rect)
        rectangles.append(rect)
        
    rectangles, weight = cv.groupRectangles(rectangles, 1, 0.2)
       
    if len(rectangles): 
        for (x, y, w, h) in rectangles:
            top_left = (x,y)
            bottom_right = (x+w, y+h)
            cv.rectangle(haystack, top_left, bottom_right, (0,255,0), 2)
       
    if debug == True:
        print(f"Rectangles: {rectangles}")
        
    if click == True:
        for (x,y,w,h) in rectangles:
            pyautogui.moveTo(x+int(w/2), y+int(h/2))
            pyautogui.click(x+int(w/2), y+int(h/2))
            time.sleep(1)
      
 

count = 0
while True:
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2GRAY)
    
    if count == 10:
        pyautogui.moveTo(1633, 220)
        pyautogui.click(1633, 220)
        count = 0
    else:
        count += 1
        
    find(screenshot, cookie, 0.5, True)           
    find(screenshot, cursor, 0.8, True)           
    find(screenshot, gran, 0.8, True)           
    find(screenshot, farm, 0.8, True)           
    find(screenshot, mine, 0.8, True)           
    find(screenshot, factory, 0.8, True)           
    find(screenshot, bank, 0.8, True)           



    
    cv.imshow("CV", screenshot)
    
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break
    
print("done.")