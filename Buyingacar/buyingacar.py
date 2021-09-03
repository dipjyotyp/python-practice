def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    print(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth, sep=", ")
    answer = []
    if startPriceOld > startPriceNew:
        answer.append(0)
        answer.append(startPriceOld - startPriceNew)
        return answer
    if startPriceOld == startPriceNew:
        answer.append(0)
        answer.append(0)
        return answer
    months = 1
    savingperMonthIncrement = savingperMonth
    while True:
        startPriceOld -= float(startPriceOld * (percentLossByMonth / 100))
        startPriceNew -= float(startPriceNew * (percentLossByMonth / 100))
        totalSavings = float(startPriceOld + savingperMonth)
        available = float(totalSavings - startPriceNew)
        savingperMonth += savingperMonthIncrement
        if totalSavings >= startPriceNew:
            answer.append(months)
            answer.append(round(available))
            return answer
        months += 1
        if months % 2 == 0:
            percentLossByMonth += 0.5

print(nbMonths(2000, 8000, 1000, 1.5))
print(nbMonths(7500, 32000, 300, 1.55))
print(nbMonths(2200, 2200, 1000, 1))