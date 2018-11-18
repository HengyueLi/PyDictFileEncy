
import sys,os

python   = sys.executable
filepath = os.path.realpath(__file__)
projpath = os.path.dirname(filepath)
dist = os.path.join(projpath,'dist')




install_requires = [ jc for jc in open('requirements.txt').read().split('\n') if len(jc)>1  ]

setupcontext = '''
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
    install_requires={},
)
'''.format(install_requires)



os.system('rm -rf {}/*'.format(dist))
os.system('rm -rf setup.py')
with open('setup.py','w') as f:
    f.write(setupcontext)
os.system('{} setup.py sdist'.format(python))
os.system('twine upload dist/*')
