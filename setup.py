from setuptools import setup, find_packages

setup(
    name="vtt_tech_public",
    version="0.1",
    packages=find_packages(),
    package_data={'': ['*.yaml', '*.yml', '*.gds']},
    include_package_data=True,
)
