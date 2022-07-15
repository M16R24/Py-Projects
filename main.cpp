/*
 * main.cpp
 *
 *  Created on: Jul 15, 2022
 *      Author: Dell
 */


#include <iostream>

using namespace std;

int main() {

	int secretNum = 7;
	int guess;
	int guessCount = 0;
	int guessLimit = 3;
	bool outofGuesses = false;


	while(secretNum != guess && !outofGuesses) {
		if (guessCount < guessLimit) {
		cout << "Enter guess " << endl;
		cin >> guess;
		guessCount++;
		} else {
			outofGuesses = true;
		}

	}

	if(outofGuesses){
		cout << "You lose!" << endl;
	} else {
		cout << "You Win" << endl;
	}


	return 0;
}

