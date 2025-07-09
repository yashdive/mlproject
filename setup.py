#finds all packages i install for the project
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, "r") as file_obj:
        for line in file_obj:
            line = line.strip()
            if line and line != HYPEN_E_DOT:
                requirements.append(line)
    return requirements

        
#includes metadata info about project
setup(
    name='mlproject',
    version='0.0.1',
    author='Yash',
    author_email='yashdive190@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)