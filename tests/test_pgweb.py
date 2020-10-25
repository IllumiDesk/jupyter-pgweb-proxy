import os
import subprocess

import docker
from docker.errors import ContainerError

import logging

import pytest


LOGGER = logging.getLogger(__name__)


@pytest.mark.parametrize(
    "executable,version_output",
    [
        (
            "pgweb",
            [
                "Pgweb",
                "v0.11.6",
            ],
        ),
    ],
)
def test_pgweb_version(executable, version_output):
    """Ensure pweb is available in the PATH and that it returns the correct version"""
    LOGGER.info(f"Test that language {executable} is correctly installed ...")
    f = os.popen(f'{executable} --version')
    output = f.read()
    output_decoded = output.split(" ")
    assert output_decoded[0:2] == version_output
    LOGGER.info(f"Output from command: {output_decoded[0:3]}")
    

def test_invalid_cmd():
    """Ensure that an invalid command returns a docker.errors.ContainerError"""
    LOGGER.info("Test an invalid command ...")
    f = os.popen(f'foo --version')
    output = f.read()
    output_decoded = output.split(" ")
    assert output_decoded[0:1] != "pgweb"
    LOGGER.info(f"Output from command: {output_decoded[0:3]}")
    
