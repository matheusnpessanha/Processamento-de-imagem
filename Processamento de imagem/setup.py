from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing-Package",
    version="0.0.2",
    author="Matheus Nascimento Pessanha",
    author_email="matheuspessa@gmail.com",
    description="Test version - Image processing. This project belongs to Karina Tiemi Kato, Tech Lead, Machine Learning Engineer, Data Scientist Specialist at Take. This package is a demo for simulation of upload on the Test Pypi website, and it's from class of the Bootcamp developer full stack Python. E-mail:karinatkato@gmail.com.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matheusnpessanha/Pacote-de-Processamento-de-Imagens",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)