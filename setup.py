from setuptools import setup, find_packages
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="TowerDefence",
    version="0.0.6",
    author="ArtemyBobkov & sevashasla",
    url="https://github.com/sevashasla/TowerDefence",
    long_description=read("README.md"),
    description="simple Tower-Defence game",
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    package_data={
        "TowerDefence": ["Assets/*", "Data/*"],
    },
    install_requires=[
        "numpy>=1.17.4",
        "pygame>=1.9.6"
    ],
    entry_points={
        'console_scripts': [
            'TowerDefence=TowerDefence:app',
        ],
    },

)
