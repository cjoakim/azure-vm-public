"""
Usage:
  python main.py <func>
  python main.py duckdb1 http://<IP-Address>/data/airports.json
Options:
  -h --help     Show this screen.
  --version     Show version.
"""

import sys
import os
import traceback

import duckdb

from docopt import docopt
from dotenv import load_dotenv


def print_options(msg):
    print(msg)
    arguments = docopt(__doc__, version="1.0.0")
    print(arguments)


def duckdb1(url):
    try:
        con = duckdb.connect(database=':memory:')
        # Install and load the httpfs extension
        # con.execute("INSTALL httpfs;")
        # con.execute("LOAD httpfs;")
        con.execute("SELECT download_count, project FROM read_csv('{}');".format(url))
        rows = con.fetchall()
        for row in rows:
            print("count: {}, project: {}".format(row[0], row[1]))
        con.close()
    except Exception as e:
        print(f"Error reading from URL: {e}")



if __name__ == "__main__":
    try:
        load_dotenv(override=True)
        if len(sys.argv) < 2:
            print_options("Error: no CLI args provided")
        else:
            func = sys.argv[1].lower()
            if func == "duckdb1":
                url = sys.argv[2]
                duckdb1(url)
            else:
                print_options("Error: invalid function: {}".format(func))
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())
