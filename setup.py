from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="autocommit",
    version="0.1.0",
    author="Julien Cassou",
    author_email="juliencassou91@gmail.com",
    description="Outil CLI pour générer des messages de commit avec Mistral",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/julien-cassou/autocommit",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "python-dotenv>=0.19.0",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "autocommit=autocommit.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)