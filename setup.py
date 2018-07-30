from setuptools import setup, find_packages

setup(
	name="PyPITest",
	packages=["pypitest", "pypitest.foo"],
	entry_points="""
	[console_scripts]
	sad = pypitest.sad:main
	hoge = pypitest.foo.hoge:main
	""",
)
