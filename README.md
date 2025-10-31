# Music Player - Python

A `Music Player` application that allows you to listen to music stored on your computer's internal or external memory.

![sc1](https://github.com/user-attachments/assets/7cdcc1e3-d90f-472f-a349-484441e8985e)

## Demo - Using My Music Player

### 1. Install Dependencies
- First, ensure you have Python installed. You can download it [here](https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe).
- This project supports and has been tested with Python 3.8 only. Please install Python 3.8 (for example, the Windows installer) or make sure your virtual environment uses Python 3.8.

    - Windows: use the 3.8 installer from the official site or the py launcher to target 3.8 (e.g. `py -3.8 -m venv .venv`).
    - macOS / Linux: install a Python 3.8 interpreter (for example with pyenv) and create the virtual environment with that interpreter.

    You can still use a later or earlier interpreter at your own risk, but the application will explicitly require Python 3.8 when started.

- Then, install the required dependencies:

Create and activate a virtual environment (recommended)

It's a good practice to use an isolated virtual environment for the project. Below are example commands for the most common shells/OS.

- Windows (PowerShell - recommended):

    ```powershell
    python -m venv .venv
    # Allow running scripts once if needed (PowerShell may block scripts):
    # Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    .\.venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

- Windows (Command Prompt):

    ```cmd
    python -m venv .venv
    .\.venv\Scripts\activate.bat
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

- macOS / Linux (bash, zsh, fish):

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

To deactivate the environment when you're done:

```bash
deactivate
```

If you prefer other tools you can use `virtualenv`, `pipx`, `pipenv`, or `poetry` instead; the same idea applies: create an isolated environment and install `requirements.txt` there.

Then, run the application:

```powershell
python Music_player.py
```


### 2. Run the `Music_player.py` File
- Open your command line and run:

    ```
    python Music_player.py
    ```

### 3. Demonstration

- Upon successful launch, the application will look like this:

![sc1](https://github.com/user-attachments/assets/47dcf51e-156b-498c-8e10-589d867e163b)

- A pop-up will appear for first-time users to choose a folder containing at least one `.mp3` or `.wav` file. Don't skip this step.

![sc2](https://github.com/user-attachments/assets/c2fdb961-5695-4e98-99a0-50ef5ac3d38c)

- Once the folder is selected, you can access the music player interface. Here, you can `play`, `pause`, and change tracks using the <button>>></button> and <button><<</button> buttons.

![sc3](https://github.com/user-attachments/assets/96153ea3-7160-4094-bf9f-e4ea42a1fe9e)

- To change the music folder, click on the image (this is a hidden setting).

![sc4](https://github.com/user-attachments/assets/48a4d1ca-314f-443b-b429-11c485e8ce6d)

- Adjust the volume by scrolling the mouse wheel: scroll forward to `increase` volume, and scroll backward to `decrease` volume.

![sc5](https://github.com/user-attachments/assets/860c5b12-1c72-40bc-be97-f9ba7d0f3c65)

Enjoy your music!
