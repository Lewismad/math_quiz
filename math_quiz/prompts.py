from random import randrange


def random_prompt():
    a=randrange(1,12)
    b=randrange(1,12)
    prompt=dict(question=f'{a} x {b} = ?')
    return prompt