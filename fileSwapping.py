def swapFileData():
    file1 = input("Enter The Name of File 1: ")
    file2 = input("Enter The Name of File 2: ")

    read1 = open(file1, 'r')
    data_1 = read1.read()

    read2 = open(file2, 'r')
    data_2 = read2.read()

    write1 = open(file1, 'w')
    write1.write(data_2)

    write2 = open(file2, 'w')
    write2.write(data_1)

swapFileData()