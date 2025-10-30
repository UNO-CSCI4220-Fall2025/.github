import sys
import clingo

class SudokuApp(clingo.application.Application):
    def __init__(self):
        super().__init__()
    
    def print_model(self, model, printer) -> None:
        atoms = [str(atom) for atom in model.symbols(shown=True)]
        atoms = sorted(atoms)
        output = " ".join(atoms)
        print(output)

    def main(self, control, files):
        control.load("sudoku.lp")
        for file in files:
            control.load(file)
        if not files:
            control.load("-")
        control.ground([("base", [])])
        control.solve()    



        

clingo.application.clingo_main(SudokuApp())
