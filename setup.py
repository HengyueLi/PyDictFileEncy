from setuptools import setup

setup(
    name='pydictfileency',
    version='2018.11.18',
    author='Hengyue Li',
    author_email='hengyue.li@hengyue.li',
    packages=['pydictfileency', 'pydictfileency.test'],
    url='https://github.com/HengyueLi/PyDictFileEncy',
    license='LICENSE.md',
    description='A simply API to encrypt the python dict and save it into a file.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[ jc for jc in open('requirements.txt').read().split('\n') if len(jc)>1  ] ,
)
