"""Packaging logic for tunegen."""
import configparser
import pathlib
import re

from setuptools import setup


def _get_package_name_from_setup_config() -> str:
    config = configparser.ConfigParser()
    config.read("setup.cfg")
    return config["metadata"]["name"]


def _find_version() -> str:
    """Get the version string from the top-level __init__.py file."""
    package_name = _get_package_name_from_setup_config()
    top_level_init_file_path = pathlib.Path(package_name, "__init__.py")
    with top_level_init_file_path.open(encoding="utf8") as f:
        version_match = re.search(r"__version__ = \"(.*?)\"", f.read())
    if version_match:
        return version_match.group(1)
    raise RuntimeError(f"Unable to find version string in {top_level_init_file_path}.")


setup(version=_find_version())
