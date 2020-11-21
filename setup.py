from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

base = 'Console'

executables = [
    Executable('main.py', base=base, targetName = 'main.exe')
]

setup(name='Text game',
      version = '0.0.2',
      description = 'A simple text game',
      options = {'build_exe': build_options},
      executables = executables)
