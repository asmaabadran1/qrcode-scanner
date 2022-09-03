
import cv2
import numpy as np
from pyzbar.pyzbar import decode
 

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
 
with open('myDataFile.text') as f:
    myDataList = f.read().splitlines()
 
 
while True:
 
    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
 
        
        myOutput =  "Authorized" if myData in myDataList else "Un-Authorized"
        myColor = (162,228,184) if myOutput == "Authorized" else (0, 0, 255)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,myColor,5)
        pts2 = barcode.rect
        cv2.putText(img,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,myColor,2)
 
    cv2.imshow("QR code scanner", img)
    # press q to break the loop
    # and close camera
    if cv2.waitKey(1) == ord('q'):
        break
# release camera
cap.release()
# destroy windows
cv2.destroyAllWindows()