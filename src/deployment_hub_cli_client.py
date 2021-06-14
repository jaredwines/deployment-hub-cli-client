import argparse

parser = argparse.ArgumentParser(description='CLI client for Deployment Hub.')

parser.add_argument('--project', '-p', required=True,
                    help='Name of the project you want to deploy or manage.')
parser.add_argument('--action', '-a',
                    help='The action that is requested for managing the project.')
parser.add_argument('--branch', '-b',
                    help='Branch you want to deploy.')
parser.parse_args()

args = parser.parse_args()

domain = args.domain
ofile = args.ofile
lines = args.lines

print("domain:", domain)
print("output file:", ofile)
print("lines:", lines)
view raw