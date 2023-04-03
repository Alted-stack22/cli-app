#!/usr/bin/env python3
#-*- coding: utf-8 -*-


from clients.models import Client
from clients.services import ClientService

from tabulate import tabulate
import click


@click.group()
def clients():
    """Manages the client lifecycle"""
    pass


@clients.command()
@click.option('--name', '-n',
        type=str,
        prompt=True,
        help="The client's name")
@click.option('--company', '-c',
        type=str,
        prompt=True,
        help="The client's company")
@click.option('--email', '-e',
        type=str,
        prompt=True,
        help="The client's email")
@click.option('--position', '-p',
        type=str,
        prompt=True,
        help="The client's position")
@click.pass_context
def create(ctx, name, company, email, position):
    """Creates a new client"""
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['tab_name'])
    client_service.create_client(client)


@clients.command()
@click.pass_context
def read(ctx):
    """List all clients"""
    client_service = ClientService(ctx.obj['tab_name'])
    clients_list = client_service.read_clients()
    headers = [field.capitalize() for field in Client.schema()]
    headers[0] = headers[0].upper()
    table = []
    for client in clients_list:
        table.append([
            client['uid'],
            client['name'],
            client['company'],
            client['email'],
            client['position']
        ])
    click.echo(tabulate(table, headers))


@clients.command()
@click.argument('uid',
        type=str)
@click.pass_context
def update(ctx, uid):
    """Updates a client"""
    client_service = ClientService(ctx.obj['tab_name'])
    clients = client_service.read_clients()
    client = [client for client in clients if client['uid'] == uid]
    if client:
        client = _update_client_flow(Client(**client[0]))
        client_service.update_clients(client)
        click.echo('Client updated')
    else:
        click.echo('Client not found!')


def _update_client_flow(client: Client) -> Client:
    click.echo("Leave empty if you don't want to modify the value")
    client.name = click.prompt('New name', type=str, default=client.name)
    client.company = click.prompt('New company', type=str,
            default=client.company)
    client.email = click.prompt('New email', type=str,
            default=client.email)
    client.position = click.prompt('New position', type=str,
            default=client.position)
    return client


@clients.command()
@click.argument('uid',
        type=str)
@click.pass_context
def delete(ctx, uid):
    """Deletes a client"""
    client_service = ClientService(ctx.obj['tab_name'])
    clients = client_service.read_clients()
    client = [client for client in clients if client['uid'] == uid]
    if client:
        client_service.delete_client(Client(**client[0]))
        click.echo('Client deleted')
    else:
        click.echo('Client not found!')


menu = clients
