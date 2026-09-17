# wireless_aps_ipc

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/platform-Linux-333?style=flat&logo=linux&logoColor=white)

Scan nearby **wireless access points** and report changes in real time — a small Python demo of
**multiprocessing** and **inter-process communication (IPC)**. One process periodically scans the
Wi-Fi cells (SSID, SNR, channel); a second process prints the changes it receives over a
multiprocessing `Queue` — access points added or removed, and SNR or channel changes.

> 🗂️ **One of my earlier learning projects — original, authored-by-hand code, written in
> September 2022 and preserved here exactly as originally written** (no later changes to the
> source). Linux-only, as it relies on the `wifi` library.

## How it works

- `get_wireless_APs.py` — scans wireless cells with the `wifi` library and writes them to JSON.
- `main.py` — runs two processes: one re-scans on a loop, the other prints detected changes
  received through the IPC queue.

## Requirements

```bash
pip install wifi
```

## Usage

Run from the folder where the files are located:

```bash
python main.py
# or, depending on your Python version:
python3 main.py
```

If you get an error about `wlan0` not being available for scanning, run `ip link show` to find your
interface's name, then change the `wlan0` keyword on line 11 of `get_wireless_APs.py` to that name.

---

*Built by [Emine Şevval Eş Uzunay](https://www.linkedin.com/in/eminesevvalesuzunay).*
