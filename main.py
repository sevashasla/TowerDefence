import sys
from .Game.game import Game

def main():
	mode = sys.argv[1]
	game_ = Game(mode)
	game_.start()

if __name__ == "__main__":
	main()
