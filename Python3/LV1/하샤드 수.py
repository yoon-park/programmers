def num(n):
    answer = 0
    while n >= 1:
        answer += (n % 10)
        n = n // 10
    return answer

def solution(x):
	if x % num(x) == 0:
		return True
	else:
		return False

"""
자릿수를 더하기는 한줄로 해결이 가능하다.
sum([int(x) for x in str(n)])

또한, 자릿수를 더한 결과를 num 이라고 칭할 때, return 또한 한줄로 해결이 가능하다.
return x % num == 0	# 결과가 참이면 True, 거짓이면 False를 return한다
"""