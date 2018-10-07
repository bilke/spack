# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import spack.config

from spack.util.editor import editor

description = "get and set configuration options"
section = "config"
level = "long"


def setup_parser(subparser):
    scopes = spack.config.scopes()
    scopes_metavar = spack.config.scopes_metavar

    # User can only choose one
    subparser.add_argument(
        '--scope', choices=scopes, metavar=scopes_metavar,
        help="configuration scope to read/modify")

    sp = subparser.add_subparsers(metavar='SUBCOMMAND', dest='config_command')

    get_parser = sp.add_parser('get', help='print configuration values')
    get_parser.add_argument('section',
                            help="configuration section to print. "
                                 "options: %(choices)s",
                            metavar='SECTION',
                            choices=spack.config.section_schemas)

    blame_parser = sp.add_parser(
        'blame', help='print configuration annotated with source file:line')
    blame_parser.add_argument('section',
                              help="configuration section to print. "
                              "options: %(choices)s",
                              metavar='SECTION',
                              choices=spack.config.section_schemas)

    edit_parser = sp.add_parser('edit', help='edit configuration file')
    edit_parser.add_argument('section',
                             help="configuration section to edit. "
                                  "options: %(choices)s",
                             metavar='SECTION',
                             choices=spack.config.section_schemas)


def config_get(args):
    spack.config.config.print_section(args.section)


def config_blame(args):
    spack.config.config.print_section(args.section, blame=True)


def config_edit(args):
    if not args.scope:
        if args.section == 'compilers':
            args.scope = spack.config.default_modify_scope()
        else:
            args.scope = 'user'
    if not args.section:
        args.section = None

    config = spack.config.config
    config_file = config.get_config_filename(args.scope, args.section)
    editor(config_file)


def config(parser, args):
    action = {'get': config_get,
              'blame': config_blame,
              'edit': config_edit}
    action[args.config_command](args)
