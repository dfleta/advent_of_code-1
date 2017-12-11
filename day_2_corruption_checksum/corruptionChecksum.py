
def readTxt(name):
    """
    :param name: nombre del fichero que le entra
    :return: devuelve una matriz de strings del archivo leído
    """
    listTxt = []
    infile = open(name, 'r')

    for line in infile:
        listTxt.append(line.replace('\t', ', ').replace('\n', '').split(', '))
    infile.close()
    return listTxt
def listStrToInt(convertList):
    """
    Tranforma la lista de str a una lista de int
    :param strList: entra una lista de strings
    :return: devuelve la misma lista pero en int
    """
    for row in range(0, len(convertList)):
        for element in range(0, len(convertList[row])):
            convertList[row][element] = int(convertList[row][element])

    return convertList
def highNum(row):
    """
    Entra una lista de números y devuelve el mayor
    :param row: entra una fila de números
    :return: devuelve el número mayor de la fila
    """
    higherNum = row[0]

    for element in row:
        if element > higherNum:
            higherNum = element
        else:
            pass
    return higherNum
def lowNum(row):
    """
    Entra una lista de números y devuelve el menor
    :param row: entra una fila de números
    :return: devuelve el número menor de la fila
    """
    lowerNum = row[0]

    for element in row:
        if element < lowerNum:
            lowerNum = element
        else:
            pass
    return lowerNum
def checksum(row):

    """
    :param row: entra una lista de números
    :return: devuelve el checksum (mayor num - menor)
    """

    return highNum(row) - lowNum(row)

def getNumberOfDivisor(row):
    """
    Recibe una fila de la matriz, busca los dos divisores y devuelve el resultado de la división
    :param row: recibe una fila de la matriz
    :return: devuelve el resultado del único posible caso de división
    """
    finalValue=0

    for number in row:
        for divisor in row:
            if number != divisor:
                if number % divisor == 0:
                    return number/divisor


    return finalValue

def sumOfChecksum(lista):
    """
    Función principal del apartado 1. Devolverá la suma de los checksum
    :param lista: entra una lista de strings
    :return: devolverá la suma de los checksum de la matriz en forma de int
    """
    totalValue = 0
    #Transformamos la lista de str a lista de ints para poder sumar los valores
    listStrToInt(lista)

    for row in lista:
        totalValue += checksum(row)

    return totalValue

def sumOfChecksum2(lista):
    """
    Función principal del apartado 2. Devolverá la suma de los checksum
    :param lista: entra una lista de strings
    :return: devolverá la suma de los checksum de la matriz en forma de int
    """
    totalValue = 0
    # Transformamos la lista de str a lista de ints para poder sumar los valores
    listStrToInt(lista)
    for row in lista:
        totalValue += getNumberOfDivisor(row)

    return int(float(totalValue))


lista = readTxt('puzzle.txt')
print(sumOfChecksum(lista))
print(sumOfChecksum2(lista))
