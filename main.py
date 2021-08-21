
Ed = [1,2,3,4,5]
Jo = [5,4,3,2,1]
edLimit = 0
joLimit = 5


def calc(ed, jo, edlimit, jolimit):
    savings = 0
    combi = sorted(zip(ed, jo), reverse=True)
    for i in combi:

        if i[0] >= i[1] and edlimit > 0:
            edlimit += -1
            savings += i[0]
        elif jolimit > 0:
            jolimit += -1
            savings += i[1]
        else:
            continue
    return savings


print(calc(Ed, Jo, edLimit, joLimit))
