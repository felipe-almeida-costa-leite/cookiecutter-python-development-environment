# coding=latin-1
"""
File is generated by cookie cutter before project creation
"""
import os
import sys
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def install_pkgs_pip(pkg: str) -> bool:
    """
    Install package name

    Parameter
        :param pkg: Name from pip package
        :type pkg: str

    Return

    Exemple
        >>> install_pkgs_pip('virtualenv')
        True
    """
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', pkg])
        return True
    except KeyboardInterrupt:
        return False


def create_virtual_env(project_name: str = '{{ cookiecutter.projeto_nome_curto }}') -> bool:
    """
    Create virtual env from project

    Parameter

    Return

    Exemple
        >>> create_virtual_env()
        True
    """
    try:
        os.system(f'virtualenv .venv --prompt "({project_name}) "')
        return True
    except KeyboardInterrupt:
        return False


def active_and_install_packages_pip() -> bool:
    """
    Activate virtualenv and install package pip in virtualenv

    Parameter

    Return

    """
    try:
        os.system(f'. .venv/bin/activate &&'
                  f'pip install flake8 &&'
                  f'pip install pep8-naming &&'
                  f'pip install pylint &&'
                  f'pip install black &&'
                  f'pip install mypy &&'
                  f'pip install pydocstyle &&'
                  f'pip install pre-commit &&'
                  f'pip install Sphinx'
                  )
        return True
    except KeyboardInterrupt:
        return False


def activate_sphinx() -> bool:
    """
    Activate sphinx in docs directory

    Parameter

    Return
        :return: Returns True if the process was successful or False if not
        :rtype: bool

    Example
        >>> activate_sphinx()
        True

    """
    try:
        os.system('. .venv/bin/activate &&'
                  'cd docs &&'
                  'sphinx-quickstart')
        return True
    except KeyboardInterrupt:
        return False


def activate_pre_commit() -> bool:
    """
    Activate Pre Commit

    Parameter

    Return

    Example
        >>> activate_pre_commit()
        True

    """
    try:
        os.system('. .venv/bin/activate && pre-commit install')
        return True
    except KeyboardInterrupt:
        return False


def activate_git_repository() -> bool:
    """
    Activate Git Remote Repository

    Parameter

    Return

    Example
        >>> activate_git_repository()
        True

    """
    try:
        os.system('git init &&'
                  'git remote add -f -t {{cookiecutter.repositorio_branch_principal}} -m {{cookiecutter.repositorio_branch_principal}} origin {{cookiecutter.repositorio_url}}')
        return True
    except KeyboardInterrupt:
        return False


def change_conf_sphinx() -> bool:
    """
    Change Conf Sphinx

    Parameter

    Return

    Example
        >>> change_conf_sphinx()
        True

    """
    try:
        os.system('rm -rfv docs/conf.py &&'
                  'mv conf.py docs/')
        return True
    except KeyboardInterrupt:
        return False


if __name__ == '__main__':
    install_pkgs_pip('virtualenv')
    create_virtual_env()
    active_and_install_packages_pip()
    activate_git_repository()
    activate_pre_commit()
    activate_sphinx()
