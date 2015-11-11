#!/usr/bin/python
from PIL import Image
from Image import *
import binascii
from Tkinter import *
import xlsxwriter
from sricrypt import *
from tkFileDialog import askopenfilename
def rgb2hex(r,g,b):
	return '#{:02x}{:02x}{:02x}'.format(r,g,b)

def hex2rgb(hexcode):
	return tuple(map(ord,hexcode[1:].decode('hex')))

def str2bin(message):
	binary = bin(int(binascii.hexlify(message), 16))
	return binary[2:]

def bin2str(binary):
	message = binascii.unhexlify('%x' % (int('0b' +binary,2)))
	return message

def encode(hexcode, digit):
	if hexcode[-1] in ['0','1','2']:
		hexcode = hexcode[:-1]+digit
		return hexcode
	else:
		return None

def decode(hexcode):
	if hexcode[-1] in ('0','1'):
		return hexcode[-1]
	else:
		return None

def hide(filename, message):
	img = open(filename)
	binary = str2bin(message) +'1111111111111110'
	if img.mode in ('RGBA'):
		img = img.convert('RGBA')
		datas = img.getdata()
		
		newData = []
		digit = 0
		temp = ''
		for item in datas:
			if (digit < len(binary)):
				newpix = encode(rgb2hex(item[0],item[1],item[2]),binary[digit])
				if newpix == None:
					newData.append(item)
				else:
					r,g,b = hex2rgb(newpix)
					newData.append((r,g,b,255))
					digit+=1
			else:
				newData.append(item)
		img.putdata(newData)
		name=filename[:-4]+"_out.png"
		img.save(name,"PNG")
		return "Completed"
	return "Incorrect image mode"
def retr(filename):
	img = open(filename)
	binary = ''
	if img.mode in ('RGBA'):
		img = img.convert('RGBA')
		datas = img.getdata()
		for item in datas:
			digit = decode(rgb2hex(item[0],item[1],item[2])) 
			if digit ==None:
				pass
			else:
				binary=binary+digit
				if binary[-16:] == '1111111111111110':
					print "Success"
					return bin2str(binary[:-16])
		return bin2str(binary)
	return "Incorrect image mode"

#print("please enter the following Details\n1.Image file name\n2.message")
def Gui():
	filename=""	
	def btn2():
		filename = askopenfilename(parent=root,filetypes=[('All image files', '.jpg .png'),('All Files', '.*')],title='Select your image file')
	def btn():
		filename = askopenfilename(parent=root,filetypes=[('All image files', '.jpg .png'),('All Files', '.*')],title='Select your image file')
		j= test2.get("1.0","end-1c")
		print j
		k=custom_enc(str(j))
		hide(str(filename),str(k))
		a.config(text = "Stego Success")
	def btn1():
		filename = askopenfilename(parent=root,filetypes=[('All image files', '.jpg .png'),('All Files', '.*')],title='Select your image file')
		rtrttext=retr(str(filename))
		d=custom_dec(rtrttext)
		d=d.replace("T"," ")
		rtrttext ="Message:: " +d
		a.config(text=rtrttext)
	def gen():
		t = askopenfilename(parent=root,filetypes=[('All image files', '.jpg .png'),('All Files', '.*')],title='Select your image file')
		opname=t[:-4]+"_out.png"
		xlname=t[:-4]+"_stego.xlsx"
		t=open(t)
		t1=open(opname)
		t1=t1.convert('RGBA')
		t=t.convert('RGBA')
		data=t.getdata()
		data2=t1.getdata()
		data3 = [[0 for x in range(4)] for x in range(len(data))]
		workbook = xlsxwriter.Workbook(xlname)
		worksheet = workbook.add_worksheet()
		worksheet.write(0,0,"primary Image")
		row=1
		col=0

		for item1,item2,item3,item4 in (data):
			worksheet.write(row,col,item1)
			worksheet.write(row,col+1,item2)
			worksheet.write(row,col+2,item3)
			worksheet.write(row,col+3,item4)
			row +=1
		worksheet.write(0,4,"stego Image")
		row=1
		col=4
		for item1,item2,item3,item4 in (data2):
			worksheet.write(row,col,item1)
			worksheet.write(row,col+1,item2)
			worksheet.write(row,col+2,item3)
			worksheet.write(row,col+3,item4)
			row +=1
		for i in range(0,len(data)):
			for j in [0,1,2]:
				data3[i][j]=data[i][j]-data2[i][j]
		worksheet.write(0,8,"Result")
		row=1
		col=8
		for item1,item2,item3,item4 in (data3):
			worksheet.write(row,col,item1)
			worksheet.write(row,col+1,item2)
			worksheet.write(row,col+2,item3)
			worksheet.write(row,col+3,item4)
			row +=1		
		workbook.close()
		a.config(text="the excel sheet is stored as "+xlname)
	root = Tk()
	root.title("2 bit LSB Steganography")
	root.geometry("640x480")
	test2_label=Label(root,text="Enter message to encrypt").pack(side=TOP)
	test2=Text(root,height="1")
	test2.pack()
	Button(root, text = "Encrypt",command = btn).pack()
	Button(root, text= "Decrypt",command = btn1).pack(side=TOP) 
	Button(root, text= "Generate Excel sheet",command= gen).pack(side=TOP)
	a = Label(root, text = "Result")
	a.pack(side=TOP)
	root.mainloop()
if __name__=="__main__":
	Gui() 
	
