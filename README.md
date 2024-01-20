# Flutter-setup
To install Flutter on Kali Linux, you can follow these general steps:

1. **Download Flutter:**
   - Open a terminal and navigate to the directory where you want to install Flutter.
   - Run the following command to clone the Flutter repository:
     ```bash
     git clone https://github.com/flutter/flutter.git
     ```

2. **Update your PATH:**
   - Add the `flutter/bin` directory to your system PATH. You can do this by adding the following line to your shell profile file (like `.bashrc` or `.zshrc`):
     ```bash
     export PATH="$PATH:`pwd`/flutter/bin"
     ```
   - Then, restart your terminal or run `source ~/.bashrc` (or the appropriate file for your shell).

3. **Install Dependencies:**
   - Flutter has some dependencies that you need to install. Run the following command to get them:
     ```bash
     flutter doctor
     ```
   - It will guide you through the process and inform you of any missing dependencies.

4. **Accept Licenses:**
   - Some Flutter packages require accepting licenses. Run the following command to accept them:
     ```bash
     flutter doctor --android-licenses
     ```

5. **Verify Installation:**
   - Run `flutter doctor` again to verify that everything is set up correctly.

Keep in mind that Kali Linux is primarily designed for security and penetration testing, so using it for development might not be the most straightforward experience. If you encounter any issues specific to Kali Linux, you may need to troubleshoot them based on the particularities of that distribution.
