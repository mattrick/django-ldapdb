#!/usr/bin/env python

from setuptools import setup

setup(
    name="django-ldapdb",
    version="0.4.0-hotfix",
    description=u"An LDAP database backend for Django",
    long_description=open('README.md').read(),
    url="https://github.com/mattrick/django-ldapdb",
    author="Kacper Banasik",
    author_email="jeremy.laine@m4x.org",
    packages=['ldapdb', 'ldapdb.backends', 'ldapdb.backends.ldap', 'ldapdb.models'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Programming Language :: Python",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: System :: Systems Administration :: Authentication/Directory :: LDAP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=['django', 'ldap', 'database'],
    install_requires=[
        'django>=1.2',
        'python-ldap>=2.0',
    ],
    setup_requires=[
        'setuptools>=0.6c11',
    ],
    tests_require=[
        'mockldap>=0.1',
    ],
    test_suite = 'manage.run_tests'
)
