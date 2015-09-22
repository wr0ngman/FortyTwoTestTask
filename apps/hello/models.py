from django.db import models


""" Subscribe developer information model fields """


class Devinfo(models.Model):
    name = models.CharField(max_length=70)
    lastname = models.CharField(max_length=70)
    birthdate = models.DateField()
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.CharField(max_length=70)
    skype = models.CharField(max_length=70)
    othcontacts = models.TextField()

    def __unicode__(self):
        return u'Information about: %s %s' % (self.name, self.lastname)
