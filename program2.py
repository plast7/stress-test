
n,m,q=map(int,input().split())
mtx=[list(map(int,input().split())) for _ in range(n)]
winds=[(int(r),d) for r,d in [input().split() for _ in range(q)]]

#print(mtx)
def Left(mtx,r):
    row=mtx[r][:]
    temp=mtx[r][m-1]
    for i in range(m-1,0,-1):
        row[i]=row[i-1]
    row[0]=temp
    return row

def Right(mtx,r):
    row=mtx[r][:]
    temp=mtx[r][0]
    for i in range(0,m-1):
        row[i]=row[i+1]
    row[m-1]=temp
    return row

def Up(mtx,r,d):
    if 0<r<=m-1:
        for x in range(r,0,-1):
            a=False
            for t in range(m):
                if mtx[x][t]==mtx[x-1][t]:
                    a=True
            if a:
                if d=="L":
                    row=Right(mtx,x-1)
                    d="R"
                else:
                    row=Left(mtx,x-1)
                    d="L"
                mtx[x-1]=row
            else:
                break
    return mtx



def Down(mtx,r,d):
    if 0<=r<m-1:
        for x in range(r,n-1):
            a=False
            for t in range(m):
                if mtx[x][t]==mtx[x+1][t]:
                    a=True
            if a:
                if d=="L":
                    row=Right(mtx,x+1)
                    d="R"
                else:
                    row=Left(mtx,x+1)
                    d="L"
                mtx[x+1]=row
            else:
                break
    return mtx,d



for w in winds:
    r,d=w #r번째 줄, d는 방향
    r=r-1
    if d=="L":
        row=Left(mtx,r)
        mtx[r]=row
    else:
        row=Right(mtx,r)
        mtx[r]=row

    mtx_up=Up(mtx,r,d)
    mtx_down=Down(mtx,r,d)

    for x in range(r):
        for x in mtx_up:
            mtx[:r][:]=mtx_up[:r][:]
        for x in mtx_down:
            mtx[r:][:]=mtx_down[r:][:]
for x in mtx:
    for i in x:
        print(i,end=" ")
    print()


