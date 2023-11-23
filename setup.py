from setuptools import setup


setup(
    cffi_modules=["./ffibuild.py:ffi"],
    setup_requires = ['cffi'],
)
