#!/usr/bin/env python
from __future__ import print_function
import argparse
import ast
import errno
from fnmatch import fnmatch
import os
import sys



def splitall(path):
    """From:

    https://www.safaribooksonline.com/library/view/python-cookbook/0596001673/ch04s16.html
    """
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path:  # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts


parser = argparse.ArgumentParser(description="Build docs based on module level docstrings.",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-i", "--input",
                    help="python package to read from")
parser.add_argument("-o", "--output", default="./docs",
                    help='directory to output docs')
parser.add_argument("--ext", default="md",
                    help="file extension for docs, please leave off dot.")

args = parser.parse_args()



def rtfm():  # noqa
    if not args.input:
        print("")
        parser.print_help()
        print("")
        sys.exit(1)
    for root, dirs, files in os.walk(args.input):
        for f in files:
            if fnmatch(f, "*.py"):
                if fnmatch(os.path.basename(f), "__init__.py"):
                    identifier = "package"
                    output_filename = "README.md"
                else:
                    identifier = "module"
                    output_filename = "%s.%s" % (os.path.splitext(f)[0], args.ext)

                print("doc for %s: %s" %
                      (identifier, os.path.join(root, f).rstrip("/").replace("/", ".")))

                with open(os.path.join(root, f)) as py_file:
                    tree = ast.parse(py_file.read())

                relative = splitall(root)
                if len(relative) > 0:
                    relative.pop(0)

                output_dir = os.path.join(args.output, "/".join(relative))
                print(root, f)
                try:
                    os.makedirs(output_dir)
                except OSError as err:
                    if err.errno != errno.EEXIST:
                        raise err

                docfile_path = os.path.join(output_dir, output_filename)
                docstring = ast.get_docstring(tree)
                if not docstring:
                    print("...skipping, no docstring")
                else:
                    with open(docfile_path, "w") as f:
                        f.write(docstring)
                        print("...wrote", docfile_path)
