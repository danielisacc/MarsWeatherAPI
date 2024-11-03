from setuptools import setup, find_packages

setup(
    name='MarsWeatherPkg',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'matplotlib',
        'pandas'
    ],
    description='A package to interact with NASA InSight API',
    author='Daniel Delavega',
    author_email='daniel.delavega.dev@gmail.com',
    url='https://github.com/danielisacc/mars-weather-app'
)
