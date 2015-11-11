import Image
for i in [5,100,500,1024,2048]:
	crevar=Image.new('RGBA',(i,i),"blue")
	crevar.save(str(i)+".png")
