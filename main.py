import os
import sys

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Functions/models/'))
from Functions.models import utilFunctions as UF
from Functions.transformations_interface import stftMorph_function as sT

#Functions
def play_song():
    filename = filedialog.askopenfilename()
    UF.wavplay(filename)

def browse_file1():
    try:
        #
        filename = filedialog.askopenfilename(title="Please Select a File")
        master.filelocation1.delete(0, END)
        master.filelocation1.insert(0,filename)

    except Exception as e:
        print(e)

def browse_file2():
    try:
        filename = filedialog.askopenfilename(title="Please Select a File")
        master.filelocation2.delete(0, END)
        master.filelocation2.insert(0,filename)

    except Exception as e:
        print(e)

def transformation_synthesis():
    try:
        inputFile1 = master.filelocation1.get()
        inputFile2 = master.filelocation2.get()
        window1 = master.w1_type.get()
        window2 = master.w2_type.get()
        M1 = int(master.M1.get())
        M2 = int(master.M2.get())
        N1 = int(master.N1.get())
        N2 = int(master.N2.get())
        H1 = int(master.H1.get())
        smoothf = float(master.smoothf.get())
        balancef = float(master.balancef.get())
        y, fs = sT.main(inputFile1, inputFile2, window1, window2, M1, M2, N1, N2, H1, smoothf, balancef)
        save_audio(y,fs)


    except ValueError as errorMessage:
        messagebox.showerror("Input values error", errorMessage)

def save_audio(y,fs):
    outputFile = filedialog.asksaveasfile()
    print(outputFile.name + '_stftMorph.wav')
    #outputFile = 'Functions/transformations_interface/output_sounds/' + os.path.basename(inputFile1)[:-4] + '_stftMorph.wav'
    UF.wavwrite(y, fs, outputFile.name + '_stftMorph.wav')

#Initialize the master root as a Tkinter interface
master = Tk()
master.title("Sound Transformations App")

## INPUT FILE 1
choose1_label = "File 1:"
Label(master, text=choose1_label).grid(row=0, column=0, sticky="W", padx=5, pady=(10, 2))

#TEXTBOX TO PRINT PATH OF THE SOUND FILE
master.filelocation1 = Entry()
master.filelocation1.focus_set()
master.filelocation1["width"] = 30
master.filelocation1.grid(row=0,column=0, sticky=W, padx=(75, 5), pady=(10,2))
master.filelocation1.delete(0, END)

# BUTTON TO BROWSE SOUND FILE 1
open_file1 = Button(master, text="...", command= browse_file1)  # see: def browse_file(self)
open_file1.grid(row=0, column=0, sticky="W", padx=(330, 6), pady=(10, 2))  # put it beside the filelocation textbox

#BUTTON TO PREVIEW SOUND FILE 1
preview1 = Button(master, text=">", command=lambda: UF.wavplay(master.filelocation1.get()), bg="gray30", fg="white")
preview1.grid(row=0, column=0, sticky=W, padx=(375,6), pady=(10,2))

#ANALYSIS WINDOW TYPE SOUND 1
wtype1_label = "window1:"
Label(master, text=wtype1_label).grid(row=1, column=0, sticky=W, padx=5, pady=(4,2))
master.w1_type = StringVar()
master.w1_type.set("hamming") # initial value
window1_option = OptionMenu(master, master.w1_type, "rectangular", "hanning", "hamming", "blackman", "blackmanharris")
window1_option.grid(row=1, column=0, sticky="W", padx=(68,5), pady=(4,2))

#WINDOW SIZE SOUND 1
M1_label = "M1:"
Label(master, text=M1_label).grid(row=1, column=0, sticky=W, padx=(180, 5), pady=(4,2))
master.M1 = Entry(master, justify=CENTER)
master.M1["width"] = 5
master.M1.grid(row=1,column=0, sticky=W, padx=(208,5), pady=(4,2))
master.M1.delete(0, END)
master.M1.insert(0, "1024")

#FFT SIZE SOUND 1
N1_label = "N1:"
Label(master, text=N1_label).grid(row=1, column=0, sticky=W, padx=(265, 5), pady=(4,2))
master.N1 = Entry(master, justify=CENTER)
master.N1["width"] = 5
master.N1.grid(row=1,column=0, sticky=W, padx=(290,5), pady=(4,2))
master.N1.delete(0, END)
master.N1.insert(0, "1024")

#HOP SIZE SOUND 1
H1_label = "H1:"
Label(master, text=H1_label).grid(row=1, column=0, sticky=W, padx=(343,5), pady=(4,2))
master.H1 = Entry(master, justify=CENTER)
master.H1["width"] = 5
master.H1.grid(row=1, column=0, sticky=W, padx=(370,5), pady=(4,2))
master.H1.delete(0, END)
master.H1.insert(0, "256")

###
# SEPARATION LINE
Frame(master, height=1, width=50, bg="black").grid(row=2, pady=15, sticky=W + E)
###

## INPUT FILE 2
choose2_label = "inputFile2:"
Label(master, text=choose2_label).grid(row=3, column=0, sticky=W, padx=5, pady=(2, 2))

# TEXTBOX TO PRINT PATH OF THE SOUND FILE
master.filelocation2 = Entry(master)
master.filelocation2.focus_set()
master.filelocation2["width"] = 30
master.filelocation2.grid(row=3, column=0, sticky=W, padx=(75, 5), pady=(2, 2))
master.filelocation2.delete(0, END)

# BUTTON TO BROWSE SOUND FILE 2
open_file2 = Button(master, text="...", command=browse_file2)  # see: def browse_file(self)
open_file2.grid(row=3, column=0, sticky=W, padx=(330, 6), pady=(2, 2))  # put it beside the filelocation textbox

# BUTTON TO PREVIEW SOUND FILE 2
preview2 = Button(master, text=">", command=lambda: UF.wavplay(master.filelocation2.get()), bg="gray30", fg="white")
preview2.grid(row=3, column=0, sticky=W, padx=(375, 6), pady=(2, 2))

# ANALYSIS WINDOW TYPE SOUND 2
wtype2_label = "window2:"
Label(master, text=wtype2_label).grid(row=4, column=0, sticky=W, padx=5, pady=(4, 2))
master.w2_type = StringVar()
master.w2_type.set("hamming")  # initial value
window2_option = OptionMenu(master, master.w2_type, "rectangular", "hanning", "hamming", "blackman","blackmanharris")
window2_option.grid(row=4, column=0, sticky=W, padx=(68, 5), pady=(4, 2))

# WINDOW SIZE SOUND 2
M2_label = "M2:"
Label(master, text=M2_label).grid(row=4, column=0, sticky=W, padx=(180, 5), pady=(4, 2))
master.M2 = Entry(master, justify=CENTER)
master.M2["width"] = 5
master.M2.grid(row=4, column=0, sticky=W, padx=(208, 5), pady=(4, 2))
master.M2.delete(0, END)
master.M2.insert(0, "1024")

# FFT SIZE SOUND 2
N2_label = "N2:"
Label(master, text=N2_label).grid(row=4, column=0, sticky=W, padx=(265, 5), pady=(4, 2))
master.N2 = Entry(master, justify=CENTER)
master.N2["width"] = 5
master.N2.grid(row=4, column=0, sticky=W, padx=(290, 5), pady=(4, 2))
master.N2.delete(0, END)
master.N2.insert(0, "1024")

###
# SEPARATION LINE
Frame(master, height=1, width=50, bg="black").grid(row=5, pady=15, sticky=W + E)
###

# SMOOTHING FACTOR
smoothf_label1 = "Smooth factor of sound 2 (bigger than 0 to max of 1, where 1 is no"
Label(master, text=smoothf_label1).grid(row=6, column=0, sticky=W, padx=(5, 5), pady=(2, 2))
smoothf_label2 = "smothing):"
Label(master, text=smoothf_label2).grid(row=7, column=0, sticky=W, padx=(5, 5), pady=(0, 2))
master.smoothf = Entry(master, justify=CENTER)
master.smoothf["width"] = 5
master.smoothf.grid(row=8, column=0, sticky=W, padx=(5, 5), pady=(2, 2))
master.smoothf.delete(0, END)
master.smoothf.insert(0, "0.5")

# BALANCE FACTOR
balancef_label = "Balance factor (from 0 to 1, where 0 is sound 1 and 1 is sound 2):"
Label(master, text=balancef_label).grid(row=9, column=0, sticky=W, padx=(5, 5), pady=(10, 2))
master.balancef = Entry(master, justify=CENTER)
master.balancef["width"] = 5
master.balancef.grid(row=10, column=0, sticky=W, padx=(5, 5), pady=(2, 2))
master.balancef.delete(0, END)
master.balancef.insert(0, "0.2")

# BUTTON TO DO THE SYNTHESIS
compute = Button(master, text="Apply Transformation", command = transformation_synthesis, bg="dark green",fg="white")
compute.grid(row=11, column=0, padx=5, pady=(10, 15), sticky=W)

# BUTTON TO PLAY TRANSFORMATION SYNTHESIS OUTPUT
master.transf_output = Button(master, text=">", command=play_song, bg="gray30", fg="white")
master.transf_output.grid(row=11, column=0, padx=(165, 5), pady=(10, 15), sticky=W)

# define options for opening file
file_opt = options = {}
options['defaultextension'] = '.wav'
options['filetypes'] = [('All files', '.*'), ('Wav files', '.wav')]
options['initialdir'] = '../../sounds/'
options = 'Open a mono audio file .wav with sample frequency 44100 Hz'


master.mainloop()
