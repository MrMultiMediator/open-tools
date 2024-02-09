from utils import write_top, write_bottom
import sys
import os

class pkg_dict(dict):
    def __init__(self, name):
        # String containing html code for this pkg
        self.name = name
        self.html = f'<div class="column">\n<h2> {name} </h2>\n<p>\n'

    def add_pkg_version_to_html(self, version=None):
        if version is None:
            self.html += '----------- <br>\n'
        else:
            self.html += f'{version} <br>\n'

    def finish_html(self):
        self.html += '</p>\n</div>\n'

class environment_dict(dict):
    def __init__(self, envs):
        self.current = None
        self.html = f'<div class="column">\n<h2> Packages </h2>\n<p>\n'

        for env in envs:
            self[env] = pkg_dict(env)
            with open(f"{env}.txt", 'r') as f:
                f.readline(); f.readline(); f.readline()

                for line in f:
                    l = line.split()
                    pkg = l[0]
                    version = l[1]

                    self[env][pkg] = version

    def set_current(self):
        """Set the 'current' environment to be the one with the most remaining
        packages. This is like the reference environment from which to parse
        the various packages."""

        pkgs = 0

        for env in self.values():
            if len(env.keys()) > pkgs:
                self.current = env
                pkgs = len(env.keys())

    def pkgs_remaining(self):
        for env in self.values():
            if len(env.keys()) > 0:
                return True

        return False

    def add_pkg_to_html(self, pkg):
        self.html += f"{pkg} <br>\n"

    def finish_html(self):
        for env in self.values():
            env.finish_html()

        self.html += '</p>\n</div>\n'

    def write_html(self, filename):
        with open(filename, 'a') as g:
            g.write(self.html)

            for env in self.values():
                g.write(env.html)

def conda_list_pkgs(envs):
    for env in envs:
        os.system(f"conda list -n {env} > {env}.txt")

def build_diff(envs_dict):
    envs_dict.set_current()
    ref_env = envs_dict.current

    # Look at all pkgs in ref_env
    for pkg in sorted(list(ref_env.keys())):
        envs_dict.add_pkg_to_html(pkg)

        # Find all environments that have this package
        for env in envs_dict.values():
            if pkg in env.keys():
                env.add_pkg_version_to_html(env[pkg])
                del env[pkg]
            else:
                env.add_pkg_version_to_html()

    if envs_dict.pkgs_remaining():
        build_diff(envs_dict)

if __name__ == '__main__':
    write_top('conda.html', len(sys.argv[1:]))

    conda_list_pkgs(sys.argv[1:])

    envs_dict = environment_dict(sys.argv[1:])

    build_diff(envs_dict)

    envs_dict.finish_html()
    envs_dict.write_html('conda.html')
    write_bottom('conda.html')

    #for env in envs_dict.keys():
    #    print(f"{env} : {envs_dict[env]}\n")