# jupyter-pgweb-proxy

This package was built using the [`jupyter-server-proxy` cookiecutter template](https://github.com/illumidesk/cookiecutter-jupyter-server-proxy).

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/illumidesk/jupyter-pgweb-proxy/main?urlpath=pgweb)

## Requirements

- Python 3.6+
- Jupyter Notebook 6.0+
- JupyterLab 2.1+

This package executes the standard `pgweb` command. This command assumes the `pgweb` command is available in the environment's `PATH`.

### Install jupyter-pgweb-proxy

Install the package with pip:

```
pip install .
```

## Notes

- If you would like to use a docker container, you may use any of the [Jupyter docker-stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/) images.
- You may also run this package with `binder`.

## Credits

- [`jupyter-server-proxy`](https://github.com/jupyterhub/jupyter-server-proxy)

## License

BSD 3-Clause
