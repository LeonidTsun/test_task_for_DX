from setuptools import setup, find_packages

setup(
    name="offers_sdk",
    version="0.1.0",
    description="Async Python SDK for Offers API",
    author="Leonid",
    packages=find_packages(),
    install_requires=[
        "httpx>=0.24.0",
    ],
    python_requires=">=3.8",
)
