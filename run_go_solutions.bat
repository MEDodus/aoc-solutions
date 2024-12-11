@echo off
for /r go %%f in (*.go) do (
    pushd %%~dpf
    go run "%%~nxf"
    popd
)