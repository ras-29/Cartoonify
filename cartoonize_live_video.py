import cv2

def functioncall(x):
    print(x)

cap = cv2.VideoCapture(0)

cv2.namedWindow('cartoon')
cv2.createTrackbar('C-edge','cartoon',-20,20,functioncall)
cv2.createTrackbar('filter','cartoon',100,500,functioncall)
cv2.createTrackbar('Block size','cartoon',3,40,functioncall)

#blurred = cv2.medianBlur(img_gray,5) #reducing noise, before applying threshold

while 1:
    ret,frame = cap.read()
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)

    Cedge = cv2.getTrackbarPos('C-edge','cartoon')
    filter = cv2.getTrackbarPos('filter','cartoon') #value for sigmaColor and sigmaSpace
    block_size = cv2.getTrackbarPos('Block size','cartoon')
    #since adaptive thresold function accepts only odd block size
    value_BSize = max(3,block_size)
    if (value_BSize % 2 == 0):
        value_BSize  += 1

    blurred = cv2.medianBlur(frame_gray,5)
    edge = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,value_BSize,Cedge)
    img_color = cv2.bilateralFilter(frame,9,filter,filter)
    cartoon = cv2.bitwise_and(img_color,img_color,mask=edge)
    
    cv2.imshow('cartoon',cartoon)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()







