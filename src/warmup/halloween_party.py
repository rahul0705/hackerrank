'''
@author: rahul
'''

def cut(K = 0):
    x = K / 2
    y = K - x
    return x * y

if __name__ == '__main__':
    T = input()
    for i in range(T):
        K = input()
        print cut(K)