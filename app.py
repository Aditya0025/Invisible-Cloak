cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('harry.avi' , fourcc, 20.0, (640,480))
time.sleep(2)
background = 0#capturing background
for i in range(30):
    ret, background = cap.read()#capturing image
while(cap.isOpened()):
    ret, img = cap.read()
    
    if not ret:
        break
        
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  
    
    #Create masks with coordinates to detect the color(HSV Vlaue)
    #geeting the color part 1 as OPen CV work on only 8 bit= 255  
#     lower_red = np.array([0,120,70])
#     upper_red = np.array([10,255,255]) 
    lower_red = np.array([110,120,70])
    upper_red = np.array([130,255,255]) 

#     Checking for the CLone part of frame(HSV)
    mask1 = cv2.inRange(hsv , lower_red , upper_red) #seprating the cloth part
    
    
    #geeting the color part 2 as OPen CV work on only 8 bit= 255
#     lower_red = np.array([170,120,70])
#     upper_red = np.array([180,255,255]) 
    lower_red = np.array([250,120,70])
    upper_red = np.array([300,255,255])

    #     Checking for the CLone part of frame(HSV)
    mask2 = cv2.inRange(hsv , lower_red , upper_red)
   
    mask1 = mask1 + mask2 #OR
    mask1=cv2.morphologyEx(mask1, cv2.MORPH_OPEN ,np.ones((3,3) , np.uint8) , iterations=2)
        
    mask2=cv2.morphologyEx(mask1, cv2.MORPH_DILATE ,np.ones((3,3) , np.uint8) , iterations=1)
        
    #Hiding part part away
    mask2 = cv2.bitwise_not(mask1)    
    
    #Copy the masked area's original part
    res1 = cv2.bitwise_and(background, background, mask=mask1)
    res2 = cv2.bitwise_and(img, img, mask=mask2)
    
    final_output = cv2.addWeighted(res1 , 1, res2 , 1, 0)
    
    cv2.imshow('CHECK' , final_output)
    k=cv2.waitKey(10)
    if k==27:
        break
        
cap.release()
cv2.destroyAllWindows()
