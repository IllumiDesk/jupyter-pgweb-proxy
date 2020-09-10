import os
import shutil
import logging


logger = logging.getLogger(__name__)
logger.setLevel("INFO")


def setup_pgweb():
    """Setup commands and icon paths and return a dictionary compatible
    with jupyter-server-proxy.
    """

    def _get_icon_path():
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "icons", "pgweb.svg"
        )

    # Make sure executable is in $PATH
    def _get_pgweb_command(port):
        executable = "pgweb"
        if not shutil.which(executable):
            raise FileNotFoundError("Can not find pgweb executable in $PATH")
        # Create working directory
        home_dir = os.environ.get("HOME") or "/home/jovyan"
        working_dir = f"{home_dir}/pgweb"
        if not os.path.exists(working_dir):
            os.makedirs(working_dir)
            logger.info("Created directory %s" % working_dir)
        else:
            logger.info("Directory %s already exists" % working_dir)
        return ["pgweb", "--bind=0.0.0.0", "--listen=" + str(port)]

    return {
        "command": _get_pgweb_command,
        "timeout": 20,
        "new_browser_tab": True,
        "launcher_entry": {"title": "pgweb", "icon_path": _get_icon_path()},
    }
