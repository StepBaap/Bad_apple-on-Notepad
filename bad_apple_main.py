from PIL import Image
import os

output = open("output.txt",'w')

def Resize(image,w):
	
	width,height = image.size
	aspect_ratio = height/width
	new_height = int(w*aspect_ratio)
	image = image.resize((w,new_height))
	dest_src = "renderframe.png"
	image.save(dest_src)
	return dest_src

def gryscale(image):
        #converts given image to grayscale
	for i in range(image.width):
		for j in range(image.height):
			px = image.getpixel((i,j))      
			avg = int((px[0] + px[1] + px[2])/3) 
			image.putpixel((i,j), (avg,avg,avg,255))


def gaytoascii(image,file_stream):
        #converts the grayscale image to ascii text and writes it on an output text file
	gryscale(image)
	for i in range(image.height):
		for j in range(image.width):
			px = image.getpixel((j,i)) 
			if px==(255,255,255):
				#write '*' onto the output.txt file
				file_stream.write('*')
			
			else:
				#write '@' onto the output.txt file
				file_stream.write('@')
		file_stream.write('\n')


def render_bad_apple(image_list,src):
        #writes all the frames into the output text file in ascii seperated by a '[.]' 	 
	for img_num in image_list:
		img_name = str(img_num) + ".png"  # considering every to be of type {frame%d}
		frame = Image.open(os.path.join(src,img_name))
		dest_src = Resize(frame,75)
		Frame = Image.open(dest_src)
		gaytoascii(Frame,output)
		output.write('[.]'+'\n')
		print("writing frame " +str(img_num))
		
# folder containing frames
src = "frames"
image_list = []
for i in range(len(os.listdir(src))):
	image_list.append(i+1)
render_bad_apple(image_list,src)
output.close()


