def solution(n, k):
    answer = []
    answer = [i for i in range(1,n+1)
        if i % k ==0]
    return answer