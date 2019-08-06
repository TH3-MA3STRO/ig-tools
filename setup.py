from cli import que1, que2
import glob
import json

from tools import tag_based, profile
import pyautogui

ata = glob.glob('./*.json')

if './configs.json' not in ata:
    cn = pyautogui.alert("Configs doesn't exists! Please create it first!")
    uname = pyautogui.prompt("Enter Username")
    password = pyautogui.prompt("Enter Password")
    with open('configs.json', 'w') as f:
        f.write('''
{
    "configs": {
        "username" :"''' + uname + '''",
        "password" :"''' + password + '''"
    }
}
''')
        f.close()
else:
    with open('configs.json', 'r') as f:
        data = json.load(f)
print()
a = que1()
b = que2(a=a['tch'])


u_name = data['configs']['username']
pass_w = data['configs']['password']
if a['tch'].lower() == 'tag-spammer':
    from tag_gettr import tag_get
    w0hashes = tag_get(url=b['p_link'])

if a['tch'].lower() == 'tag-spammer':
    w0hashes=['tech']
    tag_based(u_name=u_name, pass_w=pass_w,w0hash=w0hashes)
else:
    profile(u_name=u_name, pass_w=pass_w, tar_uname=b['tar_uname'])
