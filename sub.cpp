#include <iostream>
using namespace std;

void findSubsets(int arr[], int n, int index, int sum, int target, string current) {
    // If subset sum equals target, print the subset
    if (sum == target) {
        cout << "{ " << current << "}" << endl;
        return;
    }

    // If index reaches end or sum exceeds target, return
    if (index == n || sum > target) {
        return;
    }

    // Include the current element and recur
    findSubsets(arr, n, index + 1, sum + arr[index], target, current + to_string(arr[index]) + " ");

    // Exclude the current element and recur
    findSubsets(arr, n, index + 1, sum, target, current);
}

int main() {
    int n, target;

    // Input the number of elements and target sum
    cout << "Enter number of elements: ";
    cin >> n;

    int arr[n];
    cout << "Enter elements: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    cout << "Enter target sum: ";
    cin >> target;

    cout << "Subsets with sum " << target << " are:" << endl;
    findSubsets(arr, n, 0, 0, target, "");

    return 0;
}