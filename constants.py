UNCHANGED = 'unchanged'
# shape actions
DELETE_ACTION = 'delete'
ADD_ACTION = 'add'
# size actions
EXPAND_ACTION = 'expand'
CONTRACT_ACTION = 'contract'

# angle actions

# rotate by 90 degrees, to rotate more - combine rotations
ROTATE_ACTION = 'rotate'
REFLECT_ACTION = 'reflect'
# fill actions
FILL_ACTION = 'fill'
SLIDE_ACTION = 'slide'


ACTIONS = [UNCHANGED, DELETE_ACTION, ADD_ACTION, EXPAND_ACTION, CONTRACT_ACTION, ROTATE_ACTION, REFLECT_ACTION]

SIMILARITY_WEIGHTS = dict()
# unchanging is the best transformation
# so it carries the biggest weight
SIMILARITY_WEIGHTS[UNCHANGED] = 5
# scaling actions are next best
SIMILARITY_WEIGHTS[REFLECT_ACTION] = 4
SIMILARITY_WEIGHTS[ROTATE_ACTION] = 3
SIMILARITY_WEIGHTS[EXPAND_ACTION] = 2
SIMILARITY_WEIGHTS[CONTRACT_ACTION] = 2
SIMILARITY_WEIGHTS[FILL_ACTION] = 2
SIMILARITY_WEIGHTS[DELETE_ACTION] = 1
SIMILARITY_WEIGHTS[ADD_ACTION] = 1
SIMILARITY_WEIGHTS[SLIDE_ACTION] = 1


class Attributes(object):
    SHAPE = 'shape'
    SIZE = 'size'
    COLOR = 'fill'
    ANGLE = 'angle'
    INSIDE = 'inside'
    ALIGNMENT = 'alignment'
    ABOVE = 'above'
    LEFT_OF = 'left_of'
    ATTRIBUTES = [SHAPE, SIZE, COLOR, ANGLE, INSIDE, ALIGNMENT, ABOVE, LEFT_OF]

VERY_SMALL = 'very small'
SMALL = 'small'
MEDIUM = 'medium'
LARGE = 'large'
VERY_LARGE = 'very large'
HUGE = 'huge'
SIZES = [VERY_SMALL, SMALL, MEDIUM, LARGE, VERY_LARGE, HUGE]

