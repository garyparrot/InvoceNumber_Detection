# 影像辨識破專題 發票辨識

* [houghcircle.py](./houghcircle.py): 透過HoughCircle找到圓的所在位置

## Hough Circle Transform 步驟

1. Cutting 如果圖片過長裁切
![Cutting](https://github.com/garyparrot/InvoceNumber_Detection/raw/master/misc/init.png | width=300)
2. GaussianBlur/MedianBlur 高斯濾波和中值濾波去除非必要的雜訊
![Blur](https://github.com/garyparrot/InvoceNumber_Detection/raw/master/misc/medianblur.png | width=300)
3. Dilate/Erode 侵蝕和膨脹，嘗試去除文字雜訊
![erode](https://github.com/garyparrot/InvoceNumber_Detection/raw/master/misc/erode.png | width=300)
4. Canny 邊緣偵測
![canny](https://github.com/garyparrot/InvoceNumber_Detection/raw/master/misc/canny.png | width=300)
5. Hough Circle Transform 找到近似圓的浮水印位置
![canny-result](https://github.com/garyparrot/InvoceNumber_Detection/raw/master/misc/canny_result.png | width=300)
6. Done
![result](https://github.com/garyparrot/InvoceNumber_Detection/raw/master/misc/result.png | width=300)

