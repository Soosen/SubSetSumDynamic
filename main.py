import numpy


def SubSetSum(NumbersSet, ExpectedSum, printMatrix):
    matrix = numpy.zeros((len(NumbersSet), ExpectedSum + 1))


    #define the sum of 0 as true
    for i in range(len(NumbersSet)):
        matrix[i][0] = 1

    for i in range(len(NumbersSet)):
        for j in range(len(matrix[i])):
            #copy all 1s from the row above
            if(i != 0 and matrix[i - 1][j] == 1):
                matrix[i][j] = 1

            #dont check j - current Number is negative
            if(j - NumbersSet[i] < 0):
                continue

            #0 + j = j set to true
            if(j == NumbersSet[i]):
                matrix[i][j] = 1
                continue

            #if its the first row
            if(i == 0):
                continue

            #if previous row[j - current Number] == true set  matrix[i][j] to true
            if(matrix[i - 1][j - NumbersSet[i]] == 1):
                matrix[i][j] = 1

    if(printMatrix):
        print(matrix)

    if(matrix[len(NumbersSet) - 1][ExpectedSum] != 1):
        print("The is no such a subset.")
        return

    output = []
    i, j = len(NumbersSet) - 1, ExpectedSum
    while(j != 0 and i != 0):      
        if(matrix[i - 1][j] == 1):
            i -= 1
        else:
            output.append(NumbersSet[i])
            j -= NumbersSet[i]
            i -= 1

    print("Input set: ", NumbersSet)
    print("Expected sum: ", ExpectedSum)
    print("The subset is: ", output)



#HERE IS THE INPUT
NUMBER_SET = [2, 3, 6, 7, 10, 13, 35, 40, 55, 62, 128]
EXPECTED_SUM = 293
PRINT_MATRIX = False
SubSetSum(NUMBER_SET, EXPECTED_SUM, PRINT_MATRIX) 