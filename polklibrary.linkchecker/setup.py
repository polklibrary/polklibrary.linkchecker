# -*- coding: utf-8 -*-
"""Installer for the polklibrary.linkchecker package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='polklibrary.linkchecker',
    version='1.0a1',
    description="Utility to cChecks all links on page.",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='hietpasd',
    author_email='hietpasd@uwosh.edu',
    url='https://github.com/collective/polklibrary.linkchecker',
    project_urls={
        'PyPI': 'https://pypi.python.org/pypi/polklibrary.linkchecker',
        'Source': 'https://github.com/collective/polklibrary.linkchecker',
        'Tracker': 'https://github.com/collective/polklibrary.linkchecker/issues',
        # 'Documentation': 'https://polklibrary.linkchecker.readthedocs.io/en/latest/',
    },
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['polklibrary'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires="==2.7",
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'z3c.jbot',
        'Products.GenericSetup>=1.8.2',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            'plone.testing>=5.0.0',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = polklibrary.linkchecker.locales.update:update_locale
    """,
)
