from tkinter import *
import time
import datetime

text = "my name is keneema grace mercy, am a female from uganda, i love coding and approaching difficult challenges."
total_seconds = 60


def type_test():
    global text
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

    input_text = Entry(width=70)
    input_text.grid(row=7, column=0, columnspan=3)
    input_text.focus()

    def typingErrors(prompt):
        global text

        word = input_text.get()
        word = word.split()
        errors_made = 0

        for i in range(len(text)):
            if i in (0, len(text) - 1):
                if text[i] == words[i]:
                    continue
                else:
                    errors_made += 1
            else:
                if text[i] == words[i]:
                    if (text[i + 1] == words[i + 1]) & (text[i - 1] == words[i - 1]):
                        continue
                    else:
                        errors_made += 1
                else:
                    errors_made += 1
        return errors_made

    # calculate the speed in words per minute
    def typingSpeed(ip, st, et):
        global time_take

        words_text = input_text.get()
        iwords = words_text.split()
        twords = len(iwords)
        current_speed = twords / time_take

        return current_speed

    # calculate total time elapsed
    def timeElapsed(st, et):
        time_taken = et - st

        return time_taken

    text_list = tuple(text)
    text_fl = str(text_list[0])

    words = input_text.get()
    words_list = tuple(words)
    words_fl = str(words_list[0])

    if text_fl == words_fl:
        stime = time.time()
        iprompt = input_text.get()
        etime = time.time()

        time_take = round(timeElapsed(stime, etime), 2)
        speed = typingSpeed(iprompt, stime, etime)
        errors = typingErrors(text)
        score_label.config(text=f"Most recent score: {speed}")
        time_label.config(text=f"time: {time_take}")

    window.mainloop()


type_test()
