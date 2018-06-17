import os
from pprint import pprint

os.chdir(os.path.dirname(__file__))

PASSWD_FILE_NAME = os.getcwd() + "/passwd"

SHADOW_FILE_NAME = os.getcwd() + "/shadow"

GROUP_FILE_NAME = os.getcwd() + "/group"

#zamiast wrzucać cały plik do pamięcie i potem robić strip_file() lepiej sprawdzać osobno każdą linie pliku /
#i dpoiero wtedy wrzucać odpowiednie  linie do listy końcowej
# w ten sposób lepiej działa to  na pamięć (ważne przy dużych plikach
with open(PASSWD_FILE_NAME) as file:
    passwd_content = file.readlines()

with open(SHADOW_FILE_NAME) as file:
    shadow_content = file.readlines()

with open(GROUP_FILE_NAME) as file:
    group_content = file.readlines()

def strip_file(file_content):
    file_content_lines = []
    for line in file_content:
        if line.strip() == "":
            continue
        if not line.startswith("#"):
            file_content_lines.append(line)
    return file_content_lines

passwd_important_lines = strip_file(passwd_content)
shadow_important_lines = strip_file(shadow_content)
group_important_lines = strip_file(group_content)

ENCRIPTION_DICT = {
       "$1$": "MD5",
       "$2a$": "Blowfish",
       "$2y$": "Blowfish",
       "$5$": "SHA-256",
       "$6$": "SHA-512",
        "!!": "pass not set"}

LIMIT_USERID = 1000

user_data = {}

for txt in passwd_important_lines:
    user_passwd_data = {}
    user_login = txt.split(":")[0]
    user_id = txt.split(":")[2]
    user_gid = txt.split(":")[3]
    user_home_dir = txt.split(":")[5]
    user_shell = txt.split(":")[6]

    user_passwd_data["id"] = user_id
    user_passwd_data["gid"] = user_gid
    user_passwd_data["home"] = user_home_dir
    user_passwd_data["shell"] = user_shell

    if int(user_id) >= LIMIT_USERID:
        user_data[user_login] = user_passwd_data


user_shadow = {}
for txt in shadow_important_lines:
    user_shadow_data = {}
    user_login = txt.split(":")[0]
    user_pass_field = txt.split(":")[1]

    user_pass_encryption = "not set"
    user_pass = "not set"
    user_locked = False

    for key in ENCRIPTION_DICT.keys():
        if user_pass_field.startswith(key):
            user_pass_encryption = ENCRIPTION_DICT[key]
            if key == "!!":
                user_locked = True
            user_pass = user_pass_field[len(key):]
            break

    if user_data.get(user_login) is not None:
        user_data[user_login]["algorithm"] = user_pass_encryption
        user_data[user_login]["password"] = user_pass
        user_data[user_login]["locked"] = user_locked


user_groups = {}
for txt in group_important_lines:
    group_name = [] #txt.split(":")[0]
    group_name.append(txt.split(":")[0])
    group_users = txt.split(":")[3].split(",")

    for user in group_users:
        try:
            user_clean = user.split()[0]
        except IndexError:
            continue
        if user_groups.get(user_clean) is not None:
            user_groups[user_clean].append(group_name[0])
        else:
            user_groups[user_clean] = group_name

for k in user_groups.keys():
    # user_groups[k] = set(user_groups[k])
    if user_data.get(k) is not None:
        user_data.get(k)["groups"] = set(user_groups[k])

users = []
for key in user_data.keys():
    user_data_dict = {}
    user_data_dict["user"] = key
    for val in user_data.values():
        for v in val.keys():
            user_data_dict[v] = val[v]
    users.append(user_data_dict)

pprint(user_data)
pprint(users)
# pprint(user_shadow)
# pprint(user_groups)

