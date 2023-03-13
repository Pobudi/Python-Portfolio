import turtle
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

def spin(mode, setup):
    final_list = []
    if mode == "human":
        for i in range(8):
            for j in range(8):
                final_list.append(setup[56+i-8*j])

    return final_list


f = open("ruchy.txt", "r+")
lines = f.readlines()
pawns_setup = lines[0].split(" ")[:-1]
pawns_setup = spin("human", pawns_setup)
pawn_cords = dict(zip(cords, pawns_setup))


f.write("1")


