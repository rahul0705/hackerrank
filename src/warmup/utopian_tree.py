class Tree:
    def __init__(self):
        self.__height = 0

    def grow(self, num_cycles = 0):
        for i in range(0, num_cycles+1):
            if i % 2 == 0:
                self.__height += 1
            else:
                self.__height += self.__height

    def get_height(self):
        print self.__height
        
if __name__ == '__main__':
    num_tests = input()
    for i in range(0, num_tests):
        t = Tree()
        num_cycles = input()
        t.grow(num_cycles)
        t.get_height()