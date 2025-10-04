from django.db import models
from django.utils import timezone

# User model
class User(models.Model):
    username = models.CharField(max_length=150, unique=True, default='user1')
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255, default='password')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username

# Service Fee Slabs
class ServiceFeeSlab(models.Model):
    min_sip_amount = models.DecimalField(max_digits=15, decimal_places=2, default=1000)
    max_sip_amount = models.DecimalField(max_digits=15, decimal_places=2, default=100000)
    fee_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.min_sip_amount} - {self.max_sip_amount}"

# SIP Transactions
class SIPTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    monthly_sip_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    bitcoin_price_inr = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    bitcoin_quantity = models.DecimalField(max_digits=15, decimal_places=8, default=0)
    service_fee_paid = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    net_investment = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return f"SIP {self.id} - {self.user.username}"

# Bitcoin Price History
class BitcoinPriceHistory(models.Model):
    date = models.DateField(default=timezone.now)
    price_inr = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.date} - {self.price_inr}"

# User SIP Running Metrics
class UserSIPRunningMetric(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    metric_name = models.CharField(max_length=255)
    metric_value = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.username} - {self.metric_name}"
