'''
@author: rahul
'''

if __name__ == '__main__':
    T = input()
    for i in range(T):
        N = input()
        A = input()
        B = input()
        vals = set()
        for x in range(N):
            vals.add(x * A + (N - 1 - x) * B)
        for val in sorted(vals):
            print(val),
        print