```java
for(nowN : )
dfs(nowN){
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
        nextN=2였으면 좋겠느ㅡㄴ데 한단계 위 어떻게...
    }
}