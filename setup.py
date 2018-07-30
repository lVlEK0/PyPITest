from setuptools import setup, find_packages

setup(
	name="pypi",
	version="0.1.0",
	packages=find_packages(),
	url="https://github.com/IVIEK0/PyPITest.git",
	description="Test for PyPI",
	install_requires=['setuptools'],
	entry_points="""
	[console_scripts]
	pypi = pypi.pypi:main
	hoge = pypi.foo.hoge:main
	""",
)
