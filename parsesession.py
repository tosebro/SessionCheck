import argparse
import pathlib
import re
import base64
import json

parser = argparse.ArgumentParser(description='Parse session check log')
parser.add_argument('-i', type=str, nargs=1, required=True, help='ID for the session')
parser.add_argument('-f', type=pathlib.Path, nargs=1, required=True, help='log file')

args = parser.parse_args()

session_file = args.f[0]
session_id = args.i[0]

# print(session_file)
# print(session_id)

session_dict = {}

with open(session_file) as f:
    for line in f:
        pattern = r'\?i=(\w+)\&s=(\d+)\&d=([^\s]+)'
        match = re.findall(pattern, line)
        if match:
            # print(match[0])
            if match[0][0] == session_id:
                seq = match[0][1]
                sess = match[0][2]
                # print(seq)
                # print(sess)
                session_dict[seq] = sess

# session info in JSON
session_info = ''

# sort session dictionary, combine
for seq, sess in sorted(session_dict.items()):
    # print(seq + ": " + sess)
    session_info += sess

session_info = base64.b64decode(session_info)
session_info = session_info.decode('utf-8')
# print(session_info)

session_info_json = json.loads(session_info)
# print(session_info_json)

session_info_json_dump = json.dumps(session_info_json,indent=4)
print(session_info_json_dump)

