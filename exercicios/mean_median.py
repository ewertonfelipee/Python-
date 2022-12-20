import math

def calc_mean_median(notas):
    mean = sum(notas) / len(notas)
    median = 0

    if len(notas) % 2 == 0:
        index_central_lesser = int(len(notas)/2 - 1)
        index_central_greater = int(len(notas)/2)
        #len() is returning a float number
        point_central_lesser = notas[index_central_lesser]
        point_central_greater = notas[index_central_greater]

        median = (point_central_greater+point_central_lesser)/2

    else:
        ordered_grades = sorted(notas)
        median_index = math.floor(len(notas)/2)
        median = ordered_grades[median_index]

    return mean, median


result_mean, result_median = calc_mean_median([5,7,3,9])
print(f'Your mean is: {result_mean} and median is: {result_median}')
# print(calc_mean_median([5,7,3,9, 6]))