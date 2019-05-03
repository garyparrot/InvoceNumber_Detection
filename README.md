# 影像辨識破專題 發票辨識

* [houghcircle.py](./houghcircle.py): 透過HoughCircle找到圓的所在位置

## Hough Circle Transform 步驟

1. Cutting 如果圖片過長裁切
![Cutting](./misc/init.png =300x)
2. GaussianBlur/MedianBlur 高斯濾波和中值濾波去除非必要的雜訊
![Blur](./misc/medianblur.png =300x)
3. Dilate/Erode 侵蝕和膨脹，嘗試去除文字雜訊
![erode](./misc/erode.png =300x)
4. Canny 邊緣偵測
![canny](./misc/canny.png =300x)
5. Hough Circle Transform 找到近似圓的浮水印位置
![canny-result](./misc/canny_result.png =300x)
6. Done
![result](./misc/result.png =300x)

