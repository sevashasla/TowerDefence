import sys
from .Game.game import Game

def main():
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> add files to checkpoint 2
	try:
		mode = sys.argv[1]
	except IndexError:
		print(
			"One should choose mode of the game.\n" + \
			"It can be 'graphics' or 'command'.\n" + \
			"To get more visit our github: https://github.com/sevashasla/TowerDefence/"
			)
		return
<<<<<<< HEAD
=======
	mode = sys.argv[1]
>>>>>>> delete it later
=======
>>>>>>> add files to checkpoint 2
	game_ = Game(mode)
	game_.start()

if __name__ == "__main__":
	main()
