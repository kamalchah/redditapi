import requests
import praw
import tkinter as tk
import RedditPraw as rapi

print("======================================================")
subreddits = [
    ("CarletonU",0),
    ("Python",1),
    ("AskReddit",2),
    ("Soccer",3),
    ("worldnews",4)
]

sortby = [
    ("New",0),
    ("Hot",1),
    ("Top",2),
]

root = tk.Tk()
root.minsize(210, 100) 
y = tk.IntVar()
v = tk.IntVar()
v.set(0)  # initializing the choice
y.set(0)

def ShowChoice():
    # print(v.get())
    print()

def ShowChoice2():
    print()
    # print(y.get())
def showSubReds():
    sub = v.get()
    sortByThis = y.get()
    lim=int(entry1.get())
    rapi.redditAPI(subreddits[sub][0],sortby[sortByThis][0],lim)

tk.Label(root, 
         text="Pick a subreddit",
         justify = tk.LEFT,
         padx = 20).pack()

for val, subr in enumerate(subreddits):
    tk.Radiobutton(root, 
                  text=subr[0],
                  padx = 0, 
                  variable=v, 
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)

tk.Label(root, 
         text="Sort by:",
         justify = tk.LEFT,
         padx = 40).pack()

for sortval, sort in enumerate(sortby):
    tk.Radiobutton(root, 
                  text=sort[0],
                  padx = 0, 
                  variable=y, 
                  command=ShowChoice2,
                  value=sortval).pack(anchor=tk.W)

root.title('SubS')#SubSearch

canvas1 = tk.Canvas(root, width = 200, height = 75)
canvas1.pack()

label1 = tk.Label(root,text="# of posts:")
canvas1.create_window(100,20,window=label1)
entry1 = tk.Entry(root) 
canvas1.create_window(100, 50, window=entry1)
entry1.insert(5,"5")

btn1 = tk.Button(root, text="Search",command=lambda:showSubReds())
btn1.pack()

root.mainloop()
