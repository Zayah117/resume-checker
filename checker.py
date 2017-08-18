import sys
import re
import json
from pprint import pprint

VARS = ["var bio = ", "var work = ", "var projects = ", "var education = "]

def get_text():
    my_file = open(sys.argv[1], "r")
    text = my_file.read()
    my_file.close()

    return text

# For testing
def object_text(var, text):
    result = re.search(var + '((.|\n)*?);', text)
    return result.group(1)

def json_object(var, text):
    text = object_text(var, text)
    data = json.loads(text)
    return data

def check_bio(bio):
    print "checking"

def check_work(work):
    print "checking"

def check_projects(projects):
    print "checking"

def check_education(education):
    print "checking"

def main():
    text = get_text()
    
    # Bio
    print "\n\n***BIO***"
    try:
        bio_data = json_object(VARS[0], text)
        check_bio(bio_data)
    except:
        print "Could not get bio_data"

    # Work
    print "\n\n***WORK***"
    try:
        work_data = json_object(VARS[1], text)
        check_work(work_data)
    except:
        print "Could not get work_data"

    # Projects
    print "\n\n***PROJECTS***"
    try:
        project_data = json_object(VARS[2], text)
        check_projects(project_data)
    except:
        print "Could not get project_data"

    # Education
    print "\n\n***EDUCATION***"
    try:
        education_data = json_object(VARS[3], text)
        check_education(education_data)
    except:
        print "Could not get education_data"



main()
