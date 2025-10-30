#const max = 9.
#const min = 1.
#const upper = 9.
#show sudoku/3.

:- sudoku(X1, Y1, N1), sudoku(X2, Y2, N1), subgrid(X1, Y1, B1), subgrid(X2, Y2, B1), (X1, Y1) != (X2, Y2).

:- sudoku(X1, Y1, N1), sudoku(X1, Y2, N1), Y1 != Y2.
:- sudoku(X1, Y1, N1), sudoku(X2, Y1, N1), X1 != X2.

:- sudoku(X, Y, N1), initial(X, Y, N2), N1 != N2.

{sudoku(X, Y, N) : N = 1..upper} = 1 :- X = min..max, Y = min..max.

sudoku(X, Y, Z) :- initial(X, Y, Z).

subgrid(X, Y, 1) :- X = 1..3, Y = 1..3.
subgrid(X, Y, 2) :- X = 1..3, Y = 4..6.
subgrid(X, Y, 3) :- X = 1..3, Y = 7..9.
subgrid(X, Y, 4) :- X = 4..6, Y = 1..3.
subgrid(X, Y, 5) :- X = 4..6, Y = 4..6.
subgrid(X, Y, 6) :- X = 4..6, Y = 7..9.
subgrid(X, Y, 7) :- X = 7..9, Y = 1..3.
subgrid(X, Y, 8) :- X = 7..9, Y = 4..6.
subgrid(X, Y, 9) :- X = 7..9, Y = 7..9.
