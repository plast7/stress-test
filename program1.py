#include <iostream>

#define OVER 2222

using namespace std;
int secA[10000000] = {OVER}, secB[10000000] = {OVER};

int main() {
    int na, mb;
    cin >> na >> mb;

    int posA = 0, posB = 0, sa = 1;
    // int secA[10000] = {OVER}, secB[10000] = {OVER};
    for (int i = 0; i < na; i++) {
        // int d, t;
        char d;
        int tc;
        cin >> d >> tc;
        while (tc--) {
            posA += (d == 'R') ? 1 : -1;
            secA[sa++] = posA;
        }
    }

    int sb = 1;
    for (int i = 0; i < mb; i++) {
        // int d, t;
        char d;
        int tc;
        cin >> d >> tc;
        while (tc--) {
            posB += (d == 'R') ? 1 : -1;
            secB[sb++] = posB;
        }
    }

    bool isMeet = false;
    for (int i = 1; i < 1001; i++) {
        // if (secA[i] == secB[i]) {
        if (secA[i] == secB[i] && (i < sa && i < sb)) {
            cout << i;
            isMeet = true;
            break;
        }
    }
    if( ! isMeet) cout << -1;
}
