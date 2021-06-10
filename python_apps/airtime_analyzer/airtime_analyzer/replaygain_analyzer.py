import logging
import os
import re
import subprocess
from os import PathLike

from .analyzer import Analyzer
from .utils import run_command


class ReplayGainAnalyzer(Analyzer):
    """This class extracts the replay gain using ffmpeg."""

    FFMPEG_EXECUTABLE = "ffmpeg"
    FFPROBE_EXECUTABLE = "ffprobe"

    @staticmethod
    def analyze(filename, metadata):
        """
        Extracts the Replaygain loudness normalization factor of a track.

        :param filename: The full path to the file to analyzer
        :param metadata: A metadata dictionary where the results will be put
        :return: The metadata dictionary
        """
        # See https://github.com/savonet/liquidsoap/blob/main/scripts/extract-replaygain

        # First probe for existing replaygain metadata.
        command = [ReplayGainAnalyzer.FFPROBE_EXECUTABLE, filename]
        try:
            probe_result = run_command(command)

            track_gain_match = re.search(
                r".*REPLAYGAIN_TRACK_GAIN: ([-+]?[0-9]+\.[0-9]+) dB.*",
                probe_result.stderr,
            )

            if track_gain_match:
                metadata["replay_gain"] = float(track_gain_match.group(1))
                return metadata

        except Exception as exception:
            logging.warning(exception)

        # We didn't find replaygain metadata while probing, calculate it.
        command = [
            ReplayGainAnalyzer.FFMPEG_EXECUTABLE,
            "-i",
            filename,
            "-vn",
            "-filter",
            "replaygain",
            "-f",
            "null",
            "/dev/null",
            "-hide_banner",
            "-nostats",
        ]
        try:
            calculate_result = run_command(command)

            track_gain_match = re.search(
                r".* track_gain = ([-+]?[0-9]+\.[0-9]+) dB.*", calculate_result.stderr
            )

            if track_gain_match:
                metadata["replay_gain"] = float(track_gain_match.group(1))
        except Exception as exception:
            logging.warning(exception)

        return metadata
