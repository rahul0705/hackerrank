def tree_height(num_cycles = 0):
    height = 0
    for i in range(0, num_cycles+1):
        if i % 2:
            height += height
        else:
            height += 1
    return height
        
if __name__ == '__main__':
    num_tests = input()
    for i in range(0, num_tests):
        n = input()
        print tree_height(n)