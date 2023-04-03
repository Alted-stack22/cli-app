#!/usr/bin/env python3
#-*- coding: utf-8 -*-


from clients.models import Client

import csv
import os


class ClientService:
    def __init__(self, tab_name: str) -> None:
        self.tab_name = tab_name

    def create_client(self, client: Client) -> None:
        with open(self.tab_name, mode='a') as file:
            writer = csv.DictWriter(file, fieldnames=Client.schema())
            writer.writerow(client.to_dict())

    def read_clients(self) -> list:
        with open(self.tab_name, mode='r') as file:
            reader = csv.DictReader(file, fieldnames=Client.schema())
            return list(reader)

    def update_clients(self, upd_client: Client) -> None:
        clients: list[dict[str, str]] = self.read_clients()
        upd_clients: list = []
        for client in clients:
            if client['uid'] == upd_client.uid:
                upd_clients.append(upd_client.to_dict())
            else:
                upd_clients.append(client)
        self._export(upd_clients)

    def delete_client(self, del_client: Client) -> None:
        clients: list[dict[str, str]] = self.read_clients()
        upd_clients: list = [client for client in clients if client['uid'] != del_client.uid]
        self._export(upd_clients)

    def _export(self, clients: list) -> None:
        tmp_table = self.tab_name + '.tmp'
        with open(tmp_table, mode='w') as file:
            writer = csv.DictWriter(file, fieldnames=Client.schema())
            writer.writerows(clients)
        os.remove(self.tab_name)
        os.rename(tmp_table, self.tab_name)
