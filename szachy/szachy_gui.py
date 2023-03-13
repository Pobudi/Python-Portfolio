import turtle


# cordinates of all tiles
cords = [(-238, 250), (-166, 250), (-94, 250), (-22, 250), (50, 250), (122, 250), (194, 250), 
(266, 250), (-238, 178), (-166, 178), (-94, 178), (-22, 178), (50, 178), (122, 178), 
(194, 178), (266, 178), (-238, 106), (-166, 106), (-94, 106), (-22, 106), (50, 106), 
(122, 106), (194, 106), (266, 106), (-238, 34), (-166, 34), (-94, 34), (-22, 34), 
(50, 34), (122, 34), (194, 34), (266, 34), (-238, -38), (-166, -38), (-94, -38), 
(-22, -38), (50, -38), (122, -38), (194, -38), (266, -38), (-238, -110), (-166, -110), 
(-94, -110), (-22, -110), (50, -110), (122, -110), (194, -110), (266, -110), (-238, -182), 
(-166, -182), (-94, -182), (-22, -182), (50, -182), (122, -182), (194, -182), (266, -182), 
(-238, -254), (-166, -254), (-94, -254), (-22, -254), (50, -254), (122, -254), (194, -254), 
(266, -254)]


# read board setup from file, and place pawns
def read_setup():
    global pawn_cords
    with open("ruchy.txt", "r") as f:
            lines = f.readlines()
    pawns_setup = lines[0].split(" ")[:-1]

    # spin board so that it is easier to read and create dict
    pawns_setup = spin("human", pawns_setup)
    pawn_cords = dict(zip(cords, pawns_setup))

    # place pawns on board and add pawns belonging to player to a list
    player_pawns = []
    for pawn in pawn_cords.keys():
        if int(pawn_cords[pawn]) != 12:
            diego = turtle.Turtle()
            diego.penup()
            diego.shape(d_pawns[int(pawn_cords[pawn])])
            diego.goto(pawn)
            if int(pawn_cords[pawn]) < 6:
                player_pawns.append(diego)
    return player_pawns

# function for spinnig the board
def spin(mode, setup):
    final_list = []
    if mode == "human":
        for i in range(8):
            for j in range(8):
                final_list.append(setup[56+i-8*j])

    else:
        for i in reversed(range(8)):
            for j in range(8):
                final_list.append(setup[i+j*8])
                
    return final_list

# function is trggered when player chooses pawn which will be moved
def pawn_clicked(x, y):
    global pawn_to_move
    global player_pawns
    global screen

    pawn_to_move = None
    min_dist = 1000

    for pawn in player_pawns:
        if pawn.distance(x, y) < min_dist:
            min_dist = pawn.distance(x, y)
            pawn_to_move = pawn

    screen.onclick(place_clicked)

    # clear place from where pawn moved
    pawn_cords[(pawn_to_move.xcor(), pawn_to_move.ycor())] = 12

# function triggered after choosing pawn and clicking on destination place
def place_clicked(x, y):
    global pawn_to_move
    global pawn_cords

    min_dist = 1000
    spot = None

    # placing a turtle in place where user clicked to compare distances
    dummy = turtle.Turtle()
    dummy.hideturtle()
    dummy.penup()
    dummy.goto(x, y)

    for cord in pawn_cords:
        if dummy.distance(cord) < min_dist:
            min_dist = dummy.distance(cord)
            spot = cord
    
    # move chosen pawn to destination
    pawn_to_move.goto(spot)
    
    for i, seek in enumerate(d_pawns):
        if pawn_to_move.shape() == seek:
            pawn_cords[spot] = i

    list_to_send = []        
    for cord in pawn_cords.keys():
        list_to_send.append(pawn_cords[cord])

    list_to_send = spin("bot", list_to_send)
    string_to_send = ""

    for i in list_to_send:
        string_to_send += f"{i} " 
    
    with open("ruchy.txt", "w") as f:
        f.write(string_to_send)

    screen.onclick(None)
    screen.update()

    
screen = turtle.Screen()
screen.tracer(False)
screen.setup(width=602, height=649)
screen.bgpic("./szachownica.resized.png")
screen.update()

w_pawn_img = "w_pawn.gif"
screen.addshape(w_pawn_img)

w_rook_img = "w_rook.resized.gif"
screen.addshape(w_rook_img)

w_knight_img = "w_knight.resized.gif"
screen.addshape(w_knight_img)

w_bishop_img = "w_bishop.resized.gif"
screen.addshape(w_bishop_img)

w_queen_img = "w_queen.resized.gif"
screen.addshape(w_queen_img)

w_king_img = "w_king.resized.gif"
screen.addshape(w_king_img)

b_pawn_img = "b_pawn.gif"
screen.addshape(b_pawn_img)

b_rook_img = "b_rook.resized.gif"
screen.addshape(b_rook_img)

b_knight_img = "b_knight.resized.gif"
screen.addshape(b_knight_img)

b_bishop_img = "b_bishop.resized.gif"
screen.addshape(b_bishop_img)

b_queen_img = "b_queen.resized.gif"
screen.addshape(b_queen_img)

b_king_img = "b_king.resized.gif"
screen.addshape(b_king_img)

d_pawns = [b_king_img, b_queen_img, b_rook_img, b_bishop_img, b_knight_img, b_pawn_img, w_king_img, 
           w_queen_img, w_rook_img, w_bishop_img, w_knight_img, w_pawn_img]




screen.onclick(pawn_clicked)
player_pawns = read_setup()  
screen.update()
screen.mainloop()

