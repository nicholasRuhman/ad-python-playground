def check_skip(obj_name):
    with open(f"{obj_name}/{obj_name}.py",'r') as o:
        first_line = o.readline()
        if "NO-TEST" in first_line:
            return True
        else:
            return False

skip_reason = "Remove the NO-TEST comment from the top of the module to run this test."