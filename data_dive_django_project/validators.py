from django.core.exceptions import ValidationError
from django.utils.translation import gettext

import re
from abc import ABC, abstractmethod


class MinimumCharsValidator(ABC):
    def __init__(self, min_chars=0):
        self.min_chars = min_chars

   
    def validate(self, password, user=None):
        if self.min_chars == 0:  # Password doesnt require numbers
            return

        counter = 0
        for char in password:
            if re.match(self.get_pattern(), char):
                counter += 1
            if counter > self.min_chars:
                break

        if counter < self.min_chars:
            raise ValidationError(
                self.get_help_text(),
                code='password_not_enough_numbers'
            )

    @property
    @abstractmethod
    def get_pattern(self):
        pass

    @abstractmethod
    def get_help_text(self):
        pass


class MinimumNumbersCharsValidator(MinimumCharsValidator):

    def get_pattern(self):
        return '[0-9]'

    def get_help_text(self):
        gettext(
            f'This password must contain at least {self.min_chars} numbers!'),


class MinimumSpecialCharsValidator(MinimumCharsValidator):

    def get_pattern(self):
        return '?=.*\W'

    def get_help_text(self):
        gettext(
            f'This password must contain at least {self.min_chars} special characters!')
