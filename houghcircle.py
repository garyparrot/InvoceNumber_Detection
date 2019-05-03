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
    """圓偵測"""

    # 讀取圖片
    img = cv2.imread(filename, 0)
    origin_img = img.copy()
    h,w = img.shape

    # 圖片比例達到發票長寬比時裁切一半
    if h/w > 18/6:
        print("Cut half")
        img = half(img)
    if show_prcoess: showimg(img)
    cv2.imwrite('./result/init.png', img)
    
    # 預處理,套用高斯濾波和中值濾波，嘗試保留浮水印體積
    img = cv2.GaussianBlur(img,(5,5), 100, 100)
    img = cv2.medianBlur(img,39)
    img = cv2.GaussianBlur(img,(3,3), 100, 100)
    if show_prcoess: showimg(img)
    cv2.imwrite('./result/medianblur.png', img)

    # 侵蝕，去除討人厭的細部文字
    # kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3, 3))
    kernel = np.array([[1,1,1],[1,1,1],[1,1,1]])
    img = cv2.dilate(img,kernel,iterations=10)
    img = cv2.erode(img,kernel,iterations=25)
    if show_prcoess: showimg(img)
    cv2.imwrite('./result/erode.png', img)

    # Canny 邊緣偵測
    img = cv2.Canny(img,1, 20, 3)
    if show_prcoess: showimg(img)
    cv2.imwrite('./result/canny.png', img)

    # 圓偵測
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, int(h*0.3), param1=1, param2=10, minRadius=int(w*0.5*2.8/4), maxRadius=int(w*0.5*3.2/4))
    if circles is None: 
        showimg(img)
        print("No Circle found.")
        return 0 
    circles = np.uint16(np.around(circles)) 

    # 畫出浮水印位置
    #cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    cimg = origin_img
    for i in circles[0,:1]:
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

    showimg(cimg)
    cv2.imwrite('./result/result.png',cimg)
    return 1

def runTest(show=False,test_size=10000):
    """嘗試套用每個testcase內的圖片"""
    count = 0
    testfiles = os.listdir('./testcase')[:test_size]
    for filename in testfiles:
        filename = "./testcase/" + filename
        print("Filename %s" % filename)
        count += operate(filename,show)

    print(count,"/",len(testfiles))

def testFile(filename):
    """測試單張圖片"""
    operate(filename,True)

if __name__ == "__main__":
    # testFile('./testcase/fuckit.jpg')
    runTest()
