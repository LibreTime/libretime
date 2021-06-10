import logging
from subprocess import CalledProcessError, run
from typing import List


def run_command(command: List[str], check=True):
    try:
        return run(
            command,
            check=check,
            # TODO: Replace std* with capture_output after dropping <python3.7
            # capture_output=True,
            stdout=PIPE,
            stderr=PIPE,
            # TODO: Replace universal_newlines with text after dropping <python3.7
            # text=True,
            universal_newlines=True,
        )

    except OSError as exception:  # executable was not found
        logging.warning(
            "Failed to run: {executable} - {exception}. Is {executable} installed?".format(
                executable=command[0],
                exception=exception,
            )
        )

    except CalledProcessError as exception:  # returned an error code
        raise Exception("{}\n{}".format(exception, exception.stderr)) from exception
