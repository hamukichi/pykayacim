#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a command-line tool for PyKayacIM.

Functions defined in this module should not be used directly.

"""

from __future__ import unicode_literals
from __future__ import absolute_import
import pykayacim.api
import pykayacim.exceptions
import argparse
import sys
import builtins


def decode_params(params):
    """Decode values of the provided dictionary if necessary. 
    
    """
    
    decoded_params = dict()
    for k, v in params.items():
        if isinstance(v, builtins.bytes):
            decoded_params[k] = v.decode(sys.stdin.encoding)
        else:
            decoded_params[k] = v
    return decoded_params

def _send_notification(args):
    """Send a notification.
    
    """
    
    init_params = {"username": args.username, "method": args.method}
    send_params = {"message": args.message, "handler": args.scheme}
    if args.method == "password":
        init_params["key"] = args.password
    elif args.method == "secret":
        init_params["key"] = args.secret
    
    api = pykayacim.api.KayacIMAPI(**decode_params(init_params))
    api.send(**send_params)

def main():
    """Used if this module is run as a script.
    
    """
    
    # Top-level
    parser = argparse.ArgumentParser(
    description="Send push notifications via im.kayac.com.",
    epilog="See '%(prog)s <method> --help' for details.")
    subparsers = parser.add_subparsers(
    help="Available authorization methods.",
    dest="method")
    
    # Subcommands
    parser_none = subparsers.add_parser("none",
    help="No authorization.")
    parser_none.set_defaults(func=_send_notification)

    parser_password = subparsers.add_parser("password",
    help="Use authorization with a password.")
    parser_none.set_defaults(func=_send_notification)
    
    parser_secret = subparsers.add_parser("secret",
    help="Use secret key cryptosystem.")
    parser_secret.set_defaults(func=_send_notification)
    
    # Common arguments
    for p in [parser_none, parser_password, parser_secret]:
        p.add_argument("username",
        help="The username of your im.kayac.com account.")
        p.add_argument("message",
        help="The message to be sent.")
        p.add_argument("-s", "--scheme",
        help="The URI scheme for iPhone applications.")
    
    # Other arguments
    parser_password.add_argument("password",
    help="The password for notifications, not for your account.")
    parser_secret.add_argument("key",
    help="The secret key for sending notifications.")
    
    args = parser.parse_args()
    
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
    

if __name__ == "__main__":
    main()