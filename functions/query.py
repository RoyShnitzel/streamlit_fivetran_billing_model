import streamlit as st
import pandas as pd

data_columns = ['header_id',
                'line_item_id',
                'line_item_index',
                'record_type',
                'created_at',
                'currency',
                'header_status',
                'product_id',
                'product_name',
                'transaction_type',
                'billing_type',
                'product_type',
                'quantity',
                'unit_amount',
                'discount_amount',
                'tax_amount',
                'total_amount',
                'payment_id',
                'payment_method_id',
                'payment_method',
                'payment_at',
                'fee_amount',
                'refund_amount',
                'subscription_id',
                'subscription_plan',
                'subscription_period_started_at',
                'subscription_period_ended_at',
                'subscription_status',
                'customer_id',
                'customer_created_at',
                'customer_level',
                'customer_name',
                'customer_company',
                'customer_email',
                'customer_city',
                'customer_country'
                ]

@st.cache_data(ttl=600)

def query_results():
    ## Currently we are only pulling from the dummy sample data. However, this could be expanded for direct table in warehouse connection.
    query = pd.read_csv('data/example__line_item_enhanced.csv')
    data = pd.DataFrame(query, columns=data_columns)

    # Convert all datetime columns to UTC timezone-aware datetimes
    datetime_columns = ['created_at', 'customer_created_at', 'payment_at', 'subscription_period_started_at', 'subscription_period_ended_at']
    for col in datetime_columns:
        if col in data.columns:
            data[col] = pd.to_datetime(data[col], errors='coerce', utc=True)
        
    data_load_state = st.text('Loading data...')
    # Convert created_at to date for filtering purposes, but keep timezone info
    data['created_at'] = data['created_at'].dt.date
    data_load_state.text("Done! (using st.cache_data)")

    return data