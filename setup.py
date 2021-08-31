from setuptools import setup, find_namespace_packages

setup(
    name='personal_assistant_cli',
    version='1.0',
    description='A personal assistant that will make your life easier and \
help you unleash your creative potential. Join your inspired! Leave the \
routine to our assistant!',
    url='https://github.com/vita-olshevska/personal_assistant_cli/tree/dev',
    author='SpaceV',
    author_email='vaolshevska@gmail.com',
    maintainer='http://140.238.212.157/index.html',
    license='GNU General Public License',
    entry_points = {'personal_assistant_cli': ['personal_assistant_cli = personal_assistant_cli.main:main']},
    packages=find_namespace_packages()
)
