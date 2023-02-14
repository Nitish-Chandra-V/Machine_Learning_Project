from setuptools import setup
from typing import List


#Declaring variables for setup funtions
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Nitish"
DESCRIPTION="FSDS Machine Learning Project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    
    #Description: This funtion is ging to return list of requirement
    #mention in requirements.txt requirement_file
    # Return this funtion is going to return a list which contain name of libraries mentioned in requirements.txt file

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()


setup(
name="housing-predictor",
version="0.0.1",
author="Nitish",
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()

)