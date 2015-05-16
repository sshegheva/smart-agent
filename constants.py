UNCHANGED = 'unchanged'
# shape actions
DELETE_ACTION = 'delete'
ADD_ACTION = 'add'
# size actions
EXPAND_ACTION = 'expand'
CONTRACT_ACTION = 'contract'
# angle actions
ROTATE_ACTION = 'rotate'
REFLECT_ACTION = 'reflect'
# fill actions
FILL_ACTION = 'fill'
SLIDE_ACTION = 'slide'


ACTIONS = [UNCHANGED, DELETE_ACTION, ADD_ACTION, EXPAND_ACTION, CONTRACT_ACTION, ROTATE_ACTION, REFLECT_ACTION]

ACTION_WEIGHTS = dict()
# unchanging is the best transformation
# so it carries the biggest weight
ACTION_WEIGHTS[UNCHANGED] = 0.5
# scaling actions are next best
ACTION_WEIGHTS[EXPAND_ACTION] = 0.4
ACTION_WEIGHTS[CONTRACT_ACTION] = 0.4


INSIDE = 'inside'
ABOVE = 'above'
LEFT_OF = 'left_of'

SHAPE = 'shape'
SIZE = 'size'
COLOR = 'fill'
ANGLE = 'angle'
LOCATION = 'inside'
ATTRIBUTES = [SHAPE, SIZE, COLOR, ANGLE, LOCATION]

VERY_SMALL = 'very small'
SMALL = 'small'
MEDIUM = 'medium'
LARGE = 'large'
VERY_LARGE = 'very large'
HUGE = 'huge'
SIZES = [VERY_SMALL, SMALL, MEDIUM, LARGE, VERY_LARGE, HUGE]

