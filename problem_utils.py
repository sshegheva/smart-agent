"""
Utility class for helper functions dealing with problems
"""
import logging

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


def is_problem2x2(problem):
    return problem_dimension(problem) == '2x2'


def is_problem3x3(problem):
    return problem_dimension(problem) == '3x3'


def problem_dimension(problem):
    return problem.problemType


def problem_choices(problem):
    """
    return only for choices for the problem
    which are usually numbered from 1 to 6
    :param problem: raven problem definition
    :return: dictionary of possible choices
    """
    # retrieve solutions from 1 to 6
    choices = map(str, range(1, 7))
    return {figure: value for figure, value in problem.figures.iteritems() if figure in choices}


def print_raven_object(obj):
    for x in obj:
        LOGGER.info('Raven object name: {} \n Attributes: {}'.format(obj[x].name, obj[x].attributes))
