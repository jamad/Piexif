from PIL import Image
import piexif

filename=r"C:\\Users\\jamad\\Desktop\\IMG-4199.JPG"  

D = piexif.load(filename)
for k in D:
    if k=='thumbnail':continue
    if k=='Exif':E=D[k]
    print(k,D[k])

for k in E:print(k)
#print(D)
#if piexif.ImageIFD.Orientation in D["0th"]:print("Orientation is ", D["0th"][piexif.ImageIFD.Orientation])
#if piexif.ExifIFD.Gamma in D["Exif"]:print("Gamma is ", D["Exif"][piexif.ExifIFD.Gamma])
