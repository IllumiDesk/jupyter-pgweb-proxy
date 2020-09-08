import os
import shutil
import logging


logger = logging.getLogger(__name__)
logger.setLevel('INFO')


def setup_vscode():
    def _get_vscode_cmd(port):
        executable = 'code-server'
        if not shutil.which(executable):
            raise FileNotFoundError('Can not find code-server in PATH')
        
        # Start vscode in CODE_WORKINGDIR env variable if set
        # If not, start in 'current directory', which is $REPO_DIR in mybinder
        # but /home/jovyan (or equivalent) in JupyterHubs
        working_dir = os.getenv('CODE_WORKINGDIR', '.')

        extensions_dir = os.getenv('CODE_EXTENSIONSDIR', None)
        extra_extensions_dir = os.getenv('CODE_EXTRA_EXTENSIONSDIR', None)

        cmd = [
            executable,
            '--auth',
            'none',
            '--disable-telemetry',
            '--port=' + str(port),
        ]

        if extensions_dir:
            cmd += ['--extensions-dir', extensions_dir]

        if extra_extensions_dir:
            cmd += ['--extra-extensions-dir', extra_extensions_dir]

        cmd.append(working_dir)
        return cmd

def setup_pgweb():
    """Setup commands and icon paths and return a dictionary compatible
    with jupyter-server-proxy.
    """
    def _get_icon_path():
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'icons', 'pgweb.svg'
    )

    # Make sure executable is in $PATH
    def _get_pgweb_command(port):
        executable = 'pgweb'
        if not shutil.which(executable):
            raise FileNotFoundError('Can not find pgweb executable in $PATH')
        # Create working directory
        home_dir = os.environ.get('HOME') or '/home/jovyan'
        working_dir = f'{home_dir}/pgweb'
        if not os.path.exists(working_dir):
            os.makedirs(working_dir)
            logger.info("Created directory %s" % working_dir)
        else:    
            logger.info("Directory %s already exists" % working_dir)
        return ['pgweb', '--bind=0.0.0.0', '--listen=' + str(port)]
    
    return {
        'command': '_get_pgweb_command',
        'timeout': 20,
        'new_browser_tab': True,
        'launcher_entry': {
            'title': 'pgweb',
            'icon_path': _get_icon_path()
        },
    }
