import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="API REST GildedRose",
    version="0.0.1",
    author="MateoGarciaG, Pau Llinàs Amat",
    author_email="mgarciag@cifpfbmoll.eu, pllinas@cifpfbmoll.eu",
    description="API REST Flask example",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pau13-loop/Ollivander_double_db.git",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "alabaster==0.7.12",
        "aniso8601==9.0.1",
        "anyio==2.0.2",
        "appdirs==1.4.4",
        "argon2-cffi==20.1.0",
        "astroid==2.4.2",
        "async-generator==1.10",
        "atomicwrites==1.4.0",
        "attrs==20.3.0",
        "autopep8==1.5.6",
        "Babel==2.9.0",
        "backcall==0.2.0",
        "bleach==3.2.3",
        "bson==0.5.10",
        "certifi==2020.12.5",
        "cffi==1.14.4",
        "cfgv==3.2.0",
        "chardet==4.0.0",
        "click==7.1.2",
        "colorama==0.4.4",
        "decorator==4.4.2",
        "defusedxml==0.6.0",
        "distlib==0.3.1",
        "dnspython==2.1.0",
        "docopt==0.6.2",
        "docutils==0.16",
        "dominate==2.6.0",
        "email-validator==1.1.2",
        "entrypoints==0.3",
        "fett==0.3.2",
        "filelock==3.0.12",
        "Flask==1.1.2",
        "Flask-Bootstrap==3.3.7.1",
        "Flask-Cors==3.0.10",
        "flask-expects-json==1.5.0",
        "Flask-json-schema==0.0.5",
        "Flask-Login==0.5.0",
        "flask-marshmallow==0.14.0",
        "flask-mongoengine==1.0.0",
        "Flask-PyMongo==2.3.0",
        "Flask-RESTful==0.3.8",
        "Flask-SQLAlchemy==2.5.1",
        "Flask-WTF==0.14.3",
        "gitdb==4.0.7",
        "GitPython==3.1.14",
        "greenlet==1.0.0",
        "identify==2.2.2",
        "imagesize==1.2.0",
        "importlib-metadata==3.10.1",
        "iniconfig==1.1.1",
        "install==1.3.4",
        "ipykernel==5.3.4",
        "ipython==7.19.0",
        "ipython-genutils==0.2.0",
        "isort==5.6.4",
        "itsdangerous==1.1.0",
        "jedi==0.17.2",
        "Jinja2==2.11.3",
        "json5==0.9.5",
        "jsonschema==3.2.0",
        "jupyter-client==6.1.7",
        "jupyter-core==4.6.3",
        "jupyter-server==1.2.2",
        "jupyterlab==3.0.6",
        "jupyterlab-pygments==0.1.2",
        "jupyterlab-server==2.1.3",
        "lazy-object-proxy==1.4.3",
        "MarkupSafe==1.1.1",
        "marshmallow==3.11.1",
        "marshmallow-sqlalchemy==0.24.2",
        "mccabe==0.6.1",
        "mistune==0.8.4",
        "mongoengine==0.23.0",
        "mongomock==2.3.0",
        "mypy-extensions==0.4.3",
        "nbclassic==0.2.6",
        "nbclient==0.5.1",
        "nbconvert==6.0.7",
        "nbformat==5.1.2",
        "nest-asyncio==1.5.1",
        "networkx==2.5.1",
        "nodeenv==1.5.0",
        "notebook==6.2.0",
        "packaging==20.9",
        "pandocfilters==1.4.3",
        "parso==0.7.1",
        "pathspec==0.8.1",
        "pbr==5.5.1",
        "pickleshare==0.7.5",
        "pluggy==0.13.1",
        "pre-commit==2.11.1",
        "prometheus-client==0.9.0",
        "prompt-toolkit==3.0.8",
        "py==1.10.0",
        "pycodestyle==2.7.0",
        "pycparser==2.20",
        "Pygments==2.8.1",
        "pylint==2.6.0",
        "pymongo==3.11.3",
        "PyMySQL==1.0.2",
        "pyparsing==2.4.7",
        "pyrsistent==0.17.3",
        "pytest==6.2.3",
        "python-dateutil==2.8.1",
        "python-jsonrpc-server==0.3.4",
        "pytz==2021.1",
        "pywin32==228",
        "pywinpty==0.5.7",
        "PyYAML==5.4.1",
        "pyzmq==19.0.2",
        "rand-string==0.50",
        "regex==2021.4.4",
        "requests==2.25.1",
        "Send2Trash==1.5.0",
        "sentinels==1.0.0",
        "six==1.15.0",
        "smmap==4.0.0",
        "sniffio==1.2.0",
        "snooty-lextudio==1.8.10.dev0",
        "snowballstemmer==2.1.0",
        "Sphinx==3.5.4",
        "sphinxcontrib-applehelp==1.0.2",
        "sphinxcontrib-devhelp==1.0.2",
        "sphinxcontrib-htmlhelp==1.0.3",
        "sphinxcontrib-jsmath==1.0.1",
        "sphinxcontrib-qthelp==1.0.3",
        "sphinxcontrib-serializinghtml==1.1.4",
        "SQLAlchemy==1.4.7",
        "stevedore==3.3.0",
        "terminado==0.9.2",
        "testpath==0.4.4",
        "toml==0.10.2",
        "tornado==6.1",
        "traitlets==5.0.5",
        "typed-ast==1.4.3",
        "typing-extensions==3.7.4.3",
        "urllib3==1.26.4",
        "virtualenv==20.4.3",
        "visitor==0.1.3",
        "watchdog==1.0.2",
        "wcwidth==0.2.5",
        "webencodings==0.5.1",
        "Werkzeug==1.0.1",
        "wrapt==1.12.1",
        "WTForms==2.3.3",
        "zipp==3.4.1",
    ],
)
