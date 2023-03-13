L = int(input())
L_list = sorted(list(map(int, input().split())))  # 순서대로 정리
N = int(input())
start = 0

if N in L_list:
    print(0)  # 만들 수 없음

else:
  for i in L_list:
      if N > i:
          start = i + 1  # 가능한 첫 숫자
      else:
          end = i - 1  # 가능한 끝 숫자
          break
   print(end - start + (end - N) * (N - start))
