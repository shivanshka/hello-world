from setuptools import find_packages, setup
from typing import List

# Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.2ins"
AUTHOR="Shivansh Kaushal"
DESCRIPTION="This is my first end to end project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement mentioned in requirements.txt
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()  #.remove("-e .")

setup(
    name = PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,    # find_packages()
    install_requires=get_requirements_list()
)

if __name__=="__main__":
    print(get_requirements_list())