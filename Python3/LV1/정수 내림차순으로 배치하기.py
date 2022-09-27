def solution(n):
    num = list(map(int, str(n)))
    num.sort()
    num.reverse()
    answer = "".join(map(str,num))
    return int(answer)

"""
내 풀이에서는 2번 줄에서 str을 int로 전환하고, 5번 줄에서 join을 하기 위해 int를 str로 전환해준 뒤, 6번 줄에서 정답의 형식에 맞추어 다시 str을 int로 변환해준다.
그런데 꼭 int로 변환하지 않아도 sort가 가능하므로, 중간 과정을 한번 없애줄 수 있다.

num = list(str(n))
num.sort(reverse = True)	# sort에 reverse 옵션을 True 로 설정하면 내림차순으로 정렬해준다
answer = int("".join(num))
"""