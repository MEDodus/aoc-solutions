@echo off
for /r python %%f in (*.py) do (
    rem set directory to python file directory, ~dpf is the directory of the file and references f
    pushd %%~dpf 
    rem run python file, ~nxf is the name of the file and references f
    python "%%~nxf"
    popd
)