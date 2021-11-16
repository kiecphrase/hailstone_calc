x = int(input('Give an integer greater than 0: '))
print('calculating the hailstone series for all numbers up to and including', x)

y = 1

# go through every number
while y <= x:

    # reset helper variables
    biggest = y
    z = y
    series = []

    # add first number to list of significant values
    series.append(z)

    #  find all significant values for the number
    while z != 1 and z != 2 and z != 4 and z >= y:

        # even number
        if z % 2 == 0:
            z = z // 2

        # odd number
        else:
            z = (z * 3) + 1

            # check to see if the number is the biggest
            if z > biggest:
                biggest = z

        # add new number to list of significant values   
        series.append(z)

    print('starting number: ', y)
    print('biggest number in series: ', biggest)
    print('all significant number in series: ', series)
    print(' ')

    # move to next number
    y = y + 1


input('press enter to exit')