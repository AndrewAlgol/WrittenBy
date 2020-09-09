"https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/D7AH7/xor"
print(
    *list(
        map(
            lambda xy: (xy[0] + xy[1]) % 2,
            zip(
                map(
                    int,
                    input().split()),
                map(
                    int,
                    input().split()
                    )
                )
            )
        )
    )
