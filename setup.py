from setuptools import find_packages,setup
from typing import list

def get_requirements(file_path:str)->List[str]
'''
this function return the list of requirements
'''
requirements=[]

with open(file_path) as file_obj:
    requirements=file_obj.readlines()
    requirements=[req.replace('/n',"")for req in requirements]

return requirements






setup(
name="mlproject1",
version='0.0.1',
author='nikhil',
author_email='nihkilkumarkumawat7120@gmail.com', 
packages=find_packages(),
install_requires=get_requirements(requirements.txt),
)