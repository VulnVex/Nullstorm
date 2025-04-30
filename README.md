<<<<<<< HEAD
Denial of Service Tool - Instructions

Created by Nullvex

Usage:

start.py [-h] [--target IP:PORT, URL, PHONE] [--method SMS/EMAIL/NTP/UDP/SYN/ICMP/POD/SLOWLORIS/MEMCACHED/HTTP>] [--time <time>] [--threads <threads>]


---

Options:

-h, --help
Show this help message and exit.

--target IP:PORT, URL, PHONE
Specify the target for the attack.

For attacking an IP address, use IP:PORT.

For targeting a website, provide the full URL.

For targeting a phone number (though this might not work effectively), provide the phone number.


--method SMS/EMAIL/NTP/UDP/SYN/ICMP/POD/SLOWLORIS/MEMCACHED/HTTP
Choose the method of attack.
Options include:

SMS, EMAIL, NTP, UDP, SYN, ICMP, POD, SLOWLORIS, MEMCACHED, HTTP.


--time time
Specify how long to carry out the attack in seconds.
Example: 200 (for 200 seconds).

--threads threads
Define the number of threads to use for the attack.
This can range from 1 to 200.
Example: 187.



---

Example:

To target a website with a SYN attack for 300 seconds using 150 threads:

start.py --target example.com --method SYN --time 300 --threads 150


---

This tool is designed for stress testing and learning about network security. Use responsibly and legally.

if you find a bug or any ideas please contact nullvex.uio on instagram nullvex.ui on tiktok.
# Nullstorm
A powerful ddos/dos tool
 b5fb6b79d9155e8aeef3358c33cc540385e8d99a
