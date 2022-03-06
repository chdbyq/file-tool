import argparse, os
from platform import system

ps = argparse.ArgumentParser()
ps.add_argument('--path', type=str, required=True)
ps.add_argument('-value', type=str, required=False)
ps.add_argument('-rm', action='store_true', required=False)
ps.add_argument('-dir', action='store_true', required=False)
arg=ps.parse_args()

path = arg.path
value = arg.value
remove = arg.rm
directory = arg.dir

class operation():

    def make_file():
        f=open(path, 'w')
        if value != None: f.write(value)
        f.close()

    def make_dir():
        command = f'mkdir {path}'
        os.system(command)

    def delete():
        if system().lower() == 'windows' and directory == False:
            command = f'del /f {path}'
            os.system(command)
        elif system().lower() == 'windows' and directory == True:
            command = f'rd /s /q  {path}'
            os.system(command)
        else:
            command = f'rm -r -f {path}'
            os.system(command)

if remove == False and directory == False:
    operation.make_file()
elif remove == False and directory == True:
    operation.make_dir()
else:
    operation.delete()