obj_name = 'objective_2'

from importlib import import_module
import pytest
import sys
sys.path.append(obj_name)
sys.path.append('tests')
obj_module = import_module(f'{obj_name}')
import helpers

@pytest.mark.skipif(helpers.check_skip(obj_name),reason=helpers.skip_reason)
def test_objective():
    result = obj_module.chop(4,"Autodesk")
    assert type(result) == type(tuple())
    assert result[0] == "Auto"
    assert result[1] == "desk"
 