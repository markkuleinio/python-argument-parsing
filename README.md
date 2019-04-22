# Argument Parsing in Python

Sample output:

```
$ python3 argtest.py
usage: argtest.py [-h] [-c CONFIG_FILE] -i INPUT_FILE [-n]
argtest.py: error: the following arguments are required: -i/--input-file

$ python3 argtest.py -h
usage: argtest.py [-h] [-c CONFIG_FILE] -i INPUT_FILE [-n]

My Argument Testing

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG_FILE, --config-file CONFIG_FILE
                        specify the configuration file to read (default:
                        argtest.cfg)
  -i INPUT_FILE, --input-file INPUT_FILE
                        specify the input file to read
  -n, --no-modify       do not modify anything, just inform

$ python3 argtest.py -i filename.txt
Configuration file: argtest.cfg
Input file: filename.txt

$ python3 argtest.py -i filename.txt -n
No-modify flag set, not saving any changes
Configuration file: argtest.cfg
Input file: filename.txt

$ python3 argtest.py -i filename.txt -n -c special_set_of_configs.cfg
No-modify flag set, not saving any changes
Configuration file: special_set_of_configs.cfg
Input file: filename.txt
```

More information: <https://docs.python.org/3/library/argparse.html>
