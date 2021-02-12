obj_name = 'objective_4'

from importlib import import_module
import pytest
import sys
sys.path.append(obj_name)
sys.path.append('tests')
obj_module = import_module(f'{obj_name}')
import helpers

@pytest.mark.skipif(helpers.check_skip(obj_name),reason=helpers.skip_reason)
def test_objective():
    result1 = obj_module.params("required")
    assert type(result1) == type(list())
    assert len(result1) == 1
    result2 = obj_module.params("required","optional")
    assert len(result2) == 2
    assert result2 == ["required","optional"]



