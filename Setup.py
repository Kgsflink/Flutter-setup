import os
import subprocess

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode(), error.decode(), process.returncode

def setup_flutter():
    # Clone Flutter repository
    run_command("git clone https://github.com/flutter/flutter.git")

    # Add Flutter binaries to PATH
    os.system("echo 'export PATH=\"$PATH:{}/flutter/bin\"' >> ~/.bashrc".format(os.getcwd()))
    os.system("source ~/.bashrc")

    # Run Flutter doctor to install dependencies
    run_command("flutter doctor")

def setup_android_sdk():
    # Download Android SDK tools
    run_command("wget https://dl.google.com/android/repository/commandlinetools-linux-6858069_latest.zip")
    run_command("unzip commandlinetools-linux-6858069_latest.zip -d cmdline-tools")
    
    # Move SDK tools to a known location
    os.makedirs(os.path.expanduser("~/.android-sdk/cmdline-tools"), exist_ok=True)
    os.system("mv cmdline-tools ~/.android-sdk/cmdline-tools/latest")

    # Add Android SDK binaries to PATH
    os.system("echo 'export PATH=\"$PATH:$HOME/.android-sdk/cmdline-tools/latest/bin\"' >> ~/.bashrc")
    os.system("source ~/.bashrc")

def main():
    print("Setting up Flutter and Android SDK on Kali Linux...")
    setup_flutter()
    setup_android_sdk()
    print("Setup complete.")

if __name__ == "__main__":
    main()
