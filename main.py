from GoL.gol import GameOfLife
from time import sleep

if __name__ == "__main__":

    gol = GameOfLife()
    while True:
        print(gol)
        gol.turn()
        if gol.heat_death:
            print(gol)
            print(":GAME OVER:\n")
            break
        sleep(2)

