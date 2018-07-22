# Python program to illustrate  
# template matching 
import cv2 
import numpy as np 
import webbrowser 
import time 

app_names = ['qq','WeChat','AliPay','TaoBao','BaiduMaps']
lim = len(app_names)
address=["https://v.qq.com/x/page/q0541el4gq7.html","https://v.qq.com/x/page/y05227kqmgk.html","http://www.pearvideo.com/video_1295135","http://www.pearvideo.com/video_1296911","http://www.pearvideo.com/video_1267505"]
time_break=[436,170,305,290,225]

src = 'img/S'+str(4)+'.png'
img_rgb = cv2.imread(src)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

#print(counter)

for j in range(0,lim):
    tmpl = 'img/' + app_names[j] + '.jpg'
    #print(tmpl)
    template = cv2.imread(tmpl, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    #print(res)
    threshold = 0.8 
    loc = np.where( res >= threshold)  
    #(array([], dtype=int64), array([], dtype=int64))
    #if(max(loc.any()) == 0):
    #if(loc == "(array([], dtype=int64), array([], dtype=int64))"):
    tmp = zip(*loc[::-1])
    #print(tmp)
    if tmp:
        print(j, tmpl)
        #print(loc.size())
        webbrowser.open(address[j])
        #time.sleep(20)
        time.sleep(time_break[j])
        #for pt in zip(*loc[::-1]): 
            #cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2) 

# Show the final image with the matched area. 
#cv2.imshow(src,img_rgb)
#cv2.resizeWindow(img_rgb, 600,600)

cv2.waitKey(0)
cv2.destroyAllWindows()
print ("OKAY, finished")
