import random
from random import randrange


def random_prompt(division_enabled: bool=False):
    if division_enabled:
        prompt_fn=random.choice([multiplication, division])
        return prompt_fn()
    else:
        return multiplication()

def multiplication():
    a=randrange(1,12)
    b=randrange(1,12)
    prompt=dict(
        type='multiplication',
        question=f'{a} x {b} = ?',
        a=a,
        b=b
    )
    return prompt

def division():
    a=randrange(1,12)
    b=randrange(1,12)
    product=a*b

    prompt=dict(
        type='division',
        question=f'{product} / {b} = ?',
        a=product,
        b=b
    )
    return prompt