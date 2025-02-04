"""setup.py file."""

import uuid

from setuptools import setup, find_packages
try:
    from pip._internal.req import parse_requirements
except ImportError:
    from pip.req import parse_requirements
__author__ = 'David Barroso <dbarrosop@dravetech.com>'

install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())
try:
    reqs = [str(ir.req) for ir in install_reqs]
except:
    reqs = [str(ir.requirement) for ir in install_reqs]

setup(
    name="napalm-fortios",
    version="0.4.1",
    packages=find_packages(),
    author="David Barroso",
    author_email="dbarrosop@dravetech.com",
    description="Network Automation and Programmability Abstraction Layer with Multivendor support",
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="https://github.com/napalm-automation/napalm-fortios",
    include_package_data=True,
    install_requires=reqs,
)
