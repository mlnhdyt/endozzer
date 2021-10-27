from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class PositiveBigIntegerField(models.BigIntegerField):
    empty_strings_allowed = False
    description = _("Big (8 byte) positive integer")

    def db_type(self, connection):
        """
        Returns MySQL-specific column data type. Make additional checks
        to support other backends.
        """
        return 'bigint UNSIGNED'

    def formfield(self, **kwargs):
        defaults = {'min_value': 0,
                    'max_value': models.BigIntegerField.MAX_BIGINT * 2 - 1}
        defaults.update(kwargs)
        return super(PositiveBigIntegerField, self).formfield(**defaults)