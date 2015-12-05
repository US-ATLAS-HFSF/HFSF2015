#!/usr/bin/env python
import utils
from rootpy.io import root_open
from rootpy.tree import TreeBuffer

'''
Turn off warnings from rootpy.tree for buffer:
    WARNING:rootpy.tree] Skipping entry in buffer with the same name as an existing branch '<>'
'''
from rootpy import log as rootpy_log
rootpy_log["/rootpy.tree"].setLevel(rootpy_log.ERROR)

import argparse
import subprocess
import os
import json
import operator

class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter):
  pass

__version__ = subprocess.check_output(["git", "describe", "--always"], cwd=os.path.dirname(os.path.realpath(__file__))).strip()
__short_hash__ = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=os.path.dirname(os.path.realpath(__file__))).strip()

parser = argparse.ArgumentParser(description='Author: G. Stark. v.{0}'.format(__version__), formatter_class=lambda prog: CustomFormatter(prog, max_help_position=30), epilog='Take in ROOT files, scale the event weight by sample weight, and add to a new branch')
parser.add_argument('files', type=str, nargs='+', help='ROOT files to process and reweight')
parser.add_argument('--weights', type=str, dest='weights', required=True, help='The weights.json file containing sample weights to apply.')
parser.add_argument('--lumi', required=False, type=int, dest='lumi', metavar='<L>', help='luminosity to use in units of ifb', default=1)
parser.add_argument('--treename', required=False, type=str, help='The name of the tree to update', default='CollectionTree')
parser.add_argument('--branch', required=False, type=str, help='The name of the new branch to make in the file', default='sample_scaled_event_weight')
parser.add_argument('--event_weight', required=False, type=str, help='The name of the branch containing the event weights', default='event_weight')
parser.add_argument('--delete_older_cycles', required=False, action='store_true', help='By default, this will create a tree of the same name in your file, effectively copying it by incrementing the cycle number. If this is not something you want because your file size is getting large, enable this flag to delete all older cycles.')

# parse the arguments, throw errors if missing any
args = parser.parse_args()

# load the weights file
try:
    weights = json.load(file(args.weights))
except IOError:
    print('Could not find the file')
    raise
except ValueError:
    print('Could not parse the weights file')
    raise

for fname in args.files:
    if not os.path.exists:
        print('{0:s} does not exist. Skipping.'.format(fname))
        continue

    # attempt to extract DSID from file
    try:
        dsid = utils.get_dsid(fname)
    except ValueError:
        print('Could not extract the DSID from {0:s}. Skipping.'.format(fname))
        continue

    # open for updating to add a branch
    f = root_open(fname, "UPDATE")
    try:
        tree = getattr(f, args.treename)
    except AttributeError:
        print('Could not find the tree {0:s} in {1:s}. Skipping.'.format(args.treename, fname))
        continue

    # let's make sure branches are ok
    tree_branches = tree.branchnames
    if args.event_weight not in tree_branches:
        # missing, we can't do shit
        print('{0:s} is missing {1:s}'.format(fname, args.event_weight))
        continue

    try:
        # get the scale factor for the given file name then
        # use reduce and multiply everything to the default (args.lumi)
        weight = weights[dsid]
        scale_factor = args.lumi
        scale_factor *= weight.get('cross section')
        scale_factor *= weight.get('filter efficiency')
        scale_factor *= weight.get('k-factor')
        scale_factor /= weight.get('num events')
    except KeyError:
        print('The weights file does not have an entry for DSID#{0:s}'.format(dsid))
        continue

    if args.branch not in tree_branches:
        # this is expected, we need to create the branch first then as float type
        newBuffer = TreeBuffer({args.branch: 'F', args.event_weight: 'F'})
        tree.set_buffer(newBuffer, create_branches=True, ignore_duplicates=True)

    for event in tree:
        # for each event, set the value to the event_weight * scale factor
        setattr(event, args.branch, getattr(event, args.event_weight)*scale_factor)
        # fill it up again
        tree.fill()
    tree.write()

    if args.delete_older_cycles:
        # all but the latest cycle
        for cycle in sorted([k.get_cycle() for k in f.keys() if k.name == args.treename])[:-1]:
            print('Deleting {0:s};{1:d} from file'.format(args.treename, cycle))
            f.delete('{0:s};{1:d}'.format(args.treename, cycle))
    f.close()
    print("Finished {0:s}".format(fname))
