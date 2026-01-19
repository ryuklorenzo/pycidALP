from setuptools import setup, find_packages


setup(
    name="optativa_pycicd",
    version="1.0.0",
    author="Angel Lorenzo-Penalva Lozano",
    author_email="anglorloz@alu.edu.gva.es",
    description="Descripción de tu proyecto",
    packages=find_packages(),
    install_requires=[
        "pytest",
        "flake8",
    ],
)