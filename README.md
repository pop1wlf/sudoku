# sudoku
使用python递归解决数独问题。

sudoku-mindless.py：
顺次找出数独中的空位置，并使用递归逐个试错1-9。

sudoku-pre-efcval.py：
提前算出每个空位置的可能取值，只在可能值范围中递归循环。