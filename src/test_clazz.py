"""These are my tests."""

from src import clazz


def test_it():
    """Tests whether something is cool."""
    expected_output = ["shells", "gorgonzola", "parsley", "hello"]
    assert clazz.get_random_ingredients3("hello") == expected_output
