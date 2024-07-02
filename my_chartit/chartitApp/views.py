from django.shortcuts import render
from .models import SalesReport
from chartit import DataPool, Chart

def home(request):
    first_graph = "My first chartit_django graph"
    return render(request, 'home.html', {'first_graph': first_graph})

def sales(request):
    # Retrieve sales data from your model
    sales_data = SalesReport.objects.all()

    # Check if there's no data
    if not sales_data.exists():
        return render(request, 'sales.html', {'message': 'No sales data available.'})

    print("Sales Data:", sales_data)  # Print retrieved sales data

    # Prepare data for Chartit
    sales_data_for_chartit = DataPool(
        series=[
            {
                'options': {
                    'source': sales_data,
                },
                'terms': {
                    'month': 'month_name',
                    'sales': 'sales'
                }
            },
        ]
    )

    # Print the processed data
    for entry in sales_data:
        print(f"Month: {entry.month_name}, Sales: {entry.sales}")

    # Create the column chart
    column_chart = Chart(
        datasource=sales_data_for_chartit,
        series_options=[
            {
                'options': {
                    'type': 'column',
                    'stacking': False
                },
                'terms': {
                    'month': ['sales']  # Use 'month_name' field from SalesReport model
                },
            },
        ],
        chart_options={
            'title': {
                'text': 'Sales Amount Over Months - Column Chart'
            },
            'accessibility': {
                'enabled': True
            },
            'xAxis': {
                'title': {
                    'text': 'Month'
                },
                'categories': [entry.month_name for entry in sales_data]
            }
        },
    )

    # Render the template with the column chart
    return render(request, 'sales.html', {'column_chart': column_chart})

# views.py

from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()  # Fetches all products from the database
    return render(request, 'product_list.html', {'products': products})

# views.py or custom_query.py

from django.db import connection

def custom_query():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM your_table WHERE condition;")
        rows = cursor.fetchall()
    return rows
