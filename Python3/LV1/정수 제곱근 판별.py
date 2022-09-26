import math

def solution(n):
    answer = 0
    if float.is_integer(math.sqrt(n)):	# math.sqrt(n) 대신에 n ** (1/2) 를 사용할 수 있다
		# 그리고, math.sqrt 연산은 결과가 항상 float로 나오기 때문에 ** 연산자를 사용하는 것이 더 편하다
		# 제곱근이 정수인지 여부는, (제곱근) % 1 == 0 로 판별할 수 있다
        answer = math.pow(math.sqrt(n) + 1, 2)	# 마찬가지 이유로 math.pow 연산 대신에 ** 연산자를 사용하는 것이 좋다
    else:
        answer = -1
    return answer