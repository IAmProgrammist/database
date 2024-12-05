echo "> Read .env file"

# Default location of venv file
set-content env:\VENV_DIR .venv

get-content .env | foreach {
    $name, $value = $_.split('=')
    set-content env:\$name $value
}

if (!(Test-Path "$env:VENV_DIR/Scripts/python.exe")){
   echo "> Venv is not found, let's install it. It'd take some time, grab some coffee!"
   if (Test-Path "$env:VENV_DIR") {
        rm -r "$env:VENV_DIR"
   }
   mkdir "$env:VENV_DIR"
   python -m venv "$env:VENV_DIR"
}

echo "> Installing requirments"
powershell "$env:VENV_DIR/Scripts/pip.exe install -r ./requirments.txt"

echo "> Convert .ui files into .py files"
powershell "$env:VENV_DIR/Lib/site-packages/PySide6/uic.exe widgets/main.ui -g python -o widgets/main_ui.py"
powershell "$env:VENV_DIR/Lib/site-packages/PySide6/uic.exe widgets/repotab.ui -g python -o widgets/repotab_ui.py"

powershell "$env:VENV_DIR/Scripts/alembic-autogen-check"
if (!($?)) {
    echo "> Database is not up-to-date"
    echo "> Autogen new revision"
    powershell "$env:VENV_DIR/Scripts/alembic revision --autogenerate"
    echo "> Upgrade to latest alembic version"
    powershell "$env:VENV_DIR/Scripts/alembic upgrade head"
} else {
    echo "> Database is up-to-date"
}

echo "> Start application"
powershell "$env:VENV_DIR/Scripts/python.exe main.py"
