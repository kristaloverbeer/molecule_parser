import pytest as pytest

from src.parser.molecule_parser import MoleculeParser


def test_should_return_empty_dict_when_given_an_empty_formula():
    # Given
    string_formula = ''

    molecule_parser = MoleculeParser()
    # When
    formula = molecule_parser.parse(string_formula)
    # Then
    assert formula == {}


def test_should_return_atoms_counts_given_a_basic_formula_without_digit():
    # Given
    string_formula = 'HO'

    molecule_parser = MoleculeParser()
    # When
    formula = molecule_parser.parse(string_formula)
    # Then
    assert formula == {'H': 1, 'O': 1}


@pytest.mark.parametrize('string_formula,expected_formula', [
    ('H2O', {'H': 2, 'O': 1}),
    ('MgO2', {'Mg': 1, 'O': 2})
])
def test_should_return_atoms_counts_when_given_a_formula_without_brackets(string_formula, expected_formula):
    # Given
    molecule_parser = MoleculeParser()
    # When
    formula = molecule_parser.parse(string_formula)
    # Then
    assert formula == expected_formula


@pytest.mark.parametrize('string_formula,expected_formula', [
    ('K4(ON)2', {'K': 4, 'O': 2, 'N': 2}),
    ('K4[ON(SO3)2]2', {'K': 4, 'O': 14, 'N': 2, 'S': 4}),
    ('K4[ON(SO3{K2O3Cu40}4)2]2', {'Cu': 640, 'K': 36, 'N': 2, 'O': 62, 'S': 4}),
])
def test_should_return_atoms_counts_when_given_a_complex_formula(string_formula, expected_formula):
    # Given
    molecule_parser = MoleculeParser()
    # When
    formula = molecule_parser.parse(string_formula)
    # Then
    assert formula == expected_formula
