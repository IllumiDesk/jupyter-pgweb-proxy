import docker
from docker.errors import ContainerError

import logging

import pytest


LOGGER = logging.getLogger(__name__)


@pytest.mark.parametrize(
    "language,version_output",
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
def test_pgweb_version(language, version_output):
    """Ensure pweb is available in the PATH and that it returns the correct version"""
    LOGGER.info(f"Test that language {language} is correctly installed ...")
    client = docker.from_env()
    output = client.containers.run("illumidesk/pgweb:latest", f"{language} --version")
    output_decoded = output.decode("utf-8").split(" ")
    assert output_decoded[0:2] == version_output
    LOGGER.info(f"Output from command: {output_decoded[0:3]}")


def test_invalid_cmd():
    """Ensure that an invalid command returns a docker.errors.ContainerError"""
    with pytest.raises(ContainerError):
        LOGGER.info("Test an invalid command ...")
        client = docker.from_env()
        client.containers.run("illumidesk/pgweb", "foo --version")
