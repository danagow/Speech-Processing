from tkinter import*
from tkinter import messagebox
import pygame
import random
import aubio
import pyaudio
import numpy as np
from aubio import midiconv as m
from threading import Thread
import time
pygame.init()
root = Tk()

root.title = ('Piano')
num1= StringVar()
def sound_Cs():
	sNote.set("C#4")
	pygame.mixer.Sound("F:\\Speech Processing\\Music_Notes\\C_s.wav").play()

def sound_Ds():
	sNote.set("D#4")
	pygame.mixer.Sound("F:\\Speech Processing\\Music_Notes\\D_s.wav").play()

def sound_Fs():
	sNote.set("F#4")
	pygame.mixer.Sound("F:\\Speech Processing\\Music_Notes\\F_s.wav").play()

def sound_Gs():
	sNote.set("G#4")
	pygame.mixer.Sound("F:\\Speech Processing\\Music_Notes\\G_s.wav").play()

def sound_Bb():
	sNote.set("A#4")
	pygame.mixer.Sound("F:\\Speech Processing\\Music_Notes\\Bb.wav").play()

def sound_Cs1():
	sNote.set("C#5")
	pygame.mixer.Sound("F:\\Speech Processing\\Music_Notes\\C_s1.wav").play()

def sound_Ds1():
	sNote.set("D#5")
	pygame.mixer.Sound("F:\\Speech Processing\\Music_Notes\\D_s1.wav").play()

value=StringVar()
sNote=StringVar()
singing=StringVar()
topframe = Frame(root)
topframe.pack(side=TOP)
random_note=Button(topframe, padx= 8, pady=8,text='Random note',width=10)
random_note.grid(row=0,column=0,padx=30,pady=1)
txtDisplay=Entry(topframe,textvariable= value, insertwidth=5, font =40 , justify= 'center', width= 4)
txtDisplay.grid(row=1, column=1, pady = 5)
txtDisplay2=Entry(topframe,textvariable= sNote, insertwidth=5, font =40 , justify= 'center', width= 4)
txtDisplay2.grid(row=0, column=1, pady = 5)
singing.set('Sing')
sing_button=Button(topframe, padx= 8, pady=8,textvariable=singing,width=10)
sing_button.grid(row=0,column=2,pady=1,padx=30)
# correct=Button(topframe, padx= 8, pady=8,textvariable=corrected,width=10)
# sing_button.grid(row=0,column=2,pady=1,padx=30)


frame = Frame(root)
frame.pack()
note_Cs = Button(frame, padx= 8, pady=8, height = 6,width=2, bd=8, text='C#4', bg='black', fg='white',command=sound_Cs)
note_Cs.pack(side=LEFT)
space = Button(frame, state= DISABLED,padx= 0, pady=0, height = 7, width =1, relief= FLAT)
space.pack(side=LEFT)
note_Ds = Button(frame, padx= 8, pady=8, height = 6, width=2,bd=8, text='D#4', bg='black', fg='white',command=sound_Ds)
note_Ds.pack(side=LEFT)
space = Button(frame, state= DISABLED,padx= 0, pady=0, height = 7, width =4, relief= FLAT)
space.pack(side=LEFT)
note_Fs = Button(frame, padx= 8, pady=8, height = 6, width=2,bd=8, text='F#4', bg='black', fg='white',command=sound_Fs)
note_Fs.pack(side=LEFT)
space = Button(frame, state= DISABLED,padx= 0, pady=0, height = 7, width =1, relief= FLAT)
space.pack(side=LEFT)
note_Gs = Button(frame, padx= 8, pady=8, height = 6, width=2,bd=8, text='G#4', bg='black', fg='white',command=sound_Gs)
note_Gs.pack(side=LEFT)
space = Button(frame, state= DISABLED,padx= 0, pady=0, height = 7, width =1, relief= FLAT)
space.pack(side=LEFT)
note_Bb = Button(frame, padx= 8, pady=8, height = 6, width=2,bd=8, text='A#4', bg='black', fg='white',command=sound_Bb)
note_Bb.pack(side=LEFT)
space = Button(frame, state= DISABLED,padx= 0, pady=0, height = 7, width =4, relief= FLAT)
space.pack(side=LEFT)
note_Cs1 = Button(frame, padx= 8, pady=8, height = 6,width=2, bd=8, text='C#5', bg='black', fg='white',command=sound_Cs1)
note_Cs1.pack(side=LEFT)
space = Button(frame, state= DISABLED,padx= 0, pady=0, height = 7, width =1, relief= FLAT)
space.pack(side=LEFT)
note_Ds1 = Button(frame, padx= 8, pady=8, height = 6,width=2, bd=8, text='D#5', bg='black', fg='white',command=sound_Ds1)
note_Ds1.pack(side=LEFT)


bottomframe = Frame(root)
bottomframe.pack()

def sound_C():
	sNote.set("C4")
	pygame.mixer.Sound("F:\\Speech Processing\\Music_Notes\\C.wav").play()

def sound_D():
	sNote.set("D4")
	pygame.mixer.Sound("F:\\Speech Processing\\Music_Notes\\D.wav").play()

def sound_E():
	sNote.set("E4")
	pygame.mixer.Sound("F:\\Speech Processing\\Music_Notes\\E.wav").play()

def sound_F():
	sNote.set("F4")
	pygame.mixer.Sound("F:\\Speech Processing\\Music_Notes\\F.wav").play()

def sound_G():
	sNote.set("G4")
	pygame.mixer.Sound("F:\\Speech Processing\\Music_Notes\\G.wav").play()

def sound_A():
	sNote.set("A4")
	pygame.mixer.Sound("F:\\Speech Processing\\Music_Notes\\A.wav").play()

def sound_B():
	sNote.set("B4")
	pygame.mixer.Sound("F:\\Speech Processing\\Music_Notes\\B.wav").play()

def sound_C1():
	sNote.set("C5")
	pygame.mixer.Sound("F:\\Speech Processing\\Music_Notes\\C1.wav").play()

def sound_D1():
	sNote.set("C5")
	pygame.mixer.Sound("F:\\Speech Processing\\Music_Notes\\D1.wav").play()

def sound_E1():
	sNote.set("E5")
	pygame.mixer.Sound("F:\\Speech Processing\\Music_Notes\\E1.wav").play()

def sound_F1():
	sNote.set("F5")
	pygame.mixer.Sound("F:\\Speech Processing\\Music_Notes\\F1.wav").play()


note_C = Button(bottomframe, padx= 16, pady=16, height = 8, bd=8, text='C4', bg='white', fg='black',command=sound_C)
note_C.pack(side=LEFT)
note_D = Button(bottomframe, padx= 16, pady=16, height = 8, bd=8, text='D4', bg='white', fg='black',command=sound_D)
note_D.pack(side=LEFT)
note_E = Button(bottomframe, padx= 16, pady=16, height = 8, bd=8, text='E4', bg='white', fg='black',command=sound_E)
note_E.pack(side=LEFT)
note_F = Button(bottomframe, padx= 16, pady=16, height = 8, bd=8, text='F4', bg='white', fg='black',command=sound_F)
note_F.pack(side=LEFT)
note_G = Button(bottomframe, padx= 16, pady=16, height = 8, bd=8, text='G4', bg='white', fg='black',command=sound_G)
note_G.pack(side=LEFT)
note_A = Button(bottomframe, padx= 16, pady=16, height = 8, bd=8, text='A4', bg='white', fg='black',command=sound_A)
note_A.pack(side=LEFT)
note_B = Button(bottomframe, padx= 16, pady=16, height = 8, bd=8, text='B4', bg='white', fg='black',command=sound_B)
note_B.pack(side=LEFT)
note_C1 = Button(bottomframe, padx= 16, pady=16, height = 8, bd=8, text='C5', bg='white', fg='black',command=sound_C1)
note_C1.pack(side=LEFT)
note_D1 = Button(bottomframe, padx= 16, pady=16, height = 8, bd=8, text='D5', bg='white', fg='black',command=sound_D1)
note_D1.pack(side=LEFT)
note_E1 = Button(bottomframe, padx= 16, pady=16, height = 8, bd=8, text='E5', bg='white', fg='black',command=sound_E1)
note_E1.pack(side=LEFT)
note_F1 = Button(bottomframe, padx= 16, pady=16, height = 8, bd=8, text='F5', bg='white', fg='black',command=sound_F1)
note_F1.pack(side=LEFT)

def random_notes():
	note_list = [note_C,note_C1,note_Cs1,note_Cs,note_D,note_D1,note_Ds1,note_Ds,
	note_F,note_F1,note_Fs,note_G,note_Gs,note_B,note_Bb,note_E,note_E1,note_A]
	note = random.choice(note_list)
	note.config(state=ACTIVE)
	note.invoke()
	root.after(400, lambda: note.config(state=NORMAL))

random_note.config(command=random_notes)

def main_analysis(start):
	NOTE_MIN = 60       # 
	NOTE_MAX = 69       # Midi note number
	FSAMP = 44100      	# Sampling frequency in Hz
	FRAME_SIZE = 2048   # How many samples per frame?
	FRAMES_PER_FFT = 16 # FFT takes average across how many frames? 

	SAMPLES_PER_FFT = FRAME_SIZE*FRAMES_PER_FFT
	FREQ_STEP = float(FSAMP)/SAMPLES_PER_FFT    

	def number_to_freq(n): return 440 * 2.0**((n-69)/12.0)
	# Get min/max index within FFT of notes we care about.
	def note_to_fftbin(n): return number_to_freq(n)/FREQ_STEP
	#imin = max(0, int(np.floor(note_to_fftbin(NOTE_MIN-1))))
	imin = 0
	imax = min(SAMPLES_PER_FFT, int(np.ceil(note_to_fftbin(NOTE_MAX+1))))   
	# Allocate space to run an FFT. 
	buf = np.zeros(SAMPLES_PER_FFT, dtype=np.float32)
	num_frames = 0  
	# Initialize audio
	if(start):
		singing.set('Singing~')
		stream = pyaudio.PyAudio().open(format=pyaudio.paInt16,
		                                channels=1,
		                                rate=FSAMP,
		                                input=True,
		                                frames_per_buffer=FRAME_SIZE)   
		stream.start_stream()   
		# Create Hanning window function
		window = 0.5 * (1 - np.cos(np.linspace(0, 2*np.pi, SAMPLES_PER_FFT, False)))    		

		# Have 7 seconds for input sound
		t_end = time.time() + 7
		count =0 
		while time.time() < t_end:
		    # Shift the buffer down and new data in
		    buf[:-FRAME_SIZE] = buf[FRAME_SIZE:]
		    buf[-FRAME_SIZE:] = np.fromstring(stream.read(FRAME_SIZE), np.int16)    
		    # Run the FFT on the windowed buffer
		    fft = np.fft.rfft(buf * window) 
		    # Get frequency of maximum response in range
		    freq = (np.abs(fft[imin:imax]).argmax() + imin) * FREQ_STEP  
		    # Console output once we have a full buffer
		    note = m.freq2note(freq)
		    value.set(note)
		    num_frames += 1 
		    selected_note = sNote.get()
		    previous_note=''
		    if num_frames >= FRAMES_PER_FFT:
		        # print ('freq: {:7.2f} Hz     note: {:>3s} {:+.2f}'.format(
		        #     freq, note_name(n0), n-n0))
		        print('freq: {:7.2f} Hz     note: {}'.format(freq,note))
		        if(note==selected_note):
		        		if(previous_note==''):continue
		        		elif(note==previous_note):
		        			count+=1
		        		else:
		        			count=0
		        		print(count)
		        previous_note = note
	singing.set('Sing')
	if(count>=15):
		pop_up_success()
	else: 
		pop_up_failed()
	

def main_analysis_thread():
	Thread(target=lambda: main_analysis(1)).start()		    	

def pop_up_success():
	window = Tk()
	window.wm_title("Message")
	window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
	window.withdraw()
	messagebox.showinfo('Information','You sing correctly')
	window.deiconify()
	window.destroy()

def pop_up_failed():
	window = Tk()
	window.wm_title("Message")
	window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
	window.withdraw()
	messagebox.showinfo('Information','You sing incorrectly. Try again :)')
	window.deiconify()
	window.destroy()

sing_button.config(command=main_analysis_thread)


root.mainloop() 
