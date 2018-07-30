from setuptools import setup

setup(
	name="test",
	version="0.1.0",
	packages=['test'],
	url="https://github.com/IVIEK0/PyPITest.git",
	description="Test for PyPI",
	install_requires=['setuptools'],
	entry_points={
		'console_scripts': [
			'sad = test.test:main'
		]
	}
)
