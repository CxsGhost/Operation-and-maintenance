def grid_1():
    for i in range(4):
        print('|         |         |')
def grid_2():
    print('+ - - - - + - - - - +')
def grid():
    for j in range(2):
        grid_2(),grid_1()
    grid_2()
grid()
