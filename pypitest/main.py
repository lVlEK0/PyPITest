import sys, subprocess

update = {
	'pegpy': ('git+https://github.com/lVlEK0/pegpy.git', 'workspace'),
	'macaron': ('git+https://github.com/lVlEK0/macaron.git', 'server'),
}

def main():
	try:
		argv = sys.argv
		(url, branch) = update[argv[1]]
		if len(argv) > 2:
			branch = argv[2]
		subprocess.check_call(['pip3', 'install', '-U'] + [url + '@' + branch])
	except:
		pass

if __name__ == '__main__':
	main()
