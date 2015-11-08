import unittest
from .rules import LifeRule
from .gol import GameOfLife
from .gol import ConfigException

class TestGameOfLife(unittest.TestCase):

    def setUp(self):

        self.sample = [[LifeRule.ALIVE]]
        self.gol = GameOfLife(universe=self.sample)

    def test_constructor(self):

        with self.assertRaises(ConfigException):
            GameOfLife(initial=None)
        with self.assertRaises(ConfigException):
            GameOfLife(initial=None, universe=None)
        with self.assertRaises(ConfigException):
            GameOfLife(universe=[[LifeRule.ALIVE, LifeRule.ALIVE]])

    def test_check_edges(self):
        gol = self.gol
        gol._check_edges()

        for r in gol.universe[0]:
            self.assertEqual(LifeRule.DEAD, r, "universe edges should be initialized dead")
        for r in gol.universe[gol.height-1]:
            self.assertEqual(LifeRule.DEAD, r, "universe edges should be initialized dead")
        for r in gol.universe:
            self.assertEqual(r[0], LifeRule.DEAD)
            self.assertEqual(r[gol.width-1], LifeRule.DEAD)

    def test_check_edges_idempotent(self):
        gol = self.gol
        gol._check_edges()
        h = gol.height
        w = gol.width
        gol._check_edges()
        self.assertEqual(gol.height, h)
        self.assertEqual(gol.width, w)

    def test_build_adjacency(self):
        self.gol._check_edges()
        adj = self.gol._build_adjacency(1,1)
        self.assertEqual(len(adj), 3)
        with self.assertRaises(IndexError):
            adj = self.gol._build_adjacency(0,0)



if __name__ == '__main__':
    unittest.main()