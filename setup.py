from setuptools import setup, find_packages

setup(
    name="promptcraft",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "openai",
        "typer",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "promptcraft=promptcraft.cli:app",
        ],
    },
)
