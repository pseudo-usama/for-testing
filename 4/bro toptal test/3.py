from decimal import Decimal, localcontext


def solution(S, B):
    with localcontext() as ctx:
        ctx.prec = 100
        S = Decimal(S)

        B = [Decimal(b) for b in B]
        B_enum = list(enumerate(B))
        B_enum = sorted(B_enum, key=lambda b: b[1], reverse=True)

        B_index = [b[0] for b in B_enum]
        B_sorted = [b[1] for b in B_enum]

        remaining_S = S
        R = []

        for i in range(len(B_sorted)):
            excess = remaining_S * (B_sorted[i] / sum(B_sorted[i:]))
            R.append(excess)
            remaining_S -= excess

        R_enum = zip(B_index, R)

        R_unsorted_enum = sorted(R_enum, key=lambda r: r[0])
        R_unsorted = [round(r[1], 2) for r in R_unsorted_enum]
        print(type(R_unsorted[0]))
        return R_unsorted


def solution_high_precision(S, B):
    S = Decimal(S)

    B = [Decimal(b) for b in B]
    B_enum = list(enumerate(B))
    B_enum = sorted(B_enum, key=lambda b: b[1], reverse=True)

    B_index = [b[0] for b in B_enum]
    B_sorted = [b[1] for b in B_enum]

    remaining_S = S
    R = []

    for i in range(len(B_sorted)):
        excess = remaining_S * (B_sorted[i] / sum(B_sorted[i:]))
        R.append(excess)
        remaining_S -= excess

    R_enum = zip(B_index, R)

    R_unsorted_enum = sorted(R_enum, key=lambda r: r[0])
    R_unsorted = [round(r[1], 2) for r in R_unsorted_enum]
    print(type(R_unsorted[0]))
    return R_unsorted


print(solution_high_precision("300.01", ["300.00", "200.00", "100.00"]))
# print(solution("1.00", ["0.05", "1.00"]))
