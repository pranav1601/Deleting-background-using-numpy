from PIL import Image,ImageFilter
import numpy as np
img=Image.open("name.jpg")

#name is the name of the image you want to crop

array=np.array(img)

#function which crops the columns

def crop(ar):
    c = ar.shape[1]
    ro = ar.shape[0]
    i = 0
    while(i<c):
        k=0
        j=0
        while(j<ro):
            r = ar[j][i][0]
            g = ar[j][i][1]
            b = ar[j][i][2]
            j=j+1
            if(r!=255 or g!=255 or b!=255):
            
            #255 is used because im considering my background as white
            #RGB representation of white is (255,255,255)
            
            k=1
                break
        if(k==0):
            ar=np.delete(ar,i,axis=1)
            c=c-1
        else:
            i=i+1
    return ar
temp=crop(array)
arr2=np.rot90(temp)

#now the intitial background rows are columns
#and columns are rows

temp2=crop(arr2)

#the initial background rows are cropped

finalarr=np.rot90(temp2,3)
finalim=Image.fromarray(finalarr)
finalim.show()