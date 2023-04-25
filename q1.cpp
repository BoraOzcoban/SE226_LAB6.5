#include <iostream>
#include <unordered_set>
using namespace std;

int main() {
    int array1[] = {1, 2, 3};
    int array2[] = {2, 3, 4, 5};
    int n1 = sizeof(array1) / sizeof(array1[0]);
    int n2 = sizeof(array2) / sizeof(array2[0]);
    unordered_set<int> set1(array1, array1 + n1);
    for (int i = 0; i < n2; i++) {
        if (set1.erase(array2[i]) > 0) {
            cout << array2[i] << " ";
        }
    }
    return 0;
}
