import cv2, os
import numpy as np

def half(img):
    """ Cut half """
    # height width channel
    h,w = img.shape
    return img[0:h//2,0:w]

def showimg(img):
    """ Display specified image """
    cv2.namedWindow('sub',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('sub', 600, 600)
    cv2.imshow("sub",img)
    cv2.waitKey()
    cv2.destroyAllWindows()

def operate(filename, show_prcoess = False):
    img = cv2.imread(filename, 0)
    h,w = img.shape
    if h/w > 18/5:
        img = half(img)
    showimg(img) if show_prcoess else 0
    cv2.imwrite('./result/init.png', img)
    
    img = cv2.GaussianBlur(img,(5,5), 100, 100)
    img = cv2.medianBlur(img,23)
    img = cv2.GaussianBlur(img,(3,3), 100, 100)
    showimg(img)
    showimg(img) if show_prcoess else 0
    cv2.imwrite('./result/medianblur.png', img)

    img = cv2.Canny(img,1, 20, 3)
    showimg(img) if show_prcoess else 0
    cv2.imwrite('./result/canny.png', img)

    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

    h,w = img.shape
    print(w,h)

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, int(h*0.3), param1=1, param2=10, minRadius=int(w*0.5*2.8/4), maxRadius=int(w*0.5*3.2/4))
    if circles is None: 
        showimg(cimg)
        return 0 
    circles = np.uint16(np.around(circles)) 

    for i in circles[0,:1]:
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

    cv2.imshow('result', cimg)
    cv2.imwrite('./result/result.png',cimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return 1

def runTest():
    count = 0
    testfiles = os.listdir('./testcase')
    for filename in testfiles:
        filename = "./testcase/" + filename
        print("Filename %s" % filename)
        count += operate(filename,False)

    print(count,"/",len(testfiles))

def testFile(filename):
    operate(filename,True)

runTest()
# testFile("./testcase/fuckit.jpg")
