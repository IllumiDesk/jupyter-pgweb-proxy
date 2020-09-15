c = get_config()


# load base config
load_subconfig("/etc/jupyter/jupyter_notebook_config_base.py")


# supports iframe and samesite cookies
c.NotebookApp.tornado_settings = {
    "headers": {"Content-Security-Policy": "frame-ancestors 'self' *"},
    "cookie_options": {"SameSite": "None", "Secure": True},
}
c.NotebookApp.allow_root = True
c.NotebookApp.allow_origin = "*"
c.NotebookApp.token = ""
c.NotebookApp.default_url = "/lab"
