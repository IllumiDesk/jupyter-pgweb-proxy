# jupyter-pgweb-proxy

This package was built using the [`illumidesk/jupyter-server-proxy` cookiecutter template](https://github.com/illumidesk/cookiecutter-jupyter-server-proxy).

## Requirements

- Python 3.6+
- Jupyter Notebook 6.0+
- JupyterLab 2.1+

This package executes the standard `pgweb` command. This command assumes the `pgweb` command is available in the environment's `PATH`.

### Install jupyter-pgweb-proxy

Install the package with pip:

```
pip install git+https://github.com/illumidesk/jupyter-pgweb-proxy.git
```

## Example

Try with binder:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/illumidesk/jupyter-pgweb-proxy/main?urlpath=pgweb)

Test locally:

```bash
docker build -t jupyter/pgweb .
docker build -it --rm -p 8888:8888 jupyter/pgweb
```

## Credits

- [`jupyter-server-proxy`](https://github.com/jupyterhub/jupyter-server-proxy)

## License

BSD 3-Clause
