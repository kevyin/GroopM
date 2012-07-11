from distutils.core import setup

setup(
    name='GroopM',
    version='0.0.1',
    author='Michael Imelfort',
    author_email='mike@mikeimelfort.com',
    packages=['groopm', 'groopm.test'],
    scripts=['bin/groopm.py','bin/groopm_utils.py'],
	url='http://pypi.python.org/pypi/GroopM/',
    license='LICENSE.txt',
    description='Metagenomic binning suite',
    long_description=open('README.txt').read(),
    install_requires=[
        "numpy >= 1.6.1",
        "scipy >= 0.10.1",
        "matplotlib >= 1.1.0",
    ],
)