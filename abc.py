from tkinter import *
master = Tk()
v = StringVar()
master.wm_title("Password Generator Application")

# The title
b = Label(master, text="Password Generator Application",font=("Helvetica", 32))
b.pack()
# A lenght writing
z = Label(master, text="Length",font=("Helvetica", 24))
z.pack()

# A scroolbar to select the length
a = Scale(master, from_=0, to=20, orient=HORIZONTAL, length=32*10)
length = IntVar()
length.set(16)
print(a.get())
a.pack()

# A type Label
d = Label(master, text="Type",font=("Helvetica", 24))
d.pack()

# A dropdown to select the type of the password
TYPE = StringVar()
Radiobutton(master, text="Numbers", variable=TYPE, value='Numbers',font=("Helvetica", 24)).pack(anchor=W)
Radiobutton(master, text="Alphabet", variable=TYPE, value="Alphabet",font=("Helvetica", 24)).pack(anchor=W)
Radiobutton(master, text="Alphabet and numbers", variable=TYPE, value="Alphabet and numbers",font=("Helvetica", 24)).pack(anchor=W)
Radiobutton(master, text="Alphabet, numbers and symbols", variable=TYPE, value="Alphabet, numbers and symbols",font=("Helvetica", 24)).pack(anchor=W)
def foo():
	HELLO.set(make_password(TYPE.get(),a.get()))
	master.clipboard_clear()
	master.clipboard_append(HELLO.get())

def make_password(TYPE,LENGTH):
	import random
	digits = '0123456789'
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	alphabet_with_uppercase = '''abcdefghijklmnopqrstuvwxyz
	ABCDEFGHIJKLMNOPQRSTUVWXYZ'''
	digits_and_alphabet = digits + alphabet
	all_characters = '''\1234567890'qwertyuiop+asdfghjkl<zxcvbnm,.-!"/()=?^QWERTYUIOP*ASDFGHJKLZXCVBNM;:_[]#'''
	if TYPE == 'Numbers' : TYPE = digits
	if TYPE == 'Alphabet' : TYPE = alphabet
	if TYPE == 'Alphabet and numbers' : TYPE = digits_and_alphabet
	if TYPE == 'Alphabet, numbers and symbols' : TYPE = all_characters
	password = ''
	while len(password) < LENGTH:
		password = password + random.choice(TYPE)
	return(password)

# A make password button
g = Button(master, text=" Tape Here To Make password",command= foo,font=("Helvetica", 12))
g.pack()


# A password label
HELLO = StringVar()
w = Label(master, textvariable=HELLO,font=("Helvetica", 24))
w.pack()
q = Label(master, text='Your password is automatically copied in your clipboard,',font=("Helvetica", 18))
q.pack()
y = Label(master, text='just right-click and paste where you want your password.',font=("Helvetica", 18))
y.pack()
z = Label(master, text='Developed By Shivam Soni')
z.pack()
mainloop()
