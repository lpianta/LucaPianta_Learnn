from tkinter import *
from tkinter import font as tkfont


class RockPaperScissor(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # Root
        root = Tk()
        root.title("Rock Paper Scissors")
        root.configure(background="#202020")
        self.title_font = tkfont.Font(
            family='Helvetica', size=18, weight="bold", slant="italic")

        # Images
        self.rock_img = PhotoImage(file="imgs/rock.png")
        self.paper_img = PhotoImage(file="imgs/paper.png")
        self.scissors_img = PhotoImage(file="imgs/scissor.png")
        self.human_img = PhotoImage(file="imgs/human.png")
        self.computer_img = PhotoImage(file="imgs/robot.png")
        self.win_human_img = PhotoImage(file="imgs/human_biceps.png")
        self.win_computer_img = PhotoImage(file="imgs/robot_biceps.png")

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.visible_frame = "StartPage"
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        self.visible_frame = page_name


class StartPage(Frame, RockPaperScissor):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        RockPaperScissor.__init__(self)
        self.controller = controller
        label = Label(self, text="This is the start page",
                      font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = Button(self, text="Go to Page One", image=self.computer_img,
                         command=lambda: controller.show_frame("PageOne"))
        button2 = Button(self, text="Go to Page Two",
                         command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


class PageOne(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="This is page 1",
                      font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Go to the start page",
                        command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="This is page 2",
                      font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Go to the start page",
                        command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = RockPaperScissor()
    app.mainloop()
