<br>

## [1] 자료형
<br>

### 1. 수 자료형
```python
# 지수 표현
a = 1e4		#10000.0
b = 752.5e1	#752.5
c = 3954e-3	#3.954

# 실수 연산
num_round = 0.3 + 0.6	# 0.899999..., !=0.9

# 반올림 함수 round(실수형 데이터, 반올림하고자하는 위치 -1)
round(123.456, 2)	#123.46
round(num_round, 4)	#0.9

# 연산
7 // 3	# 2, 몫
2 ** 3	# 8, 거듭제곱
```
<br>

### 2. 리스트 자료형
```python
# 빈 리스트 선언 방법
a = list()
b = []

# 값이 0인 1차원 리스트 초기화
a = [0] * 5	#[0,0,0,0,0]

# 리스트 인덱싱과 슬라이싱 
b = [1,2,3,4,5,6,7,8,9]
b[1:4]	#[2,3,4]
b[-2]	#8

# 리스트 컴프리핸션
arr1 = [i for i in range(10) if i%2 == 1]	#[1,3,5,7,9]
arr2 = [i * i for i in range(1,5)]		#[1,4,9,16]

# 2차원 배열 선언을 위한 리스트 컴프리핸션
arr3 = [[0] * 3 or _ in range(2))]	# [[0,0,0],[0,0,0]]

# 2차원 배열 선언 나쁜 예
arr4 = [[0] * 3] * 2	# [[0,0,0],[0,0,0]]
arr4[1][1] = 3		# [[0,3,0],[0,3,0]]

# 리스트 관련 메서드와 시간복잡도
a = [1,4,5]
a.append(2)		# O(1)
a.sort()		# O(NlogN)
a.sort(reverse = True)	# O(NlogN)
a.reverse()		# O(N)
a.insert(2,1)		# O(N), [1,4,1,5,2]
a.count(1)		# O(N), 2
a.remove(1)		#O(N), [4,1,5,2] 하나밖에 안 지워줌..ㅠㅠ

b = [1,2,3,4,5,5,5]
remove_set =[3,5]
result = [i for i in b if i not in remove_set]	#[1,2,4]
```
<br>

### 3. 문자열 자료형

```python
data = "Suzie's \"python\""	# Suzie's "python", 초기화 한 따옴표 종류가 다르면 \(백슬래시) 없어도 됨
a = "A"
a * 3	# AAA

b = "abcdef"
b[2:4]	# cd
```

<br>

### 4. 튜플 자료형 Tuple
```python
a = (1,2,3,4)
```
> #### 튜플 특징
  - 튜플은 한 번 선언된 값을 변경할 수 없다.
  - 리스트에 비해 공간 효율적
  - (비용, 노드번호) 형태로 주로 사용함

<br>

### 5. 사전 자료형 Dict
```python
data = dict()
data['A']='a'
data['B']='b'
data['C']='c'

key_list = data.keys()		#['A','B','C']
value_list = data.values()	#['a','b','c']

```
> #### 사전 특징
  - Key - Value 쌍
  - 사전은 Hash Table을 사용하므로 데이터 검색과 수정에서 O(1)의 시간복잡도를 가짐

### 6. 집합 자료형 Set
```python
# set 초기화
a = set([1,1,2,3,4,4,5])	#{1,2,3,4,5}
b = {3,3,4,5,6,6,7}		#{3,4,5,6,7}

a | b	# 합집합 {1,2,3,4,5,6,7}
a & b	# 교집합 {3,4,5}
a - b	# 차집합 {1,2}

c = set([1,2,3])
c.add(4)	#{1,2,3,4}
c.update([5,6])	#{1,2,3,4,5,6}, 원소 여러개 추가
c.remove(3)	#{1,2,4,5,6}

```
> #### 집합 특징
- 중복을 허용하지 않는다
- 순서가 없다
- 검사할 때 O(1)

<br>

## [2] 조건문 & 반복문
```python
# if문
if a == b:
elif a > b: 
else:	# 한 줄이면 줄 바꿈 안해도 됨

# 조건부 표현식 Conditional Expression
score = 85
result = "Success" if score >= 80 else "Fail"	# Success

# in, not in 
X in list	# list에 X가 있을 때 True
X not in 'abc'	# 문자열 안에 X가 있지 않으면 True

# for문
for x in range(1,4):	[1,2,3]
```
<br>

## [3] 함수
```python
def add(a,b):
	global cnt	# 함수 밖의 변수 데이터를 변경하고 싶을 때 
    cnt +=1
    
	return a+b
# 호출 1
add(b=3,a=7)	# 순서 상관없이 지정할 수 있다.

# 람다 표현식으로 add() 메서드 구현
(lambda a, b: a+b)(3,7)	
```
<br>

## [4] 입출력

### 1. 입력
```python
# 입력값이 적을 때 input()이 속도가 느림 ㅜㅜ
n = int(input())
data = list(map(int, inpput().split()))
n,m,k = map(int, input().split())

# 입력값이 많을 때(빠름)
import sys
data = sys.stdin.readline().rstrip()	# (공백포함된)한줄 문자열 입력, rstrip()으로 공백문자 제거 (readline이 엔터 만듦)
```

### 2. 출력

```python
a = 1
b = 2
print(a,b)	# 1 2
print("안녕" + str(a))	# 안녕1, str()안쓰면 int랑 못 더한다고 에러남
print("안녕", str(a))	# 안녕 1, 공백 삽입
print(f"안녕 {a}")	# 안녕 1, f-string(python 3.6)
```
<br>

## [5] 라이브러리

### 1. 내장함수 
- print(), input(), sorted(), import 없이 사용 가능
```python
a = [3,1,2]	# python에서는 iterable 객체는 반복 가능한 객체를 말한다.(list, dict, tuple...)
sum(a)	# 6
max(a)	# 3
min(1,2,3)	# 1

eval("3+4")			# 7, 문자열 수식 계산
sorted(a)			# [1,2,3]
sorted(a, reverse = True)	# [3,2,1]
sorted([('A', 35), ('B', 75), ('C', 50)], key = lambda x: x[1], reverse = True)	
# x[1] : 튜플의 두번째 원소를 key로 
# [('B', 75), ('C', 50), ('A', 35)]
```
<br>

### 2. itertools 
- 순열, 조합 등
```python
from itertools import permutations			# 순열
from itertools import combinations			# 조합
from itertools import product				# 중복 순열
from itertools import combinations_with_replacement	# 중복 조합

data = ['A','B','C']

# data에서 3개를 뽑아 나열
list(permutations(data,3))	# [('A','B','C'),('A','C','B'), ... ]

# data에서 2개 뽑는 조합
list(combinations(data,2))	# [('A','B'), ('A','C'), ('B','C')]

# data에서 중복을 허용하고 2개를 뽑는 순열
list(product(data, repeat=2))	#[('A','A'), ('A','B'), ('B','A'), ...]

# data에서 중복을 허용하고 2개를 뽑는 조합
list(combinations_with_replacement(data,2)) #[('A','A'), ('A','B'), ('A','C'), ...]
```
<br>

### 3. heapq 
- 힙 Heap 제공, 우선순위 큐에 사용
```python
import heapq

a = [1,4,0,3,2]
# 오름차순
def heapsort(iterable):
	h = []
    result = []
    
    for value in iterable:	# 힙에 원소 넣기
    	heapq.heappush(h,value)
    
    for i in range(len(h)):	# 힙에서 원소 꺼내기
    	result.append(heapq.heappop(h))
    
    return result

heapsort(a)	# [0,1,2,3,4]


# 내림차순
def heapsort_rev(iterable):
	h = []
    result = []
    
    for value in iterable:	# 힙에 원소 넣기
    	heapq.heappush(h,-value)
    
    for i in range(len(h)):	# 힙에서 원소 꺼내기
    	result.append(-heapq.heappop(h))
    
    return result

heapsort_rev(a)	#[4,3,2,1,0]
```
<br>

### 4. bisect 
- 이진 탐색 Binary Search 제공

>#### bisect는?
- 시간복잡도 : O(logN)
- 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수 구할 때 사용 가능


```python
from bisect import bisect_left, bisect_right
a = [1,2,4,4,8]	
x = 4
bisect_left(a,x)	# 2, 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스 출력
bisect_right(a,x)	# 4, 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스 출력

def func_range(a,left_val,right_val):
	right_idx = bisect_right(a, right_val)
    left_idx = bisect_left(a, right_val)
    return right_idx - left_idx

func_range(a,4,4)	# 2, 값이 4인 개수 출력
func_range(a,2,10)	# 4, [2,10] 범위에 있는 개수 출력
```
<br>

### 5. collections 
- deque 덱, Counter 카운터 등 자료구조 제공

>#### deque
>- python의 Queue는 일반적인 자료구조 라이브러리가 아니므로 deque를 사용한다.

```python
from collections import deque

data = deque([2,3,4])
data.appendleft(1)
data.append(5)
```

> #### Counter
- iterable 객체에서 내부 원소가 몇 번씩 등장했는 지 알려줌

```python
from collections import Counter

counter = Counter(['a','b','a','c','a','c'])
counter['a']	# 3
dict(counter)	# {'a': 3, 'b': 1, 'c': 2}, 사전 자료형으로 변환
```
<br>

### 6. math 
- 팩토리얼, 제곱근, 최대공약수 GCD, 삼각함수, pi 등 포함
```python
import math

math.factorial(5)	# 팩토리얼
math.sqrt(7)		# 제곱근
math.gcd(21, 14)	# 최대공약수
math.pi			# pi
math.e			# e
```


## [추가]

```python
# 자릿수 구하기 1
len(str(a))

# 자릿수 구하기 2
def digit_length(n):
    ans = 0

    while n:
        n //= 10
        ans += 1

    return ans

```

<br>

### References

https://shoark7.github.io/programming/algorithm/3-ways-to-get-length-of-natural-number#3a
이것이 코딩 테스트다 with 파이썬 - 나동빈 저