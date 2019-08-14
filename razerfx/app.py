"""RazerFX executable script.
"""

import argparse
from functools import partial

from razerfx import RazerFX
from .version import version as __version__


def main():
    """Main entry-point for executable.
    """

    parser = argparse.ArgumentParser(
        description='RazerFX {} for Razer BlackWidow 2019 (en_US) keyboard'.format(__version__))

    parser.add_argument(
        'cmd',
        metavar='command',
        type=str,
        help='Command')

    parser.add_argument(
        '--colorpal',
        metavar='colorpalette',
        type=str,
        help='Seaborn color palette, such as "bright", "deep", or "pastel"',
        default='bright')

    parser.add_argument(
        '--brightness',
        metavar='value',
        type=int,
        help='Set brightness when applying advanced effect.',
        default=None)

    args = parser.parse_args()

    razerfx = RazerFX(args.colorpal)

    switcher = {
        'apply': partial(razerfx.apply_advanced_fx, args.brightness),
        'device_info': partial(razerfx.print_device_info),
        'keyboard_matrix': partial(razerfx.show_keyboard_matrix),
        'show_colorpal': partial(razerfx.show_colorpal)
    }
    choice = switcher.get(args.cmd, lambda: parser.print_help())
    choice()
