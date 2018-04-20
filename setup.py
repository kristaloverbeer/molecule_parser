from setuptools import setup, find_packages

setup(
    name='molecule-parser',
    version='1.0',
    author='Emeric BRIS',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['setuptools'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    scripts=['bin/molecule-parser']
)
