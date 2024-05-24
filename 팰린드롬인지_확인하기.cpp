#include <iostream>
#include <string>

using namespace std;

int main()
{
    string a;
    cin >> a;
    int size = a.length();
    int p = 1;
    for (int i = 0; i < size / 2; i++)
    {
        if (a[i] != a[size - 1 - i])
        {
            p = 0;
            break;
        }
    }
    cout << p;
    return 0;
}
