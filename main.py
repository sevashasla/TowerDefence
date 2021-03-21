import sys
from Game import Game

def main():
	mode = sys.argv[1]
	game = Game.Game(mode)
	game.start()

if __name__ == "__main__":
	main()
