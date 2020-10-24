import setuptools
from os import path


# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setuptools.setup(
    name="jupyter-pgweb-proxy",
    version="0.2.0",
    url="https://github.com/illumidesk/jupyter-pgweb-proxy",
    author="IllumiDesk Team",
    description="hello@illumidesk.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=["jupyter", "pgweb", "jupyterhub", "jupyter-server-proxy"],
    classifiers=["Framework :: Jupyter"],
    install_requires=[
        "jupyter-server-proxy>=1.5.0",
    ],
    entry_points={
        "jupyter_serverproxy_servers": [
            "pgweb = jupyter_pgweb_proxy:setup_pgweb",
        ]
    },
    package_data={
        "jupyter_pgweb_proxy": ["icons/pgweb.svg"],
    },
)
