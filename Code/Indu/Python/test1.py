# # maze = ['#', ' ', '#', '#', '#'], ['#', ' ', '#', ' ', '#'], ['#', ' ', '#', ' ', '#'], ['#', ' ', ' ', ' ', '#'], ['#', ' ', '#', '#', '#']]
# # for i in maze:
# #      print("".join(i))
# import string
# import colorama
# from colorama import Fore, Back, Style
# colorama.init()
# print(Fore.black + Back.LIGHTBLACK_EX,'rgdfv')
# # with open('maze.txt', 'r', encoding='utf-8') as f:
# #     contents = f.read()  # read the contents
# #     print(type(contents))
# # #maze = contents.replace('a',u"\u1F33x")
# # maze = contents.replace('a','🌳')
# # maze = maze.replace('8','🌳')
# # print(maze)
import colorama
from colorama import init
init()
from colorama import Fore, Back, Style

print (Fore.RED + "My Text is Red")