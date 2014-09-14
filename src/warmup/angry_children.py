'''
@author: rahul
'''

if __name__ == '__main__':
    N = input()
    K = input()
    candies = []
    for i in range(N):
        candies.append(input())
    candies.sort()
    min_diff = candies[K-1] - candies[0]
    for i in range(K, len(candies)):
        if min_diff > candies[i] - candies[i-K+1]:
            min_diff = candies[i] - candies[i-K+1]
    print min_diff