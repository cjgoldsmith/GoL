class RulePluginMetaClass(type):
    '''
    Provides plugin capability for rule generation
    '''

    def _init_(cls):
        if not hasattr(cls, 'plugins'):
            cls.plugins = []
        else:
            cls.plugins.append(cls)


class LifeRule(metaclass=RulePluginMetaClass):
    ALIVE = 1
    DEAD = -1
    '''
    Base class for life rules. Registers new rules.
    '''
    pass


class RuleUnderpopulation(LifeRule):
    '''
    Any live cell with fewer than two live neighbours dies,
    as if by needs caused by underpopulation.
    '''
    pass

class RuleOvercrowding(LifeRule):
    '''
    Any live cell with more than three live neighbours dies,
    as if by overcrowding.
    '''
    pass

class RuleLive(LifeRule):
    '''
    Any live cell with two or three live neighbours lives,
    unchanged, to the next generation.
    '''
    pass

class RuleNewLife(LifeRule):
    '''
    Any dead cell with exactly three live neighbours cells
    will come to life.
    '''
    pass