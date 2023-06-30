# https://www.hackerrank.com/challenges/s10-basic-statistics/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input().strip())
X = input().split(" ")
X = [int(i) for i in X]
X.sort()
# mean
sum = 0
for i in X:
    sum+=i
mean = sum/N
print(mean)
# median
if N % 2 == 0:
    median = (X[(N//2)-1] + X[((N//2))] ) / 2
print(median)
# mode
frequency = {}
for i in X:
    frequency[i] = X.count(i)
sorted_freq = sorted(frequency, key = frequency.get, reverse=True)
mode = sorted_freq[0]
print(mode)
