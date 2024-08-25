cd rf_keyboard_sound

python -m venv venv

venv/Scripts/activate

pip install -r requirements.txt

pip install pyinstaller

python App.py

pyinstaller --noconsole --icon=.\icon.ico --name=rf_keyboard_sound App.py
