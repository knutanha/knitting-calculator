import json

"""temporary input"""
# mFrom = int(input("Ant masker du har: "))
# mTo = int(input("Ant masker du vil ende med: "))


def calc_knit(mfrom, mto):
    """input validation"""
    inputerror = input_validation(mfrom, mto)

    if inputerror:
        return {'knittingMsg': inputerror, 'solList': []}

    """initialize """
    reduce = None
    applist = list()

    solutionv = ['x'] * mto
    z = mto // abs(mfrom - mto)
    r = mto / abs(mfrom - mto) - z

    if mto < mfrom:
        reduce = True
        res = r
    else:
        reduce = False
        res = 0

    solution, knittingmessage, errormessage = calc(solutionv, z, res, r, applist, mto, mfrom, reduce)

    if errormessage:
        return {'knittingMsg': errormessage, 'solList': []}

    # serialize json
    solution_json = jsonify_result(knittingmessage, solution)

    # print(solution_json)

    return solution_json


def input_validation(mfrom, mto):
    inputerr = None

    if mto == mfrom:
        inputerr = 'Vil du ikke endre noe? sjekk inputen :)'

    if mto > mfrom and mto > 2 * mfrom:
        inputerr = 'Jeg støtter ikke økning til mer enn dobbelt så mange masker. '

    if mfrom > mto and mfrom > 2 * mto:
        inputerr = 'Jeg støtter ikke reduksjon med mer enn halvparten av maskene.'

    return inputerr


def calc(solutionv, z, res, r, applist, mto, mfrom, reduce):
    errormessage = None
    knittingmessage = None
    solution = []

    for i in range(len(solutionv)):
        if (i + 1) % z == 0 and res <= 1:
            solutionv[i] = 'Y'
            res = res + r
        elif (i + 1) % z == 0 and res > 1:
            applist.append(i)
            solutionv[i] = 'Y'
            res = res + r - 1

    for i in range(len(applist)):
        solutionv.insert(applist[i] + i, 'x')
        solutionv.pop(-1)

    # check result
    if len(solutionv) != mto:
        errormessage = 'Noe har skjedd feil :( '
    if not (solutionv.count('x') > 0 and solutionv.count('Y')):
        errormessage = 'Noe har skjedd feil :( '

    # replace Y with knitting action
    if reduce:
        solutionv = ['Strikk 2 sammen' if a == 'Y' else a for a in solutionv]
        knittingmessage = 'Du må redusere ' + str(mfrom - mto) + ' masker. Under er forslag til mønster'

    if not reduce:
        solutionv = ['Lag en ny maske' if a == 'Y' else a for a in solutionv]
        knittingmessage = 'Du må øke med ' + str(mto - mfrom) + ' masker. Under er forslag til mønster  '

    # make solution a nice, readable list
    counter = 0
    for i in range(len(solutionv)):
        if solutionv[i] == 'x':
            counter += 1
            if i < len(solutionv) - 1 and solutionv[i+1] != 'x':
                solution.append('Strikk ' + str(counter) + ' m')
                counter = 0
            elif i == len(solutionv) - 1:
                solution.append('Strikk ' + str(counter) + ' m')
        else:
            solution.append(solutionv[i])

    return solution, knittingmessage, errormessage


def jsonify_result(knittingmessage, solution):
    # create dictionary
    solDict = {'knittingMsg': knittingmessage, 'solList': solution}

    # create json
    return solDict
    # return json.dumps(solDict, ensure_ascii=False)

# calc_knit(mFrom, mTo)


if __name__ == '__main__':
    print(calc_knit(17, 20))
    print(calc_knit(20, 17))