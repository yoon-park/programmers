def solution(s):
    p = 0
    y = 0
    word = list(str(s))
    for x in word:
        if x == 'p' or x == 'P':
            p += 1
        elif x == 'y' or x == 'Y':
            y += 1
    return p == y

"""
무려 모든 풀이를 한줄로 끝낼 수 있다.
return s.lower().count('p') == s.lower().count('y')

lower() : 문자열을 소문자로 바꿔준다
count() : 문자열 안에서 찾고 싶은 문자의 개수를 찾아준다
"""