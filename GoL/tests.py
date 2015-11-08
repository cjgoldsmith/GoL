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


from .rules import RuleUnderpopulation
class TestRule(unittest.TestCase):

    def test_rule(self):

        # only 1 live neighbor
        adj = [
            [LifeRule.DEAD for x in range(3)],
            [LifeRule.ALIVE, LifeRule.ALIVE, LifeRule.DEAD],
            [LifeRule.DEAD for x in range(3)],
        ]
        self.assertEqual(LifeRule.DEAD, RuleUnderpopulation()(adj))

from .rules import RuleOvercrowding
class TestRuleOverCrowding(unittest.TestCase):

    def test_rule(self):

        # more than 3 living neighbors
        adj = [
            [LifeRule.ALIVE for x in range(3)],
            [LifeRule.ALIVE, LifeRule.ALIVE, LifeRule.DEAD],
            [LifeRule.DEAD for x in range(3)],
        ]
        self.assertEqual(LifeRule.DEAD, RuleOvercrowding()(adj))

from .rules import RuleLive
class TestRuleLive(unittest.TestCase):

    def test_rule(self):

        # 2-3 live neighbors
        adj = [
            [LifeRule.ALIVE for x in range(3)],
            [LifeRule.DEAD, LifeRule.ALIVE, LifeRule.DEAD],
            [LifeRule.DEAD for x in range(3)],
        ]
        self.assertEqual(LifeRule.ALIVE, RuleLive()(adj))

from .rules import RuleNewLife
class TestRuleNewLife(unittest.TestCase):

    def test_rule(self):

        # not alive but with 3 neighbors that are.
        adj = [
            [LifeRule.ALIVE for x in range(3)],
            [LifeRule.DEAD for x in range(3)],
            [LifeRule.DEAD for x in range(3)],
        ]
        self.assertEqual(LifeRule.ALIVE, RuleNewLife()(adj))


if __name__ == '__main__':
    unittest.main()