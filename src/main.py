import sys

from src.parser.molecule_parser import MoleculeParser

if __name__ == '__main__':
    try:
        molecule_formula_to_parse = sys.argv[1]
        molecule_parser = MoleculeParser()
        parsed_formula = molecule_parser.parse(molecule_formula_to_parse)
        print(parsed_formula)
    except IndexError:
        print('No molecule formula was given.')
