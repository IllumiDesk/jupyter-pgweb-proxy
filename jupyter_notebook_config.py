c = get_config()


# load base config
load_subconfig("/etc/jupyter/jupyter_notebook_config_base.py")


# supports iframe and samesite cookies
c.NotebookApp.tornado_settings = {
    "headers": {"Content-Security-Policy": "frame-ancestors 'self' *"},
    "cookie_options": {"SameSite": "None", "Secure": True},
}

# allows running the notebook as root
c.NotebookApp.allow_root = True
<<<<<<< HEAD

# accepts any origin by default, change to add restrictions
c.NotebookApp.allow_origin = '*'

# add a token if you would like to run this notebook on a public network
c.NotebookApp.token = ''

# forward to jupyterlab by default
c.NotebookApp.default_url = '/lab'
=======
c.NotebookApp.allow_origin = "*"
c.NotebookApp.token = ""
c.NotebookApp.default_url = "/lab"
>>>>>>> 7c4467fc3bba33a2b0621bfada4178706ff2c324
