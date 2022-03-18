from matplotlib import pyplot
from datetime import datetime

def plot_limits(data):
    dates = [item.date() for item in data]
    maxs = [item.max() for item in data]
    avgs = [item.avg() for item in data]
    mins = [item.min() for item in data]
    local_maxima = data[0].max()
    for item in data:
        if item.max() > local_maxima:
            local_maxima = item.max()
            pyplot.axvline(item.date(), color='black')
    pyplot.plot(dates, maxs, color = 'red', label = 'Max')
    pyplot.plot(dates, avgs, color = 'orange', label = 'Avg')
    pyplot.plot(dates, mins, color = 'green', label = 'Min')
    pyplot.ylabel('€/MWh')
    pyplot.xlabel('Date')
    pyplot.legend(loc='upper left', frameon=True)
    pyplot.show()

def plot_maxweekly(data):
    dates = [item.date() for item in data]
    avgs = [item.avg() for item in data]
    groups = []
    week = [0, 0, 0, 0, 0, 0, 0]
    for i in range(len(dates)):
        wd = dates[i].weekday()
        week[wd] = avgs[i]
        if wd == 6:
            groups.append(week)
            week = [0, 0, 0, 0, 0, 0, 0]
    if [True if day > 0 else False for day in week]:
        groups.append(week)
    hist = [0, 0, 0, 0, 0, 0, 0]
    for group in groups:
        max = 0
        max_i = 0
        for i in range(7):
            if group[i] > max:
                max = group[i]
                max_i = i
        hist[max_i] += 1
    labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    pyplot.ylabel('Count')
    pyplot.bar(labels, hist, color = 'blue')
    pyplot.show()

def print_csv(data):
    print('date;max;avg;min')
    for p in data:
        print('{};{};{};{}'.format(p.date().strftime("%d/%m/%Y"), p.max(), p.avg(), p.min()))

