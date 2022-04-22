from PIL import Image

img = Image.open('rgb_0054.png')
data = img.getdata()

img1 = Image.open('nir_0054.png')
data2 = img1.getdata()

r = [d[0] for d in data]
g = [d[1] for d in data]
b = [d[2] for d in data]

ndvi=[]
nir=list(data2)
count=0
value_l0=0
value_0_4=0
value_1=0
value_g1=0
ndvi_255=[]
ndviSum = []

count = 0

for i in range(len(r)):
	try:
		nd=(nir[i]-r[i])/(nir[i]+r[i])
		if (0.235 <= nd <= 1):
			ndviSum.append(nd)
			count +=1
		if(-1<=nd<=-0.941):
				ndvi_255.append((119, 0, 0))
		elif(-0.941<nd<=-0.824):
			ndvi_255.append((136,0,0))
		elif(-0.824<nd<=-0.706):
			ndvi_255.append((153,0,0))
		elif(-0.706<nd<=-0.588):
			ndvi_255.append((170,0,0))
		elif(-0.588<nd<=-0.471):
			ndvi_255.append((187,0,0))
		elif(-0.471<nd<=-0.353):
			ndvi_255.append((204,0,0))
		elif(-0.353<nd<=-0.235):
			ndvi_255.append((221,0,0))
		elif(-0.235<nd<=-0.118):
			ndvi_255.append((238,0,0))
		elif(-0.118<nd<=0.235):
			ndvi_255.append((255,0,0)) #ground red
		elif(0.235<nd<=0.353):
			ndvi_255.append((255,204,0))#light yellow
		elif(0.353<nd<=0.471):
			ndvi_255.append((255,255,0)) #yellow 
		elif(0.471<nd<=0.588):
			ndvi_255.append((0,255,0))
		elif(0.588<nd<=0.706):
			ndvi_255.append((0,136,0))
		elif(0.706<nd<=1):
			ndvi_255.append((0,66,0))
		ndvi.append((nd))
	except Exception as e:
		print(e)
		ndvi.append(1)
		ndvi_255.append((0,66,0))
		count+=1

puraNdvi = sum(ndviSum)/ count
print(round(puraNdvi, 4))

if(0.0000 <= puraNdvi <= 0.3300):
	print("PLant is Unhealthy")
elif(0.3300 <= puraNdvi <= 0.6600):
	print("Plant is Moderately Healthy")
elif(0.6600 <= puraNdvi <= 1.0000):
	print("Plant is very Healthy")

# print(ndvi_255)
img.putdata(ndvi_255)
img.save('ndvi_0054.png')



# Logic

# ndvi_all_pixel = []
# count_per_pixel +=1

# for every pixel in image:
# 	nd=(nir[i]-r[i])/(nir[i]+r[i])
# 			if (0.235 <= nd <= 1): #ignores red color in this case the soil
# 				ndvi_all_pixel.append(nd)
# 				count_per_pixel +=1

# puraNdvi = sum(ndvi_all_pixel)/ count_per_pixel
# print(round(puraNdvi, 4)) #upto 4 decimal