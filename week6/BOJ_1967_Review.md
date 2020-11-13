```java
global stack
for(nowN : )
dfs(nowN){
    stack.push(nowN)
    visited[nowN]=true
    cnt =0
    for(nextN : nowN가 만나는 nodes){
        if(nextN != visited){
            cnt++
            length +=arr[newN][nextN]
            if(nextN = 7~12){
                saveL[nextN]+= length
                nextN = nowN
            }
        }
    }
    if(cnt==0){
        stack.pop(nowN)
        nextN=stack.peek()
    }
    dfs(nextN)
}
```
