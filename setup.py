from setuptools import setup

setup(
	name = 'PyPITest',
    version = '1.0.0',
    url = 'https://github.com/lVlEK0/PyPITest.git',
    license = 'Kusoge',
    author = 'Yutaka Kase',
    author_email = 'kaseyutaka.suffix@gmail.com',
    description = 'test for pip install git+',
    install_requires = ['setuptools'],
	packages = ["pypitest", "pypitest.foo"],
	entry_points = {
		'console_scripts': [
			'maniac = pypitest.sad.maniac:sub',
			'sad = pypitest.sad:kd',
			'hoge = pypitest.foo.hoge:main'
		]
	}
)
