#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8
#*****************************************************************************#

import argparse
import sys
from pathlib import Path

from remote_target import remote_conf, stfp_connection


def info(args: argparse.Namespace):
    """Displays information about the current remote_target configuration"""
    target_path = remote_conf.find_remote_target_file_in_parents(Path.cwd())
    if target_path is None:
        raise FileNotFoundError(f"Couldn't find '.remote_target' file in parents of {Path.cwd()}")
    
    print(f"Configuration loaded from {target_path}")
    target = remote_conf.RemoteTargetConf.load(target_path)
    print(target)

def init(args: argparse.Namespace):
    """Initializes a .remote_target file in the current working directory"""
    target_path = Path(".remote_target")
    print("Creating example .remote_target file in the current directory")
    remote_conf.RemoteTargetConf.create_default(target_path)
    
def push(args: argparse.Namespace):
    """Pushes the local files to the remote target"""
    target_path = remote_conf.find_remote_target_file_in_parents(Path.cwd())
    if target_path is None:
        raise FileNotFoundError(f"Couldn't find '.remote_target' file in parents of {Path.cwd()}")
    
    target = remote_conf.RemoteTargetConf.load(target_path)
    stfp_connection.push_updates(target)


def main():
    parser = argparse.ArgumentParser(
        prog="remote_target",
        description="A tool for automating software deployments and directory replication over sftp"
    )
    subparsers = parser.add_subparsers(
        required=True,
        title='subcommands',
    )

    # Create the argument parser for the 'info' command
    info_parser = subparsers.add_parser('info', help='Displays information about the current remote_target configuration')
    info_parser.set_defaults(func=info)

    # Create the argument parser for the 'init' command
    init_parser = subparsers.add_parser('init', help='Initializes a .remote_target file in the current working directory')
    init_parser.set_defaults(func=init)

    # Create the argument parser for the 'push' command
    init_parser = subparsers.add_parser('push', help='Pushes the local files to the remote target')
    init_parser.set_defaults(func=push)

    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
