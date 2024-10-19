# Generated by Django 5.1.1 on 2024-10-08 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AllSecurities",
            fields=[
                ("id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("companyName", models.TextField(max_length=255)),
                ("symbol", models.TextField(max_length=50)),
                ("securityName", models.TextField(max_length=255)),
                ("status", models.TextField(max_length=1)),
                (
                    "companyEmail",
                    models.TextField(blank=True, max_length=255, null=True),
                ),
                ("website", models.TextField(blank=True, max_length=255, null=True)),
                ("sectorName", models.TextField(max_length=255)),
                ("regulatoryBody", models.TextField(max_length=255)),
                ("instrumentType", models.TextField(max_length=50)),
            ],
            options={
                "db_table": "all_securities",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="BrokerData",
            fields=[
                (
                    "total_pages",
                    models.IntegerField(
                        db_column="totalPages", primary_key=True, serialize=False
                    ),
                ),
                ("last", models.BooleanField()),
                ("total_elements", models.IntegerField(db_column="totalElements")),
                ("size", models.IntegerField()),
                ("number", models.IntegerField()),
                ("first", models.BooleanField()),
                (
                    "number_of_elements",
                    models.IntegerField(db_column="numberOfElements"),
                ),
                ("empty", models.BooleanField()),
                (
                    "pageable_sort_unsorted",
                    models.BooleanField(db_column="pageable.sort.unsorted"),
                ),
                (
                    "pageable_sort_sorted",
                    models.BooleanField(db_column="pageable.sort.sorted"),
                ),
                (
                    "pageable_sort_empty",
                    models.BooleanField(db_column="pageable.sort.empty"),
                ),
                ("pageable_offset", models.IntegerField(db_column="pageable.offset")),
                (
                    "pageable_page_number",
                    models.IntegerField(db_column="pageable.pageNumber"),
                ),
                (
                    "pageable_page_size",
                    models.IntegerField(db_column="pageable.pageSize"),
                ),
                ("pageable_paged", models.BooleanField(db_column="pageable.paged")),
                ("pageable_unpaged", models.BooleanField(db_column="pageable.unpaged")),
                ("sort_unsorted", models.BooleanField(db_column="sort.unsorted")),
                ("sort_sorted", models.BooleanField(db_column="sort.sorted")),
                ("sort_empty", models.BooleanField(db_column="sort.empty")),
            ],
            options={
                "db_table": "broker_data",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="FloorSheet",
            fields=[
                ("SN", models.TextField(primary_key=True, serialize=False)),
                ("Contract_No", models.TextField(db_column="Contract No.")),
                ("stockSymbol", models.TextField(db_column="Stock Symbol")),
                ("Buyer", models.DecimalField(decimal_places=2, max_digits=20)),
                ("Seller", models.DecimalField(decimal_places=2, max_digits=20)),
                (
                    "Rate",
                    models.DecimalField(
                        db_column="Rate (Rs)", decimal_places=2, max_digits=20
                    ),
                ),
                (
                    "Amount",
                    models.DecimalField(
                        db_column="Amount (Rs)", decimal_places=2, max_digits=20
                    ),
                ),
            ],
            options={
                "db_table": "floorsheet_data",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="LiveIndices",
            fields=[
                (
                    "key",
                    models.BigIntegerField(
                        db_column="0", primary_key=True, serialize=False
                    ),
                ),
                ("value", models.FloatField(db_column="1")),
            ],
            options={
                "db_table": "live_indices",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="LiveStock",
            fields=[
                (
                    "securityId",
                    models.BigIntegerField(primary_key=True, serialize=False),
                ),
                ("securityName", models.TextField(max_length=200)),
                ("symbol", models.TextField(max_length=20)),
                ("indexId", models.BigIntegerField()),
                ("openPrice", models.DecimalField(decimal_places=2, max_digits=20)),
                ("highPrice", models.DecimalField(decimal_places=2, max_digits=20)),
                ("lowPrice", models.DecimalField(decimal_places=2, max_digits=20)),
                ("totalTradeQuantity", models.BigIntegerField()),
                (
                    "totalTradeValue",
                    models.DecimalField(decimal_places=2, max_digits=20),
                ),
                (
                    "lastTradedPrice",
                    models.DecimalField(decimal_places=2, max_digits=20),
                ),
                (
                    "percentageChange",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                ("lastUpdatedDateTime", models.TextField()),
                ("lastTradedVolume", models.BigIntegerField()),
                ("previousClose", models.DecimalField(decimal_places=2, max_digits=20)),
                (
                    "averageTradedPrice",
                    models.DecimalField(decimal_places=2, max_digits=20),
                ),
            ],
            options={
                "db_table": "live_stock",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="MarketCap",
            fields=[
                ("businessDate", models.TextField(primary_key=True, serialize=False)),
                ("senMarCap", models.DecimalField(decimal_places=2, max_digits=20)),
                (
                    "senFloatMarCap",
                    models.DecimalField(decimal_places=2, max_digits=20),
                ),
                ("floatMarCap", models.DecimalField(decimal_places=2, max_digits=20)),
                ("marCap", models.DecimalField(decimal_places=2, max_digits=20)),
            ],
            options={
                "db_table": "market_cap",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="MarketSummary",
            fields=[
                ("businessDate", models.TextField(primary_key=True, serialize=False)),
                ("totalTurnover", models.FloatField()),
                ("totalTradedShares", models.BigIntegerField()),
                ("totalTransactions", models.BigIntegerField()),
                ("tradedScrips", models.BigIntegerField()),
            ],
            options={
                "db_table": "market_summary",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="NepalListedSecurities",
            fields=[
                ("SN", models.BigIntegerField(primary_key=True, serialize=False)),
                ("Name", models.TextField(max_length=200)),
                ("Symbol", models.TextField(max_length=20)),
                ("Status", models.TextField(max_length=50)),
                ("Sector", models.TextField(max_length=100)),
                ("Instrument", models.TextField(max_length=100)),
                ("Email", models.TextField(blank=True, max_length=100, null=True)),
                ("Website", models.TextField(blank=True, max_length=200, null=True)),
            ],
            options={
                "db_table": "nepal_listed_securities_data",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="SectorwiseSummary",
            fields=[
                ("businessDate", models.TextField(primary_key=True, serialize=False)),
                ("sectorName", models.TextField(max_length=100)),
                (
                    "turnOverValues",
                    models.DecimalField(decimal_places=2, max_digits=20),
                ),
                ("turnOverVolume", models.BigIntegerField()),
                ("totalTransaction", models.BigIntegerField()),
            ],
            options={
                "db_table": "sectorwise_summary",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="TodaysPrices",
            fields=[
                ("BUSINESS_DATE", models.DateTimeField(blank=True, null=True)),
                ("SECURITY_ID", models.IntegerField(primary_key=True, serialize=False)),
                ("SYMBOL", models.CharField(max_length=20)),
                ("SECURITY_NAME", models.CharField(max_length=200)),
                ("OPEN_PRICE", models.DecimalField(decimal_places=2, max_digits=20)),
                ("HIGH_PRICE", models.DecimalField(decimal_places=2, max_digits=20)),
                ("LOW_PRICE", models.DecimalField(decimal_places=2, max_digits=20)),
                ("CLOSE_PRICE", models.DecimalField(decimal_places=2, max_digits=20)),
                ("TOTAL_TRADED_QUANTITY", models.IntegerField()),
                (
                    "TOTAL_TRADED_VALUE",
                    models.DecimalField(decimal_places=2, max_digits=20),
                ),
                (
                    "PREVIOUS_DAY_CLOSE_PRICE",
                    models.DecimalField(decimal_places=2, max_digits=20),
                ),
                (
                    "FIFTY_TWO_WEEKS_HIGH",
                    models.DecimalField(decimal_places=2, max_digits=20),
                ),
                (
                    "FIFTY_TWO_WEEKS_LOW",
                    models.DecimalField(decimal_places=2, max_digits=20),
                ),
                ("LAST_UPDATED_TIME", models.DateTimeField(blank=True, null=True)),
                (
                    "LAST_UPDATED_PRICE",
                    models.DecimalField(decimal_places=2, max_digits=20),
                ),
                ("TOTAL_TRADES", models.IntegerField()),
                (
                    "AVERAGE_TRADED_PRICE",
                    models.DecimalField(decimal_places=2, max_digits=20),
                ),
                (
                    "MARKET_CAPITALIZATION",
                    models.DecimalField(decimal_places=2, max_digits=20),
                ),
            ],
            options={
                "db_table": "todays_prices",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="TopGainer",
            fields=[
                (
                    "symbol",
                    models.TextField(max_length=20, primary_key=True, serialize=False),
                ),
                ("ltp", models.DecimalField(decimal_places=2, max_digits=20)),
                ("pointChange", models.DecimalField(decimal_places=2, max_digits=20)),
                (
                    "percentageChange",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                ("securityName", models.TextField(max_length=200)),
                ("securityId", models.BigIntegerField()),
            ],
            options={
                "db_table": "top_gainers",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="TopLoser",
            fields=[
                (
                    "symbol",
                    models.TextField(max_length=20, primary_key=True, serialize=False),
                ),
                ("ltp", models.DecimalField(decimal_places=2, max_digits=20)),
                ("pointChange", models.DecimalField(decimal_places=2, max_digits=20)),
                (
                    "percentageChange",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                ("securityName", models.TextField(max_length=200)),
                ("securityId", models.BigIntegerField()),
            ],
            options={
                "db_table": "top_losers",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="TopTrades",
            fields=[
                (
                    "symbol",
                    models.TextField(max_length=20, primary_key=True, serialize=False),
                ),
                ("shareTraded", models.BigIntegerField()),
                ("closingPrice", models.DecimalField(decimal_places=2, max_digits=20)),
                ("securityName", models.TextField(max_length=200)),
                ("securityId", models.BigIntegerField()),
            ],
            options={
                "db_table": "top_trades",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="TopTransaction",
            fields=[
                (
                    "securityId",
                    models.BigIntegerField(primary_key=True, serialize=False),
                ),
                ("totalTrades", models.BigIntegerField()),
                (
                    "lastTradedPrice",
                    models.DecimalField(decimal_places=2, max_digits=20),
                ),
                ("securityName", models.TextField(max_length=200)),
                ("symbol", models.TextField(max_length=20)),
            ],
            options={
                "db_table": "top_transactions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="TopTurnover",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("symbol", models.CharField(max_length=20)),
                ("turnover", models.DecimalField(decimal_places=2, max_digits=20)),
                ("closingPrice", models.DecimalField(decimal_places=2, max_digits=20)),
                ("securityName", models.CharField(max_length=200)),
                ("securityId", models.IntegerField()),
            ],
            options={
                "db_table": "top_turnover",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="TradingAverage",
            fields=[
                (
                    "securityId",
                    models.BigIntegerField(primary_key=True, serialize=False),
                ),
                ("symbol", models.TextField(max_length=20)),
                ("securityName", models.TextField(max_length=200)),
                (
                    "closingPriceAverage",
                    models.DecimalField(decimal_places=2, max_digits=20),
                ),
                (
                    "totalTradedAmount",
                    models.DecimalField(decimal_places=2, max_digits=20),
                ),
                ("totalTradedShares", models.BigIntegerField()),
                ("totalTrades", models.BigIntegerField()),
                (
                    "weightedAverage",
                    models.DecimalField(decimal_places=2, max_digits=20),
                ),
                ("closePrice", models.DecimalField(decimal_places=2, max_digits=20)),
                ("closingDate", models.TextField()),
            ],
            options={
                "db_table": "trading_average",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="WeeklyReport",
            fields=[
                ("SN", models.BigIntegerField(primary_key=True, serialize=False)),
                ("Name", models.TextField(db_column="Contract No.")),
                ("Description", models.TextField(db_column="Stock Symbol")),
                ("publishedDate", models.TextField(db_column=" Published Date")),
                ("fileLink", models.TextField(db_column="File Link")),
            ],
            options={
                "db_table": "weekly_reports",
                "managed": False,
            },
        ),
    ]
