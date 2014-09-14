'''
@author: rahul
'''

def tree_height(N = 0):
    height = 0
    for i in range(N+1):
        if i % 2:
            height += height
        else:
            height += 1
    return height
        
if __name__ == '__main__':
    T = input()
    for i in range(T):
        N = input()
        print tree_height(N)