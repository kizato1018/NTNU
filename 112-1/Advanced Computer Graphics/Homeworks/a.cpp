#include <iostream>
#include <vector>
using namespace std;

struct Student{
    int id;
    string s;
};

void test(Student& std) {
    Student std1;

}

int main() {
    vector<Student> v;
    v.push_back(Student{0, "A"});
    v.push_back(Student{1, "B"});
    cout << v[0].id << " " << &v[0] << endl;
    cout << v[1].id << " " << &v[1] << endl;
    // for (vector<Student>::iterator it : v) {
    //     cout << &i << endl;
    // }
}