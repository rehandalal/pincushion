import click
import random

from six import print_

from pincushion import __version__


CHOICES = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'


@click.group(invoke_without_command=True)
@click.option('--version', '-V', is_flag=True, help='Show the version and exit.')
def cli(version):
    """Command line tool for generating random pin numbers."""
    if version:
        print_('v{}'.format(__version__))


@cli.command()
@click.option('--count', '-n', default=1)
@click.option('--length', '-l', default=10)
@click.option('--output', '-o', default=None)
def generate(**kwargs):
    """Generate a list of pins"""
    count = kwargs.get('count')
    length = kwargs.get('length')
    output = kwargs.get('output')

    pins = []
    while len(pins) < count:
        pin = ''.join(random.choice(CHOICES) for _ in range(length))
        if pin not in pins:
            pins.append(pin)

    if output:
        with open(output, mode='w+') as f:
            f.write('\n'.join(pins))
    else:
        print_('\n'.join(pins))
