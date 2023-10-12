"""Python setup.py for project_name package"""
from pathlib import Path

from setuptools import find_packages, setup


def read(*paths, **kwargs) -> str:
    return Path(*paths).read_text(encoding=kwargs.get('encoding', 'utf8')).strip()


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).splitlines(keepends=False)
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="hermaeus",
    version=read("VERSION"),
    python_requires=">3.9.0",
    description="project_description",
    # url="https://github.com/Leikt/riri",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Leikt Sol'Reihin",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements/main.txt"),
    # entry_points={
    #     "console_scripts": ["riri = riri.__main__:main"]
    # },
    extras_require={"test": read_requirements("requirements/testing.txt")},
)
