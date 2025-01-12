### template code - needs improvement.

from setuptools import setup, find_packages

setup(
    name="float,
    version="0.1.0",
    description="A latent-thought based learning agent",
    author="Kai Simpson",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "sqlalchemy",
        "psycopg2",
        "chromadb",
        "cryptography",
        "celery",
        "redis",
        "pytest",
        # Add all essential dependencies here
    ],
    entry_points={
        "console_scripts": [
            "float-launch=app.main:run",  # Allows running the app via `float-launch`
        ],
    },
)

### python setup.py develop
