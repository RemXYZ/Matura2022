import keyboard as keyb
# pip install keyboard
from colorama import Fore, Back, Style, init
# pip install colorama
init()
import os
import time
import msvcrt

""" 
pip install pyinstaller
to install ability .exe file

pyinstaller main.py
to create .exe file
run it in dist dirictory
"""
### Development started 19.03.22 ###

# print(Back.WHITE + Fore.BLACK + "Hi")
# print(Style.RESET_ALL)

####### GLOBAL VARIABLE ##########

# in lines



# document
# class Window():
#     def __init__(self):





class Window():
    def __init__(self):
        self.win_width = 40
        self.win_height = 20
        self.render_time = 0.08

        ### frame PART ###
        self.text_position = {
            "y": ["top", "bottom", "center"],
            "x": ["left", "right", "center"]
        }
        self.align_y = {
                "x": "left",
                "y": "top"
            }
        self.print_space = []


    def get_render_time(self):
        return self.render_time


    def resize(self):
        os.system(f'mode con: cols={self.win_width} lines={self.win_height}')


    def cons_prepare(self, clear = 1, align:dict = None):
        if align is None:
            align = {
                "x": "left",
                "y": "top"
            }

        self.align_y = align

        if clear == 1:
            self.print_space.clear()


    def prt(self, text, align:dict = None, end = "\n"):
        if align is None:
            align = {"x": "left"}

        spl_t = str(text).split("\n")
        # print({text})
        if end == "" and len(self.print_space) != 0:
            self.print_space[len(self.print_space)-1]["text"] = self.print_space[len(self.print_space)-1]["text"] + str(text)
            return


        for t in spl_t:
            self.print_space.append({
                "text": str(t) + str(end),
                "align": align
            })



    def set_position(self, i):
        print(self.print_space)
        #if self.print_space[i]["align"]:



    def print_frame(self):
        #clear_console()
        to_print = self.print_space
        text_len = len(to_print)
        text_i = 0
        start_point = 0
        win_height = self.win_height - 1
        win_width = self.win_width
        paragraph_align = self.align_y
        ### center
        if paragraph_align["y"] == self.text_position["y"][2]:
            start_point = (win_height - text_len) // 2
        ### bottom
        if paragraph_align["y"] == self.text_position["y"][1]:
            start_point = win_height - text_len

        #print(to_print)

        # start, end
        # start_endl = ""
        # end_endl = ""
        # end_i = win_height - start_point - text_len + 1
        # for i in range(start_point-1):
        #     start_endl = start_endl + "\n"
        # for i in range(end_i):
        #     end_endl = end_endl + "\n"

        #print({start_endl}, {end_endl}, start_point, text_len, win_height, end_i)

        # for i in range(win_height):
        #     if start_endl != "":
        #         print(start_endl)
        #         start_endl = ""
        #
        #     if i == start_point and text_i < text_len:
        #         if paragraph_align["x"] == self.text_position["y"][2]:
        #             t_space = (win_width - len(to_print[text_i]["text"])) // 2
        #             for sp in range(t_space):
        #                 print(" ", end="")
        #         print(to_print[text_i]["text"], end="")
        #         text_i += 1
        #         start_point += 1
        #
        #
        #
        #     if i == end_i and end_endl != "" :
        #         print(end_endl)
        #         end_endl = ""
        #


        for i in range(win_height):
            if i == start_point and text_i < text_len:
                if paragraph_align["x"] == self.text_position["y"][2]:
                    t_space = (win_width - len(to_print[text_i]["text"])) // 2
                    for sp in range(t_space):
                        print(" ", end="")
                print(to_print[text_i]["text"], end="")
                text_i += 1
                start_point += 1
            else:
                print("")



WIN = Window()
#
# #WIN.cons_prepare(align={"x":"center", "y":"center"})
# WIN.cons_prepare()
# WIN.prt("Hello\nKek\nHeh")
# WIN.prt("Wow")
# WIN.print_frame()
# exit()

####### END OF GLOBALS ###########


def close_prog():
    if keyb.is_pressed("esc"):
        os.system("cls")
        return 1
    return 0


def clear_console():
    os.system("cls")


#Yes, this is a workaround for which I am ashamed
def clear_cmd_input(reset_pos = None):
    keyb.send("esc")
    if reset_pos == 1:
        keyb.press("enter")
        input()
        keyb.release("enter")


def some_key_pressed():
    for i in range(32, 127):
        key = chr(i)
        if keyb.is_pressed(key):
            return chr(i)
    return 0




class Arrows_keys:

    def __init__(self):
        self.lol = 0


    def up(self):
        if keyb.is_pressed("up"):
            clear_cmd_input(1)
            return 1
        return 0


    def down(self):
        if keyb.is_pressed("down"):
            clear_cmd_input(1)
            return 1
        return 0



class Hello_menu():
    def __init__(self):
        self.buttons = ["Start new game", "Continue game"]
        self.point = 0
        self.menu_on = 1


    def get_sts(self):
        return self.menu_on


    def select(self, arrow_key):
        if arrow_key == "up":
            self.point -= 1
        if arrow_key == "down":
            self.point += 1

        # check for selector
        if self.point < 0:
            self.point = 0
        if self.point >= len(self.buttons) - 1:
            self.point = len(self.buttons) - 1


    def show(self):
        WIN.cons_prepare()

        hello_text = "Cześć, miło mi Cię widzić w mojej grze \n'Podrzóż maturalna'\nAby wyjść naciśnij 'Esc'\nWybieraj strzełkami i naciśnij Enter"
        WIN.prt(hello_text)
        WIN.prt("")

        for i, v in enumerate(self.buttons):
            highlighter = ""
            if self.point == i:
                highlighter = Fore.RED + Back.WHITE

            WIN.prt(" " + highlighter + v, end="")
            WIN.prt(Style.RESET_ALL)

        WIN.print_frame()


    def on_select(self):
        if keyb.is_pressed("enter"):
            self.menu_on = 0
            return self.point
        return None




class Training_menu():
    def __init__(self):
        self.training_menu_on = 0


    def start_training_menu(self):
        self.training_menu_on = 1


    def get_sts(self):
        return self.training_menu_on


    def show(self):
        #clear_console()
        WIN.cons_prepare()
        WIN.prt("Use 'w a s d' to move\nPress E to take key\nPress Enter to continue\nPress Esc to exit")



class Game_map():
    def __init__(self):
        super().__init__()
        self.player_crd = [1, 1]
        self.symb = {
            "wall": "#",
            "space": " ",
            "keys": [1,2,3,4,5,6,7,8,9],
            "player_symb": "@"
        }
        # self.wall = "#"
        # self.space = " "
        # self.keys = [1,2,3,4,5,6,7,8,9]

        wl = self.symb["wall"]
        sp = self.symb["space"]
        k = self.symb["keys"]
        self.map = [
            [wl, wl, wl, wl, wl, wl, wl, wl, wl],
            [wl, sp, sp, sp, sp, sp, sp, sp, wl],
            [wl, sp, sp, sp, sp, sp, sp, sp, wl],
            [wl, sp, sp, sp, wl, wl, wl, sp, wl],
            [wl, sp, sp, sp, wl, k[0], wl, sp, wl],
            [wl, sp, sp, sp, sp, sp, sp, sp, wl],
            [wl, wl, wl, wl, wl, wl, wl, wl, wl]

        ]


    # create
    # def cr(self):


    def get_symb(self):
        return self.symb


    def get_map(self):
        return self.map


    def get_map_size(self):
        return [len(self.map)-1, len(self.map[0])-1]


    def set_map(self, new_map):
        self.map = new_map


    def set_player_crd(self, crd):
        self.player_crd = crd


    def draw(self, my_map: dict = 0):
        # if my_map == 0 or len(my_map) == 0:
        my_map = self.map
        u_crd = self.player_crd
        p_sb = self.symb["player_symb"]

        for y in range(len(my_map)):
            for x in range(len(my_map[y])):
                if [x, y] == u_crd:
                    WIN.prt(p_sb, end="")
                    continue
                WIN.prt(my_map[y][x], end="")
            WIN.prt("")




class Player():
    def __init__(self):
        self.keys = []


    def set_keys(self, key):
        # for i in range(len(self.keys) - 1):
        #     if self.keys[i] != key:
        self.keys.append(key)


    def print_keys(self):
        l_keys = len(self.keys)
        text = ["Masz", "klucz", "kluczy"]
        t_keys = text[2]
        if l_keys % 10 == 1:
            t_keys = text[1]
        WIN.prt(text[0]+ " " + str(self.keys) + " " + t_keys)



class Player_control():
    def __init__(self):
        super().__init__()
        self.go_up = "w"
        self.go_left = "d"
        self.go_down = "s"
        self.go_right = "a"

        # [x, y]
        self.player_crd = [1, 1]

        self.map_range = []
        self.world_map = []

        self.map_symb = {}


    def set_user_crd(self, crd:list):
        self.set_map_range = crd


    def set_map_range(self, size):
        self.map_range = size


    def set_map(self, map:list):
        self.world_map = map


    def get_map(self):
        return self.world_map

    def set_map_symb(self, symb):
        self.map_symb = symb


    def collision(self, crd:list):
        map_crd = self.world_map
        #print(crd, len(map_crd))
        wl = self.map_symb["wall"]

        ### OUT OF RANGE COLLISION ###
        if crd[1] >= len(map_crd):
            return 1
        if crd[0] >= len(map_crd[crd[1]]):
            return 1

        #print(map_crd[crd[1]][crd[0]], map_crd[crd[1]])

        ### WALL COLISION ###
        if map_crd[crd[1]][crd[0]] == wl:
            return 1

        return 0


    def move(self):

        p_crd = self.player_crd.copy()

        if keyb.is_pressed(self.go_up):
            p_crd[1] -= 1
        if keyb.is_pressed(self.go_left):
            p_crd[0] += 1
        if keyb.is_pressed(self.go_down):
            p_crd[1] += 1
        if keyb.is_pressed(self.go_right):
            p_crd[0] -= 1

        if p_crd[0] <= 0:
            p_crd[0] = 0
        if p_crd[1] <= 0:
            p_crd[1] = 0

        if self.collision(p_crd) == 1:
            return self.player_crd

        # print("hi")
        self.player_crd = p_crd
        return self.player_crd


    def interaction(self):
        map_crd = self.world_map
        crd = self.player_crd

        ### key interaction ###
        g_keys = self.map_symb["keys"]
        sp = self.map_symb["space"]

        take = keyb.is_pressed("e")

        for i in range(len(g_keys)):
            if map_crd[crd[1]][crd[0]] == g_keys[i]:
                self.intr_msg = "You found key '" + str(g_keys[i]) + "' press [e] To take it"
                if take:
                    map_crd[crd[1]][crd[0]] = sp
                    return g_keys[i]
                return "msg"
        return 0


    def print_intr_msg(self):
        WIN.prt(self.intr_msg)




# if __name__ == '__main__':

arrows = Arrows_keys()
h_menu = Hello_menu()
tr_menu = Training_menu()

g_map = Game_map()
p_ctrl = Player_control()
pl = Player()

WIN.resize()

# world render
while 1:

    ###### IMPORTANT PART ######
    time.sleep(WIN.get_render_time())
    if close_prog():
        break

    # my_key = some_key_pressed()
    # if my_key != 0:
    #     clear_cmd_input()

    ######## MENU #########
    menu_on = h_menu.get_sts()

    if menu_on == 1:
        aup = arrows.up()
        adown = arrows.down()

        if aup == 1:
            h_menu.select("up")
        if adown == 1:
            h_menu.select("down")

        h_menu.show()

        if h_menu.on_select() == 0:
            tr_menu.start_training_menu()
        # continue


    #### TRANINING MENU #####
    if tr_menu.get_sts() == 1:
        tr_menu.show()

        my_map = g_map.get_map()
        my_map_size = g_map.get_map_size()
        g_symb = g_map.get_symb()


        p_ctrl.set_map_range(my_map_size)
        p_ctrl.set_map_symb(g_symb)
        p_ctrl.set_map(my_map)

        p_crd = p_ctrl.move()
        g_map.set_player_crd(p_crd)


        pl.print_keys()

        g_map.draw()

        p_intr = p_ctrl.interaction()
        if p_intr == "msg":
            p_ctrl.print_intr_msg()
        if p_intr != 0 and p_intr != "msg":
            pl.set_keys(p_intr)
            g_map.set_map(p_ctrl.get_map())


        WIN.print_frame()
        # continue











#input()
# to clear all pressed buttons
keyb.press("esc")
#clear_console()

#keyb.press('enter')
#n = input()
#keyb.press('enter')
