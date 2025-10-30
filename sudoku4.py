import sys
import clingo

class SudokuApp(clingo.application.Application):
    def __init__(self):
        super().__init__()
    
    def print_model(self, model, printer) -> None:

        sudoku = {}
        for symbol in model.symbols(shown=True):
            if symbol.name == "sudoku":
                a = symbol.arguments[0].number
                b = symbol.arguments[1].number
                c = symbol.arguments[2].number
                sudoku[(a, b)] = c
        
        s = ""
        for row in range(1, 10):
            for column in range(1, 10):
                s += str(sudoku[(row, column)])
                if column % 3 == 0 and column != 9:
                    s += '  '
                elif column != 9:
                    s += ' '
                elif row % 3 == 0 and column == 9 and row != 9:
                    s += '\n\n'
                elif column == 9 and row !=9:
                    s += '\n'
        print(s)

    def main(self, control, files):
        control.load("sudoku.lp")
        for file in files:
            control.load(file)
        if not files:
            control.load("-")
        control.ground([("base", [])])
        control.solve()    



        

clingo.application.clingo_main(SudokuApp())
