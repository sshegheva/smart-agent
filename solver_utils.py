

def is_problem2x2(problem):
    return problem_dimension(problem) == '2x2'


def is_problem3x3(problem):
    return problem_dimension(problem) == '3x3'


def problem_dimension(problem):
    return problem.problemType


def score_pair(source, destination):
    print [(key, value.attributes) for key, value in source.objects.iteritems()]
    print [(key, value.attributes) for key, value in destination.objects.iteritems()]
