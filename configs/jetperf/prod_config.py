# This is a template config file for jetperf production

config = {

    "datazilla_urls": ['https://datazilla.mozilla.org/jetperf'],

    "exes": {
        'python': '/tools/buildbot/bin/python',
        'virtualenv': ['/tools/buildbot/bin/python', '/tools/misc-python/virtualenv.py'],
    },

    "find_links": ["http://repos/python/packages"],
    "pip_index": False,

    "default_actions": [
        'clobber',
        'pull',
        'build',
        'download-and-extract',
        'create-virtualenv',
        'install',
        'test',
        'baseline',
        'report-tbpl-status'
        ],
}
