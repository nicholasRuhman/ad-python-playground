import sys
sys.path.append('objective_2')

import objective_2

def test_obj_2():
    result = objective_2.chop(4,"Autodesk")
    assert type(result) == type(tuple())
    assert result[0] == "Auto"
    assert result[1] == "desk"
 