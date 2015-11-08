class RulePluginRegister(type):
    '''
    Provides plugin capability for rule generation
    '''

    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, 'plugins'):
            cls.plugins = []
        else:
            cls.plugins.append(cls)


class LifeRule(metaclass=RulePluginRegister):
    ALIVE = 1
    DEAD = -1
    INERT = 0
    '''
    Base class for life rules. Registers new rules.
    '''


    def __call__(self, *args, **kwargs):
        return self.INERT


    def count_neighbors(self, adj):
        center = adj[1][1]
        count = 0
        for r in adj:
            for c in r:
                count  = count + 1 if c == self.ALIVE else count
        count  = count - 1 if center == self.ALIVE else count
        return count




class RuleUnderpopulation(LifeRule):
    '''
    Any live cell with fewer than two live neighbours dies,
    as if by needs caused by underpopulation.
    '''
    def __call__(self, adj, *args, **kwargs):

        subject = adj[1][1]
        if subject != self.ALIVE:
            return self.INERT

        c = self.count_neighbors(adj)
        if c < 2:
            return self.DEAD
        else:
            return self.INERT


class RuleOvercrowding(LifeRule):
    '''
    Any live cell with more than three live neighbours dies,
    as if by overcrowding.
    '''
    def __call__(self, adj, *args, **kwargs):

        subject = adj[1][1]
        if subject != self.ALIVE:
            return self.INERT

        c = self.count_neighbors(adj)
        if c > 3:
            return self.DEAD
        else:
            return self.INERT


class RuleLive(LifeRule):
    '''
    Any live cell with two or three live neighbours lives,
    unchanged, to the next generation.
    '''
    def __call__(self, adj, *args, **kwargs):

        subject = adj[1][1]
        if subject != self.ALIVE:
            return self.INERT

        c = self.count_neighbors(adj)
        if c in (2,3):
            return self.ALIVE
        else:
            return self.INERT


class RuleNewLife(LifeRule):
    '''
    Any dead cell with exactly three live neighbours cells
    will come to life.
    '''
    def __call__(self, adj, *args, **kwargs):

        subject = adj[1][1]
        if subject != self.DEAD:
            return self.INERT

        c = self.count_neighbors(adj)
        if c == 3:
            return self.ALIVE
        else:
            return self.INERT