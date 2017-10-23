#!/usr/local/bin/python3
# File: class_git_cloner
# Description: This script will clone the same repository from each student. The
#   only thing that needs to happen is a students.txt file with all of the
#   GitHub account names listed on individual lines.
import sys, os
from git import Repo

# Open student file and read
try:
    students_file = open('students.txt', 'r')
except:
    print('Students.txt is missing, please try again')
    sys.exit()
students = students_file.read().splitlines()

# Read Repo name and create new directory
repo_name = input('Repository Name for Assignment: ')
os.mkdir(repo_name)

# Loop through students and clone all repos
for student in students:
    git_url = 'https://github.com/' + student + '/' + repo_name + '-' + student
    print(git_url)
    repo_dir = repo_name + '/' + student
    try:
        Repo.clone_from(git_url, repo_dir)
    except:
        print(student + "'s repo was not found" )
