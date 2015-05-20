# parse-massmimikatz
Parser for the output of running mimikatz against a large number of machines

Currently the process_parsed.py script spits out a list of user passwords to stdout. Modify to taste.

The password printing piece in process_parsed will exclude any passwords over length 40 and any password listed as (null). This supresses output of "(null)" dumps and hashes.

The parse_all.sh script should be run from within the MimikatzOutput directory. Or just copy out the command and run it. You will need to redirect this script to a file for processing with process_parsed.py.

The process_parsed.py script is expecting "--" delimited grep output with filenames on each line. The script also expects every filename to be the machine name.

# TODO

Dig into Invoke-MassMimikatz to make it output anything more regular than a text dump.
