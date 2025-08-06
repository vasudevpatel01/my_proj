from setuptools import find_packages,setup

def get_requirement(file_path:str)-> list[str]:

    requirement = []

    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace("\n","") for req in requirement]

    return requirement







setup(
    name= "my_proj",
    version="0.0.1",
    author="Vasudev Patel",
    packages= find_packages(),
    install_req = get_requirement("requirement.txt")
    
)