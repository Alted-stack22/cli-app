#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import os
# import pylint
import readline


CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ["name", "company", "email", "position"]
clients = []


def _import_storage():
    file_exists = os.path.exists(CLIENT_TABLE)
    if not file_exists:
        file = open(CLIENT_TABLE, "w")
        file.close()
    with open(CLIENT_TABLE, "r") as file:
        reader = csv.DictReader(file, fieldnames=CLIENT_SCHEMA)
        for row in reader:
            clients.append(row)


def _export_storage():
    tmp_table = "{}.tmp".format(CLIENT_TABLE)
    with open(tmp_table, "w") as file:
        writer = csv.DictWriter(file, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)
    os.remove(CLIENT_TABLE)
    os.rename(tmp_table, CLIENT_TABLE)


def _print_welcome():
    print(" WELCOME TO MY SALES SYSTEM ".center(40, "*"))
    # print("*" * 40)
    print("What would you like to do today?".center(40, " "))
    print("[C]reate client".center(40, " "))
    print("[R]ead client/s".center(40, " "))
    print("[U]pdate client".center(40, " "))
    print("[D]elete client".center(40, " "))
    print("[S]earch client".center(40, " "))
    print("[E]xit".center(40, " "))
    print("*" * 40)


def _messages(code: str):
    if code == "not found":
        print("The client's name is not registered!")
    elif code == "exists":
        print("Client already is in the client's list")


def _get_client_field(opt: str):
    field = input("What is the client {}? ".format(opt)).strip()
    if opt == 'email' and field:
        return field
    return field.capitalize() if field else _get_client_field(opt)


def _get_client_id():
    try:
        idx = int(_get_client_field("id"))
    except ValueError:
        print("The id must be a number")
    else:
        return idx


def _register_client():
    return {
        "name": _get_client_field("name"),
        "company": _get_client_field("company"),
        "email": _get_client_field("email"),
        "position": _get_client_field("position")
    }


def create_client(client: dict):
    global clients
    if client not in clients:
        clients.append(client)
    else:
        _messages("exists")


def read_clients():
    global clients
    for idx, client in enumerate(clients):
        print(" {} | {} | {} | {} | {}".format(
            idx,
            client["name"],
            client["company"],
            client["email"],
            client["position"]
        ))


def update_client(client_idx: int):
    global clients
    if client_idx >= len(clients):
        _messages("not found")
        return
    new_client = _register_client()
    if new_client in clients:
        _messages("exists")
        return
    clients[client_idx] = new_client


def delete_client(client_idx: int):
    global clients
    if len(clients) - 1 >= client_idx:
        # clients.remove(clients[client_idx])
        del clients[client_idx]
    else:
        _messages("not found")


def search_client(client_data, opt: str):
    global clients
    for client in clients:
        if opt not in client.keys():
            print("Invalid option!")
            return False
        if client_data == client[opt]:
            return True
    return False


def run():
    _import_storage()
    _print_welcome()
    while (command := input("M> ").upper()) != 'E':
        if command == 'C':
            client = _register_client()
            create_client(client)
        elif command == 'R':
            read_clients()
        elif command == 'U':
            client = _get_client_id()
            if client is None:
                continue
            update_client(client)
        elif command == 'D':
            client = _get_client_id()
            if client is None:
                continue
            delete_client(client)
        elif command == 'S':
            opt = input("How do you want to search for the client? ").lower()
            client = _get_client_field(opt)
            if search_client(client, opt):
                print("The client is in the client's list")
            else:
                print("The client: {} is not in our client's list".format(client))
        else:
            print("Invalid command!")
    _export_storage()
    print("See you soon!")


if __name__ == '__main__':
    run()
