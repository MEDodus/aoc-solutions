@echo off
for /r python %%f in (*.py) do (
    pushd %%~dpf
    python "%%~nxf"
    popd
)