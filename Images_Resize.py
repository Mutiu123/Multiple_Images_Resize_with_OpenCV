import cv2
import glob
import os

path = "Resources"
os.mkdir("Resized Images")

i = 0

for images in glob.glob(path + "/*.jpg"):
    image = cv2.imread(images)
    imageResized = cv2.resize(image, (600, 600))
    cv2.imwrite("Resized Images/image%i.jpg" %i, imageResized)
    
    
    i +=1
    cv2.imshow("image", imageResized)
    cv2.waitKey(500)
    
    
cv2.destroyAllWindows()