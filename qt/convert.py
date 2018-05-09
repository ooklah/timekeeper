import os
import subprocess

UI = ".ui"
PY = ".py"
PATH = os.path.dirname(__file__)
COMPILE = "C:/Python27/Lib/site-packages/PySide/scripts/uic.py"

for ui in [u for u in os.listdir(PATH) if u.endswith(UI)]:
    ui_path = os.path.join(PATH, ui)
    command = list()
    command.append("python ")
    command.append("{}".format(COMPILE))
    command.append(" -o {} ".format(ui_path.replace(UI, PY)))
    command.append(ui_path)

    print "".join(command)
    subprocess.Popen("".join(command))
