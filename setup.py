from setuptools import setup, find_packages

setup(
	name="PyPITest",
	version="0.1.0",
	packages=["pypitest"],
	url="https://github.com/IVIEK0/PyPITest.git",
	description="Test for PyPI",
	install_requires=['setuptools'],
	entry_points="""
	[console_scripts]
	sad = pypi.sad:main
	hoge = pypi.foo.hoge:main
	""",
)
