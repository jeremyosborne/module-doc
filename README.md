# module-doc

Recurses through one directory of python code, attempting to copy the module
doc strings and paste them into more accessible docs (think markdown checked
into github).

    usage: module-doc [-h] [-i INPUT] [-o OUTPUT] [--ext EXT]

    optional arguments:
      -h, --help            show this help message and exit
      -i INPUT, --input INPUT
                            python package to read from (default: None)
      -o OUTPUT, --output OUTPUT
                            directory to output docs (default: ./docs)
      --ext EXT             file extension for docs, please leave off dot.
                            (default: md)


Install via pip:

    pip install git+https://github.com/jeremyosborne/module-doc.git
