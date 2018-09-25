"""A script to set up virtual environment in VSCode.""" 
import json
import venv
import platform

__author__ = 'Aji'

venv_path = '.venv'
settings_path = '.vscode/settings.json'
plat = platform.system()

print('Determining OS...')
if plat not in ('Windows', 'Darwin', 'Linux'):
    raise Exception(f'Unsupported platform: {plat}')

print('Creating virtual environment...')
venv.create(venv_path)

print('Updating VSCode settings...')
with open(settings_path) as f:
    settings = json.load(f)
if plat == 'Windows':
    bin_path = r'${workspaceFolder}\.venv\Scripts/python'
else:
    bin_path = '${workspaceFolder}/.venv/bin/python'
settings['python.pythonPath'] = bin_path
with open(settings_path, 'w') as f:
    json.dump(settings, f, indent=4)

print('Done! Please kill this terminal and restart VSCode.')