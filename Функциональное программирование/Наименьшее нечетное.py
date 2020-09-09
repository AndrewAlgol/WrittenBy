"https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/EMsJG/naimien-shii-niechietnyi"
print(
    min(
        filter(
            lambda x:
            x % 2 != 0,
            list(
                map(
                    int,
                    input().split()
                    )
                )
            )
        )
    )
