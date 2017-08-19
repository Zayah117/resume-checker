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

def check(value, my_object, object_name, types):
    errors = []

    if type(value) is str:
        if value in my_object:
            if not (type(my_object[value]) in types):
                errors.append("'%s' is not %s" % (str(value), str(types)))
        else:
            errors.append("'%s' not in %s" % (str(value), str(object_name)))

    return errors

def check_value(variable, types, object_name):
    errors = []

    if not (type(variable) in types):
        errors.append("'%s' in %s is not %s" % (str(variable), str(object_name), str(types)))

    return errors

def append_errors(results, error_list):
    for i in range(len(results)):
        error_list.append(results[i])
    return error_list

def check_bio(bio):
    errors = []

    # name
    results = check("name", bio, "bio", [str, unicode])
    errors = append_errors(results, errors)

    # role
    results = check("role", bio, "bio", [str, unicode])
    errors = append_errors(results, errors)

    # contact info
    results = check("contacts", bio, "bio", [dict])
    errors = append_errors(results, errors)
    if len(results) == 0:
        # mobile
        results = check("mobile", bio["contacts"], "bio['contacts']", [str, unicode])
        errors = append_errors(results, errors)

        # email
        results = check("email", bio["contacts"], "bio['contacts']", [str, unicode])
        errors = append_errors(results, errors)

        # github
        results = check("github", bio["contacts"], "bio['contacts']", [str, unicode])
        errors = append_errors(results, errors)

        # location
        results = check("location", bio["contacts"], "bio['contacts']", [str, unicode])
        errors = append_errors(results, errors)

    # welcome message
    results = check("welcomeMessage", bio, "bio", [str, unicode])
    errors = append_errors(results, errors)

    # skills
    results = check("skills", bio, "bio", [list])
    errors = append_errors(results, errors)
    if len(results) == 0:
        for i in range(len(bio["skills"])):
            results = check_value(bio["skills"][i], [str, unicode], "bio['skills']")
            errors = append_errors(results, errors)

    # print errors
    if len(errors) > 0:
        for i in range(len(errors)):
            print errors[i]
    else:
        print "Test passed"

def check_work(work):
    print "checking"

def check_projects(projects):
    print "checking"

def check_education(education):
    print "checking"

def main():
    text = get_text()
    bio_data = None
    work_data = None
    project_data = None
    education_data = None
    
    # Bio
    print "\n\n***BIO***"
    try:
        bio_data = json_object(VARS[0], text)
    except:
        print "Could not get bio_data"

    if bio_data:
        check_bio(bio_data)

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
