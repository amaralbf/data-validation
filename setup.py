from setuptools import setup


def README():
    with open("README.md", "rt", encoding="utf-8") as f:
        readme = f.read()
    return readme


setup(
    name="data-validation",
    version="0.1.0",
    author="Bruno Amaral",
    author_email="amaralbf@gmail.com",
    url="https://github.com/amaralbf/data-validation",
    project_urls={"Documentation": "https://amaralbf.github.io/data-validation/"},
    description=("Lightweight data validation library for python."),
    long_description=README(),
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=["data_validation"],
    python_requires=">=3.7,<4.0",
    install_requires=[],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
