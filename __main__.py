#  _________  ________  ___       __   _______   ________  ________  _______   ________ _______   ________   ________  _______      
# |\___   ___\\   __  \|\  \     |\  \|\  ___ \ |\   __  \|\   ___ \|\  ___ \ |\  _____\\  ___ \ |\   ___  \|\   ____\|\  ___ \     
# \|___ \  \_\ \  \|\  \ \  \    \ \  \ \   __/|\ \  \|\  \ \  \_|\ \ \   __/|\ \  \__/\ \   __/|\ \  \\ \  \ \  \___|\ \   __/|    
#      \ \  \ \ \  \\\  \ \  \  __\ \  \ \  \_|/_\ \   _  _\ \  \ \\ \ \  \_|/_\ \   __\\ \  \_|/_\ \  \\ \  \ \  \    \ \  \_|/__  
#       \ \  \ \ \  \\\  \ \  \|\__\_\  \ \  \_|\ \ \  \\  \\ \  \_\\ \ \  \_|\ \ \  \_| \ \  \_|\ \ \  \\ \  \ \  \____\ \  \_|\ \ 
#        \ \__\ \ \_______\ \____________\ \_______\ \__\\ _\\ \_______\ \_______\ \__\   \ \_______\ \__\\ \__\ \_______\ \_______\
#         \|__|  \|_______|\|____________|\|_______|\|__|\|__|\|_______|\|_______|\|__|    \|_______|\|__| \|__|\|_______|\|_______|


from argparse import ArgumentParser
from .Game.game import Game
from .Game.main_menu import MainMenu

def main():
	try:
		parser = ArgumentParser("Tower Defence")
		parser.add_argument("--console", help="this type is good for debug", action="store_true")
		args = parser.parse_args()
	except IndexError:
		print(
			"One should choose mode of the game.\n" + \
			"It can be 'graphics' or 'command'.\n" + \
			"To get more information visit our github: https://github.com/sevashasla/TowerDefence/"
			)
		return

	if(args.console):
		menu_ = MainMenu("console")
	else:
		menu_ = MainMenu("graphics")

	menu_.start()

if __name__ == "__main__":
	main()
