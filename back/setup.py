#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = 'taiga-contrib-issue-colouring',
    version = "0.1",
    description = "Add colouring to issues (green/amber/red)",
    long_description = """We need colours on issues to display them in dashboards.
                          Initially, the colour should be set manually, but later
                          on, we can maybe alter them by workflow etc.""",
    keywords = 'taiga, issues, dashboard',
    author = 'Toni Mueller',
    author_email = 'dev@tonimueller.org',
    url = 'https://github.com/muellert/taiga-contrib-issue-colouring',
    license = 'AGPL',
    package_dir={'': 'src'},
    include_package_data = True,
    packages = find_packages(),
    install_requires=[],
    setup_requires = [
        'versiontools >= 1.9',
    ],
    classifiers = [
        "Programming Language :: Python",
        'Development Status :: 1 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
