import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_ecommerce_data(days=90, sessions_per_day_avg=200):
    np.random.seed(42)
    random.seed(42)
    
    end_date = datetime.today()
    start_date = end_date - timedelta(days=days)
    date_range = pd.date_range(start=start_date, end=end_date)
    
    sources = ['google / organic', 'google / cpc', 'direct / none', 'facebook / referral', 'email / newsletter']
    source_weights = [0.4, 0.25, 0.15, 0.1, 0.1]
    
    countries = ['United States', 'India', 'United Kingdom', 'Canada', 'Australia', 'Germany']
    country_weights = [0.4, 0.2, 0.15, 0.1, 0.05, 0.1]
    
    devices = ['Mobile', 'Desktop', 'Tablet']
    device_weights = [0.55, 0.40, 0.05]
    
    pages = ['/home', '/shop', '/product/shoes', '/product/tshirt', '/cart', '/checkout', '/blog']
    
    journeys_converted = [
        "/home > /shop > /product/shoes > /cart > /checkout",
        "/home > /product/tshirt > /cart > /checkout",
        "/google / cpc > /product/shoes > /cart > /checkout"
    ]
    
    journeys_bounced = [
        "/home",
        "/blog",
        "/product/shoes",
        "/shop"
    ]
    
    journeys_engaged_not_converted = [
        "/home > /shop > /product/shoes",
        "/home > /blog > /shop",
        "/shop > /product/tshirt > /cart",
        "/home > /shop > /product/shoes > /product/tshirt"
    ]
    
    data = []
    user_id_counter = 1000
    
    for current_date in date_range:
        daily_sessions = int(np.random.normal(sessions_per_day_avg, sessions_per_day_avg * 0.2))
        if current_date.weekday() >= 5:
            daily_sessions = int(daily_sessions * 0.8) 
            
        for _ in range(daily_sessions):
            session_id = f"S_{random.randint(100000, 999999)}"
            
            is_returning = random.choices([True, False], weights=[0.3, 0.7])[0]
            if is_returning:
                user_id = f"U_{random.randint(1000, user_id_counter)}"
                user_type = "Returning"
            else:
                user_id_counter += 1
                user_id = f"U_{user_id_counter}"
                user_type = "New"
                
            source_medium = random.choices(sources, weights=source_weights)[0]
            country = random.choices(countries, weights=country_weights)[0]
            device = random.choices(devices, weights=device_weights)[0]
            
            base_cr = 0.03
            if device == 'Desktop': base_cr += 0.02
            if source_medium == 'email / newsletter': base_cr += 0.03
            if source_medium == 'google / organic': base_cr += 0.01
            if is_returning: base_cr += 0.02
            
            converted = 1 if random.random() < base_cr else 0
            
            if converted == 1:
                engaged = 1
                journey = random.choice(journeys_converted)
                session_duration = random.randint(120, 600)
                revenue = round(random.uniform(20.0, 150.0), 2)
            else:
                engaged = 1 if random.random() < 0.4 else 0
                if engaged == 1:
                    journey = random.choice(journeys_engaged_not_converted)
                    session_duration = random.randint(30, 300)
                else:
                    journey = random.choice(journeys_bounced)
                    session_duration = random.randint(0, 10)
                revenue = 0.0
                
            top_page = journey.split(" > ")[-1] if not converted else journey.split(" > ")[-2]
            
            data.append([
                current_date.strftime('%Y-%m-%d'),
                user_id,
                session_id,
                user_type,
                source_medium,
                country,
                device,
                engaged,
                converted,
                revenue,
                session_duration,
                journey,
                top_page
            ])
            
    df = pd.DataFrame(data, columns=[
        'Date', 'User_ID', 'Session_ID', 'User_Type', 'Source_Medium', 
        'Country', 'Device_Category', 'Is_Engaged', 'Converted', 'Revenue',
        'Session_Duration_Seconds', 'User_Journey', 'Top_Page'
    ])
    
    df.to_csv('web_analytics_data.csv', index=False)

if __name__ == "__main__":
    generate_ecommerce_data()