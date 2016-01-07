# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='kanban',
    version=version,
    description='Kanban view to plug-into various doctypes, especially Projects and CRM',
    author='Alec Ruiz-Ramon',
    author_email='alec.ruizramon@me.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
