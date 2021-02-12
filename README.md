<span style="color:red"><b>NOTE: these instructions are written for MacOS only, at the moment.</b></span>

## python-playground
This game is a set of python programming objectives of varying difficulty. You play by completing as many objectives as you can, either by writing python code or fixing bugs hidden in existing code.

### Get Started
The requirement to get started is Python 3.8 or higher.

1. Clone the repository into a `work` directory on your local workstation. 
2. Create and activate a virtual environment in the `python-playground` directory:
```
work$ python3 -m venv python-playground
work$ cd python-playground/
~/work/python-playground$source bin/activate
(python-playground) ~/work/python-playground$
```
3. Install the python dependencies
```
(python-playground) ~/work/python-playground$pip install -r requirements.txt
```

### Complete the objectives:
In each objective directory there is a README.md file that describes the coding objective. Follow the instructions in the README.

### Test your code:
Run pytest to see if you have achieved the objective.
```
(python-playground) ~/work/python-playground$ pytest
```
When all objectives have been achieved then the tests will pass with 100% success.



