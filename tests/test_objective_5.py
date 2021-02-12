obj_name = 'objective_5'

from importlib import import_module
import pytest
import sys
sys.path.append(obj_name)
sys.path.append('tests')
obj_module = import_module(f'{obj_name}')
import helpers

@pytest.mark.skipif(helpers.check_skip(obj_name),reason=helpers.skip_reason)
def test_objective():
    greeter = obj_module.Greeter()
    assert greeter.sayhello() == "Hello, World."
    assert greeter.sayhello("Alice") == "Hello, Alice."
    assert greeter.tally() == 2



