from GoL.gol import GameOfLife
from GoL.rules import LifeRule
from time import sleep

if __name__ == "__main__":

    A = LifeRule.ALIVE
    D = LifeRule.DEAD

    toad = [
        [D for x in range(4)],
        [D, A, A, A],
        [A, A, A, D],
        [D for x in range(4)],
    ]
    gol = GameOfLife(universe=toad)
    while True:
        print(gol)
        gol.turn()
        if gol.heat_death:
            print(gol)
            print(":GAME OVER:\n")
            break
        sleep(2)

