def solution(arr):
    sum = 0
    for num in arr:
        sum += num
    answer = sum / len(arr)
    return answer