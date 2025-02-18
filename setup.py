#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md', 'r', encoding='utf-8') as history_file:
    history = history_file.read()

requirements = ['paramiko>=2.7.1']

setup_requirements = []

test_requirements = []

setup(
    author="Stephen Baker",
    author_email='sbaker@adica.com.au',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    description="py_sftp uses sftp to transfer files from remote to local and vice-versa.",
    install_requires=requirements,
    license="MIT license",
    long_description_content_type='text/markdown',
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='sftp_py',
    name='sftp_py',
    packages=find_packages(include=['sftp_py', 'sftp_py.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/wanidala/sftp_py',
    version='0.2.1',
    zip_safe=False,
)
