from setuptools import setup, find_packages

setup(name="pypitest",
	version="0.1.0",
	description="Test for PyPI",
	url="https://github.com/IVIEK0/PyPITest.git",
	packages=['pypitest'],
	install_requires=['setuptools',],
	entry_points={
		'console_scripts': [
			'sad = test.fuga:main'
		]
	}
)

