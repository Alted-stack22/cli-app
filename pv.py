#!/usr/bin/env python3
#-*- coding: utf-8 -*-


from clients import commands as cmd
import click


CLIENTS_TABLE = '.clients.csv'

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}
    ctx.obj['tab_name'] = CLIENTS_TABLE


cli.add_command(cmd.menu)
# def run():
#     pass


# if __name__ == '__main__':
#     run()
