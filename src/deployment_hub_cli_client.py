import argparse
import os

parser = argparse.ArgumentParser(description='CLI client for Deployment Hub.')
parser.add_argument('--project', '-p', required=True,
                    help='Name of the project you want to deploy or manage.')
parser.add_argument('--action', '-a',
                    help='The action that is requested for the project.')
parser.add_argument('--branch', '-b',
                    help='Branch you want to deploy.')
parser.parse_args()
args = parser.parse_args()

project = args.project
action = args.action
branch = args.branch
url = "http://192.168.1.254:5000"

list_of_projects = ['jaredwines-portfolio', 'home-assistant', 'deployment-hub-server']

print("project:", project)
print("action:", action)
print("branch:", branch)

if project in list_of_projects:
    if branch and action is None:
        os.system('curl ' + url + '/' + project + '/')
    if branch is None:
        os.system('curl ' + url + '/' + project + '/' + action + '/')
    else:
        os.system('curl ' + url + '/' + project + '/' + action + '/' + branch + '/')

else:
    print("Project does not exist!")
