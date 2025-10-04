from django.contrib import admin
from .models import User, SIPTransaction, ServiceFeeSlab, BitcoinPriceHistory, UserSIPRunningMetric

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password_hash', 'created_at')
    search_fields = ('username', 'email')

@admin.register(SIPTransaction)
class SIPTransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'monthly_sip_amount', 'bitcoin_price_inr', 'bitcoin_quantity', 'service_fee_paid', 'net_investment')
    list_filter = ('date', 'user')
    search_fields = ('user__username',)

@admin.register(ServiceFeeSlab)
class ServiceFeeSlabAdmin(admin.ModelAdmin):
    list_display = ('min_sip_amount', 'max_sip_amount', 'fee_percentage')
    search_fields = ('min_sip_amount', 'max_sip_amount')

@admin.register(BitcoinPriceHistory)
class BitcoinPriceHistoryAdmin(admin.ModelAdmin):
    list_display = ('date', 'price_inr')
    list_filter = ('date',)

@admin.register(UserSIPRunningMetric)
class UserSIPRunningMetricAdmin(admin.ModelAdmin):
    list_display = ('user', 'metric_name', 'metric_value')
    search_fields = ('user__username', 'metric_name')
