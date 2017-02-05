git-autosemver
==============

You use semver version numbers in your project ?
Tired to determine yourself if the next version of your software is a patch, a minor version or a major version ?

git-autosemver parse your commits messages searching for patterns you've specified to automatically determine the next
version number.

Useful in a CI context : now Jenkins/CircleCI/TravisCI/Whatever can push tag version without any human intervention

Configuration
-------------

git-autosemver can be configured from the command-line, or by adding an autosemver.json file in the repository

The configuration options are :

- **prefix**: A prefix before the semver number. Example : "alpha-" will match/generate "alpha-1.0.1". Default is empty (No prefix)
- **suffix**: A suffix after the semver number. Example : "-SNAPSHOT" will match/generate "1.0.1-SNAPSHOT". Default is empty (No suffix)
- **default**: If no tag with semver number and given preffix/suffix has been found, autosemver will use this version number as fallback. Default : "1.0.0",
- **major_keywords**: If any of those words are found in a commit message, autosemver will generate a major version. Default:["#major"],
- **minor_keywords**: If any of those words are found in a commit message, autosemver will generate a minor version. Default:["feat"],
- **create_tag**: Does autosemver should automaticaly add a git tag with the generated version number ? If false, just print it on std output. Default: false
- **config_file**: (Only on command-line) Specify a different configuration file than "autosemver.json"


Roadmap
-------

Currently, I want to add two new different ways to configure autosemver : by a YAML file if PyYAML is installed, and by
environnement variables
