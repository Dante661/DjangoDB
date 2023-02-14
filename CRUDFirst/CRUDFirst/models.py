from django.db import models


class EmpModel(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """

    empname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    occuapation = models.CharField(max_length=100)
    salary = models.IntegerField()
    gender = models.CharField(max_length=1)

    class Meta:
        '''good'''
        db_table = 'employ11'
