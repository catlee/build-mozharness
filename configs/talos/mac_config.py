ENABLE_SCREEN_RESOLUTION_CHECK = True

SCREEN_RESOLUTION_CHECK = {
    "name": "check_screen_resolution",
    "cmd": ["bash", "-c", "screenresolution get && screenresolution list && system_profiler SPDisplaysDataType"],
    "architectures": ["32bit", "64bit"],
    "halt_on_failure": False,
    "enabled": ENABLE_SCREEN_RESOLUTION_CHECK
}

import os
import socket

PYTHON = '/tools/buildbot/bin/python'
VENV_PATH = '%s/build/venv' % os.getcwd()

config = {
    "log_name": "talos",
    "buildbot_json_path": "buildprops.json",
    "installer_path": "installer.exe",
    "virtualenv_path": VENV_PATH,
    "pypi_url": "http://repos/python/packages/",
    "find_links": ["http://repos/python/packages/"],
    "pip_index": False,
    "use_talos_json": True,
    "exes": {
        'python': PYTHON,
        'virtualenv': [PYTHON, '/tools/misc-python/virtualenv.py'],
    },
    "title": os.uname()[1].lower().split('.')[0],
    "results_url": "http://graphs.mozilla.org/server/collect.cgi",
    "default_actions": [
        "clobber",
        "read-buildbot-config",
        "download-and-extract",
        "create-virtualenv",
        "install",
        "run-tests",
    ],
    "python_webserver": False,
    "webroot": '%s/../talos-data' % os.getcwd(),
    "populate_webroot": True,
    "run_cmd_checks_enabled": True,
    "preflight_run_cmd_suites": [
        SCREEN_RESOLUTION_CHECK,
    ],
    "postflight_run_cmd_suites": [
        SCREEN_RESOLUTION_CHECK,
    ],
}
