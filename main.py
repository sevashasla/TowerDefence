import sys
from .Game.game import Game

def main():
	try:
		mode = sys.argv[1]
	except IndexError:
		print(
			"One should choose mode of the game.\n" + \
			"It can be 'graphics' or 'command'.\n" + \
			"To get more visit our github: https://github.com/sevashasla/TowerDefence/"
			)
		return
	game_ = Game(mode)
	game_.start()

if __name__ == "__main__":
	main()
