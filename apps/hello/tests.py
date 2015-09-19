from apps.hello import models
from django.test import TestCase


class HelloTests(TestCase):
    """
    create a test record into base
    """    
    def test_devinfo_displayed(self):            
        models.Devinfo.objects.create(name='Roma',
            lastname='Shevchuk',
            birthdate='1985-05-17', bio='...',
            email='wrongman@gmail.com',
            jabber='wr0ngman@khavr.com',
            skype='wr0ngman',
            othcontacts='+380989682061')
        dev = models.Devinfo.objects.get(pk=1)
        assert(dev.name == u'Roma')
        assert(dev.lastname == u'Shevchuk')
        assert(dev.birthdate.strftime('%Y-%m-%d') == u'1985-05-17')
        assert(dev.email == u'wrongman@gmail.com')
        assert(dev.jabber == u'wr0ngman@khavr.com')
        assert(dev.skype == u'wr0ngman')
        assert(dev.othcontacts == u'+380989682061')
