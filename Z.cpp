// G5

#include <iostream>
#include <cmath>

using namespace std;
int cnt = 0;
int n, r, c;

int findz(int n, int r, int c)
{
    if (n == 0)
    {
        return cnt;
    }
    if (r <= pow(2, n - 1)) // 위 2개면
    {
        if (c <= pow(2, n - 1)) // 왼쪽 위 사분면에서 탐색, 첫번째 사분면이므로 더해줄 것 없음
        {
            return findz(n - 1, r, c);
        }
        else // 오른쪽 위 사분면에서 탐색, 왼쪽 위 사분면의 갯수 더해줌
        {
            cnt += pow(pow(2, n - 1), 2);
            return findz(n - 1, r, c - pow(2, n - 1)); // 새로운 r, c 값으로 몇사분면인지 재귀적으로 파악
        }
    }
    else // 아래 2개면
    {
        if (c <= pow(2, n - 1)) // 왼쪽 아래
        {
            cnt += pow(pow(2, n - 1), 2) * 2; // 1, 2사분면의 원소 갯수만큼 더해줌
            return findz(n - 1, r - pow(2, n - 1), c);
        }
        else // 오른쪽 아래
        {
            cnt += pow(pow(2, n - 1), 2) * 3;
            return findz(n - 1, r - pow(2, n - 1), c - pow(2, n - 1));
        }
    }
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> r >> c;
    r = r + 1;
    c = c + 1;
    cout << findz(n, r, c);
    return 0;
}