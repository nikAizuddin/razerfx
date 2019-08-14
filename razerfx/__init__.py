"""Module RazerFX
"""

import logging

import numpy as np
import pandas as pd
import seaborn as sns
import openrazer.client

from .version import version as __version__


class RazerFX:
    """Client for openrazer daemon to set advanced effect on Razer BlackWidow 2019 (en_US).

    Parameters
    ----------
    palette : str
        Seaborn color palette. Default is 'bright'.
    """

    def __init__(self, palette='bright'):
        self.logger = self._init_logger()
        self.devices = openrazer.client.DeviceManager().devices
        self.colorpal = np.array(
            np.array(sns.color_palette(palette=palette, n_colors=10)) * 255,
            dtype=np.uint8)
        self.keyboard_matrix = self._get_keyboard_matrix(self.colorpal)

    def print_device_info(self):
        """Print Razer devices information.
        """

        for idx, device in enumerate(self.devices):
            self.logger.info('Device %d', idx)
            self.logger.info('  device.type: %s', device.type)
            self.logger.info('  device.name: %s', device.name)
            self.logger.info('  device.keyboard_layout: %s', device.keyboard_layout)
            self.logger.info('  device.brightness: %f', device.brightness)

    def show_colorpal(self):
        """Show color palette info.
        """

        try:
            import matplotlib.pyplot as plt
            sns.palplot(self.colorpal / 255.0)
            plt.show()
        except ImportError:
            self.logger.error('Module matplotlib is not installed.')

    def show_keyboard_matrix(self):
        """Show the details of the keyboard matrix.
        """

        pd.set_option('display.max_rows', 200)
        self.logger.info('Keyboard matrix: \n%s', self.keyboard_matrix)

    def apply_advanced_fx(self, brightness=None):
        """Apply the advanced effect.

        Parameters
        ----------
        brightness : int or float
            Set LED backlight brightness. The value should be in range [0, 100].
        """

        for _, device in enumerate(self.devices):
            if (device.name == 'Razer BlackWidow 2019') and (device.keyboard_layout == 'en_US'):

                if isinstance(brightness, (float, int)):
                    assert 0 <= brightness <= 100
                    device.brightness = brightness
                elif brightness is None:
                    pass
                else:
                    raise TypeError('brightness should be int or float')

                for _, row in self.keyboard_matrix.iterrows():
                    device.fx.advanced.matrix[row['row'], row['column']] = row['color']
                device.fx.advanced.draw()

    @staticmethod
    def _init_logger():
        """Initialize logging.

        Returns
        -------
        logger
        """

        logformat = '%(asctime)s -- PID-%(process)d:%(levelname)s:%(name)s: %(message)s'
        logging.basicConfig(level=logging.INFO, format=logformat)
        logger = logging.getLogger(__name__)

        return logger

    @staticmethod
    def _get_keyboard_matrix(colorpal):
        """Generate keyboard matrix for Razer BlackWidow 2019.

        Parameters
        ----------
        colorpal : np.array
            Color palette.

        Returns
        -------
        pd.DataFrame
            The generated keyboard matrix.
        """

        keyboard_matrix = {
            'esc':  {'row': 0, 'column': 1, 'color': tuple(colorpal[2])},
            'F1': {'row': 0, 'column': 3, 'color': tuple(colorpal[3])},
            'F2': {'row': 0, 'column': 4, 'color': tuple(colorpal[3])},
            'F3': {'row': 0, 'column': 5, 'color': tuple(colorpal[3])},
            'F4': {'row': 0, 'column': 6, 'color': tuple(colorpal[3])},
            'F5': {'row': 0, 'column': 7, 'color': tuple(colorpal[9])},
            'F6': {'row': 0, 'column': 8, 'color': tuple(colorpal[3])},
            'F7': {'row': 0, 'column': 9, 'color': tuple(colorpal[3])},
            'F8': {'row': 0, 'column': 10, 'color': tuple(colorpal[3])},
            'F9': {'row': 0, 'column': 11, 'color': tuple(colorpal[3])},
            'F10': {'row': 0, 'column': 12, 'color': tuple(colorpal[3])},
            'F11': {'row': 0, 'column': 13, 'color': tuple(colorpal[3])},
            'F12': {'row': 0, 'column': 14, 'color': tuple(colorpal[9])},
            'prt sc': {'row': 0, 'column': 15, 'color': tuple(colorpal[3])},
            'scr lk': {'row': 0, 'column': 16, 'color': tuple(colorpal[3])},
            'pause': {'row': 0, 'column': 17, 'color': tuple(colorpal[3])},
            '`': {'row': 1, 'column': 1, 'color': tuple(colorpal[1])},
            '1': {'row': 1, 'column': 2, 'color': tuple(colorpal[4])},
            '2': {'row': 1, 'column': 3, 'color': tuple(colorpal[4])},
            '3': {'row': 1, 'column': 4, 'color': tuple(colorpal[4])},
            '4': {'row': 1, 'column': 5, 'color': tuple(colorpal[4])},
            '5': {'row': 1, 'column': 6, 'color': tuple(colorpal[4])},
            '6': {'row': 1, 'column': 7, 'color': tuple(colorpal[4])},
            '7': {'row': 1, 'column': 8, 'color': tuple(colorpal[4])},
            '8': {'row': 1, 'column': 9, 'color': tuple(colorpal[4])},
            '9': {'row': 1, 'column': 10, 'color': tuple(colorpal[4])},
            '0': {'row': 1, 'column': 11, 'color': tuple(colorpal[4])},
            '-': {'row': 1, 'column': 12, 'color': tuple(colorpal[1])},
            '=': {'row': 1, 'column': 13, 'color': tuple(colorpal[1])},
            'backspace': {'row': 1, 'column': 14, 'color': tuple(colorpal[2])},
            'ins': {'row': 1, 'column': 15, 'color': tuple(colorpal[3])},
            'home': {'row': 1, 'column': 16, 'color': tuple(colorpal[3])},
            'page_up': {'row': 1, 'column': 17, 'color': tuple(colorpal[3])},
            'num_lk': {'row': 1, 'column': 18, 'color': tuple(colorpal[8])},
            'numpad_forward_slash': {'row': 1, 'column': 19, 'color': tuple(colorpal[1])},
            'numpad_*': {'row': 1, 'column': 20, 'color': tuple(colorpal[1])},
            'numpad_-': {'row': 1, 'column': 21, 'color': tuple(colorpal[1])},
            'tab': {'row': 2, 'column': 1, 'color': tuple(colorpal[8])},
            'Q': {'row': 2, 'column': 2, 'color': tuple(colorpal[0])},
            'W': {'row': 2, 'column': 3, 'color': tuple(colorpal[0])},
            'E': {'row': 2, 'column': 4, 'color': tuple(colorpal[0])},
            'R': {'row': 2, 'column': 5, 'color': tuple(colorpal[0])},
            'T': {'row': 2, 'column': 6, 'color': tuple(colorpal[0])},
            'Y': {'row': 2, 'column': 7, 'color': tuple(colorpal[0])},
            'U': {'row': 2, 'column': 8, 'color': tuple(colorpal[0])},
            'I': {'row': 2, 'column': 9, 'color': tuple(colorpal[0])},
            'O': {'row': 2, 'column': 10, 'color': tuple(colorpal[0])},
            'P': {'row': 2, 'column': 11, 'color': tuple(colorpal[0])},
            '[': {'row': 2, 'column': 12, 'color': tuple(colorpal[1])},
            ']': {'row': 2, 'column': 13, 'color': tuple(colorpal[1])},
            'backword_slash': {'row': 2, 'column': 14, 'color': tuple(colorpal[1])},
            'del': {'row': 2, 'column': 15, 'color': tuple(colorpal[2])},
            'end': {'row': 2, 'column': 16, 'color': tuple(colorpal[3])},
            'page_down': {'row': 2, 'column': 17, 'color': tuple(colorpal[3])},
            'numpad_7': {'row': 2, 'column': 18, 'color': tuple(colorpal[4])},
            'numpad_8': {'row': 2, 'column': 19, 'color': tuple(colorpal[4])},
            'numpad_9': {'row': 2, 'column': 20, 'color': tuple(colorpal[4])},
            'numpad_+': {'row': 2, 'column': 21, 'color': tuple(colorpal[1])},
            'caps': {'row': 3, 'column': 1, 'color': tuple(colorpal[8])},
            'A': {'row': 3, 'column': 2, 'color': tuple(colorpal[0])},
            'S': {'row': 3, 'column': 3, 'color': tuple(colorpal[0])},
            'D': {'row': 3, 'column': 4, 'color': tuple(colorpal[0])},
            'F': {'row': 3, 'column': 5, 'color': tuple(colorpal[0])},
            'G': {'row': 3, 'column': 6, 'color': tuple(colorpal[0])},
            'H': {'row': 3, 'column': 7, 'color': tuple(colorpal[0])},
            'J': {'row': 3, 'column': 8, 'color': tuple(colorpal[0])},
            'K': {'row': 3, 'column': 9, 'color': tuple(colorpal[0])},
            'L': {'row': 3, 'column': 10, 'color': tuple(colorpal[0])},
            ';': {'row': 3, 'column': 11, 'color': tuple(colorpal[1])},
            "'": {'row': 3, 'column': 12, 'color': tuple(colorpal[1])},
            'enter': {'row': 3, 'column': 14, 'color': tuple(colorpal[8])},
            'numpad_4': {'row': 3, 'column': 18, 'color': tuple(colorpal[4])},
            'numpad_5': {'row': 3, 'column': 19, 'color': tuple(colorpal[4])},
            'numpad_6': {'row': 3, 'column': 20, 'color': tuple(colorpal[4])},
            'left_shift': {'row': 4, 'column': 1, 'color': tuple(colorpal[2])},
            'Z': {'row': 4, 'column': 3, 'color': tuple(colorpal[0])},
            'X': {'row': 4, 'column': 4, 'color': tuple(colorpal[0])},
            'C': {'row': 4, 'column': 5, 'color': tuple(colorpal[0])},
            'V': {'row': 4, 'column': 6, 'color': tuple(colorpal[0])},
            'B': {'row': 4, 'column': 7, 'color': tuple(colorpal[0])},
            'N': {'row': 4, 'column': 8, 'color': tuple(colorpal[0])},
            'M': {'row': 4, 'column': 9, 'color': tuple(colorpal[0])},
            ',': {'row': 4, 'column': 10, 'color': tuple(colorpal[1])},
            '.': {'row': 4, 'column': 11, 'color': tuple(colorpal[1])},
            'forward_slash': {'row': 4, 'column': 12, 'color': tuple(colorpal[1])},
            'right_shift': {'row': 4, 'column': 14, 'color': tuple(colorpal[2])},
            'arrow_up': {'row': 4, 'column': 16, 'color': tuple(colorpal[2])},
            'numpad_1': {'row': 4, 'column': 18, 'color': tuple(colorpal[4])},
            'numpad_2': {'row': 4, 'column': 19, 'color': tuple(colorpal[4])},
            'numpad_3': {'row': 4, 'column': 20, 'color': tuple(colorpal[4])},
            'numpad_enter': {'row': 4, 'column': 21, 'color': tuple(colorpal[8])},
            'left_ctrl': {'row': 5, 'column': 1, 'color': tuple(colorpal[5])},
            'windows': {'row': 5, 'column': 2, 'color': tuple(colorpal[9])},
            'left_alt': {'row': 5, 'column': 3, 'color': tuple(colorpal[8])},
            'space': {'row': 5, 'column': 6, 'color': tuple(colorpal[0])},
            'right_alt': {'row': 5, 'column': 10, 'color': tuple(colorpal[5])},
            'razer_logo': {'row': 5, 'column': 11, 'color': tuple(colorpal[2])},
            'fn': {'row': 5, 'column': 12, 'color': tuple(colorpal[9])},
            'properties': {'row': 5, 'column': 13, 'color': tuple(colorpal[8])},
            'right_ctrl': {'row': 5, 'column': 14, 'color': tuple(colorpal[6])},
            'arrow_left': {'row': 5, 'column': 15, 'color': tuple(colorpal[2])},
            'arrow_down': {'row': 5, 'column': 16, 'color': tuple(colorpal[2])},
            'arrow_right': {'row': 5, 'column': 17, 'color': tuple(colorpal[2])},
            'numpad_0': {'row': 5, 'column': 19, 'color': tuple(colorpal[4])},
            'numpad_.': {'row': 5, 'column': 20, 'color': tuple(colorpal[2])}
        }

        return pd.DataFrame(keyboard_matrix).T
