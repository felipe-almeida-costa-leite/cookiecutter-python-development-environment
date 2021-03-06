# coding=latin-1
"""
File is generated by cookie cutter before project creation
"""
import os
import sys
import subprocess
import logging

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
logging.basicConfig(format='%(asctime)s -%(levelname)s - %(message)s', level=logging.INFO)


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
        logging.info(f'Package: {pkg} intalled successfully')
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
        logging.info(f'Environment Virtual: {project_name} create successfully')
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
                  f'pip install -r requirements.txt'
                  )
        logging.info(f'Package from Requirements: installed successfully')
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
                  'sphinx-quickstart -q --no-sep -p {{cookiecutter.projeto_nome_curto}} -a "{{cookiecutter.projeto_nome_curto}}" -v "0.0.0" -l pt_BR &&'
                  'rm -rfv conf.py &&'
                  'cd .. &&'
                  'cp conf.py docs/ &&'
                  'rm -rfv conf.py')
        logging.info(f'Sphinx: start successfully')
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
        logging.info(f'Pre Commit: start successfully')
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
        os.system('git init')
        os.system('git remote add -f -t {{cookiecutter.repositorio_branch_principal}} -m {{cookiecutter.repositorio_branch_principal}} origin {{cookiecutter.repositorio_url}}')
        os.system('git checkout -f main')
        os.system('git checkout -b develop main')
        logging.info(f'Git: Start successfully')
        return True
    except KeyboardInterrupt:
        return False


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    install_pkgs_pip('virtualenv')
    create_virtual_env()
    active_and_install_packages_pip()
    activate_git_repository()
    activate_pre_commit()
    activate_sphinx()
