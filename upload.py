
import sys,os

python   = sys.executable
filepath = os.path.realpath(__file__)
projpath = os.path.dirname(filepath)
dist = os.path.join(projpath,'dist')

os.system('rm -rf {}/*'.format(dist))
os.system('{} setup.py sdist'.format(python))
os.system('twine upload dist/*')
