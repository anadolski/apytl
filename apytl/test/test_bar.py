"""
A module for testing the `apytl.Bar` class.
"""
import apytl
import pytest

TEST_BAR = apytl.Bar()

def test_classattr_iteration_toggle_state_initial():
    """Check initial setup toggle"""
    expected = True
    assert TEST_BAR.first_iteration == expected

def test_classattr_iteration_toggle_state_postsetup():
    """Check setup toggle after trigger"""
    expected = False
    TEST_BAR.setup_bar(barsize=50)
    assert TEST_BAR.first_iteration == expected

def test_setup_bar_barsize():
    """Change the bar size"""
    expected = 10
    TEST_BAR.setup_bar(barsize=expected)
    assert TEST_BAR.barsize == expected

def test_setup_bar_decimal():
    """Change the reported completion precision"""
    expected = 99
    TEST_BAR.setup_bar(decimal=expected)
    assert TEST_BAR.decimal == expected

def test_setup_bar_prefix():
    """Change the bar prefix"""
    expected = 'testprefix'
    TEST_BAR.setup_bar(prefix=expected)
    assert TEST_BAR.prefix == expected

def test_setup_bar_suffix():
    """Change the bar suffix"""
    expected = 'testsuffix'
    TEST_BAR.setup_bar(suffix=expected)
    assert TEST_BAR.suffix == expected

@pytest.mark.parametrize('test_input, expected', [
    pytest.param('x', 'x'),
    pytest.param('\\u2620', '\u2620'),
    pytest.param('\\U0001F62C', '\U0001F62C'),
    pytest.param('random', ''),
    pytest.param('pufferfish', ''),
    ])
def test_setup_bar_fill(test_input, expected):
    """Check various types of good fill input"""
    TEST_BAR.setup_bar(fill=test_input)
    if test_input == 'random' or test_input == 'pufferfish':
        expected = {key : TEST_BAR.parse_unicode(value) \
                    for key, value in TEST_BAR._EMOJI.items()}
        TEST_BAR.setup_bar(fill='random')
        assert TEST_BAR.fill in expected.values()
    else:
        assert TEST_BAR.fill == expected

@pytest.mark.parametrize('test_input, expected', [
    pytest.param('x', 1),
    pytest.param('\\u2620', 1),
    pytest.param('\\U0001F62C', 2),
    ])
def test_setup_bar_fillfactor(test_input, expected):
    """Check for proper fill padding given different input"""
    TEST_BAR.setup_bar(fill=test_input)
    assert TEST_BAR.fillfactor == expected

def test_setup_bar_bad_input():
    """Check response to bad setup input"""
    with pytest.raises(AttributeError):
        TEST_BAR.setup_bar(badinput='foo')

def test_teardown_bar_terminator():
    """Check for proper teardown"""
    TEST_BAR.setup_bar()
    TEST_BAR.teardown_bar()
    assert TEST_BAR.logginghandler.terminator == ''

def test_teardown_bar_iteration_flag():
    """Check toggle flag after teardown"""
    TEST_BAR.setup_bar()
    TEST_BAR.teardown_bar()
    assert TEST_BAR.first_iteration == True

def test_fullbar():
    """Check the full progress bar functionality"""
    ntotal = 25
    for ind, val in enumerate(range(ntotal)): 
        TEST_BAR.drawbar(val, ntotal, fill='random')

def test_reset_bar_attrs():
    """Check that attributes are properly reset to defaults"""
    expected = apytl.Bar().__dict__
    TEST_BAR.setup_bar(barsize=99, decimal=99, fill='x', prefix='foo', suffix='bar')
    TEST_BAR.reset_bar()
    test_attrs = {key : val for key, val in TEST_BAR.__dict__.items() \
                  if key in expected.keys()}
    assert test_attrs == expected
