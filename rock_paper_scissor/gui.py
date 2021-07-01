from tkinter import *

# Main window
root = Tk()
root.title("Rock Paper Scissors")
root.configure(background="#202020")

# Images
rock_img = PhotoImage(file="imgs/rock.png")
paper_img = PhotoImage(file="imgs/paper.png")
scissors_img = PhotoImage(file="imgs/scissor.png")
human_img = PhotoImage(file="imgs/human.png")
computer_img = PhotoImage(file="imgs/robot.png")
win_human_img = PhotoImage(file="imgs/human_biceps.png")
win_computer_img = PhotoImage(file="imgs/robot_biceps.png")

# Scores
computer_score = 0
player_score = 0
player_score_display = Label(
    root, text=f"You: {player_score}", font=100, bg="#202020", fg="#828282").grid(row=1, column=1)
computer_score_display = Label(
    root, text=f"Computer: {computer_score}", font=100, bg="#202020", fg="#828282").grid(row=3, column=3)

# Buttons
rock_btn = Button(root, image=rock_img, bg="#828282",
                  height=200, width=200).grid(row=2, column=1)
paper_btn = Button(root, image=paper_img, bg="#828282",
                   height=200, width=200).grid(row=2, column=2)
scissors_btn = Button(root, image=scissors_img, bg="#828282",
                      height=200, width=200).grid(row=2, column=3)

# Main loop
root.mainloop()
