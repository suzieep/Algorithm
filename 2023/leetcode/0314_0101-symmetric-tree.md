## 230314-day1 Symmetric Tree, recursion

https://github.com/suzieep/LeetCode/tree/main/0101-symmetric-tree

199 / 199 test cases passed.
Status: Accepted
Runtime: 40 ms
Memory Usage: 14 MB

# Intuition

leetcode를 처음 써봐서 좌측처럼 array 형태로 나오는 줄 알고 2의 n승의 형태를 활용해 n/2만큼 loop를 돌면 되겠다 했는데 tree로 만들어 준 걸 보고, 바로 쓰는length함수도 모르겠고(어떻게 따로 하는 방법이 있나) recursion으로 푸는 게 더 빠르겠다고 생각했다

# Approach

parent,left,right만 잘라서 같은 Node level에 대해서 각각 반대방향과 일치하는지 확인해주면 쉽게 풀 수 있을 것이라고 생각했다, 다만 마지막 노드인지 확인하는 과정에 대해서 treenode인지 타입을 확인해서 했는데 더 깔끔한 방법을 찾아보면 좋을 것 같다. iterator로 풀면 끝까지가면~으로 풀면 되니까 좀 더 깔끔해 보일 수는 있을 것 같은데 근본적인 해결책은 아닌 것 같음

# Complexity

- Time complexity: O(n)
- Space complexity: O(1)

# Code

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = rightR
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSmallSymmetric(a,b):
            if type(a)==TreeNode and type(b)==TreeNode:
                if a.val==b.val:
                    return isSmallSymmetric(a.left,b.right) and isSmallSymmetric(a.right,b.left)
            else:
                return a==b
        return isSmallSymmetric(root.left,root.right)
```
