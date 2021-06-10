import datetime
import json
import logging
import subprocess
import traceback

from .analyzer import Analyzer
from .utils import run_command


class CuePointAnalyzer(Analyzer):
    """This class extracts the cue-in time, cue-out time, and length of a track using ffmpeg."""

    FFMPEG_EXECUTABLE = "ffmpeg"

    @staticmethod
    def analyze(filepath, metadata):
        """
        Extracts the cue-in and cue-out times along and sets the file duration based on that.
        The cue points are there to skip the silence at the start and end of a track, and are determined
        using "ffmpeg", which analyzes the loudness in a track.

        :param filepath: The full path to the file to analyzer
        :param metadata: A metadata dictionary where the results will be put
        :return: The metadata dictionary
        """

        command = [
            CuePointAnalyzer.FFMPEG_EXECUTABLE,
            "-i",
            filepath,
            "-vn",
            "-filter",
            "highpass=frequency=1000",
            "-filter",
            "silencedetect=noise=0.9:duration=1",
            "-f",
            "null",
            "/dev/null",
            "-hide_banner",
            "-nostats",
        ]

        try:
            calculate_result = run_command(command)
            out = calculate_result.stderr

            result = filter(
                lambda line: line.startswith("[silencedetect"),
                out.splitlines(),
            )
            result = map(
                lambda line: line[33:],
                result,
            )

            starts, ends = [], []
            for line in result:
                parts = line.split()
                if parts[0].startswith("silence_start"):
                    starts.append(parts[1])
                elif parts[0].startswith("silence_end"):
                    ends.append(parts[1])

            if len(starts) != len(ends):
                # TODO: Weird error
                pass

            sorted_starts, sorted_ends = sorted(starts), sorted(ends)

            first = (sorted_starts[0], sorted_ends[0])
            last = (sorted_starts[-1], sorted_ends[-1])
            if first == last:
                # TODO: Handle
                pass

            print(first)
            print(last)

        except Exception as exception:
            logging.warning(exception)

        return metadata
