import uuid
from django.db import models
from django.contrib.auth.models import User
from menus.models import Product

class Tabulation(models.Model): #cria a comanda ao entrar, mesmo sem ter pedido
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    establishment = models.ForeignKey(User, on_delete=models.CASCADE)
    origin = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    STATES = (
        ('op', 'Open'),
        ('cl', 'Close'),
    )
    state = models.CharField(max_length=2, choices=STATES, default='op')
    value = models.FloatField(default=0)

    def __str__(self):
        return "Mesa: "+ str(self.origin) + " - "+str(self.date)

class Order(models.Model): #pedido sao criados apos comanda já ter sido feita
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tabulation = models.ForeignKey(Tabulation, on_delete=models.CASCADE, related_name='orders')
    STATES = (
        ('wa', 'Waiting'),
        ('re', 'Ready'),
        ('de', 'Delivery'),
    )
    state = models.CharField(max_length=2, choices=STATES, default='wa')
    def __str__(self):
        #return str(self.quantity) + " -  MESA: " + str(self.tabulation.origin)
        return str(self.quantity) + " - "+str(self.product) + " MESA: " + str(self.tabulation.origin)
