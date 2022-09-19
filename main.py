from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#3EC70B"
YELLOW = "#FFDEB4"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="0:00")
    heading.config(text="TIMER")
    check_marks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps % 8==0:
        count_down(long_break_sec)
        heading.config(text="LONG BREAK",font=(FONT_NAME,50,"bold"),fg=(RED),bg=(YELLOW))

    elif reps % 2 == 0:
        count_down(short_break_sec)
        heading.config(text="SHORT BREAK",font=(FONT_NAME,50,"bold"),fg=(PINK),bg=(YELLOW))

    else:
        count_down(work_sec)
        heading.config(text="WORK",font=(FONT_NAME,50,"bold"),fg=(GREEN),bg=(YELLOW))



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps , wor
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✔"
        check_marks.config(text=marks)




# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title('Pamadore by Ranit')
window.config(padx=100,pady=200,bg=YELLOW)



heading=Label(text="TIMER",font=(FONT_NAME,50,"bold"),fg=(GREEN),bg=(YELLOW))
heading.grid(column=2,row=0)

canvas = Canvas(width=204, height= 224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(103,112,image=tomato_img)
timer_text=canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)


start=Button(text="Start",width=10,activebackground=GREEN,command=start_timer)
start.grid(column=1,row=3)

reset=Button(text="reset",width=10,activebackground=RED,command=reset_timer)
reset.grid(column=3,row=3)


check_marks = Label(text="✔", font=(FONT_NAME, 20, "bold"), fg=(GREEN), bg=(YELLOW))
check_marks.grid(column=2, row=4)


window.mainloop()