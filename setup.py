from setuptools import setup, find_packages

setup(name="pypitest",
	version="0.1.0",
	description="Test for PyPI",
	url="https://github.com/IVIEK0/PyPITest.git",
	packages=['test', 'test.foo'],
	install_requires=['setuptools',],
	entry_points={
		'console_scripts': [
			'happy = test.foo.hoge:main'
			'sad = test.fuga:main'
		]
	}
)

