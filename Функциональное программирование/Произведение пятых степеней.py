"https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/ML248/proizviedieniie-piatykh-stiepieniei"
from functools import reduce
print(
    reduce(
        lambda x, y:
        x * y**5,
        list(
            map(
                int,
                input().split(),
                ),
            ),
        1
        )
    )
