from .rules import LifeRule

class ConfigException(Exception):
    pass

class GameOfLife:

    TOP = "top"
    BOTTOM = "bottom"
    TB = [TOP, BOTTOM, ]

    LEFT = "left"
    RIGHT = "right"
    LR = [LEFT, RIGHT, ]

    def __init__(self, initial=3, universe=None):

        if not (initial or universe):
            raise ConfigException("GameOfLife requires either and initial gride size or a initial grid object.")
        self.universe = universe

        if(not self.universe):
            self.universe = [[LifeRule.ALIVE for x in range(initial)] for x in range(initial)]

        if len(self.universe) == 0 or len(self.universe) != len(self.universe[0]):
            raise ConfigException("Supplied universe grid is either zero length or not a perfect square.")

        self.width = len(self.universe[0])
        self.height = len(self.universe)

    def turn(self):
        self._check_edges()
        for x, row in enumerate(self.universe):
            for y, e in enumerate(row):
                try:
                    adj = self._build_adjacency(x, y)
                    #for rule in LifeRule.plugins:
                        #self._set_grid(rule(adj))
                except IndexError:
                    # this type of error indicates operation on an edge
                    # all original edges have been previously expanded.
                    pass

    def _check_edges(self):
        '''
        Creates new rows / columns if life has expanded to the
        edge of the current universe.
        :return:
        '''

        # add rows to top / bottom
        self._check_tb_edge(self.TOP)
        self._check_tb_edge(self.BOTTOM)

        # add rows to left and right
        self._check_side_edge(self.LEFT)
        self._check_side_edge(self.RIGHT)

    def _check_tb_edge(self, idx):
        """
        Check top / bottom edges
        :param idx: row index value
        """
        if idx not in self.TB:
            raise KeyError('check TB edge expects top or bottom flag value')

        ridx = 0 if idx == self.TOP else self.height -1

        for y in self.universe[ridx]:
            if y == LifeRule.ALIVE:
                self._insert_dead_row(idx)
                return


    def _check_side_edge(self, idx):

        if idx not in self.LR:
            raise KeyError('check side edge expects right or left flag value')

        ridx = 0 if idx == self.LEFT else self.width -1
        for row in self.universe:
            if row[ridx] == LifeRule.ALIVE:
                self._insert_dead_column(idx)
                return

    def _insert_dead_column(self, idx):
        '''
        Inserts a dead column at the given index.
        '''
        for r in self.universe:
            if(idx == self.LEFT):
                r.insert(0, LifeRule.DEAD)
            else:
                r.append(LifeRule.DEAD)
        self.width = len(self.universe[0])

    def _insert_dead_row(self, idx):
        '''
        Inserts a dead row at the given index.
        '''
        if idx not in self.TB:
            raise KeyError('check TB edge expects top or bottom marker value')
        if(idx == self.TOP):
            self.universe.insert(0, [LifeRule.DEAD for x in range(self.width)])
        else:
            self.universe.append([LifeRule.DEAD for x in range(self.width)])
        self.height = len(self.universe)


    def _build_adjacency(self, x, y):
        '''
        Builds out a 3x3 localized board for a specific cell
        :param x: x coord
        :param y: y coord
        :return: returns 3x3 list grid representation
        '''

        # these are safe to skip because convetions assume that
        if x == 0 or x >= (len(self.universe)-1) or y == 0 or y >= (len(self.universe[0])-1):
            raise IndexError("Cannot build adjacency grid using edge index")

        return [self.universe[x-1][y-1:3],
                self.universe[x][y-1:3],
                self.universe[x+1][y-1:3]]

    def __repr__(self):
        u = "\n<------------------>\n"
        for r in self.universe:
            u = u + str(r) + "\n"
        u += "<------------------>\n"
        return u


