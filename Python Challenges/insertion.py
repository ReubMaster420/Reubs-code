def insertion(list):
    for i in range(len(list)):

        currentvalue = list[i]
        j = i - 1
        while j >= 0 and currentvalue < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = currentvalue

list = ['Timor-Leste', 'Cambodia', 'Philippines', 'Brunei', 'Vietnam', 'Myanmar', 'Malaysia', 'Indonesia', 'Singapore', 'Philippines', 'Timor-Leste', 'Brunei', 'Timor-Leste', 'Laos', 'Thailand', 'Thailand']

insertion(list)
print(list)