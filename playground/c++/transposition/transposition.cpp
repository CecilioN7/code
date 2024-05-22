#include <iostream>
#include <cctype>
#include <cmath>
using namespace std;

bool checkalpha(char[]);
int table(char[], int);
int transpose(int, int);
int transposeDown(int, int);
void display(int, int);
int accidental(char);

int main()
{
        char note [100];
		int distance;
		int accidental;
		int alpha;

        cout << "Transpose how many halfsteps: ";
		cin >> distance;
		if (distance < -12 || distance > 12) {
			cout << "Enter a number 0-12\n";
			return 0;
		}

		cout << "Sharp (1) or Flat (2): ";
		cin >> accidental;
		if (accidental < 1 || accidental > 2) {
			cout <<"Enter either 1 or 2\n";
			return 0;
		}

		cin.ignore();
		cout << "Enter your notes: ";
		cin.getline(note, 100);
		alpha = checkalpha(note);
		/*if (alpha == 0) {
			cout << "Check notes\n";
			return 0;
		}*/

		cout << "New transposed: ";

		for (int i = 0; note[i] != '\0'; i++ ) {
			while (note[i] == ' ') {
				cout << ' ';
				++i;
				if (isspace(note[i]) && note[++i] == '\0') {
					i = i + 2;
				}
			}

			table(note, i);
			int position = table(note, i);
			if (position == 2 || position == 5 || position == 7 || position == 10 || position == 12)
				i++;
			if (distance > 0) {
				transpose(position, distance);
				int newposition = transpose(position, distance);
				display(newposition, accidental);
			} else {
				transposeDown(position, distance);
				int newposition = transposeDown(position, distance);
				display(newposition, accidental);
			}

		}
		
		cout << "\n";
		return 0;
}
bool checkalpha(char note[]) {
	bool alpha;
	for (int i = 0; note[i] != '\0'; i++ ) {
			if (isalpha(note[i])) {
				alpha = 1;
			} else {
				alpha = 0;
				return alpha;
			}
	}
}
int transpose(int p, int d)
{
	if (p <= 12 - d) {
		p = p + d;
	} else if (p > 12 - d) {
		p = p + d - 12;
	}
	return p;
}

int transposeDown(int p, int d)
{
	if (p > abs(d)) {
		p = p + d;
	} else if (p <= abs(d)) {
		p = p + d + 12;
	}
	return p;
}

int table(char text[], int count)
{
	int countup = count + 1;
	int p = 0;
	if ((text[count] == 'A') && ((isspace(text[countup])) || text[countup] == '\0')) {
		p = 1;
	} else if ((text[count] == 'A') && (text[countup] == '#')) {
		p = 2;
	} else if ((text[count] == 'B') && (text[countup] == 'b')) {
		p = 2;
	} else if ((text[count] == 'B') && ((isspace(text[countup])) || text[countup] == '\0')) {
		p = 3;
	} else if ((text[count] == 'C') && ((isspace(text[countup])) || text[countup] == '\0')) {
		p = 4;
	} else if ((text[count] == 'C') && (text[countup] == '#')) {
		p = 5;
	} else if ((text[count] == 'D') && (text[countup] == 'b')) {
		p = 5;
	} else if ((text[count] == 'D') && ((isspace(text[countup])) || text[countup] == '\0')) {
		p = 6;
	} else if ((text[count] == 'D') && (text[countup] == '#')) {
		p = 7;
	} else if ((text[count] == 'E') && (text[countup] == 'b')) {
		p = 7;
	} else if ((text[count] == 'E') && ((isspace(text[countup])) || text[countup] == '\0')) {
		p = 8;
	} else if ((text[count] == 'F') && ((isspace(text[countup])) || text[countup] == '\0')) {
		p = 9;
	} else if ((text[count] == 'F') && (text[countup] == '#')) {
		p = 10;
	} else if ((text[count] == 'G') && (text[countup] == 'b')) {
		p = 10;
	} else if ((text[count] == 'G') && ((isspace(text[countup])) || text[countup] == '\0')) {
		p = 11;
	} else if ((text[count] == 'G') && (text[countup] == '#')) {
		p = 12;
	} else if ((text[count] == 'A') && (text[countup] == 'b')) {
		p = 12;
	}

	return p;
}

void display(int p, int a) {
	if (p == 1) {
		cout << "A";
	} else if (p == 2) {
		if (a == 1) {
			cout << "A#";
		} else if (a == 2) {
			cout << "Bb";
		}
	} else if (p == 3) {
		cout << "B";
	} else if (p == 4) {
		cout << "C";
	} else if (p == 5) {
		if (a == 1) {
			cout << "C#";
		} else if (a == 2) {
			cout << "Db";
		}
	} else if (p == 6) {
		cout << "D";
	} else if (p == 7) {
		if (a == 1) {
			cout << "D#";
		} else if (a ==  2) {
			cout << "Eb";
		}
	} else if (p == 8) {
		cout << "E";
	} else if (p == 9) {
		cout << "F";
	} else if (p == 10) {
		if (a == 1) {
			cout << "F#";
		} else if (a == 2) {
			cout << "Gb";
		}
	} else if (p == 11) {
		cout << "G";
	} else if (p == 12) {
		if (a == 1) {
			cout << "G#";
		} else if (a == 2) {
			cout << "Ab";
		}
	}
}
