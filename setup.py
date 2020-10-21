import os
import setuptools

from setup_hooks import add_unittest_hooks

add_unittest_hooks()

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

# read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

setuptools.setup(
    name="neuralprophet",
    version="0.2.2",
    description="A simple yet customizable forecaster",
    author='Oskar Triebe',
    url="https://github.com/ourownstory/neural_prophet",
    packages=setuptools.find_packages(),
    python_requires=">=3",
    install_requires=requirements,
    extras_require={"dev": ["livelossplot>=0.5.3"], "live": ["livelossplot>=0.5.3"], },
    setup_requires=["flake8"],
    long_description=readme,
    long_description_content_type="text/markdown",
)
