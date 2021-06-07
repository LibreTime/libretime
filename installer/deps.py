#!/usr/bin/env python3

from argparse import ArgumentParser

SYSTEMS = ("buster", "stretch", "bionic", "xenial")
FORMATS = ("list", "line", "table")

parser = ArgumentParser()
parser.add_argument(
    "system",
    choices=SYSTEMS,
    help="retrieve dependencies for the chosen system",
)
parser.add_argument(
    "-f",
    "--format",
    choices=FORMATS,
    help="print dependencies in a specific format",
    default="table",
)
args = parser.parse_args()

apt = {
    ## Analyzer ##
    "ecasound": ("buster", "stretch", "bionic", "xenial"),
    "flac": ("buster", "stretch", "bionic", "xenial"),
    "gcc": ("buster", "bionic", "xenial"),
    "gir1.2-gtk-3.0": ("buster", "bionic", "xenial"),
    "gstreamer1.0-plugins-bad": ("buster", "stretch", "bionic", "xenial"),
    "gstreamer1.0-plugins-good": ("buster", "stretch", "bionic", "xenial"),
    "gstreamer1.0-plugins-ugly": ("buster", "stretch", "bionic", "xenial"),
    "lame": ("buster", "stretch", "bionic", "xenial"),
    "pkg-config": ("buster", "bionic", "xenial"),
    "silan": ("buster", "bionic", "xenial"),
    "vorbis-tools": ("buster", "stretch", "bionic", "xenial"),
    "vorbisgain": ("buster", "stretch", "bionic", "xenial"),
    ## API ##
    "uwsgi-plugin-python3": ("buster", "stretch", "bionic", "xenial"),
    "uwsgi": ("buster", "stretch", "bionic", "xenial"),
    ## Global ##
    "apache2": ("buster", "stretch", "bionic", "xenial"),
    "icecast2": ("buster", "stretch", "bionic", "xenial"),
    "postgresql-client": ("buster", "stretch", "bionic", "xenial"),
    "postgresql": ("buster", "stretch", "bionic", "xenial"),
    "rabbitmq-server": ("buster", "stretch", "bionic", "xenial"),
    ## Installer ##
    "xmlstarlet": ("buster", "stretch", "bionic", "xenial"),
    ## Legacy ##
    "libapache2-mod-php7.0": ("stretch", "xenial"),
    "libapache2-mod-php7.2": ("bionic"),
    "libapache2-mod-php7.3": ("buster"),
    "php-amqplib": ("buster", "stretch"),
    "php-apcu": ("buster", "stretch", "bionic", "xenial"),
    "php-bcmath": ("bionic", "xenial"),
    "php-mbstring": ("bionic", "xenial"),
    "php-pear": ("buster", "stretch", "bionic", "xenial"),
    "php7.0-bcmath": ("stretch"),
    "php7.0-curl": ("stretch", "xenial"),
    "php7.0-dev": ("stretch"),
    "php7.0-gd": ("stretch", "xenial"),
    "php7.0-mbstring": ("stretch"),
    "php7.0-pgsql": ("stretch", "xenial"),
    "php7.0": ("stretch", "xenial"),
    "php7.2-curl": ("bionic"),
    "php7.2-gd": ("bionic"),
    "php7.2-pgsql": ("bionic"),
    "php7.2": ("bionic"),
    "php7.3-bcmath": ("buster"),
    "php7.3-curl": ("buster"),
    "php7.3-dev": ("buster"),
    "php7.3-gd": ("buster"),
    "php7.3-mbstring": ("buster"),
    "php7.3-pgsql": ("buster"),
    "php7.3": ("buster"),
    ## Liquidsoap ##
    "libao-ocaml": ("buster", "stretch", "bionic", "xenial"),
    "libcairo2-dev": ("buster", "bionic", "xenial"),
    "libcamomile-ocaml-data": ("buster", "stretch", "bionic", "xenial"),
    "libfaad2": ("buster", "stretch", "bionic", "xenial"),
    "libgirepository1.0-dev": ("buster", "bionic", "xenial"),
    "libglib2.0-dev": ("buster", "bionic", "xenial"),
    "libmad-ocaml": ("buster", "stretch", "bionic", "xenial"),
    "libopus0": ("buster", "stretch", "bionic", "xenial"),
    "libportaudio2": ("buster", "stretch", "bionic", "xenial"),
    "libpq-dev": ("buster", "stretch", "bionic", "xenial"),
    "libpulse0": ("buster", "stretch", "bionic", "xenial"),
    "libsamplerate0": ("buster", "stretch", "bionic", "xenial"),
    "libsoundtouch-ocaml": ("buster", "stretch", "bionic", "xenial"),
    "libtaglib-ocaml": ("buster", "stretch", "bionic", "xenial"),
    "libvo-aacenc0": ("buster", "stretch"),
    "liquidsoap-plugin-alsa": ("bionic", "xenial"),
    "liquidsoap-plugin-ao": ("bionic", "xenial"),
    "liquidsoap-plugin-faad": ("bionic", "xenial"),
    "liquidsoap-plugin-flac": ("bionic", "xenial"),
    "liquidsoap-plugin-icecast": ("bionic", "xenial"),
    "liquidsoap-plugin-lame": ("bionic", "xenial"),
    "liquidsoap-plugin-mad": ("bionic", "xenial"),
    "liquidsoap-plugin-ogg": ("bionic", "xenial"),
    "liquidsoap-plugin-portaudio": ("bionic", "xenial"),
    "liquidsoap-plugin-pulseaudio": ("bionic", "xenial"),
    "liquidsoap-plugin-taglib": ("bionic", "xenial"),
    "liquidsoap-plugin-voaacenc": ("bionic", "xenial"),
    "liquidsoap-plugin-vorbis": ("bionic", "xenial"),
    "liquidsoap": ("buster", "stretch", "bionic", "xenial"),
    "mpg123": ("buster", "stretch", "bionic", "xenial"),
    "patch": ("buster", "stretch", "bionic", "xenial"),
    ## Misc ##
    "build-essential": ("bionic", "xenial"),
    "coreutils": ("buster", "stretch", "bionic", "xenial"),
    "curl": ("buster", "stretch", "bionic", "xenial"),
    "git": ("buster", "stretch"),
    "libffi-dev": ("bionic", "xenial"),
    "libssl-dev": ("bionic", "xenial"),
    "lsb-release": ("buster", "stretch", "bionic", "xenial"),
    "lsof": ("buster", "stretch", "bionic", "xenial"),
    "pwgen": ("buster", "stretch", "bionic", "xenial"),
    "systemd-sysv": ("buster", "stretch"),
    "sysvinit-utils": ("bionic", "xenial"),
    "unzip": ("buster", "stretch", "bionic", "xenial"),
    "zip": ("buster", "stretch", "bionic", "xenial"),
    ## Python ##
    "python3-cairo": ("buster", "stretch", "bionic", "xenial"),
    "python3-dev": ("buster", "bionic", "xenial"),
    "python3-gi-cairo": ("buster", "bionic", "xenial"),
    "python3-gi": ("buster", "bionic", "xenial"),
    "python3-gst-1.0": ("buster", "stretch", "bionic", "xenial"),
    "python3-pika": ("buster", "stretch", "bionic", "xenial"),
    "python3-pip": ("buster", "stretch", "bionic", "xenial"),
    "python3-virtualenv": ("buster", "stretch", "bionic", "xenial"),
    "python3": ("buster", "stretch", "bionic", "xenial"),
}


def fixed_length(value, width=40, sep=" "):
    return value + (sep * (width - len(value))) + (sep * 4)


if args.format in ("list", "line"):
    sep = " " if args.format == "line" else "\n"
    print(
        sep.join(pkg for pkg, targets in sorted(apt.items()) if args.system in targets)
    )

elif args.format == "table":
    max_key_length = max(len(pkg) for pkg in apt)

    for pkg, targets in sorted(apt.items()):
        row = fixed_length(pkg, max_key_length)
        for system in SYSTEMS:
            row += fixed_length(system if system in targets else "", len(system))
        print(row)
