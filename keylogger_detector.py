#!/usr/bin/env python3
"""Keylogger Detector (educational)
This script helps you inspect running processes and spot suspicious programs that
might be behaving like keyloggers (based on process names and command lines).
It is a defensive tool for learning how to detect potential keylogger activity.
Do NOT use this to attempt offensive actions.
"""

import sys

def ensure_psutil():
    try:
        import psutil  # type: ignore
    except Exception:
        print("psutil is not installed. Install it with: pip install psutil")
        sys.exit(1)
    return psutil

def find_suspicious_procs(psutil):
    suspicious_terms = [
        'keylog', 'keylogger', 'pynput', 'keyboard', 'hook', 'logger', 'logkeys',
        'klog', 'xinput', 'hid', 'winlogon', 'capture'
    ]
    found = []
    for p in psutil.process_iter(['pid', 'name', 'exe', 'cmdline']):
        try:
            info = p.info
            name = (info.get('name') or '').lower()
            cmd = ' '.join(info.get('cmdline') or []).lower()
            exe = (info.get('exe') or '') or ''
            combined = ' '.join([name, cmd, exe]).lower()
            for term in suspicious_terms:
                if term in combined:
                    found.append({
                        'pid': info.get('pid'),
                        'name': info.get('name'),
                        'cmdline': info.get('cmdline'),
                    })
                    break
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return found

def main():
    psutil = ensure_psutil()
    print('Keylogger Detector - scanning running processes (educational)')
    print('Note: this is heuristic-based. Manual investigation is required for confirmation.\n')
    suspicious = find_suspicious_procs(psutil)
    if not suspicious:
        print('No obvious suspicious processes found based on name/command line heuristics.')
    else:
        print(f'Found {len(suspicious)} suspicious process(es):\n')
        for s in suspicious:
            print(f"PID: {s['pid']}  Name: {s['name']}\n  Cmdline: {s['cmdline']}\n")
    print('\nTips:')
    print('- If you find a suspicious process, check its location (exe path), digital signature and network activity.')
    print('- Use antivirus and endpoint detection tools for deeper analysis.')
    print('- Always work on an isolated test machine when investigating.')

if __name__ == '__main__':
    main()
