# jupyter-pgweb-proxy

This package was built from the [`illumidesk/cookiecutter-jupyter-server-proxy`](https://github.com/illumidesk/cookiecutter-jupyter-server-proxy) template.

## Requirements

- Python 3.6+
- Jupyter Notebook 6.0+
- JupyterLab 2.1+

This package executes the standard `pgweb` command. This command assumes the `pgweb` command is available in the environment's `PATH`.

## What?

Check it out, [it's pretty sweet](https://github.com/sosedoff/pgweb).

## Quick Starts

### Launch with `binder`

This test requires you to have a database instance available as a public endpoint or installed within the notebook container itself.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/illumidesk/jupyter-pgweb-proxy/main?urlpath=pgweb)

### Run locally with `docker-compose`

```bash
make dev
```

1. Open your browser: http://localhost:8889
1. Click the `pgweb` item from the `New` dropdown in `Jupyter Classic` or click on the green `pgweb` icon in the Notebooks section in `Jupyter Lab`.
1. Connect with the `Scheme` or `Standard` option.

For example, with the `Scheme` option the string would look like so:

```bash
postgres://postgres:postgres@testdb:5432/postgres?sslmode=disable
```

### Cleanup

Stop services:

```bash
make dev-down
```

Remove images and running containers:

> **NOTE**: this will stop all running containers on the local, including those with the exit status.

```bash
make clean-all
```

## The Hard Way

### Create and Activate Environment

```bash
virtualenv -p python3 venv
source venv/bin/activate
```

### Install jupyter-pgweb-proxy

```bash
pip install git+https://github.com/illumidesk/jupyter-pgweb-proxy.git
```

### Enable jupyter-pgweb-proxy Extensions

1. For Jupyter Classic, activate the `jupyter-server-proxy` extension:

```bash
jupyter serverextension enable --sys-prefix jupyter_server_proxy
```

2. For Jupyter Lab, install the `@jupyterlab/server-proxy` extension:

```bash
jupyter labextension install @jupyterlab/server-proxy
jupyter lab build
```

3. Start Jupyter Classic or Jupyter Lab

4. Click on the `pgweb` icon from the Jupyter Lab Launcher or the `pgweb` item from the `New` dropdown in Jupyter Classic.

5. Connect to your database as instructed in the [Quickstart](#quickstart) section.

## Credits

- [`jupyter-server-proxy`](https://github.com/jupyterhub/jupyter-server-proxy)

## License

BSD 3-Clause
