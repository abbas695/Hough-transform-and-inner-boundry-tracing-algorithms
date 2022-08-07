import cv2
import numpy as np 

def inner_boundary_tracing():
    image = np.zeros((700, 700, 3), np.uint8)   
    
    start_point = (0, 0)
    

    end_point = (100, 100)
    
    color = (255, 255, 255)
    
    thickness = -1
    

    image = cv2.rectangle(image, start_point, end_point, color, thickness)
    center_coordinates = (200, 200)
    
    # Radius of circle
    radius = 50
    
    # Blue color in BGR
    color = (100, 100, 100)
    
    # Line thickness of 2 px
    thickness = -1
    
    # Using cv2.circle() method
    # Draw a circle with blue line borders of thickness of 2 px
    image = cv2.circle(image, center_coordinates, radius, color, thickness)
    center_coordinates = (400, 400)
    
    axesLength = (100, 50)
    
    angle = 30
    
    startAngle = 0
    
    endAngle = 360
    
    # Blue color in BGR
    color = (175, 175, 175)
    
    # Line thickness of -1 px
    thickness = -1
    
    # Using cv2.ellipse() method
    # Draw a ellipse with blue line borders of thickness of -1 px
    image = cv2.ellipse(image, center_coordinates, axesLength, angle,
                            startAngle, endAngle, color, thickness)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    value=np.unique(img)
    print(value)
    dir=3
    allborders=[]
    for value in value:
        borderlist=[]
        for i in range(img.shape[0]):
            if(len(borderlist)>0):
                break
            for j in range(img.shape[1]):
                if(img[i][j]==value):
                    borderlist.append((i,j))
                    break

        condition1=True
        icurrentpixel=borderlist[0][0]
        jcurrentpixel=borderlist[0][1]
        while(condition1):
            dir=(dir+3)%4
            condition =True
            if(dir==0):
                icurrentpixel=borderlist[len(borderlist)-1][0]+1
                jcurrentpixel=borderlist[len(borderlist)-1][1]
                
                if((0<=icurrentpixel and icurrentpixel<img.shape[0]) and (0<=jcurrentpixel and jcurrentpixel<img.shape[1])):
                    if(img[icurrentpixel][jcurrentpixel]==value):
                        borderlist.append((icurrentpixel,jcurrentpixel))
                        condition=False
                        dir=0
                if(condition):
                    icurrentpixel=borderlist[len(borderlist)-1][0]
                    jcurrentpixel=borderlist[len(borderlist)-1][1]-1
                    if((0<=icurrentpixel and icurrentpixel<img.shape[0]) and (0<=jcurrentpixel and jcurrentpixel<img.shape[1])):
                            if(img[icurrentpixel][jcurrentpixel]==value):
                                borderlist.append((icurrentpixel,jcurrentpixel))
                                condition=False
                                dir=1
                if(condition):
                    icurrentpixel=borderlist[len(borderlist)-1][0]-1
                    jcurrentpixel=borderlist[len(borderlist)-1][1]
                    if((0<=icurrentpixel and icurrentpixel<img.shape[0]) and (0<=jcurrentpixel and jcurrentpixel<img.shape[1])):
                            if(img[icurrentpixel][jcurrentpixel]==value):
                                borderlist.append((icurrentpixel,jcurrentpixel))
                                condition=False 
                                dir=2
                if(condition):
                    icurrentpixel=borderlist[len(borderlist)-1][0]
                    jcurrentpixel=borderlist[len(borderlist)-1][1]+1
                    if((0<=icurrentpixel and icurrentpixel<img.shape[0]) and (0<=jcurrentpixel and jcurrentpixel<img.shape[1])):
                            if(img[icurrentpixel][jcurrentpixel]==value):
                                borderlist.append((icurrentpixel,jcurrentpixel))
                                condition=False
                                dir=3                     
            elif(dir==1):
                icurrentpixel=borderlist[len(borderlist)-1][0]
                jcurrentpixel=borderlist[len(borderlist)-1][1]-1
                if((0<=icurrentpixel and icurrentpixel<img.shape[0]) and (0<=jcurrentpixel and jcurrentpixel<img.shape[1])):
                    if(img[icurrentpixel][jcurrentpixel]==value):
                        borderlist.append((icurrentpixel,jcurrentpixel))
                        condition=False
                        dir=1
                if(condition):
                    icurrentpixel=borderlist[len(borderlist)-1][0]-1
                    jcurrentpixel=borderlist[len(borderlist)-1][1]
                    if((0<=icurrentpixel and icurrentpixel<img.shape[0]) and (0<=jcurrentpixel and jcurrentpixel<img.shape[1])):
                            if(img[icurrentpixel][jcurrentpixel]==value):
                                borderlist.append((icurrentpixel,jcurrentpixel))
                                condition=False
                                dir=2
                if(condition):
                    icurrentpixel=borderlist[len(borderlist)-1][0]
                    jcurrentpixel=borderlist[len(borderlist)-1][1]+1
                    if((0<=icurrentpixel and icurrentpixel<img.shape[0]) and (0<=jcurrentpixel and jcurrentpixel<img.shape[1])):
                            if(img[icurrentpixel][jcurrentpixel]==value):
                                borderlist.append((icurrentpixel,jcurrentpixel))
                                condition=False 
                                dir=3
                if(condition):
                    icurrentpixel=borderlist[len(borderlist)-1][0]+1
                    jcurrentpixel=borderlist[len(borderlist)-1][1]
                    if((0<=icurrentpixel and icurrentpixel<img.shape[0]) and (0<=jcurrentpixel and jcurrentpixel<img.shape[1])):
                            if(img[icurrentpixel][jcurrentpixel]==value):
                                borderlist.append((icurrentpixel,jcurrentpixel))
                                condition=False
                                dir=0    
            elif(dir==2):
                icurrentpixel=borderlist[len(borderlist)-1][0]-1
                jcurrentpixel=borderlist[len(borderlist)-1][1]
                if((0<=icurrentpixel and icurrentpixel<img.shape[0]) and (0<=jcurrentpixel and jcurrentpixel<img.shape[1])):
                    if(img[icurrentpixel][jcurrentpixel]==value):
                        borderlist.append((icurrentpixel,jcurrentpixel))
                        condition=False
                        dir=2
                if(condition):
                    icurrentpixel=borderlist[len(borderlist)-1][0]
                    jcurrentpixel=borderlist[len(borderlist)-1][1]+1
                    if((0<=icurrentpixel and icurrentpixel<img.shape[0]) and (0<=jcurrentpixel and jcurrentpixel<img.shape[1])):
                            if(img[icurrentpixel][jcurrentpixel]==value):
                                borderlist.append((icurrentpixel,jcurrentpixel))
                                condition=False
                                dir=3
                if(condition):
                    icurrentpixel=borderlist[len(borderlist)-1][0]+1
                    jcurrentpixel=borderlist[len(borderlist)-1][1]
                    if((0<=icurrentpixel and icurrentpixel<img.shape[0]) and (0<=jcurrentpixel and jcurrentpixel<img.shape[1])):
                            if(img[icurrentpixel][jcurrentpixel]==value):
                                borderlist.append((icurrentpixel,jcurrentpixel))
                                condition=False 
                                dir=0
                if(condition):
                    icurrentpixel=borderlist[len(borderlist)-1][0]
                    jcurrentpixel=borderlist[len(borderlist)-1][1]-1
                    if((0<=icurrentpixel and icurrentpixel<img.shape[0]) and (0<=jcurrentpixel and jcurrentpixel<img.shape[1])):
                            if(img[icurrentpixel][jcurrentpixel]==value):
                                borderlist.append((icurrentpixel,jcurrentpixel))
                                condition=False
                                dir=1
            elif(dir==3):
                icurrentpixel=borderlist[len(borderlist)-1][0]
                jcurrentpixel=borderlist[len(borderlist)-1][1]+1
                if((0<=icurrentpixel and icurrentpixel<img.shape[0]) and (0<=jcurrentpixel and jcurrentpixel<img.shape[1])):
                    if(img[icurrentpixel][jcurrentpixel]==value):
                        borderlist.append((icurrentpixel,jcurrentpixel))
                        condition=False
                        dir=3
                if(condition):
                    icurrentpixel=borderlist[len(borderlist)-1][0]+1
                    jcurrentpixel=borderlist[len(borderlist)-1][1]
                    if((0<=icurrentpixel and icurrentpixel<img.shape[0]) and (0<=jcurrentpixel and jcurrentpixel<img.shape[1])):
                            if(img[icurrentpixel][jcurrentpixel]==value):
                                borderlist.append((icurrentpixel,jcurrentpixel))
                                condition=False
                                dir=0
                if(condition):
                    icurrentpixel=borderlist[len(borderlist)-1][0]
                    jcurrentpixel=borderlist[len(borderlist)-1][1]-1
                    if((0<=icurrentpixel and icurrentpixel<img.shape[0]) and (0<=jcurrentpixel and jcurrentpixel<img.shape[1])):
                            if(img[icurrentpixel][jcurrentpixel]==value):
                                borderlist.append((icurrentpixel,jcurrentpixel))
                                condition=False 
                                dir=1
                if(condition):
                    icurrentpixel=borderlist[len(borderlist)-1][0]-1
                    jcurrentpixel=borderlist[len(borderlist)-1][1]
                    if((0<=icurrentpixel and icurrentpixel<img.shape[0]) and (0<=jcurrentpixel and jcurrentpixel<img.shape[1])):
                            if(img[icurrentpixel][jcurrentpixel]==value):
                                borderlist.append((icurrentpixel,jcurrentpixel))
                                condition=False
                                dir=2
            if(len(borderlist)>2):
                if(borderlist[len(borderlist)-1]==borderlist[1] and borderlist[len(borderlist)-2]==borderlist[0]):
                    condition1=False
        allborders.extend(borderlist)
    image2=np.zeros((700, 700, 3), np.uint8)
    for i in range(len(allborders)):
        image2[allborders[i][0]][allborders[i][1]]=255
    cv2.imwrite('border.png',image2)
    cv2.imwrite('original.png',img)
    border=cv2.imread('border.png')
    original=cv2.imread('original.png')
    Hori = np.concatenate((border, original), axis=1)
    
    # concatenate image Vertically
    Verti = np.concatenate((border, original), axis=0)
    
    cv2.imshow('HORIZONTAL', Hori)
    
    cv2.waitKey(0)
inner_boundary_tracing()
