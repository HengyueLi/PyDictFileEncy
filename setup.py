
from setuptools import setup
setup(
    name='pydictfileency',
    version='2018.11.181',
    author='Hengyue Li',
    author_email='hengyue.li@hengyue.li',
    packages=['pydictfileency', 'pydictfileency.test'],
    url='https://github.com/HengyueLi/PyDictFileEncy',
    license='LICENSE.md',
    description='A simply API to encrypt the python dict and save it into a file.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=['certifi==2018.10.15', 'chardet==3.0.4', 'idna==2.7', 'Naked==0.1.31', 'pycrypto==2.6.1', 'PyYAML==3.13', 'requests==2.20.1', 'shellescape==3.4.1', 'urllib3==1.24.1'],
)
