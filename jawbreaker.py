import tkinter as tk
import random
SIZE = 16# how many pixels wide/tall each square is
X = 40### X = width, Y = height. Can technically be anything, but higher numbers lag. 
Y = 25### Keeping the product under 400 seems to minimize lag (at least on my potato).
NUM_COLORS = 8#can be 3 through 8
score = 0
class Game(tk.Tk):
    def __init__(self, *args, **kwargs):
        self.alive=True
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=X*SIZE+1, height=Y*SIZE+1+16, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.cellwidth = SIZE
        self.cellheight = SIZE
        self.bind("<Button-1>", self.click)
    def click(self, event):
        if not self.alive:return
        x = event.x // SIZE
        y = event.y // SIZE
        if x >= 0 and x < X and y >= 0 and y < Y:
            click(x,y)
            self.redraw()
            if game_over():self.end()
            

    def end(self):
        self.alive = False
        self.canvas.create_text(SIZE*X//2,SIZE*Y//2, text='GAME OVER',font=('Monaco',X*SIZE//9))
    def redraw(self):
        for column in range(X):
            for row in range(Y):
                x1 = column*self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.canvas.create_rectangle(x1,y1,x2,y2, fill=c__[g[column][row]])
        self.canvas.create_rectangle(0,SIZE*Y,SIZE*X,SIZE*Y+16, fill='#ffffff')
        self.canvas.create_text(1,SIZE*Y+8, text='SCORE:'+str(score),anchor='w',font='Monaco')
def adj(x,y,c,r_=[]):
    if c == 6:return []
    r = []
    for i in [(0,1),(0,-1),(1,0),(-1,0)]:
        x_,y_ = x+i[0],y+i[1]
        if x_ >= 0 and x_ < X and y_ >= 0 and y_ < Y and g[x_][y_] == c and not (x_,y_) in r_:
            r += [(x_,y_)] + adj(x_,y_,c,r_+[(x_,y_)])
    return r
def repack():
    global g
    for i in range(X):
        g[i] = [NUM_COLORS]*(Y-len(g[i]))+g[i]
def k(i):
    return (Y-i[1])
def game_over():
    for x in range(X):
        for y in range(Y):
            if g[x][y] != NUM_COLORS and len(adj(x,y,g[x][y],[(x,y)])) >= 2:return False
    return True
def click(x,y):
    a = [(x,y)]+adj(x,y,g[x][y],[(x,y)])
    if len(a) < 3:return
    global score
    score += 100*((len(a)-2)**2)
    for i in sorted(a,key=k):
        try:
            del g[i[0]][i[1]]
        except:
            print(i,g[i[0]])
    repack()

g = [[int(NUM_COLORS*random.random()) for i in range(Y)] for j in range(X)]

c__ = ["#ff0000","#ffff00","#44ff00","#00ffff","#0044ff","#cc00ff","#ffaaaa","#aaffbb"][:NUM_COLORS]+['#bbbbbb']

game = Game()
game.redraw()
game.mainloop()
