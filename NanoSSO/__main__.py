import argparse
from NanoSSO.Interfaces.CommandLineInterface import CommandLineInterface


def main():
    parser = argparse.ArgumentParser(
        prog='NanoSSO',
        description='A simple library handling SSO for building tools that interact with the EVE Online ESI API',
        epilog='This is the command-line interface for generating and validating one-off flows with EVE SSO.')

    parser.add_argument('--id', dest='client_id', action='store', required=False,
                        help='The EVE App client ID')
    parser.add_argument('--secret', dest='secret_key', action='store', required=False,
                        help='The EVE App secret')
    parser.add_argument('--callback', dest='callback', action='store', required=False,
                        help='The EVE App callback URL')
    parser.add_argument('--scopes', dest='scopes', action='store', required=False,
                        help='A ";" seperated string of scopes.')
    parser.add_argument('--env', dest='read_from_env_vars', action='store_true', required=False,
                        help='Read EVE app details from environmental variables')

    args = parser.parse_args()
    CommandLineInterface(client_id=args.client_id, secret_key=args.secret_key, callback=args.callback,
                         default_scopes=args.scopes, read_from_env_vars=args.read_from_env_vars).run()


if __name__ == '__main__':
    main()
