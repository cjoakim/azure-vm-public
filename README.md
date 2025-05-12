# azure-vm-public

Public repo with minimal content to run a python web server
to serve static data files.

Intended to be invoked by AI tools and agents.

## Server/VM Instructions

ssh into the VM, then clone this repo:

```
$ git clone https://github.com/cjoakim/azure-vm-public.git
```

cd into the repo directory and start the web server:

```
$ cd azure-vm-public

$ sudo python3 -m http.server 80
CTRL-C 

$ ./http_server.sh

$ ps aux | grep python | grep http.server
See the PID of the process running the server

```

## Web Client

```
$ curl http://<IP-Address>/data/top-pypi-packages.csv
```

## DuckDB Client

```
$ sudo apt-get update
$ sudo apt-get upgrade  #Optional
$ sudo apt install python3-pip
$ sudo apt install python3.12-venv
```