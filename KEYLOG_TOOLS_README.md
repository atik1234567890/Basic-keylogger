# Keylogger Detector & Keystroke Simulator (Safe, Educational)

This package contains two safe, defensive, and educational tools to learn about keylogger detection and log analysis without creating or distributing malicious software.

Files:
- `keylogger_detector.py` - heuristic-based process scanner to spot suspicious processes by name/commandline. Defensive tool.
- `keystroke_simulator.py` - reads a text file with simulated keystrokes and performs basic analysis to find likely sensitive tokens. Safe and non-invasive.

Usage
------
1. Install dependencies (for detector):
   ```bash
   pip install psutil
   ```

2. Run the detector (requires permissions to list processes):
   ```bash
   python3 keylogger_detector.py
   ```

3. Prepare a sample text file (e.g., `simulated_keys.txt`) with synthetic keystrokes and analyze it:
   ```bash
   python3 keystroke_simulator.py simulated_keys.txt
   ```

Why these instead of a real keylogger?
--------------------------------------
Creating or sharing real keylogger code that captures other people's keystrokes can enable harmful activity. These tools are intentionally defensive and educational: one helps you find suspicious processes, the other helps you practice detection on synthetic data.

Ethics and legal
----------------
Only run these tools on systems you own or are authorized to test. Do not attempt to access or monitor other users' machines or data without clear permission.
