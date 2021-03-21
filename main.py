import sys
from Game import game

def main():
	mode = sys.argv[1]
	game_ = game.Game(mode)
	game_.start()

if __name__ == "__main__":
	main()
