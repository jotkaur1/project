from tkinter import *
from tkinter import messagebox
from timeit import default_timer as timer 
import random

root=Tk()
root.geometry("500x500")
root.configure(bg="black")

img=PhotoImage(file="C:\\Users\\User1\\Downloads\\download.png")
img_label=Label(root,image=img)
img_label.place(x=100,y=300)


window=Tk()
window.geometry("550x500")
window.configure(bg="darkgrey")
window.withdraw()


hs_file=open("hscore.txt","r+")
x=0


def game():
    global x
    if x==0:
        root.withdraw()
        x=x+1
    window.deiconify()
    def check_result():
        j=error=0
        answer=entry.get("1.0","end-1c")
        end=timer()
        time_taken=end-start
        #len diff
        if len(words[word])>=len(answer):
            error=len(words[word])-len(answer)
            for i in answer:
                if i==words[word][j]:
                    pass
                else:
                    error=error+1
                j+=1
        elif len(words[word])<=len(answer):
            error=len(answer)-len(words[word])
            for i in words[words]:
                if i==answer[j]:
                    pass
                else:
                    error+=1
                j+=1
        wpm=len(answer)/5
        wpm=wpm-error
        wpm=int(wpm/(time_taken/60))
        hs_file.seek(0)
        line=int(hs_file.readline())
        if wpm>line:
            hs_file.seek(0)
            hs_file.write(str(wpm))
            result="Congratulations!! Your new highscore is: "+str(wpm)+" WPM"
            messagebox.showinfo("Score",result)
        else:
            result="Your Score is: "+str(wpm)+" WPM\nBetter Luck next time!"
            messagebox.showinfo("Score",result)

    def finish():
        hs_file.close()
        window.destroy()
        root.destroy()

    #words =['I love coding.','python is simple programming language','C is a procedural computer programming language.']
    #get a random word
    words = ["An ever-growing number of complex and rigid rules plus hard-to-cope-with regulations are now being legislated from state to state. Key federal regulations were formulated by the FDA, FTC, and the CPSC. Each of these federal agencies serves a specific mission.", "Laws sponsored by the Office of the Fair Debt Collection Practices prevent an agency from purposefully harassing clients in serious debt. The Fair Packaging and Labeling Act makes certain that protection from misleading packaging of goods is guaranteed to each buyer of goods carried in small shops as well as in large supermarkets.", "Two common terms used to describe a salesperson are 'Farmer' and 'Hunter'. The reality is that most professional salespeople have a little of both. A hunter is often associated with aggressive personalities who use aggressive sales technique.", "A late 20th century trend in typing, primarily used with devices with small keyboards (such as PDAs and Smartphones), is thumbing or thumb typing. This can be accomplished using one or both thumbs.", "One study examining 30 subjects, of varying different styles and expertise, has found minimal difference in typing speed between touch typists and self-taught hybrid typists. According to the study, 'The number of fingers does not determine typing speed... People using self-taught typing strategies were found to be as fast as trained typists... instead of the number of fingers, there are other factors that predict typing speed.", "Closed captions were created for deaf or hard of hearing individuals to assist in comprehension. They can also be used as a tool by those learning to read, learning to speak a non-native language, or in an environment where the audio is difficult to hear or is intentionally muted.", "A freelancer or freelance worker, is a term commonly used for a person who is self-employed and is not necessarily committed to a particular employer long-term. Freelance workers are sometimes represented by a company or a temporary agency that resells freelance labor to clients; others work independently or use professional associations or websites to get work."]
    word =random.randint(0, (len(words)-1))

    x2=Label(window,text=words[word],bg="black",fg="white",height=7,width=47,font="times 15",wraplength=500)
    x2.place(x=15,y=10)

    x3=Button(window,text="SUBMIT",bg="lightgreen",font="times 20",command=check_result)
    x3.place(x=220,y=350)
    
    entry=Text(window,bg="skyblue")
    entry.place(x=100,y=180,height=150,width=350)

    b2=Button(window,text="DONE",bg="#fcc003",font="times 13",width=12,command=finish)
    b2.place(x=155,y=420)

    b3=Button(window,text="Another one!",bg="#fcc003",font="times 13",width=12,command=game)
    b3.place(x=300,y=420)

    start=timer()

    window.mainloop()


x1=Label(root,text="Let's test your Typing Speed!",bg="black",fg="Yellow",font="times 25")
x1.place(x=80,y=50)

b1=Button(root,text="GO!",bg="lightgreen",font="times 20",width=10,command=game)
b1.place(x=160,y=120)

hs_text=Label(root,text="Highscore",width=12,bg="yellow",font="times 20")
hs_text.place(x=140,y=200)

hs=int(hs_file.readline())
hs_val=Label(root,text=str(hs)+" WPM",width=12,fg="white",bg="black",font="times 16")
hs_val.place(x=160,y=250)

root.mainloop()





