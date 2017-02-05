from setuptools import setup, find_packages

setup(
    name="git-autosemver",
    version="1.0.0",
    description="Parse your git history to determine the next version number of your project",
    url="https://github.com/Varkal/git-autosemver",

    author="Romain Moreau",
    author_email="moreau.romain83@gmail.comm",

    license="MIT",

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
    ],

    keywords="development git semver ci ",

    packages=find_packages(),

    install_requires=["GitPython"],
    
    entry_points={
        "console_scripts": [
            "autosemver=git_autosemver:main"
        ]
    }
)
