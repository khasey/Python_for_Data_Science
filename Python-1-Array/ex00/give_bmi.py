import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    try:
        h = np.array(height)
        w = np.array(weight)
        if h.dtype not in [np.number] or \
           w.dtype not in [np.number]:
            raise ValueError("les types ne sont pas int ou float!")

        res = w / (h ** 2)

    except ValueError as e:
        print(e)
        return None

    return list(res)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    res = np.array(bmi)
    i = 0
    lf = []
    for j in res:
        if res[i] < 26:
            lf = lf + [False]
        if res[i] > 26:
            lf = lf + [True]
        i += 1

    return list(lf)
