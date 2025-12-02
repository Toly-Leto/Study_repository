#include <string>   
#include <iostream> 

using namespace std;


string reverse_str(string line) {
    string reversed_line = "";
    for (int i = line.length() - 1; i >= 0; --i) {
        reversed_line += line[i];
    }
    return reversed_line;
}


int count_words(string line) {
    int count = 0;

    for (int i = 0; i < line.length(); i++) {
        if (line[i] == ' ' and 0 < i and !(line[i - 1] == ' '))
            count++;
    }
    if (line[line.length() - 1] == ' ')
        return count;
    else return count + 1;
}


bool is_polindrom(string word) {
    string reversed = reverse_str(word);
    return reversed == word;
}

int main() {
    string line = " Привет, как дела,   сколько лет,       сколько зим!  ";
    string word = "анна";
    cout << "Number of words is: " << count_words(line) << endl;
    cout << "is polindrom (anna): " << is_polindrom(word) << endl;
    cout << "Reversed word Anna: " << reverse_str("Anna") << endl;

}