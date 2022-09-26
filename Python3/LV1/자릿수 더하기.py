def solution(n):
    answer = 0
    while n >= 1:	# n >= 1일 때 실행하는 것이 아니라, n < 10이 되면 종료하는 방식을 사용해도 좋다
        answer += (n % 10)
        n = int(n / 10)	# / 대신 //을 사용하여 몫을 구해줘야 한다
    return answer