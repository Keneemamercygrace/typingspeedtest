from tkinter import *
import time

text = "Python is truly a seductive language and it seems to get better every time I try to do something with " \
       "it. Measuring the time between keystrokes is one such curious project I did to learn Python "


# start = time.time()

def type_test(sample_text):
    window = Tk()
    window.title("Typing speed test")
    window.config(padx=10, pady=10)

    lab_1 = Label(
        text="How fast are your fingers? Do the one-minute typing test to find out!\n Press the space bar after "
             "each word. At the end, you'll get your typing speed in CPM and WPM.\n Good luck!")
    lab_1.grid(row=0, column=0)

    score_label = Label(text="Most recent score")
    score_label.grid(row=1, column=0)
    sample = Label(text="SAMPLE TEXT")
    sample.grid(row=3, column=0)

    canvas = Canvas(window, width=700, height=350, bg="SpringGreen2")
    sample_text = canvas.create_text(400, 100, width=400,
                                     text=sample_text,
                                     fill="black",
                                     font='Helvetica 15 bold')
    canvas.grid(row=5, column=0)

    text_label = Label(text="Type your text here")
    text_label.grid(row=6, column=0)

    input_text = Entry(width=70)
    input_text.grid(row=7, column=0, columnspan=3)
    input_text.focus()

    def pressed(key_event):
        sample_text_size = len(sample_text)
        sample_text_list = tuple(sample_text)
        sample_text_fl = str(sample_text_list[0])
        sample_text_ll = str(sample_text_list[-1])

        compare_word = input_text.get()
        compare_word_size = len(compare_word)
        compare_word_list = tuple(compare_word)
        compare_word_fl = str(compare_word_list[0])
        compare_word_ll = str(compare_word_list[-1])

        if compare_word_size == 1 and sample_text_fl == key_event.char:
            global start
            start = time.time()

        if sample_text_ll == compare_word_ll:
            stop = time.time()
            total_time = start - stop
            acc = sample_text_size / compare_word_size
            wpm = compare_word_size / total_time
            return wpm, acc

    input_text.bind('<KeyRelease>', pressed)
    window.mainloop()


type_test(text)
