def solution(n):
    answer = []
    while n >= 1:
        r = n % 10
        answer.append(r)
        n = n // 10
	# answer = list(map(int, reversed(str(n)))) 이렇게 한줄로 끝내버리는 방법도 있다
	# map 함수는 list의 모든 요소를 int로 변환시켜준다
    return answer