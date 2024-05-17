#!/usr/bin/python3
"""
This module is for web application deployment with Fabric.
"""
import os
from datetime import datetime
from fabric.api import env, local, put, run, runs_once


env.hosts = ["54.90.39.81", "34.207.253.250"]
"""The list of host server IP addresses."""


@runs_once
def do_pack():
    """
    This function archives the static files.
    """
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    current_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        current_time.year,
        current_time.month,
        current_time.day,
        current_time.hour,
        current_time.minute,
        current_time.second
    )
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        archize_size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, archize_size))
    except Exception:
        output = None
    return output


def do_deploy(archive_path):
    """
    This function deploys the static files to the host servers.
    Args:
        archive_path (str): The path to the archived static files.
    """
    if not os.path.exists(archive_path):
        return False
    fileName = os.path.basename(archive_path)
    folderName = fileName.replace(".tgz", "")
    folderPath = "/data/web_static/releases/{}/".format(folderName)
    success = False
    try:
        put(archive_path, "/tmp/{}".format(fileName))
        run("mkdir -p {}".format(folderPath))
        run("tar -xzf /tmp/{} -C {}".format(fileName, folderPath))
        run("rm -rf /tmp/{}".format(fileName))
        run("mv {}web_static/* {}".format(folderPath, folderPath))
        run("rm -rf {}web_static".format(folderPath))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folderPath))
        print('New version deployed!')
        success = True
    except Exception:
        success = False
    return success


def deploy():
    """
    This function archives and deploys the static files to the host servers.
    """
    archive_path = do_pack()
    return do_deploy(archive_path) if archive_path else False
