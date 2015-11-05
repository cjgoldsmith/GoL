from GoL.gol import GameOfLife
from time import sleep

if __name__ == "__main__":

    gol = GameOfLife()
    while True:
        sleep(4)
        gol.turn()
        print(gol)

