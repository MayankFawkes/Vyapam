from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk
from PIL import ImageDraw, ImageFont
from urllib.request import urlopen
from io import BytesIO
from json import loads

def saveImage(message,date,photo,sign,hand,savelocation):
	qual=60
	photo = Image.open(photo)
	sign= Image.open(sign)
	hand=Image.open(hand)
	# imgg= Image.open('Template/1.jpg')
	imgg = Image.open("Template/1.jpg")
	photo = photo.resize((260,325), Image.ANTIALIAS)
	minus=int((325/100)*84)
	# print(minus)
	plus=int((260-(len(message)*12))/2)
	# print(plus)
	minus1=int((325/100)*91)
	# print(minus)
	plus1=int((260-(len(date)*12))/2)
	# print(plus)
	if message or date:
		temp=Image.new("RGB",(260,50), "white")
		photo.paste(temp,(0,270))
		draw = ImageDraw.Draw(photo)
		font = ImageFont.truetype('Template/Roboto-Black.ttf', size=20)
		color = 'rgb(0, 0, 0)'
		draw.text((plus, minus), message, fill=color, font=font)
		draw.text((plus1, minus1), date, fill=color, font=font)
	sign = sign.resize((290,120), Image.ANTIALIAS)
	hand =hand.resize((975,210), Image.ANTIALIAS)
	imgg.paste(photo,(230,360))
	imgg.paste(sign,(770,363))
	imgg.paste(hand,(170,1450))
	imgg =imgg.resize((1200,1700), Image.ANTIALIAS)
	imgg.save(savelocation+".jpg",optimize=True, dpi=(96,96), quality=int(qual))
	return True

def funcphotolocation():
	global photolocation
	photolocation = askopenfilename(filetypes=(('JPEG (*.jpg;*.jpeg;*.jpe;*.jfif)','.jpg'),("PNG (*.png)",'.png'),("All Files","*.*")))
def funchandwritinglocation():
	global handwritinglocation
	handwritinglocation = askopenfilename(filetypes=(('JPEG (*.jpg;*.jpeg;*.jpe;*.jfif)','.jpg'),("PNG (*.png)",'.png'),("All Files","*.*")))
def funcsignaturelocation():
	global signlocation
	signlocation = askopenfilename(filetypes=(('JPEG (*.jpg;*.jpeg;*.jpe;*.jfif)','.jpg'),("PNG (*.png)",'.png'),("All Files","*.*")))

def saving():
	if not photolocation:
		messagebox.showerror("Error", "Select Photo")
	if not handwritinglocation:
		messagebox.showerror("Error", "Select Handwriting")
	if not signlocation:
		messagebox.showerror("Error", "Select Signature")
	else:
		 savelocation=asksaveasfilename(filetypes=(('JPEG (*.jpg;*.jpeg;*.jpe;*.jfif)','.jpg'),))
		 if saveImage(nameyes.get(),dateyes.get(),photolocation,signlocation,handwritinglocation,savelocation):
		 	filename=savelocation.split("/")[-1]
		 	messagebox.showinfo("Saved","{}.jpg Saved".format(filename))

def header():
	raw_data = urlopen("https://raw.githubusercontent.com/MayankFawkes/Vyapam/master/Header.png").read()
	# raw_data = urlopen("http://fill-image.jobs160.com/350x200").read()
	im = Image.open(BytesIO(raw_data))
	photo = ImageTk.PhotoImage(im)
	return photo

def main(infomessage):
	root.destroy()
	windowg=Tk()
	windowg.geometry("500x400")
	windowg.title("Vyapam Software")
	# windowg.configure(background="black")

	opper=Frame(windowg)
	opper.pack(side=TOP)
	neche=Frame(windowg)
	neche.pack(side=BOTTOM)

	photoo=header()
	Mlabel =Label(opper,image=photoo)
	Mlabel.pack()

	NR=Frame(windowg)
	NR.pack(side=BOTTOM)
	NL=Frame(windowg)
	NL.pack(side=TOP)

	Photo=Label(NL, text="Select Photo")
	Photo.grid(row=0,column=0,sticky="E")
	Signature=Label(NL, text="Select Signature")
	Signature.grid(row=1,column=0,sticky="E")
	Handwriting=Label(NL, text="Select Handwriting")
	Handwriting.grid(row=2,column=0,sticky="E")
	savepic=Label(NR, text="Save Image")
	savepic.grid(row=0,column=0)

	PhotoButton=Button(NL,width=10,height=2,text="Photo",bg="black",fg="white", command=funcphotolocation)
	PhotoButton.grid(row=0,column=1,sticky="N")

	SignatureButton=Button(NL,width=10,height=2,text="Signature",bg="black",fg="white",command=funcsignaturelocation)
	SignatureButton.grid(row=1,column=1,sticky="N")

	HandwritingButton=Button(NL,width=10,height=2,text="Handwriting",bg="black",fg="white", command=funchandwritinglocation)
	HandwritingButton.grid(row=2,column=1,sticky="N")

	SaveButton=Button(NR,width=10,height=2,text="SAVE",bg="red",fg="black", command=saving)
	SaveButton.grid(row=0,column=1,sticky="N")
	nameprin=Label(NL, text="Enter Name")
	nameprin.grid(row=0,column=2,sticky="E")
	dateprin=Label(NL, text="Enter date")
	dateprin.grid(row=1,column=2,sticky="E")

	global nameyes
	global dateyes
	global photolocation
	global signlocation
	global handwritinglocation
	photolocation=""
	signlocation=""
	handwritinglocation=""
	nameyes=Entry(NL)
	nameyes.grid(row=0,column=3,sticky="W")
	dateyes=Entry(NL)
	dateyes.grid(row=1,column=3,sticky="W")

	hehehe=Text(NL, height=3, width=15)
	hehehe.grid(row=2,column=3,sticky="E")
	hehehe.insert(0.0,infomessage)

	windowg.mainloop()

def trying():
	keys=entry.get()
	try:
		d=loads(urlopen("https://raw.githubusercontent.com/MayankFawkes/Vyapam/master/key.json").read().decode())
		main(d[keys])
	except:
		messagebox.showerror("Error", "Invalid Key")
		root.destroy()


root=Tk()
root.title("Enter Key")
# root.configure(background="black")
root.geometry("300x100")
key=Label(root, text="Enter Key")
key.grid(row=0,column=0,sticky="W")
entry=Entry(root)
entry.grid(row=0,column=1,sticky="W")
button=Button(root,width=10,height=2,text="Submit", command=trying)
button.grid(row=0,column=2,sticky="W")
root.mainloop()
