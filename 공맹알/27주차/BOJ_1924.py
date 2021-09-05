#https://www.acmicpc.net/problem/1924

x, y = map(int, input().split(' '))
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ] #달별로 몇 일인지 저장해두기
_sum = 0
for i in range(x - 1):
    _sum += month[i]
_sum += y
 
print(week[_sum % 7]) # 총 날짜에서 7을 나눠서 요일 찾기