
def find_max(input):
    max = 0
    for e in input:
        for ee in input:
            if e > max:
             max_value = e

        print(max_value)

input_list = [100,3,4,5,28]
find_max(input_list)
