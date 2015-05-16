"""
Utility class providing helper functions for solving Raven problem
"""
import operator
import logging
import constants
import problem_utils

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


def _check_attribute(src, dst, attr):
    LOGGER.debug('Checking attr {} in {} and {}'.format(attr, src.name, dst.name))
    rules = []
    # check that attribute has not changed
    if src.attributes[attr] == dst.attributes[attr]:
        rules.append(constants.UNCHANGED)
    # check the shape
    elif attr == constants.SHAPE:
        rules.append(constants.DELETE_ACTION)
        rules.append(constants.ADD_ACTION)
    # check the color
    elif attr == constants.COLOR:
        rules.append(constants.FILL_ACTION)
    # check the size
    elif attr == constants.SIZE:
        if constants.SIZES.index(src.attributes[attr]) < constants.SIZES.index(dst.attributes[attr]):
            rules.append(constants.CONTRACT_ACTION)
        else:
            rules.append(constants.EXPAND_ACTION)
    # check the angle
    elif attr == constants.ANGLE:
        rules.append(constants.ROTATE_ACTION)
    elif attr == constants.LOCATION:
        # TODO ?
        rules.append(constants.SLIDE_ACTION)
    LOGGER.debug('Found rules {}'.format(rules))
    return rules


def transformation_rules(source, destination):
    """
    create a set of transformation rules A-to-B
    :param source: A
    :param destination: B
    :return: set of actions
    """
    LOGGER.debug('Finding transformation rules for {} and {}'.format(source.name, destination.name))
    # source.objects is a dictionary of objects in the source figure
    problem_utils.print_raven_object(source.objects)
    problem_utils.print_raven_object(destination.objects)

    # [(a,b)]
    pairs = zip(source.objects, destination.objects)
    rules = []
    for src_name, dst_name in pairs:
        src = source.objects[src_name]
        dst = destination.objects[dst_name]
        for attr in src.attributes:
            rules.extend(_check_attribute(src, dst, attr))
    LOGGER.debug('Rules: {}'.format(rules))
    return rules


def similarity_score(ab, cx, alpha=0.5, beta=0.25, gamma=0.25):
    """
    measure the similarity between two rules

    similarity = alpha x Size(Sab & Scx)
                    - beta x Size(Sab - Scx)
                    - gamma x Size(Scx - Sab)
    :return: scalar score
    """
    score = alpha * len(set(ab) & set(cx)) - beta * len(set(ab) - set(cx)) - gamma * len(set(cx) - set(ab))
    LOGGER.debug('Score for {} and {}: {}'.format(ab, cx, score))
    return score


def solve_problem(problem):
    """
    Given problem definition provide the best solution
    :param problem: problem definition
    :return: solution which has highest score
    """
    A = problem.figures['A']
    B = problem.figures['B']
    C = problem.figures['C']
    choices = problem_utils.problem_choices(problem)
    ab_rules = transformation_rules(A, B)
    cx_rules = {c: transformation_rules(C, figure) for c, figure in choices.iteritems()}
    scores = {choice: similarity_score(ab_rules, rules) for choice, rules in cx_rules.iteritems()}
    LOGGER.debug('Scores for problem {}: {}'.format(problem.name, scores))
    guess = max(scores.iteritems(), key=operator.itemgetter(1))[0]
    LOGGER.debug('Best guess: {}'.format(guess))
    return int(guess)
