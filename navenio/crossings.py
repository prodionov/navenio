def get_number_of_value_crossings(signal, value):
    counter = 0
    if len(signal) == 1:
        return 0
    start = signal[0] - value
    for i in range(0, len(signal) - 1):
        a1 = -1 if signal[i] < value else 1 if signal[i] > value else 0
        a2 = -1 if signal[i+1] < value else 1 if signal[i+1] > value else 0
        if a1 != 0 :
            start = a1
        if start * a2 < 0:
            counter += 1
    return counter



