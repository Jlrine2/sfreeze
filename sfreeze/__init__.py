from importlib.metadata import PackageNotFoundError, version

from freeze import s3_freeze, s3_thaw


try:
    __version__ = version(__name__)
except PackageNotFoundError:
    print('package is not installed!\n'
          'Install in editable/develop mode via (from the top of this repo):\n'
          '   python -m pip install -e .\n'
          'Or, to just get the version number use:\n'
          '   python setup.py --version')


__all__ = [
    's3_freeze',
    's3_thaw',
]
