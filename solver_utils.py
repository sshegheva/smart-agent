"""
Utility class providing helper functions for solving Raven problem
"""
import operator
import logging
import constants
import problem_utils
from collections import Counter
from ProblemSet import ProblemSet

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


def _check_attribute(src, dst, attr):
    rules = []
    # first make sure that attribute exists in both objects
    if attr not in src.attributes or attr not in dst.attributes:
        LOGGER.warn('Attribute {} is not present in both objects {} and {}'.format(attr, src.name, dst.name))
        return rules
    # check that attribute has not changed
    if src.attributes[attr] == dst.attributes[attr]:
        rules.append(constants.UNCHANGED)
    # check the shape
    elif attr == constants.Attributes.SHAPE:
        rules.append(constants.DELETE_ACTION)
        rules.append(constants.ADD_ACTION)
    # check the color
    elif attr == constants.Attributes.COLOR:
        rules.append(constants.FILL_ACTION)
    # check the size
    elif attr == constants.Attributes.SIZE:
        if constants.SIZES.index(src.attributes[attr]) < constants.SIZES.index(dst.attributes[attr]):
            rules.append(constants.CONTRACT_ACTION)
        else:
            rules.append(constants.EXPAND_ACTION)
    # check the angle
    elif attr == constants.Attributes.ANGLE:
        degrees_rotated = abs(int(dst.attributes[attr]) - int(src.attributes[attr]))
        [rules.append(constants.ROTATE_ACTION) for _ in range(degrees_rotated / 90)]
    elif attr == constants.Attributes.INSIDE:
        # TODO ?
        rules.append(constants.UNCHANGED)
    # check alignment
    # can move up, down, right and left and combined
    elif attr == constants.Attributes.ALIGNMENT:
        src_move = src.attributes[attr].split('-')
        dst_move = dst.attributes[attr].split('-')
        # check position top or bottom
        if src_move[0] != dst_move[0]:
            rules.append(constants.SLIDE_ACTION)
        # check position left or right
        if src_move[1] != dst_move[1]:
            rules.append(constants.SLIDE_ACTION)
    elif attr == constants.Attributes.ABOVE:
        # TODO ?
        rules.append(constants.UNCHANGED)
    LOGGER.debug('Found rules for {} and {} ({}):{}'.format(src.name, dst.name, attr, rules))
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

    # [(a,c), (b, d)]
    pairs = zip(sorted(source.objects.keys()), sorted(destination.objects.keys()))
    rules = []
    for src_name, dst_name in pairs:
        src = source.objects[src_name]
        dst = destination.objects[dst_name]
        for attr in src.attributes:
            rules.extend(_check_attribute(src, dst, attr))
    LOGGER.debug('Rules: {}'.format(rules))
    return rules


def similarity_score(ab, cx, alpha=0.5, beta=0.25, gamma=0.25, delta=0.25):
    """
    measure the similarity between two rules

    similarity = alpha x Size(Sab & Scx)
                    - beta x Size(Sab - Scx)
                    - gamma x Size(Scx - Sab)
                    - delta x Distance(ab, ax)
    :return: scalar score
    """
    LOGGER.debug('Calculating similarity between {} and {}'.format(ab, cx))
    weighted_similarity_ab = [constants.SIMILARITY_WEIGHTS[rule] * freq for rule, freq in Counter(ab).iteritems()]
    weighted_similarity_cx = [constants.SIMILARITY_WEIGHTS[rule] * freq for rule, freq in Counter(cx).iteritems()]
    distance = abs(sum(weighted_similarity_ab) - sum(weighted_similarity_cx))
    LOGGER.debug('Distance {}'.format(distance))
    common = set(ab) & set(cx)
    left = set(ab) - set(cx)
    right = set(cx) - set(ab)
    score = alpha * len(common) - beta * len(left) - gamma * len(right) - delta * distance
    LOGGER.debug('Score: {}'.format(ab, cx, score))
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

if __name__ == '__main__':
    solve_problem(ProblemSet('Basic Problems B').problems[5])