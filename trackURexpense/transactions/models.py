from django.db import models

from users.models import User


class MinMaxFloat(models.FloatField):
    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        super(MinMaxFloat, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value' : self.max_value}
        defaults.update(kwargs)
        return super(MinMaxFloat, self).formfield(**defaults)


class Expenditure(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='expenditures',
    )
    amount = MinMaxFloat(min_value=0.0)
    date = models.DateTimeField()

    def __str__(self):
        return str(self.id)


class Income(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='incomes',
    )
    amount = MinMaxFloat(min_value=0.0)
    date = models.DateTimeField()

    def __str__(self):
        return str(self.id)
