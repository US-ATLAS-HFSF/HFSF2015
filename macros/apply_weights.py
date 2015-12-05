#!/usr/bin/env python
from utils import get_dsid
from rootpy.tree import TreeChain

import argparse
import subprocess
import os

class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter):
  pass

__version__ = subprocess.check_output(["git", "describe", "--always"], cwd=os.path.dirname(os.path.realpath(__file__))).strip()
__short_hash__ = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=os.path.dirname(os.path.realpath(__file__))).strip()

parser = argparse.ArgumentParser(description='Author: G. Stark. v.{0}'.format(__version__), formatter_class=lambda prog: CustomFormatter(prog, max_help_position=30), epilog='Take in ROOT files, scale the event weight by sample weight, and add to a new branch')
parser.add_argument('files', type=str, nargs='+', help='ROOT files to process and reweight')
parser.add_argument('--weights', type=str, dest='weights', required=True, help='The weights.json file containing sample weights to apply.')
parser.add_argument('--lumi', required=False, type=int, dest='lumi', metavar='<L>', help='luminosity to use in units of ifb', default=1)
parser.add_argument('--branch', required=False, type=str, help='The name of the new branch to make in the file', default='sample_scaled_event_weight')
parser.add_argument('--event-weight', required=False, type=str, help='The name of the branch containing the event weights', default='event_weight')

# parse the arguments, throw errors if missing any
args = parser.parse_args()
