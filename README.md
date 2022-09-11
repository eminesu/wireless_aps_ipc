# wireless_aps_ipc

To enable the usage of the wifi library, run:

"pip install wifi"

You can directly run the program from the console by executing:

"python main.py"

where the file is located

If command gives an error regarding wlan0 not being available for scanning, try running 'ip link show' to see the original interface's name.

Then you can change the 'wlan0' keyword in line 11 in get_wireless_APs.py to the interface name you got from the terminal.

PS: The reason why I could not embed the instructions in the previous line to the code is that I could not run the commands regarding the status of wireless networks on my Windows 10 OS even though I used WSL.
