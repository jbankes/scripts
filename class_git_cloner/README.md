# class_git_cloner Script

This script will clone a single similar repository from multiple students repos.
It is very basic and doesn't need to be used in a fashion meant for students.

## Requirements
* Python3
* Pip3
* [GitPython](https://github.com/gitpython-developers/GitPython). To install
  via pip run the following command:
  ```
  pip3 install GitPython
  ```

* `student.txt` file located in the home directory of the class of students.

## Running the Script
There must be a `student.txt` file for the script to run. You can run the
script by running `python3 class_git_cloner` or `./class_git_cloner` if the
Python3 path matches.

The script will ask you for a name of the repo that was set up for the GitHub
classroom assignment.

## What the Script Does
The script will try to read the file `students.txt`. The script will ask for the
name of the repository used for the assignment. The script will create a
directory named the repo name followed directory by the students repository
being cloned into that directory. 
