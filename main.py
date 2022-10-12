from tkinter import *
import time
import datetime

text = "my name is keneema grace mercy, am a female from uganda."
total_seconds = 60
start = 0

window = Tk()
window.title("Typing speed test")
window.config(padx=10, pady=10)

lab_1 = Label(
    text="How fast are your fingers? Do the one-minute typing test to find out!\n Press the space bar after "
         "each word. At the end, you'll get your typing speed in CPM and WPM.\n Good luck!")
lab_1.grid(row=0, column=0)

score_label = Label(text="Most recent score: 0")
score_label.grid(row=1, column=0)

sample = Label(text="SAMPLE TEXT")
sample.grid(row=3, column=0)

time_label = Label(text="Time left: 60 s")
time_label.grid(row=4, column=0)

canvas = Canvas(window, width=700, height=350, bg="SpringGreen2")
sample_text = canvas.create_text(400, 100, width=400,
                                 text=text,
                                 fill="black",
                                 font='Helvetica 15 bold')
canvas.grid(row=5, column=0)

text_label = Label(text="Type your text here")
text_label.grid(row=6, column=0)

input_text = Entry(window, width=70)
input_text.grid(row=7, column=0, columnspan=3)
input_text.focus()

starttime = time.time()
lasttime = starttime
lapnum = 1

while lapnum < 60:
    laptime = round((time.time()) - starttime)
    lasttime = time.time()
    lapnum += 1

print(lapnum)


def pressed(keyevent):
    global start
    global text, total_seconds
    sample_text_size = len(text)
    sample_text_list = tuple(text)
    sample_text_fl = str(sample_text_list[0])
    sample_text_ll = str(sample_text_list[-1])

    compare_word = input_text.get()
    compare_word_size = len(compare_word)
    type_word_list = tuple(compare_word)
    type_word_first_letter = str(type_word_list[0])
    if compare_word_size > 0:
        type_word_list = tuple(compare_word)
        type_word_first_letter = str(type_word_list[0])
        type_word_last_letter = str(type_word_list[-1])
        for n in type_word_list:
            for p in sample_text_list:
                if n == p:
                    canvas.itemconfig(sample_text, text=text, fill='red')

    if sample_text_size == 1 and compare_word_size == 1:
        # Even though you measure time, it is insignificant! Also, it returns 0...
        print("It's just one letter... You at least need a two letter word to calculate the time!")

    if compare_word_size == 1 and sample_text_size > 1 and sample_text_fl == type_word_first_letter:
        global start
        start = time.time()
        print(f"the first start {start}")
        time_label.config(text=f"Time elapsed: {laptime}")
    if compare_word_size == sample_text_size and sample_text_size != 1:
        print("Match")
        type_word_list = tuple(compare_word)
        type_word_first_letter = str(type_word_list[0])
        type_word_last_letter = str(type_word_list[-1])
        if sample_text_ll == type_word_last_letter:
            stop = time.time()
            print(f"stop; {stop}")
            total_time = stop - start
            total_time = round(total_time, 2)
            print(f"total time; {total_time}")
            final = input_text.get()
            wpm = len(final) / total_time
            wps = round(wpm, 2)
            score_label.config(text=f"Most recent score: {wps} words per second")
            if sample_text == compare_word:
                print("You took " + str(float(total_time)) + " seconds to type the word " + str(sample_text) + ".")
            else:
                print("You took " + str(float(total_time)) + " seconds to type the word that was similar to " + str(
                    compare_word) + ".")
                print("Though the words are of the same size, it doesn't appear that the two words match! Retry again "
                      "for accurate results...")



input_text.bind('<KeyRelease>', pressed)
window.mainloop()
