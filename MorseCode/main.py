from tkinter import *

morse_code = {
    'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', '!':'-.-.--'
}

def convert_text(text: str):
    global morse_text
    if text:
        result = ""
        for c in text:
            if c.isalpha():
                result += morse_code[c.upper()]
            else:
                result += morse_code[c]
        morse_text.config(text=result)
    else:
        morse_text.config(text="Your text is empty")


window = Tk()
window.title("Text to MorseCode")
window.config(padx=20, pady=20, background="white")

text_input = Entry()
text_input.grid(column=1,row=0, padx=5, pady=10)

text_label = Label(text="Text", background="white", fg="black", font=("Sans-serif",20, "bold"))
text_label.grid(column=0, row=0, pady=10)

convert_button = Button(text="Convert", highlightthickness=0, highlightbackground="white", font=("Sans-serif",12, "normal"), pady=3, command=lambda: convert_text(text_input.get()))
convert_button.grid(column=0,row=1)

morse_text = Label(text="", bg="white", fg="black", font=("Sans-serif",12, "normal"))
morse_text.grid(column=1, row=1)

window.mainloop()