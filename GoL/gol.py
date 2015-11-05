from .rules import LifeRule

class GameOfLife:

    def __init__(self, initial=3):
        self.universe = [[LifeRule.ALIVE for x in range(initial)] for x in range(initial)]

    def turn(self):
        self.check_edges()
        for x, row in enumerate(self.universe):
            for y, e in enumerate(row):
                try:
                    adj = self.build_adjacency(x, y)
                except IndexError:
                    # this type of error indicates operation on an edge
                    # all original edges have been previously expanded.
                    pass

    def check_edges(self):
        '''
        Creates new rows / columns if life has expanded to the
        edge of the current universe.
        :return:
        '''

        # add rows to top and bottom if life has reached an edge.
        for y in self.universe[0]:
            if y == LifeRule.ALIVE:
                self._insert_dead_row(0)
                break
        for y in self.universe[len(self.universe)-1]:
            if y == LifeRule.ALIVE:
                self._insert_dead_row(len(self.universe))
                break

        # add rows to left and right
        self._check_side_edge(0)
        self._check_side_edge(len(self.universe[0])-1)

    def _check_side_edge(self, idx):
        for row in self.universe:
            if row[idx] == LifeRule.ALIVE:
                idx = -1 if idx == 0 else idx
                self._insert_dead_column(idx+1)
                return

    def _insert_dead_column(self, idx):
        '''
        Insearts a dead column at the given index.
        '''
        for r in self.universe:
            r.insert(idx, LifeRule.DEAD)

    def _insert_dead_row(self, idx):
        '''
        Inserts a dead row at the given index.
        '''
        self.universe.insert(idx, [LifeRule.DEAD for x in range(len(self.universe[0]))])


    def build_adjacency(self, x, y):
        '''
        Builds out a 3x3 localized board for a specific cell
        :param x: x coord
        :param y: y coord
        :return: returns 3x3 list grid representation
        '''
        if x == 0 or x >= (len(self.universe)-1):
            raise IndexError()
        if y == 0 or y >= (len(self.universe[0])-1):
            raise IndexError()

        return [self.universe[x-1][y-1:3],
                self.universe[x][y-1:3],
                self.universe[x+1][y-1:3]]

    def __repr__(self):
        u = ""
        for r in self.universe:
            u = u + str(r) + "\n"
        return u


