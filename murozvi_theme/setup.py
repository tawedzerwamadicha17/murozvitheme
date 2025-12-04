from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# get version from __init__.py
from murozvi_theme import __version__ as version

setup(
    name="murozvi_theme",
    version=version,
    description="Corporate Branding Theme",
    author="Murozvi",
    author_email="mtawedzerwadonald17@gmail.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
