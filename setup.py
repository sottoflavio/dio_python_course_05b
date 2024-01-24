from setuptools import setup, find_packages

with open('readme.md', 'r') as f:
    page_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name = 'package_name',
    version = '0.0.1',
    author = 'my_name',
    author_email= 'my@email.com',
    description='my very short description',
    long_description=page_description,
    long_description_content_type='text/markdown',
    url='my_github',
    packages=find_packages(),
    install_requirements=requirements,
    python_requires='>=3.8',
)