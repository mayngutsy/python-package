from setuptools import setup, find_packages

setup(
    name = 'python_package',
    version = '0.1',
    packages = find_packages(exclude = ['tests*']),
    license = 'MIT',
    description = 'my first python package',
    long_description = open('README.md').read(),
    install_requires = ['numpy'],
    url ='https://github.com/<username>/<package_name>',
    author = 'Moses Ubaku',
    author_email = 'mayngutsy@gmail.com'
)