import logging
import requests
import qbittorrentapi as qbtapi

from time import sleep
from traceback import print_exc


if __name__ == "__main__":
    with open("logo.txt", "r") as file:
        print(file.read())

    QBT_PAUSED = False
    CONNECTION_LOST = False
    DANGER_IP = input("Static address (DANGER_IP): ")
    logging.basicConfig(level=logging.INFO)
    qbt_client = qbtapi.Client(host="localhost", port=8080, username="admin", password="adminadmin")

    try:
        qbt_client.auth_log_in()
    except qbtapi.LoginFailed as e:
        logging.info("Invalid auth details while attempting to log in to qBittorrent API.")
        print_exc(file=open("errors.log", "a"))
        exit(-1)
    except qbtapi.exceptions.APIConnectionError as e:
        logging.info(f"{e.__class__.__name__}: unable to connect to qBittorrent API. Most likely, the application is not running.")
        print_exc(file=open("errors.log", "a"))
        exit(-1)
    except Exception as e:
        logging.info(f"Unhandled exception ({e.__class__.__name__}) has occurred. Reference 'errors.log' for details.")
        print_exc(file=open("errors.log", "a"))
        exit(-1)

    logging.info(f"qBittorrent: {qbt_client.app.version}")
    logging.info(f"qBittorrent Web API: {qbt_client.app.web_api_version}")

    while True:
        try:
            data = requests.get("http://ip-api.com/json/").json()
        except requests.exceptions.ConnectionError as e:
            CONNECTION_LOST = True
            logging.info("Internet connection not found. Retrying...")
            print_exc(file=open("errors.log", "a"))
            sleep(5)
            continue

        if CONNECTION_LOST:
            CONNECTION_LOST = False
            logging.info("Regained connection. Continuing.")

        if data['status'] != "success":
            logging.info("Request to ip-api failed. Trying again.")
            sleep(5)
            continue

        if data['query'] == DANGER_IP:
            logging.warning("Connection to VPN not found!")
            if not QBT_PAUSED:
                print("Pausing qBittorrent", end="...")
                qbt_client.torrents.pause.all()
                QBT_PAUSED = True
                print(" done.")
            else:
                logging.info("Ignoring reconnection protocols... will test again later.")
        elif QBT_PAUSED:
            logging.info("Connection to VPN regained.")
            print("Unpausing qBittorrent", end="...")
            qbt_client.torrents.resume.all()
            QBT_PAUSED = False
            print(" done.")

        sleep(5)
