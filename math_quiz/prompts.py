import random
from random import randrange


def random_prompt(division_enabled: bool=False, fractions_enabled: bool = False, addition_enabled: bool = False):
    prompt_fns = [multiplication]

    if division_enabled:
        prompt_fns.append(division)
    if fractions_enabled:
        prompt_fns.append(fraction_sum)
    if addition_enabled:
        prompt_fns.append(addition)
    return random.choice(prompt_fns)()


def addition():
    a=randrange(1,12)
    b=randrange(1,12)
    prompt=dict(
        type='addition',
        question=f'{a} + {b} = ?',
        a=a,
        b=b
    )
    return prompt
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
def fraction_sum():
    a=randrange(1,12)
    b=randrange(1,12)
    c=randrange(1,12)
    d=randrange(1,12)
    # 1/2 + 1/3 = ?
    # answer: 5/6

    prompt=dict(
        type='fraction',
        question=f'{a} / {b} + {c} / {d}= ?',
        a=a,
        b=b,
        c=c,
        d=d
    )
    return prompt