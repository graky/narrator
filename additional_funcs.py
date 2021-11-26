import random


def with_probability(percents):
    random_number = random.randint(1, 100)
    if random_number < percents:
        return True
    return False
