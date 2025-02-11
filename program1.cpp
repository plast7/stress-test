#include <stdio.h>

int n, m, q;
int a[105][105];

void move(int r, int dir) {
    if(!dir) {
        int last = a[r][m-1];
        for(int j=m-1; j>=1; j--)
            a[r][j] = a[r][j-1];
        a[r][0] = last;
    }
    else {
        int last = a[r][0];
        for(int j=0; j<m-1; j++)
            a[r][j] = a[r][j+1];
        a[r][m-1] = last;
    }
}

bool check(int r1, int r2) {
    for(int j=0; j<m; j++)
        if(a[r1][j] == a[r2][j])
            return true;
    return false;
}

int main() {
    scanf("%d %d %d", &n, &m, &q);
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++)
            scanf("%d", &a[i][j]);
    
    while(q--) {
        int r; char d;
        scanf("%d %c", &r, &d); r--;
        int dir = (d == 'R');

        move(r, dir);

        int cdir = dir;
        for(int j=r-1; j>=0; j--) {
            if(!check(j, j+1))
                break;
            cdir ^= 1;
            move(j, cdir);
        }
        
        cdir = dir;
        for(int j=r+1; j<n; j++) {
            if(!check(j-1, j))
                break;
            cdir ^= 1;
            move(j, cdir);
        }
    }

    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++)
            printf("%d ", a[i][j]);
        printf("\n");
    }
    return 0;
}