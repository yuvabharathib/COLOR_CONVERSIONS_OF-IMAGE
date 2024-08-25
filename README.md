# COLOR_CONVERSIONS_OF-IMAGE
## AIM:
To write a python program using OpenCV to do the following image manipulations.

i) Read, display, and write an image.

ii) Access the rows and columns in an image.

iii) Cut and paste a small portion of the image.

iv)To perform the color conversion between RGB, BGR, HSV, and YCbCr color models.


## Software Required:
Anaconda - Python 3.7
## Algorithm:
### Step1:
Choose an image and save it as a filename.jpg ,
### Step2:
Use imread(filename, flags) to read the file.
### Step3:
Use imshow(window_name, image) to display the image.
### Step4:
Use imwrite(filename, image) to write the image.
### Step5:
End the program and close the output image windows.
### Step6:
Convert BGR and RGB to HSV and GRAY
### Step7:
Convert HSV to RGB and BGR
### Step8:
Convert RGB and BGR to YCrCb
### Step9:
Split and Merge RGB Image
### Step10:
Split and merge HSV Image

##### Program:
### Developed By:Yuvabharathi.B
### Register Number: 212222230181


## Output:

### i) Read and display the image
```
    import cv2
    image=cv2.imread('flower.jpg',1)
    image=cv2.resize(image,(400,300))
    cv2.imshow('flower',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
## Output:
![s1](https://github.com/Nachiyarr/COLOR_CONVERSIONS_OF-IMAGE/assets/113497340/d8b8a852-ff3f-46f2-a39f-02935165a4a8)

### ii)Write the image
```
    image=cv2.imread('flower.jpg',0)
    cv2.imwrite('a.jpeg',image)
```
## Output:
![s3](https://github.com/Nachiyarr/COLOR_CONVERSIONS_OF-IMAGE/assets/113497340/41f39a38-d611-4339-9ce6-14ab78390f57)
### iii)Shape of the Image
```
    import cv2
    image=cv2.imread('flower.jpg',1)
    print(image.shape)
```
### Output:
![s4](https://github.com/Nachiyarr/COLOR_CONVERSIONS_OF-IMAGE/assets/113497340/5fac5557-10ce-4c8c-a149-cb5b675e1083)
### iv)Access rows and columns
```
    import random
    import cv2
    image=cv2.imread('flower.jpg',1)
    image=cv2.resize(image,(400,400))
    for i in range (150,200):
      for j in range(image.shape[1]):
          image[i][j]=[random.randint(0,255),
                       random.randint(0,255),
                       random.randint(0,255)] 
    cv2.imshow('car part image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
### Output:
![Screenshot 2024-02-20 210450](https://github.com/Nachiyarr/COLOR_CONVERSIONS_OF-IMAGE/assets/113497340/17fc1a88-003c-48ae-b286-3180b03a25ca)

### v)Cut and paste portion of image
```
  import cv2
  image=cv2.imread('flower.jpg',1)
  image=cv2.resize(image,(400,400))
  tag =image[130:200,110:190]
  image[110:180,120:200] = tag
  cv2.imshow('cut and paste',image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
```
### Output:
![s6](https://github.com/Nachiyarr/COLOR_CONVERSIONS_OF-IMAGE/assets/113497340/ecec0ea8-f09c-4a6c-9136-5a9eced67274)
### vi) BGR and RGB to HSV and GRAY
```
import cv2
img = cv2.imread('flower.jpg',1)
img = cv2.resize(img,(300,200))
cv2.imshow('Original Image',img)
hsv1 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('BGR2HSV',hsv1)
hsv2 = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
cv2.imshow('RGB2HSV',hsv2)
gray1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('BGR2GRAY',gray1)
gray2 = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow('RGB2GRAY',gray2)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
### Output:
![s7](https://github.com/Nachiyarr/COLOR_CONVERSIONS_OF-IMAGE/assets/113497340/141f67ab-346d-4ae2-890a-480e3278e654)

### vii) HSV to RGB and BGR
```
import cv2
img = cv2.imread('flower.jpg')
img = cv2.resize(img,(300,200))
img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('Original HSV Image',img)
RGB = cv2.cvtColor(img,cv2.COLOR_HSV2RGB)
cv2.imshow('2HSV2BGR',RGB)
BGR = cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
cv2.imshow('HSV2RGB',BGR)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
### Output:
![s8](https://github.com/Nachiyarr/COLOR_CONVERSIONS_OF-IMAGE/assets/113497340/b72211bd-90c0-43d9-ba76-5666271d383f)

### viii) RGB and BGR to YCrCb
```
import cv2
img = cv2.imread('flower.jpg')
img = cv2.resize(img,(300,200))
cv2.imshow('Original RGB Image',img)
YCrCb1 = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
cv2.imshow('RGB-2-YCrCb',YCrCb1)
YCrCb2 = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)
cv2.imshow('BGR-2-YCrCb',YCrCb2)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
### Output:
![ss88](https://github.com/Nachiyarr/COLOR_CONVERSIONS_OF-IMAGE/assets/113497340/a4742749-d2de-4ed0-a498-170908c52439)

### ix) Split and merge RGB Image
```
import cv2
img = cv2.imread('flower.jpg',1)
img = cv2.resize(img,(300,200))
R = img[:,:,2]
G = img[:,:,1]
B = img[:,:,0]
cv2.imshow('R-Channel',R)
cv2.imshow('G-Channel',G)
cv2.imshow('B-Channel',B)
merged = cv2.merge((B,G,R))
cv2.imshow('Merged RGB image',merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
### Output:
![s9](https://github.com/Nachiyarr/COLOR_CONVERSIONS_OF-IMAGE/assets/113497340/cbde3c5c-c6c5-4e17-9af5-b19770496a7c)
### x) Split and merge HSV Image
```
import cv2
img = cv2.imread(flower.jpg",1)
img = cv2.resize(img,(300,200))
img=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
H,S,V=cv2.split(img)
cv2.imshow('Hue',H)
cv2.imshow('Saturation',S)
cv2.imshow('Value',V)
merged = cv2.merge((H,S,V))
cv2.imshow('Merged',merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
### Output:
![s10](https://github.com/Nachiyarr/COLOR_CONVERSIONS_OF-IMAGE/assets/113497340/f0d3f963-c8f0-42ce-8078-236644ba71f7)

## Result:
Thus the images are read, displayed, and written ,and color conversion was performed between RGB, HSV and YCbCr color models successfully using the python program.






