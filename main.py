import multiprocessing

from gui import GUI
from game import Game

def game_loop(text_queue):
    while True:
        game = Game(text_queue)

if __name__ == '__main__':
	text_queue = multiprocessing.Queue()

	game_thread = multiprocessing.Process(target=game_loop, args=(text_queue,))

	gui = GUI(text_queue)
	game_thread.start()
	gui.startGUI()