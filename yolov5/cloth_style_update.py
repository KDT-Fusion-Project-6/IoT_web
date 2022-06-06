import numpy as np
import cv2,sys
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import math

def rgb2hsv(r,g,b):
    max_c = max(r,g, b)
    min_c = min(r,g, b)
    delta = max_c - min_c

    v =  (max_c/255) * 100
    if v == 0.0:
        s = 0.0
        h = 0.0
    else:
        if max_c == 0: 
            s =0.0
        else:
            s = (delta/max_c) * 100
        if s == 0.0:
            h = 0.0
        else:
            if max_c == r:
                h = 60.0 * ((g-b)/delta)
#                 h = 60.0 * ((g-b) % 6)
            elif max_c == g:
                h = 60.0 * (2.0+(b-r)/delta)
            elif max_c == b:
    #             h = 60.0 * (4.0+(b-r)/delta)
                h = 60.0 * (4.0+(r-g)/delta)
            if h < 0:
                h += 360.0

    return h,s,v

def centroid_histogram(clt): # 색상 비율계산
    # grab the number of different clusters and create a histogram
    # based on the number of pixels assigned to each cluster
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)
    

    # normalize the histogram, such that it sums to one
    hist = hist.astype("float")
    hist /= hist.sum()

    # return the histogram
    return hist

def extract_color(key, value):
    xyxy = value[1]
    xmin = int(xyxy[0])
    ymin = int(xyxy[1])
    xmax = int(xyxy[2])
    ymax = int(xyxy[3])

    image = cv2.imread(key)
    img_trim = image[ymin:ymax, xmin:xmax]
#     copy_img = image.copy()
#     img_trim = copy_img[ymin:ymax, xmin:xmax]
#     cv2.imwrite(key, img_trim)
#     sample_image = cv2.imread(key)
    sample_image = cv2.cvtColor(img_trim, cv2.COLOR_BGR2RGB)
    sample_image = sample_image.reshape((sample_image.shape[0] * sample_image.shape[1], 3)) # height, width 통합
    
    
    k = 5 # 예제는 5개로 나누겠습니다
    clt = KMeans(n_clusters = k)
    clt.fit(sample_image)
    
    
    three_color=[]
    color=[]
    for center in clt.cluster_centers_:
        color=list(center)
        three_color.append(color)
    
    
    hist = centroid_histogram(clt)  #각 클러스터(?)의 빈도수 찾기
    hist = list(hist)
    
    
    maxindex = np.argmax(hist) # 값이 큰 것의 인덱스 가져오기
    color=three_color[maxindex]

    r=color[0]
    g=color[1]
    b=color[2]
    
    
    h,s,v = rgb2hsv(r,g,b)

    
    if v>=0 and v<=18:
        c_txt='검정'    
    else:
        if s>=0 and s<=2:
            if v>=95 and v<=100:
                c_txt='하양'
            else:
                c_txt='회색'
        else: 
            if v > 18 and v <= 59:
                if h>=336 and h<=360:
                    c_txt='와인'
                elif h>288:
                    c_txt='자주'
                elif h>250:
                    c_txt='찐보라'
                elif h>192:
                    c_txt='남색'
                elif h>172:
                    c_txt='코발트블루'
                elif h>150:
                    c_txt='올리브'
                elif h>65:
                    c_txt='초록'
                elif h>52:
                    c_txt='찐노랑'
                elif h>6:
                    c_txt='브라운'
                elif h>=0:
                    c_txt='와인'
            elif v > 59 and v <= 100:
                if h>=336 and h<=360:
                    c_txt='빨강'
                elif h>288:
                    c_txt='분홍'
                elif h>250:
                    c_txt='보라'
                elif h>192:
                    c_txt='파랑'
                elif h>172:
                    c_txt='스카이블루'
                elif h>150:
                    c_txt='민트'
                elif h>65:
                    c_txt='연두'
                elif h>46:
                    c_txt='노랑'
                elif h>6:
                    c_txt='주황'
                elif h>=0:
                    c_txt='빨강'

    return c_txt, img_trim