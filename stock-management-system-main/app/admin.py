from django.contrib import admin
from .models import (
    AllSecurities,
    BrokerData,
    LiveIndices,
    LiveStock,
    MarketSummary,
    MarketCap,
    NepalListedSecurities,
    SectorwiseSummary,
    TodaysPrices,
    TopGainer,
    TopLoser,
    TopTrades,
    TopTransaction,
    TopTurnover,
    TradingAverage,
)

class AllSecuritiesAdmin(admin.ModelAdmin):
    list_display = ['companyName', 'symbol', 'securityName', 'status', 'sectorName']
    search_fields = ['companyName', 'symbol']
    list_filter = ['status', 'sectorName']
    list_editable = ['status']
    ordering = ['companyName']
    list_per_page = 20

class BrokerDataAdmin(admin.ModelAdmin):
    list_display = ['total_pages', 'last', 'total_elements']
    list_filter = ['total_pages']
    ordering = ['total_pages']
    list_per_page = 20

class LiveIndicesAdmin(admin.ModelAdmin):
    list_display = ['key', 'value']
    ordering = ['key']

class LiveStockAdmin(admin.ModelAdmin):
    list_display = ['securityId', 'securityName', 'symbol', 'lastTradedPrice', 'percentageChange']
    search_fields = ['securityName', 'symbol']
    ordering = ['lastTradedPrice']
    list_per_page = 20

class MarketSummaryAdmin(admin.ModelAdmin):
    list_display = ['businessDate', 'totalTurnover', 'totalTradedShares']
    list_filter = ['businessDate']
    ordering = ['businessDate']
    list_per_page = 20
    readonly_fields = ['businessDate']

class MarketCapAdmin(admin.ModelAdmin):
    list_display = ['businessDate', 'senMarCap', 'marCap']
    ordering = ['businessDate']

class NepalListedSecuritiesAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Symbol', 'Status', 'Sector']
    search_fields = ['Name', 'Symbol']
    list_filter = ['Status', 'Sector']
    list_per_page = 20

class SectorwiseSummaryAdmin(admin.ModelAdmin):
    list_display = ['businessDate', 'sectorName', 'turnOverVolume']
    list_filter = ['businessDate', 'sectorName']
    ordering = ['businessDate']

class TodaysPricesAdmin(admin.ModelAdmin):
    list_display = ['BUSINESS_DATE', 'SECURITY_ID', 'SYMBOL', 'OPEN_PRICE', 'CLOSE_PRICE']
    list_filter = ['BUSINESS_DATE']
    ordering = ['BUSINESS_DATE']
    list_per_page = 20

class TopGainerAdmin(admin.ModelAdmin):
    list_display = ['symbol', 'ltp', 'percentageChange', 'securityName']
    search_fields = ['symbol', 'securityName']
    fieldsets = (
        (None, {
            'fields': ('symbol', 'securityName')
        }),
        ('Performance', {
            'fields': ('ltp', 'percentageChange'),
        }),
    )
    ordering = ['percentageChange']
    list_per_page = 20

class TopLoserAdmin(admin.ModelAdmin):
    list_display = ['symbol', 'ltp', 'percentageChange', 'securityName']
    search_fields = ['symbol', 'securityName']
    fieldsets = (
        (None, {
            'fields': ('symbol', 'securityName')
        }),
        ('Performance', {
            'fields': ('ltp', 'percentageChange'),
        }),
    )
    ordering = ['percentageChange']
    list_per_page = 20

class TopTradesAdmin(admin.ModelAdmin):
    list_display = ['symbol', 'shareTraded', 'closingPrice']
    search_fields = ['symbol']
    ordering = ['shareTraded']
    list_per_page = 20

class TopTransactionAdmin(admin.ModelAdmin):
    list_display = ['securityId', 'totalTrades', 'lastTradedPrice', 'symbol']
    ordering = ['totalTrades']
    list_per_page = 20

class TopTurnoverAdmin(admin.ModelAdmin):
    list_display = ['symbol', 'turnover', 'closingPrice']
    ordering = ['turnover']
    list_per_page = 20

class TradingAverageAdmin(admin.ModelAdmin):
    list_display = ['securityId', 'symbol', 'closingPriceAverage', 'totalTradedAmount']
    list_filter = ['closingDate']
    ordering = ['closingDate']
    list_per_page = 20

# Registering models with the admin site
admin.site.register(AllSecurities, AllSecuritiesAdmin)
admin.site.register(BrokerData, BrokerDataAdmin)
admin.site.register(LiveIndices, LiveIndicesAdmin)
admin.site.register(LiveStock, LiveStockAdmin)
admin.site.register(MarketSummary, MarketSummaryAdmin)
admin.site.register(NepalListedSecurities, NepalListedSecuritiesAdmin)
admin.site.register(SectorwiseSummary, SectorwiseSummaryAdmin)
admin.site.register(TodaysPrices, TodaysPricesAdmin)
admin.site.register(TopGainer, TopGainerAdmin)
admin.site.register(TopLoser, TopLoserAdmin)
admin.site.register(TopTrades, TopTradesAdmin)
admin.site.register(TopTransaction, TopTransactionAdmin)
admin.site.register(TopTurnover, TopTurnoverAdmin)
admin.site.register(TradingAverage, TradingAverageAdmin)
admin.site.register(MarketCap, MarketCapAdmin)
