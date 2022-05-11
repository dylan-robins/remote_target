#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8
#*****************************************************************************#

import pysftp

from remote_target.remote_conf import RemoteTargetConf


def push_updates(target: RemoteTargetConf):
    with pysftp.Connection(
        target.hostname,
        username=target.username,
        password=target.password,
        private_key=target.private_key,
    ) as sftp:
        if not sftp.exists(target.remote_directory):
            print(f"Creating directory {target.remote_directory} on remote...")
            sftp.makedirs(target.remote_directory)
        print(f"Uploading files...")
        sftp.put_r(target.local_root, target.remote_directory, preserve_mtime=True)
        print(f"Done.")
