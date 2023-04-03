#!/usr/bin/env python3
#-*- coding: utf-8 -*-


import uuid


class Client:
    def __init__(self,
                name: str,
                company: str,
                email: str,
                position: str,
                uid = None) -> None:
        self.uid = uid or uuid.uuid4()
        self.name = name
        self.company = company
        self.email = email
        self.position = position

    def to_dict(self) -> dict:
        return vars(self)

    @staticmethod
    def schema() -> list:
        return ['uid', 'name', 'company', 'email', 'position']
