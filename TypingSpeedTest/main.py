from tkinter import *
import time


class MainWindow(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title('Typing Speed')
        # master.geometry('800x600')
        # master.resizable(0, 0)
        self.master = master
        self.pack()

        self.main_sentence = StringVar(self, "But just as I didn't want to resent my kids, I also didn't want to find myself too much in love with them. There are parents who don't like to hear their little girl crying at night, at the vast approaching dark of sleep, and so in their torment think why not feed her a lollipop, and a few years later that kid's got seven cavities and a pulled tooth. This is how we've arrived at the point where we give every kid on the team a trophy in the name of participation. I didn't want to love my kids so much that I was blind to their shortcomings, limitations, and mediocre personalities, not to mention character flaws and criminal leanings. But I could, I thought, I could love a kid that much. A kid really could be everything, and that scared me. Because once a kid is everything, not only might you lose all perspective and start proudly displaying his participation trophies, you might also fear for that kid's life every time he leaves your sight. I didn't want to live in perpetual fear. People don't recover from the death of a child. I knew I wouldn't. I knew that having a kid would be my chance to improve upon my shitty childhood, that it would be a repudiation of my dad's suicide and a celebration of life, but if that kid taught me how to love him, how to love, period, and then I lost him as I lost my dad, that would be it for me. I'd toss in the towel. Fuck it, fuck this world and all its heartbreak. I'd tell that to Connie, and she'd tell me that if that was how I felt I was already a slave to the fear, and good luck.")
        self.current_word = StringVar(self, '')
        self.words_per_min = 0.0
        self.words = self.word_parser()
        self.current_word_index = 0
        self.t_0 = 0
        self.t_new = 0

        self.create_widgets()
        self.place_widgets()
        self.entry_box.config(state=DISABLED)

        self.bind_all('<space>', self.next_word)

    def create_widgets(self):
        # self.text_box = Text(self)
        self.wpm_label = Label(self, text=('WPM: ' + str(self.words_per_min)))
        self.current_word_label = Label(self, text=self.words[self.current_word_index])
        self.start_btn = Button(self, text='Start', command=self.start_game)
        self.entry_box = Entry(self, textvariable=self.current_word)
        self.message_label = Label(self,text='Welcome')

    def place_widgets(self):
        # self.text_box.insert(END, self.main_sentence.get())
        # self.text_box.config(state=DISABLED)
        # self.text_box.grid(column=0, row=0, columnspan=3, rowspan=7, pady=50)
        self.grid(column=0, row=0, padx=100, pady=100)
        self.wpm_label.grid(column=0, row=2)
        self.current_word_label.grid(column=0, row=0, columnspan=2)
        self.start_btn.grid(column=1, row=2)
        self.entry_box.grid(column=0, row=1, columnspan=2)
        self.message_label.grid(column=0, row=3, columnspan=2)

    def word_parser(self):
        return self.main_sentence.get().split()

    def next_word(self, event=None):
        if self.check_word() and self.current_word_index < len(self.words) - 1:
            self.current_word_index += 1
            self.current_word_label.config(text=self.words[self.current_word_index])
            self.current_word.set('')
            self.entry_box.config(textvariable=self.current_word)
            self.t_new = time.time()
            self.words_per_min = round(self.calculate_wpm(), 1)
            self.wpm_label.config(text='WPM: ' + str(self.words_per_min))
        elif self.current_word_index >= len(self.words) - 1:
            self.message_label.config(text='Finished')
        else:
            self.message_label.config(text=f'{self.words[self.current_word_index]} is incorrect')

    def check_word(self):
        return self.current_word.get().split()[0] == self.words[self.current_word_index]

    def start_game(self):
        self.t_0 = time.time()
        self.message_label.config(text='!START TYPING!')
        self.entry_box.config(state=NORMAL)

    def calculate_wpm(self):
        return float(self.current_word_index)/((self.t_new - self.t_0)/60)


root = Tk()
main_app = MainWindow(master=root)
main_app.mainloop()
