#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask


app = Flask(__name__)


@app.route('/')
def run():
    return 'Lorem ipsum'


if __name__ == '__main__':
    app.run()
