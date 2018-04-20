import re


class MoleculeParser:
    def __init__(self):
        self.decoded_formula = {}
        self.atom_pattern = re.compile('([A-Z][a-z]?)(\d+)?')
        self.composed_atoms_pattern = re.compile('[\[\{\(](.*)[\]\}\)](\d+)')

    def parse(self, formula):
        atom_match = re.search(self.atom_pattern, formula)

        if formula.startswith(('[', '(', '{')):
            composed_atoms_match = re.search(self.composed_atoms_pattern, formula)
            raw_formula, multiplier = composed_atoms_match.group(1), int(composed_atoms_match.group(2))
            formula = self._match_atoms_with_atom_count(raw_formula, multiplier, '')
            return self.parse(formula)
        elif atom_match:
            atom_count = int(atom_match.group(2)) if atom_match.group(2) is not None else 1
            self._update_decoded_formula(atom_match.group(1), atom_count)
            formula = formula[atom_match.end():]
            return self.parse(formula)

        return self.decoded_formula

    def _update_decoded_formula(self, key, value):
        if key in self.decoded_formula:
            self.decoded_formula[key] += value
        else:
            self.decoded_formula[key] = value

    def _match_atoms_with_atom_count(self, formula, multiplier, updated_formula):
        atom_match = re.search(self.atom_pattern, formula)

        if formula.startswith(('[', '(', '{')):
            composed_atoms_match = re.search(self.composed_atoms_pattern, formula)
            atom_count = int(composed_atoms_match.group(2)) * multiplier
            updated_formula += formula[:composed_atoms_match.end() - 1] + str(atom_count)
            return self._match_atoms_with_atom_count(formula[composed_atoms_match.end():], multiplier, updated_formula)
        elif atom_match:
            atom_count = int(atom_match.group(2)) if atom_match.group(2) is not None else 1
            atom_count = atom_count * multiplier
            updated_formula += atom_match.group(1) + str(atom_count)
            return self._match_atoms_with_atom_count(formula[atom_match.end():], multiplier, updated_formula)

        return updated_formula
