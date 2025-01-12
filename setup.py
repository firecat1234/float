from setuptools import setup, find_packages

setup(
    name="float_project",
    version="0.1.0",
    description="A latent-thought based learning agent",
    author="Kai Simpson",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "requests",
        "beautifulsoup4",
        "cryptography",
        "sqlalchemy",
        "celery",
        "redis",
        "prometheus-flask-exporter",
        "flask-jwt-extended",
        "flask-limiter",
        "apscheduler",
        "marshmallow",
        "psycopg2",
        "alembic",
        "python-dotenv",
        "pytest",
        "pytest-asyncio",
        "pandas",
        "networkx",
        "matplotlib",
        "sentence-transformers",
        "pygraphviz",
        "bcrypt",
        "pyjwt",
        "pyopenssl",
        "chromadb",
        "pip-tools",
    ],
    extras_require={
        "frontend": [
            "vue-cli",
            "jinja2",
            "axios",
            "chart.js",
            "d3",
            "pyvis",
        ]
    },
    entry_points={
        "console_scripts": [
            "float-launch=app.main:run",  # Allows running the app via `float-launch`
        ],
    },
)
