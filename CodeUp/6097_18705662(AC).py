
h, w = map(int, input().split())
n = int(input())

#tmp =[list(map(int, input().split())) for _ in range(n)]


des = [[0]*w  for _ in range(h)]

for i in range(n):
    ll, dd, dx, dy = map(int, input().split())
    if dd == 0:
        for j in range(ll):
            
            des[dx -1][dy +j-1] = 1
                
                    
            
    else:
        for j in range(ll):
            
            des[dx + j -1][dy -1] = 1
                
    
        
        
                
            
        
     
            
for i in range(h):
    for j in range(w):
        print(des[i][j],end =' ')
    print()
