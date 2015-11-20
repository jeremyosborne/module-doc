from setuptools import setup

setup(
    name="module-doc",
    version="0.1.1",
    license="UNLICENSED",
    description="Simple module docstring to accessible doc files.",
    long_description=open("README.md").read(),
    author="Jeremy Osborne",
    author_email="jeremywosborne@gmail.com",
    url="https://github.com/jeremyosborne/module-doc",
    platforms="any",
    zip_safe=False,
    include_package_data=True,
    packages=[
        "module_doc",
    ],
    install_requires=[],
    scripts=['bin/module-doc'],
)
