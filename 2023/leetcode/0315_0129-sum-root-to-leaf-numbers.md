## 230315-day2 Sum Root to Leaf Numbers, Recursion

https://github.com/suzieep/LeetCode/tree/main/0129-sum-root-to-leaf-numbers

# Intuition

있는 모든 노드의 마지막 노드를 방문해서 끝까지 보내기
stack 넣으면서 내려가다가 마지막 노드면 빼면서 누적 숫자에 총합 더하기

# Approach

근데 뎁스별로 자릿수 되는 거니까 그냥 그걸로 순열계산하면 안되나? -> 40같은 거 때문에 안될듯
그냥 일단 생각나는대로 재귀로 풀었음,ㅜㅜ

처음에 풀 때는 list에다 저장하고 재귀함수에 내려줬는데(mutable인줄 몰랐음) 주소참조하길래 급하게 slice로 복사하게 했다. 근데 이렇게 하니까 메모리 너무 많이 먹는 것 같아서 immutable인 string으로 붙여서 내려주는 방식으로 수정해서 제출함
+) 바꾸면서 이전 숫자에 10씩 곱해서 미는 방식도 된다고 생각함!

근데 저 if-elif 어떻게 줄일지?, 어제 문제부터 너무 지저분하게 푸는 것 같음ㅁ,

# Code

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        s = ''
        return self.suming(root,s)

    def suming(self,leaf,s):
        s+=str(leaf.val)

        if leaf.left and leaf.right:
            return self.suming(leaf.left,s) + self.suming(leaf.right,s)
        elif leaf.left:
            return self.suming(leaf.left,s)
        elif leaf.right:
            return self.suming(leaf.right,s)
        else:
            return int(s)

```

# 처음에 쓴 코드

(메모리 구려보여서 위에로 수정해서 제출)

```py
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        s = []
        return self.suming(root,s)

    def suming(self,leaf,s):
        s.append(leaf.val)

        if leaf.left and leaf.right:
            return self.suming(leaf.left,s[:]) + self.suming(leaf.right,s[:])
        elif leaf.left:
            return self.suming(leaf.left,s[:])
        elif leaf.right:
            return self.suming(leaf.right,s[:])
        else:
            tmp = int(''.join(map(str,s)))
            s.pop()
            return tmp

```
