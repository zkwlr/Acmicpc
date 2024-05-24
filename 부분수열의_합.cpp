#include <iostream>

using namespace std;

int n, s;
int result = 0;
int a[20];
void treesum(int cnt, int sum)
{
    if (cnt == n)
    {
        if (sum == s)
        {
            result += 1;
        }
        return;
    }
    // 왼쪽 자식, 오른쪽 자식 노드 재귀
    treesum(cnt + 1, sum);
    treesum(cnt + 1, sum + a[cnt]);
}

int main()
{

    cin >> n >> s;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    treesum(0, 0); // 초기 상태는 합 0, 선택한 원소도 0개
    if (s == 0)
        result -= 1;
    cout << result;
    return 0;
}