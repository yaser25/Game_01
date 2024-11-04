import curses
import random
import time
mi = '🚀'
E = '😈'
jon = '🍎'
star = '⭐'
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.curs_set(False)
stdscr.keypad(True)
stdscr.nodelay(True)

maxl = curses.LINES - 1
maxc = curses.COLS - 1
word = []
player_l = player_c = 0  
food = []
enemy = []
score = 0

def random_ge():  # Generate random coordinates for food
    a = random.randint(0, maxl - 1)
    b = random.randint(0, maxc - 1)
    while word[a][b] != ' ':
        a = random.randint(0, maxl - 1)
        b = random.randint(0, maxc - 1)
    return a, b

def init():
    global player_l, player_c
    for i in range(maxl):
        word.append([])
        for j in range(maxc):
            word[i].append(" " if random.random() > 0.1 else '.')
    for _ in range(10):  # Generate 10 food items
        fl, fc = random_ge()
        fa = random.randint(1000, 10000)  # Food age (not used in this version)
        food.append((fl, fc, fa))
        
    for _ in range(3):  # Generate 3 enemy items 00ps
        el, ec = random_ge()
        enemy.append((el, ec))
    player_l, player_c = random_ge()             

def in_range(a, min_val, max_val):
    return max(min_val, min(a, max_val))

def check_food():  # Check for food collection
    global score
    for i in range(len(food)):
        fl, fc, fa = food[i]
        if fl == player_l and fc == player_c:
            score += 10
            newfl, newfc = random_ge()
            newfa = random.randint(1000, 10000)
            food[i] = (newfl, newfc, newfa)
def bandari_enemy():
    global playing 
    for i in range(len(enemy)):
        l, c = enemy[i]
        if random.random() > 0.8:
            if l > player_l:
                l -= 1
        if random.random()>0.7:
                
            if c > player_c:
                c -= 1
        if random.random() > 0.6:
            if l < player_l:
                l += 1
        if random.random() > 0.8:
            if c < player_c:
                c += 1
                #l += random.choice([0, 1, -1])
                #c += random.choice([0,1,-1])
                l = in_range(l,0,maxl -1)
                c = in_range(c,0,maxc -1)
                enemy[i] = (l ,c)
            if l == player_l and c == player_c:
                stdscr.addstr(maxl//2, maxc//2,"RIDI DADASH :)")# only for fun :)
                stdscr.refresh()
                time.sleep(3)
                playing = False
def move(c):
    global player_l, player_c
    if c == "w" and player_l > 0 and word[player_l - 1][player_c] != ".":
        player_l -= 1
    elif c == "s" and player_l < maxl - 1 and word[player_l + 1][player_c] != '.':
        player_l += 1
    elif c == "a" and player_c > 0 and word[player_l][player_c - 1] != '.':
        player_c -= 1
    elif c == "d" and player_c < maxc - 1 and word[player_l][player_c + 1] != '.':
        player_c += 1
    player_l = in_range(player_l, 0, maxl - 1)
    player_c = in_range(player_c, 0, maxc - 1)

def draw():
   # stdscr.clear()  # Clear the screen before drawing
    for i in range(maxl):
        for j in range(maxc):
            stdscr.addch(i, j, word[i][j])
    stdscr.addstr(1, 1, f'SCORE: {score}')       
    for f in food:  # Show food
        fl, fc, fa = f
        stdscr.addch(fl, fc, '🍎')
        
    for e in enemy:
        l, c,  = e
        stdscr.addch(l, c, E)
         
    stdscr.addch(player_l, player_c, mi)  # Show player        
    stdscr.refresh()

init()
draw()  # Initial draw

playing = True
while playing:
    try:
        c = stdscr.getkey()
    except:
        c = ''
    if c in "wasd":
        move(c)
        check_food()  # Check if food is collected
        bandari_enemy()
        time.sleep(0.03)
        
    elif c == 'q':
        playing = False
    draw()
    

stdscr.clear()
stdscr.addstr(maxl//2,maxc//2-5,"Merci ahhh")# off run
stdscr.refresh()# off run     
time.sleep(1)
stdscr.clear()
stdscr.refresh()


curses.endwin()  # End the curses mode