#!/usr/bin/env python

import argparse
import os

from helper import Helper
from decorator import registered_cmds, register_subcommands

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo-path')
    subparsers = parser.add_subparsers(dest="subcommand")   
    
    # manual subcommands
    foo_parser = subparsers.add_parser('foo')
    foo_parser.add_argument('-c', '--count')
    bar_parser = subparsers.add_parser('bar')

    # automated subcommands
    register_subcommands(subparsers)

    args = parser.parse_args()
    print(args)

    repo_path = args.repo_path
    if not repo_path:
        repo_path = os.getcwd()
    helper = Helper(repo_path)
    if args.subcommand:
        fn_params={k:v for k,v in args.__dict__.items() if k not in ['repo_path', 'subcommand']}
        getattr(helper, registered_cmds[args.subcommand]['func'])(**fn_params)
    
    print("finished")


if __name__=="__main__":
    main()




