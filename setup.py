from setuptools import setup, find_packages

setup(
    name="float_project",
    version="0.1.0",
    description="A latent-thought-based learning agent",
    author="Kai Simpson",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "sqlalchemy",
        "psycopg2-binary",  # Easier to install than psycopg2
        "cryptography",
        "celery",
        "redis",
        "python-dotenv",
        "pytest",
        "pytest-asyncio",
        "pandas",
        "networkx",
        "pygraphviz",
        "bcrypt",
        "pyjwt",
        "pyopenssl",
        "chromadb",
        "prometheus-flask-exporter",
        "alembic",
    ],
    extras_require={
        "frontend": [
            "vue-cli",
            "jinja2",
            "axios",
            "chart.js",
            "d3",
            "pyvis",
        ],
    },
    entry_points={
        "console_scripts": [
            "float-launch=app.main:run",  # Allows running the app via `float-launch`
        ],
    },
)
