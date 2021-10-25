# QBT-Guard



```
________ _____________________        ________                       .___
\_____  \\______   \__    ___/       /  _____/ __ _______ _______  __| _/
 /  / \  \|    |  _/ |    |  ______ /   \  ___|  |  \__  \\_  __ \/ __ | 
/   \_/.  \    |   \ |    | /_____/ \    \_\  \  |  // __ \|  | \/ /_/ | 
\_____\ \_/______  / |____|          \______  /____/(____  /__|  \____ | 
       \__>      \/                         \/           \/           \/ 
```
-----
### Setup
```sh
$ git clone https://voidoak/QBT-Guard
$ python -m venv venv-name
```
### Virtual Environment
Windows:
```sh
$ venv-name\scripts\activate
```
Other:
```sh
$ source venv-name/bin/activate
```
### Requirements/executing
```sh
$ pip install -r requirements.txt
$ python -m main
```
-----
After running, type in the address of your actual IP. The script will pause qBittorrent if the IP you ping to matches the `DANGER_IP` you inputted. It's quite literally that simple.
