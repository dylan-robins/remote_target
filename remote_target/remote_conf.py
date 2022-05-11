#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8
#*****************************************************************************#

from __future__ import annotations

import configparser
import os
from dataclasses import dataclass
from getpass import getuser
from pathlib import Path
from typing import Optional


@dataclass
class RemoteTargetConf:
    local_root: Path
    config: configparser.ConfigParser

    @classmethod
    def load(cls, target_file: Path) -> RemoteTargetConf:
        if not target_file.is_file():
            raise FileNotFoundError(f"{target_file} doesn't exist or is not accessible")


        # Load configuration from file
        config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
        config.read(target_file)

        return cls(
            local_root=target_file.parent,
            config=config,
        )

    @classmethod
    def create_default(cls, target_file: Path) -> RemoteTargetConf:
        if target_file.is_file():
            raise FileExistsError("Error: a .remote_target file already exists here!")

        home_dir = os.getenv("HOME")
        if home_dir is None or home_dir == '':
            home_dir = f"/home/{getuser()}"

        # Create configuration
        config = configparser.ConfigParser()
        config['DEFAULT'] = {
            'Hostname': 'url/to/server',
            'Username': getuser(),
            'PrivateKey': f'{home_dir}/.ssh/id_rsa',
            'RemoteDir': '/tmp',
        }
        with target_file.open('w') as configfile:
            config.write(configfile)



        return cls(
            local_root=target_file.parent,
            config=config,
        )

    def __repr__(self) -> str:
        return (
            f"hostname: {self.hostname}\n"
            f"username: {self.username}\n"
            f"password: {self.password}\n"
            f"private_key: {self.private_key}\n"
            f"remote_directory: {self.remote_directory}\n"
        )

    @property
    def hostname(self) -> str:
        return self.config["DEFAULT"]["Hostname"]

    @property
    def username(self) -> str:
        return self.config["DEFAULT"]["Username"]

    @property
    def password(self) -> Optional[str]:
        if "Password" in self.config["DEFAULT"]:
            return self.config["DEFAULT"]["Password"]
        else:
            return None

    @property
    def private_key(self) -> Optional[str]:
        if "PrivateKey" in self.config["DEFAULT"]:
            return self.config["DEFAULT"]["PrivateKey"]
        else:
            return None

    @property
    def remote_directory(self) -> str:
        return self.config["DEFAULT"]["RemoteDir"]

def find_remote_target_file_in_parents(start_path: Path) -> Optional[Path]:
    """
    Looks in the specified directory and all it's parents until one of two things happens:
    - It finds a file called '.target_file', which is then returned
    - It hits the filesystem root and returns None
    """

    # Trivial case: if file exists in start_path, just return it
    if (start_path / ".remote_target").is_file():
        return (start_path / ".remote_target")
    # Otherwise, recurse upwards
    parent = start_path.parent
    # Check if we've hit root of filesystem
    if parent == start_path:
        return None
    # If not, recurse upwards
    return find_remote_target_file_in_parents(parent)
