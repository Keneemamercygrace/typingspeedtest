from tkinter import *
import ctypes
import random
import tkinter

# ctypes.windll.shcore.SetProcessDpiAwareness(1)

window = Tk()
window.title('Type Speed Test')
window.config(padx=10, pady=10)


def resetWritingLabels():
    # Text List
    possibleTexts = [
        'For writers, a random sentence can help them get their creative juices flowing. Since the topic of the '
        'sentence is completely unknown, it forces the writer to be creative when the sentence appears. There are a '
        'number of different ways a writer can use the random sentence for creativity. The most common way to use the '
        'sentence is to begin a story. Another option is to include it somewhere in the story. A much more difficult '
        'challenge is to use it to end a story. In any of these cases, it forces the writer to think creatively since '
        'they have no idea what sentence will appear from the tool.',
        'The goal of Python Code is to provide Python tutorials, recipes, problem fixes and articles to beginner and '
        'intermediate Python programmers, as well as sharing knowledge to the world. Python Code aims for making '
        'everyone in the world be able to learn how to code for free. Python is a high-level, interpreted, '
        'general-purpose programming language. Its design philosophy emphasizes code readability with the use of '
        'significant indentation. Python is dynamically-typed and garbage-collected. It supports multiple programming '
        'paradigms, including structured (particularly procedural), object-oriented and functional programming. It is '
        'often described as a "batteries included" language due to its comprehensive standard library.',
        'As always, we start with the imports. Because we make the UI with tkinter, we need to import it. We also '
        'import the font module from tkinter to change the fonts on our elements later. We continue by getting the '
        'partial function from functools, it is a genius function that excepts another function as a first argument '
        'and some args and kwargs and it will return a reference to this function with those arguments. This is '
        'especially useful when we want to insert one of our functions to a command argument of a button or a key '
        'binding. '
    ]
    # Chosing one of the texts randomly with the choice function
    text = random.choice(possibleTexts).lower()
    # defining where the text is split
    splitPoint = 0
    # This is where the text is that is already written
    global labelLeft
    labelLeft = Label(window, text=text[0:splitPoint], fg='grey')
    labelLeft.place(relx=0.5, rely=0.5, anchor=E)

    # Here is the text which will be written
    global labelRight
    labelRight = Label(window, text=text[splitPoint:])
    labelRight.place(relx=0.5, rely=0.5, anchor=W)

    # This label shows the user which letter he now has to press
    global currentLetterLabel
    currentLetterLabel = Label(window, text=text[splitPoint], fg='grey')
    currentLetterLabel.place(relx=0.5, rely=0.6, anchor=N)

    # this label shows the user how much time has gone by
    global timeleftLabel
    timeleftLabel = Label(window, text=f'0 Seconds', fg='grey')
    timeleftLabel.place(relx=0.5, rely=0.4, anchor=S)

    global writeAble
    writeAble = True
    window.bind('<Key>', keyPress)

    global passedSeconds
    passedSeconds = 0

    # Binding callbacks to functions after a certain amount of time.
    window.after(60000, stopTest)
    window.after(1000, addSecond)


def stopTest():
    global writeAble
    writeAble = False

    # Calculating the amount of words
    amountWords = len(labelLeft.cget('text').split(' '))

    # Destroy all unwanted widgets.
    timeleftLabel.destroy()
    currentLetterLabel.destroy()
    labelRight.destroy()
    labelLeft.destroy()

    # Display the test results with a formatted string
    global ResultLabel
    ResultLabel = Label(window, text=f'Words per Minute: {amountWords}', fg='black')
    ResultLabel.grid(row=4, column=0)

    # Display a button to restart the game
    global ResultButton
    ResultButton = Button(window, text=f'Retry', command=restart)
    ResultButton.grid(row=5, column=0)


def restart():
    # Destry result widgets
    ResultLabel.destroy()
    ResultButton.destroy()

    # re-setup writing labels.
    resetWritingLabels()


def addSecond():
    # Add a second to the counter.

    global passedSeconds
    passedSeconds += 1
    timeleftLabel.configure(text=f'{passedSeconds} Seconds')

    # call this function again after one second if the time is not over.
    if writeAble:
        window.after(1000, addSecond)


def keyPress(event=None):
    try:
        if event.char.lower() == labelRight.cget('text')[0].lower():
            # Deleting one from the right side.
            labelRight.configure(text=labelRight.cget('text')[1:])
            # Deleting one from the right side.
            labelLeft.configure(text=labelLeft.cget('text') + event.char.lower())
            # set the next Letter Lavbel
            currentLetterLabel.configure(text=labelRight.cget('text')[0])
    except tkinter.TclError:
        pass


# This will start the Test
resetWritingLabels()

# Start the mainloop
window.mainloop()

