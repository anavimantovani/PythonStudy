#include <iostream>
using namespace std;

int main()
{
	const char BLANK = '-';
	const char PLAYER_X = 'X';
	const char PLAYER_O = 'O';
	const int SIZE = 3;
	char board[SIZE][SIZE];
	char whoseTurn = PLAYER_X;

	// initialize the board
	for (int r = 0; r < SIZE; r++)
		for (int c = 0; c < SIZE; c++)
			board[r][c] = BLANK;

	while (true)
	{
		// display board
		for (int r = 0; r < SIZE; r++)
		{
			for (int c = 0; c < SIZE; c++)
				cout << board[r][c] << " ";
			cout << endl;
		}

		// prompt for player's move
		cout << "Player " << whoseTurn << ", enter your move: ";
		int moveRow, moveCol;
		cin >> moveRow >> moveCol;

		if (moveRow >= 0 && moveRow < SIZE
			&& moveCol >= 0 && moveCol < SIZE)
		{
			if (board[moveRow][moveCol] == BLANK)
			{
				board[moveRow][moveCol] = whoseTurn;

				// check for victory
				// horizontal wins
				for (int r = 0; r < SIZE; r++)
				{
					bool win = true;
					for (int c = 0; c < SIZE; c++)
					{
						if (board[r][c] != whoseTurn)
							win = false;
					}
					if (win)
					{
						cout << "Player " << whoseTurn << " wins!" << endl;
						return 0;
					}
				}

				// vertical wins
				for (int c = 0; c < SIZE; c++)
				{
					bool win = true;
					for (int r = 0; r < SIZE; r++)
					{
						if (board[r][c] != whoseTurn)
							win = false;
					}
					if (win)
					{
						cout << "Player " << whoseTurn << " wins!" << endl;
						return 0;
					}
				}

				// diagonal wins
				if ((board[0][0] == whoseTurn && 
					board[1][1] == whoseTurn &&
					board[2][2] == whoseTurn)
					|| (board[0][2] == whoseTurn && 
						board[1][1] == whoseTurn &&
						board[2][0] == whoseTurn))
				{
					cout << "Player " << whoseTurn << " wins!" << endl;
						return 0;
				}

				// advance to next player
				if (whoseTurn == PLAYER_X)
					whoseTurn = PLAYER_O;
				else
					whoseTurn = PLAYER_X;
			}
			else
				cout << "That space is occupied. Try again." << endl;
		}
		else
			cout << "That space is off the board. Try again." << endl;

		
	}
}