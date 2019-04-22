import argparse

parser = argparse.ArgumentParser(description="My Argument Testing")
parser.add_argument(
        "-c", "--config-file",
        help="specify the configuration file to read (default: argtest.cfg)",
        dest="config_file",
        default="argtest.cfg")
parser.add_argument(
        "-i", "--input-file",
        help="specify the input file to read",
        required=True,
        dest="input_file")
parser.add_argument(
        "-n", "--no-modify",
        help="do not modify anything, just inform",
        action="store_true")

args = parser.parse_args()

if args.no_modify:
    print("No-modify flag set, not saving any changes")

print("Configuration file: {}".format(args.config_file))
print("Input file: {}".format(args.input_file))
# Do Stuff
