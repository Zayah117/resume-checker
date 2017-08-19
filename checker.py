import sys
import re
import json
from pprint import pprint

VARS = ["var bio =", "var work =", "var projects =", "var education ="]

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

def no_errors(results):
    if len(results) == 0:
        return True
    else:
        return False

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
    if no_errors(results):
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
    if no_errors(results):
        for i in range(len(bio["skills"])):
            results = check_value(bio["skills"][i], [str, unicode], "bio['skills']")
            errors = append_errors(results, errors)

    # bio pic
    results = check("biopic", bio, "bio", [str, unicode])
    errors = append_errors(results, errors)    

    # print errors
    if len(errors) > 0:
        for i in range(len(errors)):
            print errors[i]
    else:
        print "Test passed"

def check_work(work):
    errors = []

    # jobs
    results = check("jobs", work, "work", [list])
    errors = append_errors(results, errors)
    # check that each 'job' is an object
    if no_errors(results):
        for i in range(len(work["jobs"])):
            results = check_value(work["jobs"][i], [dict], "work['jobs']")
            errors = append_errors(results, errors)
            # check each item in work["jobs"][i]
            if no_errors(results):
                # employer
                results = check("employer", work["jobs"][i], "work['jobs'][" + str(i) + "]", [str, unicode])
                errors = append_errors(results, errors)

                # title
                results = check("title", work["jobs"][i], "work['jobs'][" + str(i) + "]", [str, unicode])
                errors = append_errors(results, errors)

                # location
                results = check("location", work["jobs"][i], "work['jobs'][" + str(i) + "]", [str, unicode])
                errors = append_errors(results, errors)

                # dates
                results = check("dates", work["jobs"][i], "work['jobs'][" + str(i) + "]", [str, unicode])
                errors = append_errors(results, errors)

                # description
                results = check("description", work["jobs"][i], "work['jobs'][" + str(i) + "]", [str, unicode])
                errors = append_errors(results, errors)

    # print errors
    if len(errors) > 0:
        for i in range(len(errors)):
            print errors[i]
    else:
        print "Test passed"

def check_projects(projects):
    errors = []

    # projects
    results = check("projects", projects, "projects", [list])
    errors = append_errors(results, errors)
    # check that each 'project' is an object
    if no_errors(results):
        for i in range(len(projects["projects"])):
            results = check_value(projects["projects"][i], [dict], "projects['projects']")
            errors = append_errors(results, errors)
            # check each item in projects["projects"][i]
            if no_errors(results):
                # title
                results = check("title", projects["projects"][i], "projects['projects'][" + str(i) + "]", [str, unicode])
                errors = append_errors(results, errors)

                # dates
                results = check("dates", projects["projects"][i], "projects['projects'][" + str(i) + "]", [str, unicode])
                errors = append_errors(results, errors)

                # description
                results = check("description", projects["projects"][i], "projects['projects'][" + str(i) + "]", [str, unicode])
                errors = append_errors(results, errors)

                # images
                results = check("images", projects["projects"][i], "projects['projects'][" + str(i) + "]", [list])
                errors = append_errors(results, errors)
                # check that each image is a string url
                if no_errors(results):
                    for j in range(len(projects["projects"][i]["images"])):
                        results = check_value(projects["projects"][i]["images"][j], [str, unicode], "projects['projects'][" + str(i) + "]['images']")
                        errors = append_errors(results, errors)

    # print errors
    if len(errors) > 0:
        for i in range(len(errors)):
            print errors[i]
    else:
        print "Test passed"

def check_education(education):
    errors = []

    # schools
    results = check("schools", education, "education", [list])
    errors = append_errors(results, errors)
    # check that each 'school' is an object
    if no_errors(results):
        for i in range(len(education["schools"])):
            results = check_value(education["schools"][i], [dict], "education['schools']")
            errors = append_errors(results, errors)
            # check each item in education["schools"][i]
            if no_errors(results):
                # name
                results = check("name", education["schools"][i], "education['schools'][" + str(i) + "]", [str, unicode])
                errors = append_errors(results, errors)

                # location
                results = check("location", education["schools"][i], "education['schools'][" + str(i) + "]", [str, unicode])
                errors = append_errors(results, errors)

                # degree
                results = check("degree", education["schools"][i], "education['schools'][" + str(i) + "]", [str, unicode])
                errors = append_errors(results, errors)

                # majors
                results = check("majors", education["schools"][i], "education['schools'][" + str(i) + "]", [list])
                errors = append_errors(results, errors)
                # check that each major is a string
                if no_errors(results):
                    for j in range(len(education["schools"][i]["majors"])):
                        results = check_value(education["schools"][i]["majors"][j], [str, unicode], "education['schools'][" + str(i) + "]['majors']")
                        errors = append_errors(results, errors)                        

                # dates
                results = check("dates", education["schools"][i], "education['schools'][" + str(i) + "]", [str, unicode])
                errors = append_errors(results, errors)

                # url
                results = check("url", education["schools"][i], "education['schools'][" + str(i) + "]", [str, unicode])
                errors = append_errors(results, errors)

    # online courses
    results = check("onlineCourses", education, "education", [list])
    errors = append_errors(results, errors)
    # check that each 'onlineCourses' is an object
    if no_errors(results):
        for i in range(len(education["onlineCourses"])):
            results = check_value(education["onlineCourses"][i], [dict], "education['onlineCourses']")
            errors = append_errors(results, errors)
            # check each item in education["onlineCourses"][i]
            if no_errors(results):
                # title
                results = check("title", education["onlineCourses"][i], "education['onlineCourses'][" + str(i) + "]", [str, unicode])
                errors = append_errors(results, errors)

                # school
                results = check("school", education["onlineCourses"][i], "education['onlineCourses'][" + str(i) + "]", [str, unicode])
                errors = append_errors(results, errors)

                # dates
                results = check("dates", education["onlineCourses"][i], "education['onlineCourses'][" + str(i) + "]", [str, unicode])
                errors = append_errors(results, errors)

                # url
                results = check("url", education["onlineCourses"][i], "education['onlineCourses'][" + str(i) + "]", [str, unicode])
                errors = append_errors(results, errors)

    # print errors
    if len(errors) > 0:
        for i in range(len(errors)):
            print errors[i]
    else:
        print "Test passed"

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
    except:
        print "Could not get work_data"

    if work_data:
        check_work(work_data)

    # Projects
    print "\n\n***PROJECTS***"
    try:
        project_data = json_object(VARS[2], text)
    except:
        print "Could not get project_data"

    if project_data:
        check_projects(project_data)

    # Education
    print "\n\n***EDUCATION***"
    try:
        education_data = json_object(VARS[3], text)
    except:
        print "Could not get education_data"

    if education_data:
        check_education(education_data)



main()
