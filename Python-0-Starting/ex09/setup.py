from setuptools import setup, find_packages

setup(
    Name="ft_package",
    Version="0.0.1",
    Summary="A sample test package",
    Home="https://github.com/eagle/ft_package",
    author="kev",
    author_email="kthierry@42.fr",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        # Choisissez vos classificateurs comme il convient à votre package
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
