import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Web Analytics Dashboard", layout="wide", initial_sidebar_state="expanded")

@st.cache_data
def load_data():
    df = pd.read_csv('web_analytics_data.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

st.sidebar.title("Dashboard Controls")

min_date = df['Date'].min().date()
max_date = df['Date'].max().date()

start_date, end_date = st.sidebar.date_input(
    "Select Date Range",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

traffic_sources = df['Source_Medium'].unique().tolist()
selected_sources = st.sidebar.multiselect(
    "Filter by Traffic Source",
    options=traffic_sources,
    default=traffic_sources
)

mask = (df['Date'].dt.date >= start_date) & (df['Date'].dt.date <= end_date) & (df['Source_Medium'].isin(selected_sources))
filtered_df = df.loc[mask]

st.title("Web Analytics Dashboard")

if filtered_df.empty:
    st.warning("No data available for the selected filters.")
    st.stop()

tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Traffic Analysis", "Behaviour", "Conversion"])

with tab1:
    st.header("Overview")
    
    total_users = filtered_df['User_ID'].nunique()
    total_sessions = filtered_df['Session_ID'].nunique()
    total_conversions = filtered_df['Converted'].sum()
    engagement_rate = (filtered_df['Is_Engaged'].sum() / total_sessions) * 100 if total_sessions > 0 else 0
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Users", f"{total_users:,}")
    col2.metric("Sessions", f"{total_sessions:,}")
    col3.metric("Conversions", f"{total_conversions:,}")
    col4.metric("Engagement Rate", f"{engagement_rate:.2f}%")

    daily_sessions = filtered_df.groupby(filtered_df['Date'].dt.date)['Session_ID'].nunique().reset_index()
    daily_sessions.columns = ['Date', 'Sessions']
    fig_sessions = px.line(daily_sessions, x='Date', y='Sessions', title="Daily Sessions Trend", markers=True)
    st.plotly_chart(fig_sessions, use_container_width=True)

with tab2:
    st.header("Traffic Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        users_by_source = filtered_df.groupby('Source_Medium')['User_ID'].nunique().reset_index()
        users_by_source.columns = ['Source/Medium', 'Users']
        users_by_source = users_by_source.sort_values(by='Users', ascending=True)
        fig_source = px.bar(users_by_source, x='Users', y='Source/Medium', orientation='h', title="Users by Source/Medium")
        st.plotly_chart(fig_source, use_container_width=True)
        
    with col2:
        new_vs_returning = filtered_df.groupby('User_Type')['User_ID'].nunique().reset_index()
        fig_new_ret = px.pie(new_vs_returning, values='User_ID', names='User_Type', title="New vs Returning Users", hole=0.4)
        st.plotly_chart(fig_new_ret, use_container_width=True)

    top_countries = filtered_df.groupby('Country')['User_ID'].nunique().reset_index()
    top_countries.columns = ['Country', 'Users']
    top_countries = top_countries.sort_values(by='Users', ascending=False)
    fig_countries = px.bar(top_countries, x='Country', y='Users', title="Top Countries by Users", color='Users')
    st.plotly_chart(fig_countries, use_container_width=True)

with tab3:
    st.header("Behaviour Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        top_pages = filtered_df['Top_Page'].value_counts().reset_index()
        top_pages.columns = ['Page', 'Pageviews']
        fig_pages = px.bar(top_pages, x='Page', y='Pageviews', title="Top Pages")
        st.plotly_chart(fig_pages, use_container_width=True)
        
    with col2:
        device_perf = filtered_df.groupby('Device_Category').agg(
            Sessions=('Session_ID', 'nunique'),
            Avg_Duration=('Session_Duration_Seconds', 'mean')
        ).reset_index()
        fig_device = px.bar(device_perf, x='Device_Category', y='Sessions', title="Device Category Performance", text_auto=True)
        st.plotly_chart(fig_device, use_container_width=True)

    st.subheader("User Journey (Path)")
    journey_counts = filtered_df['User_Journey'].value_counts().reset_index()
    journey_counts.columns = ['Path', 'Frequency']
    st.dataframe(journey_counts, use_container_width=True)

with tab4:
    st.header("Conversion Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        conv_by_channel = filtered_df.groupby('Source_Medium')['Converted'].sum().reset_index()
        conv_by_channel = conv_by_channel.sort_values(by='Converted', ascending=True)
        fig_conv_channel = px.bar(conv_by_channel, x='Converted', y='Source_Medium', orientation='h', title="Conversions by Channel")
        st.plotly_chart(fig_conv_channel, use_container_width=True)
        
    with col2:
        device_conv = filtered_df.groupby('Device_Category')['Converted'].sum().reset_index()
        fig_device_conv = px.pie(device_conv, values='Converted', names='Device_Category', title="Conversions by Device")
        st.plotly_chart(fig_device_conv, use_container_width=True)

    daily_conv = filtered_df.groupby(filtered_df['Date'].dt.date).agg(
        Sessions=('Session_ID', 'nunique'),
        Conversions=('Converted', 'sum')
    ).reset_index()
    daily_conv['Conversion Rate (%)'] = (daily_conv['Conversions'] / daily_conv['Sessions']) * 100
    daily_conv['Conversion Rate (%)'] = daily_conv['Conversion Rate (%)'].fillna(0)
    
    fig_cr_trend = px.line(daily_conv, x='Date', y='Conversion Rate (%)', title="Conversion Rate Trend", markers=True)
    st.plotly_chart(fig_cr_trend, use_container_width=True)