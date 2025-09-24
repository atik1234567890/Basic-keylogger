#!/usr/bin/env python3
"""Keystroke Simulator (safe, educational)
This program reads a text file that contains simulated keystrokes and shows
analysis (frequency, likely sensitive tokens, example lines).

Purpose: Understand how logs might look and how to detect sensitive entries
without capturing real user input.
"""

import argparse
import re
from collections import Counter

SENSITIVE_PATTERNS = [
    r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',  # emails
    r'\b\d{12,19}\b',  # possible credit card numbers (very naive)
    r'password\s*[:=]\s*\S+',  # explicit password mentions
]

def analyze_text(text):
    words = re.findall(r"\w+", text.lower())
    freq = Counter(words).most_common(30)
    findings = []
    for pat in SENSITIVE_PATTERNS:
        for m in re.finditer(pat, text, re.IGNORECASE):
            findings.append((pat, m.group(0)))
    return freq, findings

def main():
    parser = argparse.ArgumentParser(description='Keystroke Simulator - analyze a text file of simulated keystrokes')
    parser.add_argument('file', help='Path to text file with simulated keystrokes (safe sample)')
    args = parser.parse_args()

    try:
        with open(args.file, 'r', encoding='utf-8', errors='replace') as f:
            data = f.read()
    except Exception as e:
        print('Could not read file:', e)
        return

    freq, findings = analyze_text(data)
    print('\n--- Keystroke Simulator Analysis ---\n')
    print('Top words (sample):')
    for w, c in freq[:15]:
        print(f'  {w}: {c}')
    if findings:
        print('\nPotential sensitive tokens found:')
        for pat, token in findings:
            print(f'  Pattern: {pat}  =>  {token}')
    else:
        print('\nNo obvious sensitive tokens found by naive patterns.')
    print('\n--- End of analysis ---\n')
    print('Tip: Use this tool with safe, synthetic data to practice detection and red-team analysis.')


if __name__ == '__main__':
    main()
