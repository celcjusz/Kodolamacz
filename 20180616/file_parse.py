import os
from pprint import pprint

os.chdir(os.path.dirname(__file__))

FILE_NAME = os.getcwd() + "/hosts"

file = open(FILE_NAME)
content = file.read()

#dzięki with nie trzeba pamiętać o zamykaniu  pliku - używa się tego  częściej niż
# with open(FILE_NAME) as file:
#     content = file.read()

lines = content.split("\n")

# a teraz podział  na linijki  za jednym  zamachem
# with open(FILE_NAME) as file:
#     content = file.readlines()

important_lines = []
for line in lines:
    if line.strip() == "":
        continue
    if not line.startswith("#"):
        important_lines.append(line)

# print(important_lines)

host_dict = {}

for line in important_lines:
    line_inputs = line.split()

    # print(line_inputs)

    if len(line_inputs) < 2:
        continue

    # print(line_inputs[0])

    i = 1
    hosts = []
    while i < len(line_inputs):
        # print(line_inputs[i])
        hosts.append(line_inputs[i])
        if host_dict.get(line_inputs[0]) is not None:
            host_dict[line_inputs[0]].append(line_inputs[i])
        else:
            host_dict[line_inputs[0]] = hosts

        i += 1


# print(host_dict)

one_host_dict = {}
all_hosts = []
for host in host_dict.keys():
    one_host_dict["ip"] = host
    one_host_dict["hostnames"] = host_dict[host]
    one_host_dict["protocol"] = 'iv4' if ":" in host else "ipv6"

    all_hosts.append(one_host_dict)

    one_host_dict = {}

pprint(all_hosts)
# musisz pamiętać aby zamknąć
file.close()
