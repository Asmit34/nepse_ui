from django.shortcuts import render, redirect
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
    WeeklyReport,
    MonthlyReport,
    AnnualReport,
    AGMReport,
    ClassificationOfListedCompany,
)
from django.core.mail import send_mail
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q


def fetch_and_render(request, model, template_name):
    """Fetch all records from the given model and render the specified template."""
    data = model.objects.all()
    context = {model.__name__.lower() + 's': data}
    return render(request, template_name, context)

def index_view(request):
    """Render the index page with the latest market summary."""
    try:
        market_summary = MarketSummary.objects.latest('businessDate')
    except MarketSummary.DoesNotExist:
        market_summary = None  # Handle the case where there is no data

    context = {
        'market_summary': market_summary,
    }
    return render(request, 'app/index.html', context)

def terms_condition_view(request):
    """Render the terms and conditions page."""
    return render(request, 'app/terms_conditions.html')

def all_securities_view(request):
    """Render the all securities page."""
    all_securities = AllSecurities.objects.all()
    return render(request, 'app/all_securities.html', {'all_securities': all_securities})

def broker_data_view(request):
    """Render the broker data page."""
    broker_data = BrokerData.objects.all()
    return render(request, 'app/broker_data.html', {'broker_data': broker_data})

def live_indices_view(request):
    search_query = request.GET.get('search', '')

    if search_query:
        # Filter by the "key" (column '0') or "value" (column '1'), converting them to strings for comparison
        live_indices = LiveIndices.objects.filter(
            Q(key__icontains=search_query) | Q(value__icontains=search_query)
        )
    else:
        live_indices = LiveIndices.objects.all()

    # Since key and value are numeric, ensure they are cast to strings for display in the template
    live_indices = [
        {'key': str(index.key), 'value': str(index.value)} for index in live_indices
    ]

    return render(request, 'app/live_indices.html', {'live_indices': live_indices})

def live_stock_view(request):
    live_stocks = LiveStock.objects.all()
    paginator = Paginator(live_stocks, 25)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'live_stocks': page_obj}
    return render(request, 'app/live_stock.html', context)


def market_cap_view(request):
    market_caps_list = MarketCap.objects.all()
    paginator = Paginator(market_caps_list, 10)

    page_number = request.GET.get('page')
    market_caps = paginator.get_page(page_number)

    context = {
        'market_caps': market_caps
    }
    return render(request, 'app/market_cap.html', context)

def market_summary_view(request):
    query = request.GET.get('search', '')
    # Fetch all MarketSummary objects
    market_summaries_list = MarketSummary.objects.all()

    # Filter by search query if it exists
    if query:
        market_summaries_list = market_summaries_list.filter(businessDate__icontains=query)

    paginator = Paginator(market_summaries_list, 20) 
    page_number = request.GET.get('page')
    market_summaries = paginator.get_page(page_number)

    context = {
        'market_summaries': market_summaries,
        'search_query': query,
    }
    return render(request, 'app/market_summary.html', context)

def nepal_listed_securities_view(request):
    # Get the search query from the request, if provided
    search_query = request.GET.get('q', '')

    # Filter listed securities based on the search query
    if search_query:
        securities = NepalListedSecurities.objects.filter(Name__icontains=search_query)
    else:
        securities = NepalListedSecurities.objects.all()

    paginator = Paginator(securities, 25) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }

    return render(request, 'app/nepal_listed_securities_data.html', context)

def sectorwise_summary_view(request):
    # Get the search query from the request (for Business Date)
    search_query = request.GET.get('q', '')

    # Filter sectorwise summaries based on the search query (Business Date)
    if search_query:
        summaries = SectorwiseSummary.objects.filter(businessDate__icontains=search_query)
    else:
        summaries = SectorwiseSummary.objects.all()

    context = {
        'sectorwise_summaries': summaries,
        'search_query': search_query,
    }

    return render(request, 'app/sectorwise_summary.html', context)

def todays_prices_view(request):
    query = request.GET.get('query', '')
    todays_prices = TodaysPrices.objects.all()

    if query:
        todays_prices = todays_prices.filter(Q(security_id__icontains=query) | 
                                             Q(symbol__icontains=query) | 
                                             Q(security_name__icontains=query))
    paginator = Paginator(todays_prices, 25)
    page_number = request.GET.get('page')
    todays_prices = paginator.get_page(page_number)

    return render(request, 'app/todays_prices.html', {'todays_prices': todays_prices, 'query': query})

def top_gainers_view(request):
    # Get the search query from the request (for Security ID)
    search_query = request.GET.get('q', '')

    # Filter top gainers based on the search query (Security ID)
    if search_query:
        gainers = TopGainer.objects.filter(securityId__icontains=search_query)
    else:
        gainers = TopGainer.objects.all()


    paginator = Paginator(gainers, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }

    return render(request, 'app/top_gainers.html', context)

def top_loser_view(request):
    """Render the top loser page."""
    return fetch_and_render(request, TopLoser, 'app/top_losers.html')

def top_loser_view(request):
    # Get the search query from the request (for Security ID)
    search_query = request.GET.get('q', '')

    # Filter top losers based on the search query (Security ID)
    if search_query:
        losers = TopLoser.objects.filter(securityId__icontains=search_query)
    else:
        losers = TopLoser.objects.all()

    # Pagination - 10 items per page
    paginator = Paginator(losers, 25)  # Show 10 results per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }

    return render(request, 'app/top_losers.html', context)

def top_trades_view(request):
    query = request.GET.get('query', '')
    top_trades = TopTrades.objects.all()

    if query:
        top_trades = top_trades.filter(security_id__icontains=query)

    paginator = Paginator(top_trades, 25)
    page_number = request.GET.get('page')
    top_trades = paginator.get_page(page_number)

    return render(request, 'app/top_trades.html', {'top_trades': top_trades, 'query': query})

from django.shortcuts import render
from django.core.paginator import Paginator
from .models import FloorSheet

def floorsheet_data_view(request):
    # Get the query parameter for stock symbol search
    query = request.GET.get('query', '')

    # Fetch all FloorSheet records, or filter by stockSymbol if a search is performed
    if query:
        floorsheet_records = FloorSheet.objects.filter(stockSymbol__icontains=query)
    else:
        floorsheet_records = FloorSheet.objects.all()

    # Pagination (25 records per page)
    paginator = Paginator(floorsheet_records, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'floorsheet_records': page_obj,
        'query': query,
    }

    return render(request, 'app/floorsheet_data.html', context)

def top_transactions_view(request):
    query = request.GET.get('query', '')
    transactions = TopTransaction.objects.all()

    if query:
        transactions = transactions.filter(security_id__icontains=query)

    paginator = Paginator(transactions, 25)
    page_number = request.GET.get('page')
    top_transactions = paginator.get_page(page_number)

    return render(request, 'app/top_transactions.html', {
        'top_transactions': top_transactions,
    })

def top_turnover_view(request):
    """Render the top turnover page."""
    return fetch_and_render(request, TopTurnover, 'app/top_turnover.html')

def trading_average_view(request):
    query = request.GET.get('query', '')
    trading_averages = TradingAverage.objects.all()

    if query:
        trading_averages = trading_averages.filter(security_id__icontains=query)

    paginator = Paginator(trading_averages, 25)
    page_number = request.GET.get('page')
    trading_averages = paginator.get_page(page_number)

    return render(request, 'app/trading_average.html', {
        'trading_averages': trading_averages,
    })

def about_view(request):
    """Render the about page."""
    return render(request, 'app/about_us.html')

def contact_us_view(request):
    """Render the contact us page."""
    return render(request, 'app/contact.html')

def faq_view(request):
    """Render the FAQ page."""
    return render(request, 'app/faq.html')

def send_message_view(request):
    """Handle the contact form submission."""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            f'Message from {name}',
            message,
            email,
            ['your_email@example.com'],
            fail_silently=False,
        )

        messages.success(request, 'Your message has been sent successfully!')

        # Redirect to the contact page or another success page
        return redirect('contact_us')

    # Handle invalid requests
    messages.error(request, 'Invalid request. Please try again.')
    return redirect('contact_us')  # Redirect to the contact page


def weekly_reports_view(request):
    query = request.GET.get('q', '')
    date = request.GET.get('date', '')

    # Use the correct field name for ordering
    reports = WeeklyReport.objects.all().order_by('-publishedDate')

    # Filter by name
    if query:
        reports = reports.filter(Name__icontains=query)
    # Filter by date
    if date:
        reports = reports.filter(publishedDate=date)

    # Paginate results
    paginator = Paginator(reports, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Handle case where no reports are found
    if not reports.exists():
        message = "No reports found for the given criteria."
    else:
        message = None

    context = {
        'query': query,
        'date': date,
        'page_obj': page_obj,
        'message': message,
    }

    return render(request, 'app/weekly_reports.html', context)





def monthly_reports_view(request):
    query = request.GET.get('q', '')
    date = request.GET.get('date', '')

    # Retrieve all reports and order them by published date
    reports = MonthlyReport.objects.all().order_by('-publishedDate')

    # Filter by name if a query is provided
    if query:
        reports = reports.filter(Name__icontains=query)
    
    # Filter by date if provided
    if date:
        reports = reports.filter(publishedDate=date)

    # Paginate the results, showing 25 reports per page
    paginator = Paginator(reports, 25)  # Show 25 reports per page
    page_number = request.GET.get('page', 1)  # Default to the first page if none provided
    page_obj = paginator.get_page(page_number)  # Get the page object

    # Handle case where no reports are found
    if not reports.exists():
        message = "No reports found for the given criteria."
    else:
        message = None

    # Prepare the context for rendering the template
    context = {
        'query': query,
        'date': date,
        'page_obj': page_obj,
        'message': message,
    }

    return render(request, 'app/monthly_reports.html', context)




def annual_reports_view(request):
    query = request.GET.get('q', '')
    date = request.GET.get('date', '')

    # Use the correct field name for ordering
    reports = AnnualReport.objects.all().order_by('-publishedDate')

    # Filter by name
    if query:
        reports = reports.filter(Name__icontains=query)
    # Filter by date
    if date:
        reports = reports.filter(publishedDate=date)

    # Paginate results
    paginator = Paginator(reports, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Handle case where no reports are found
    if not reports.exists():
        message = "No reports found for the given criteria."
    else:
        message = None

    context = {
        'query': query,
        'date': date,
        'page_obj': page_obj,
        'message': message,
    }

    return render(request, 'app/annual_reports.html', context)



def agm_reports_view(request):
    query = request.GET.get('q', '')
    date = request.GET.get('date', '')

    # Use the correct field name for ordering
    reports = AGMReport.objects.all().order_by('-publishedDate')

    # Filter by name
    if query:
        reports = reports.filter(Name__icontains=query)
    # Filter by date
    if date:
        reports = reports.filter(publishedDate=date)

    # Paginate results
    paginator = Paginator(reports, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Handle case where no reports are found
    if not reports.exists():
        message = "No reports found for the given criteria."
    else:
        message = None

    context = {
        'query': query,
        'date': date,
        'page_obj': page_obj,
        'message': message,
    }

    return render(request, 'app/agm_reports.html', context)


def listing_info(request):
    return render(request, 'app/listing_info.html')

def listed_company_view(request):
    # Get the 'class' parameter from the query string for filtering
    search_class = request.GET.get('class', '')

    # Filter the queryset based on the search criteria if provided
    if search_class:
        companies = ClassificationOfListedCompany.objects.filter(Class__icontains=search_class)
    else:
        companies = ClassificationOfListedCompany.objects.all()

    # Set up pagination with 10 items per page
    paginator = Paginator(companies, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Render the template with the companies and the current search term
    context = {
        'page_obj': page_obj,
        'search_class': search_class,
    }
    return render(request, 'app/listed_company.html', context)