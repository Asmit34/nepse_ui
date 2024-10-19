from django.db import models
from django.utils import timezone

class AllSecurities(models.Model):
    id = models.BigIntegerField(primary_key=True)
    companyName = models.TextField(max_length=255)
    symbol = models.TextField(max_length=50)
    securityName = models.TextField(max_length=255)
    status = models.TextField(max_length=1)
    companyEmail = models.TextField(max_length=255, null=True, blank=True)
    website = models.TextField(max_length=255, null=True, blank=True)
    sectorName = models.TextField(max_length=255)
    regulatoryBody = models.TextField(max_length=255)
    instrumentType = models.TextField(max_length=50)

    class Meta:
        db_table = 'all_securities'
        managed = False

class BrokerData(models.Model):
    total_pages = models.IntegerField(db_column='totalPages',primary_key=True)
    last = models.BooleanField()
    total_elements = models.IntegerField(db_column='totalElements')
    size = models.IntegerField()
    number = models.IntegerField()
    first = models.BooleanField()
    number_of_elements = models.IntegerField(db_column='numberOfElements')
    empty = models.BooleanField()

    # Pageable-related fields
    pageable_sort_unsorted = models.BooleanField(db_column='pageable.sort.unsorted')
    pageable_sort_sorted = models.BooleanField(db_column='pageable.sort.sorted')
    pageable_sort_empty = models.BooleanField(db_column='pageable.sort.empty') 
    pageable_offset = models.IntegerField(db_column='pageable.offset') 
    pageable_page_number = models.IntegerField(db_column='pageable.pageNumber')
    pageable_page_size = models.IntegerField(db_column='pageable.pageSize')
    pageable_paged = models.BooleanField(db_column='pageable.paged')
    pageable_unpaged = models.BooleanField(db_column='pageable.unpaged')

    # Sort-related fields
    sort_unsorted = models.BooleanField(db_column='sort.unsorted')
    sort_sorted = models.BooleanField(db_column='sort.sorted')
    sort_empty = models.BooleanField(db_column='sort.empty')

    class Meta:
        db_table = 'broker_data'
        managed = False



class LiveIndices(models.Model):
    key = models.BigIntegerField(db_column='0',primary_key= True)
    value = models.FloatField(db_column='1')

    class Meta:
        db_table = 'live_indices'
        managed = False


class LiveStock(models.Model):
    securityId = models.BigIntegerField(primary_key= True)
    securityName = models.TextField(max_length=200)
    symbol = models.TextField(max_length=20)
    indexId = models.BigIntegerField()
    openPrice = models.DecimalField(max_digits=20, decimal_places=2)
    highPrice = models.DecimalField(max_digits=20, decimal_places=2)
    lowPrice = models.DecimalField(max_digits=20, decimal_places=2)
    totalTradeQuantity = models.BigIntegerField()
    totalTradeValue = models.DecimalField(max_digits=20, decimal_places=2)
    lastTradedPrice = models.DecimalField(max_digits=20, decimal_places=2)
    percentageChange = models.DecimalField(max_digits=5, decimal_places=2)
    lastUpdatedDateTime = models.TextField()
    lastTradedVolume = models.BigIntegerField()
    previousClose = models.DecimalField(max_digits=20, decimal_places=2)
    averageTradedPrice = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        db_table = 'live_stock'
        managed = False


class MarketSummary(models.Model):
    businessDate = models.TextField(primary_key=True) 
    totalTurnover = models.FloatField()
    totalTradedShares = models.BigIntegerField() 
    totalTransactions = models.BigIntegerField()
    tradedScrips = models.BigIntegerField()

    class Meta:
        db_table = 'market_summary'

        managed = False


class NepalListedSecurities(models.Model):
    SN = models.BigIntegerField(primary_key=True)
    Name = models.TextField(max_length=200)
    Symbol = models.TextField(max_length=20)
    Status = models.TextField(max_length=50)
    Sector = models.TextField(max_length=100)
    Instrument = models.TextField(max_length=100)
    Email = models.TextField(max_length=100, blank=True, null=True)
    Website = models.TextField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'nepal_listed_securities_data'
        managed = False


class SectorwiseSummary(models.Model):
    businessDate = models.TextField(primary_key=True)
    sectorName = models.TextField(max_length=100)
    turnOverValues = models.DecimalField(max_digits=20, decimal_places=2)
    turnOverVolume = models.BigIntegerField()
    totalTransaction = models.BigIntegerField()

    class Meta:
        db_table = 'sectorwise_summary'
        managed = False

class TodaysPrices(models.Model):
    BUSINESS_DATE = models.DateTimeField(null=True, blank=True)
    SECURITY_ID = models.IntegerField(primary_key=True)
    SYMBOL = models.CharField(max_length=20)
    SECURITY_NAME = models.CharField(max_length=200)
    OPEN_PRICE = models.DecimalField(max_digits=20, decimal_places=2)
    HIGH_PRICE = models.DecimalField(max_digits=20, decimal_places=2)
    LOW_PRICE = models.DecimalField(max_digits=20, decimal_places=2)
    CLOSE_PRICE = models.DecimalField(max_digits=20, decimal_places=2)
    TOTAL_TRADED_QUANTITY = models.IntegerField()
    TOTAL_TRADED_VALUE = models.DecimalField(max_digits=20, decimal_places=2)
    PREVIOUS_DAY_CLOSE_PRICE = models.DecimalField(max_digits=20, decimal_places=2)
    FIFTY_TWO_WEEKS_HIGH = models.DecimalField(max_digits=20, decimal_places=2)
    FIFTY_TWO_WEEKS_LOW = models.DecimalField(max_digits=20, decimal_places=2)
    LAST_UPDATED_TIME = models.DateTimeField(null=True, blank=True)
    LAST_UPDATED_PRICE = models.DecimalField(max_digits=20, decimal_places=2)
    TOTAL_TRADES = models.IntegerField()
    AVERAGE_TRADED_PRICE = models.DecimalField(max_digits=20, decimal_places=2)
    MARKET_CAPITALIZATION = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        db_table = 'todays_prices'
        managed = False


class TopGainer(models.Model):
    symbol = models.TextField(max_length=20, primary_key=True)
    ltp = models.DecimalField(max_digits=20, decimal_places=2)
    pointChange = models.DecimalField(max_digits=20, decimal_places=2)
    percentageChange = models.DecimalField(max_digits=5, decimal_places=2)
    securityName = models.TextField(max_length=200)
    securityId = models.BigIntegerField()

    class Meta:
        db_table = 'top_gainers'
        managed = False


class TopLoser(models.Model):
    symbol = models.TextField(max_length=20, primary_key=True)
    ltp = models.DecimalField(max_digits=20, decimal_places=2)
    pointChange = models.DecimalField(max_digits=20, decimal_places=2)
    percentageChange = models.DecimalField(max_digits=5, decimal_places=2)
    securityName = models.TextField(max_length=200)
    securityId = models.BigIntegerField()

    class Meta:
        db_table = 'top_losers'
        managed = False


class TopTrades(models.Model):
    symbol = models.TextField(max_length=20, primary_key=True)
    shareTraded = models.BigIntegerField()
    closingPrice = models.DecimalField(max_digits=20, decimal_places=2)
    securityName = models.TextField(max_length=200)
    securityId = models.BigIntegerField()

    class Meta:
        db_table = 'top_trades'
        managed = False


class TopTransaction(models.Model):
    securityId = models.BigIntegerField(primary_key=True)
    totalTrades = models.BigIntegerField()
    lastTradedPrice = models.DecimalField(max_digits=20, decimal_places=2)
    securityName = models.TextField(max_length=200)
    symbol = models.TextField(max_length=20)

    class Meta:
        db_table = 'top_transactions'
        managed = False


class TopTurnover(models.Model):
    symbol = models.CharField(max_length=20)
    turnover = models.DecimalField(max_digits=20, decimal_places=2)
    closingPrice = models.DecimalField(max_digits=20, decimal_places=2)
    securityName = models.CharField(max_length=200)
    securityId = models.IntegerField()

    class Meta:
        db_table = 'top_turnover'
        managed = False


class TradingAverage(models.Model):
    securityId = models.BigIntegerField(primary_key=True)
    symbol = models.TextField(max_length=20)
    securityName = models.TextField(max_length=200)
    closingPriceAverage = models.DecimalField(max_digits=20, decimal_places=2)
    totalTradedAmount = models.DecimalField(max_digits=20, decimal_places=2)
    totalTradedShares = models.BigIntegerField()
    totalTrades = models.BigIntegerField()
    weightedAverage = models.DecimalField(max_digits=20, decimal_places=2)
    closePrice = models.DecimalField(max_digits=20, decimal_places=2)
    closingDate = models.TextField()

    class Meta:
        db_table = 'trading_average'
        managed = False


class MarketCap(models.Model):
    businessDate = models.TextField(primary_key=True)
    senMarCap = models.DecimalField(max_digits=20, decimal_places=2)  
    senFloatMarCap = models.DecimalField(max_digits=20, decimal_places=2) 
    floatMarCap = models.DecimalField(max_digits=20, decimal_places=2)
    marCap = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        db_table = 'market_cap'
        managed = False

from django.db import models

class FloorSheet(models.Model):
    SN = models.TextField(primary_key=True)
    Contract_No = models.TextField(db_column='Contract No.')
    stockSymbol = models.TextField(db_column='Stock Symbol')
    Buyer = models.DecimalField(max_digits=20, decimal_places=2) 
    Seller = models.DecimalField(max_digits=20, decimal_places=2)
    Rate = models.DecimalField(max_digits=20, decimal_places=2, db_column='Rate (Rs)')
    Amount = models.DecimalField(max_digits=20, decimal_places=2, db_column='Amount (Rs)')

    class Meta:
        db_table = 'floorsheet_data'
        managed = False

class WeeklyReport(models.Model):
    SN = models.BigIntegerField(primary_key=True)
    Name = models.TextField()
    Description = models.TextField()
    publishedDate = models.TextField(db_column="Published Date") 
    fileLink = models.TextField(db_column="File Link")


    class Meta:
        db_table = 'weekly_reports'
        managed = False



class MonthlyReport(models.Model):
    SN = models.BigIntegerField(primary_key=True)
    Name = models.TextField()
    Description = models.TextField()
    publishedDate = models.TextField(db_column="Published Date") 
    fileLink = models.TextField(db_column="File Link")


    class Meta:
        db_table = 'monthly_reports'
        managed = False

class AnnualReport(models.Model):
    SN = models.BigIntegerField(primary_key=True)
    Name = models.TextField()
    Description = models.TextField()
    publishedDate = models.TextField(db_column="Published Date") 
    fileLink = models.TextField(db_column="File Link")


    class Meta:
        db_table = 'annual_reports'
        managed = False


class AGMReport(models.Model):
    SN = models.BigIntegerField(primary_key=True)
    Name = models.TextField()
    Description = models.TextField()
    publishedDate = models.TextField(db_column="Published Date") 
    fileLink = models.TextField(db_column="File Link")


    class Meta:
        db_table = 'agm_reports'
        managed = False

class ClassificationOfListedCompany(models.Model):
    SN = models.BigIntegerField(primary_key=True)
    Name = models.TextField()
    Symbol = models.TextField()
    Status = models.TextField() 
    Sector = models.TextField()
    Class = models.TextField()
    Instrument = models.TextField()


    class Meta:
        db_table = 'listed_company'
        managed = False