from PIL import Image
import os

def get_index():
	#file names list
	rgbNames = []
	for i in os.listdir('uploads/rgb/'):
		rgbNames.append(i)
	# print(rgbNames)

	nirNames = []
	for i in os.listdir('uploads/nir'):
		nirNames.append(i)
	# print(nirNames)

	for i in range(len(rgbNames)):
		rgbImg = Image.open('uploads/rgb/'+rgbNames[i])
		rgbData = rgbImg.getdata()
		r = [d[0] for d in rgbData]
		print(rgbNames[i])

		nirImg = Image.open('uploads/nir/'+nirNames[i])
		nirData = nirImg.getdata()
		nir = list(nirData)
		print(nirNames[i])

		#initializing for computations
		ndvi=[]
		output=[]
		ndviSum = []
		count = 0

		for i in range(len(r)):
			try:
				nd=(nir[i]-r[i])/(nir[i]+r[i])
				if (0.235 <= nd <= 1):
					ndviSum.append(nd)
					count +=1
				if(-1<=nd<=-0.941):
						output.append((119, 0, 0))
				elif(-0.941<nd<=-0.824):
					output.append((136,0,0))
				elif(-0.824<nd<=-0.706):
					output.append((153,0,0))
				elif(-0.706<nd<=-0.588):
					output.append((170,0,0))
				elif(-0.588<nd<=-0.471):
					output.append((187,0,0))
				elif(-0.471<nd<=-0.353):
					output.append((204,0,0))
				elif(-0.353<nd<=-0.235):
					output.append((221,0,0))
				elif(-0.235<nd<=-0.118):
					output.append((238,0,0))
				elif(-0.118<nd<=0.235):
					output.append((255,0,0)) #ground red
				elif(0.235<nd<=0.353):
					output.append((255,204,0))#light yellow
				elif(0.353<nd<=0.471):
					output.append((255,255,0)) #yellow 
				elif(0.471<nd<=0.588):
					output.append((0,255,0))
				elif(0.588<nd<=0.706):
					output.append((0,136,0))
				elif(0.706<nd<=1):
					output.append((0,66,0))
				ndvi.append((nd))
			except Exception as e:
				print(e)
				ndvi.append(1)
				output.append((0,66,0))
				count+=1
		rgbImg.putdata(output)
		rgbImg.save('ndvi' + str(i) + '.png')

		puraNdvi = sum(ndviSum)/ count
		print(round(puraNdvi, 4))

		if(0.0000 <= puraNdvi <= 0.3300):
			print("PLant is Unhealthy\n")
		elif(0.3300 <= puraNdvi <= 0.6600):
			print("Plant is Moderately Healthy\n")
		elif(0.6600 <= puraNdvi <= 1.0000):
			print("Plant is very Healthy\n")

	# # print(output)
		# rgbImg.putdata(output)
		# rgbImg.save('ndvi' + str(i) + '.png')
	return "hello"

