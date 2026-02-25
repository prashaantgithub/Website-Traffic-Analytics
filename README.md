# 📊 E-Commerce Web Analytics Dashboard

An interactive web analytics dashboard built with Python and Streamlit to analyze website performance, user behavior, and conversion metrics. This project provides actionable insights into traffic sources, user journeys, and sales trends to support data-driven decision-making.

## 🚀 Live Demo

**[View the Live Dashboard](https://share.streamlit.io/prashaantgithub/website-traffic-analytics/main/app.py)**  
*(Note: If the link is not yet active, please deploy via Streamlit Community Cloud)*

---

## 📌 Project Overview

This dashboard serves as a central hub for monitoring key e-commerce metrics. It is designed to help marketing and product teams understand:
*   **Acquisition:** Where are users coming from? (Organic, Paid, Social, etc.)
*   **Engagement:** Which pages are most popular and how long do users stay?
*   **Retention:** How many users are returning vs. new?
*   **Conversion:** What is the conversion rate across different devices and channels?

## 📂 Features

### 1. Overview Page
*   **KPI Metrics:** Total Users, Sessions, Conversions, and Engagement Rate.
*   **Trend Analysis:** Daily sessions trend line to spot traffic spikes and drops.

### 2. Traffic Analysis
*   **Source/Medium Breakdown:** Visualizes traffic distribution (e.g., Google/Organic vs. Facebook/Referral).
*   **User Demographics:** Top countries map and New vs. Returning user ratio.

### 3. Behaviour Analysis
*   **Top Pages:** Identifies the most visited content and product pages.
*   **User Journey (Path):** Tracks the sequence of pages users visit (e.g., Home > Shop > Cart > Checkout).
*   **Device Performance:** Compares engagement metrics across Desktop, Mobile, and Tablet.

### 4. Conversion Analysis
*   **Sales Funnel:** Analysis of conversion rates by marketing channel.
*   **Device Conversion:** Highlights which devices drive the most revenue.
*   **Trend Monitoring:** tracks daily conversion rate fluctuations over the selected period.

---

## 🛠️ Tech Stack

*   **Python:** Core programming language.
*   **Streamlit:** Framework for building the interactive web application.
*   **Pandas:** For data manipulation and analysis.
*   **Plotly:** For creating interactive and dynamic visualizations.
*   **NumPy:** For numerical operations.

---

## 🔧 Installation & Setup

To run this dashboard locally on your machine:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/prashaantgithub/Website-Traffic-Analytics.git
    cd Website-Traffic-Analytics
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    streamlit run app.py
    ```

The dashboard will open automatically in your browser at `http://localhost:8501`.

---

## 📊 Data Structure

The dashboard utilizes a structured dataset containing the following key fields:
*   `Date`: Daily timestamps for trend analysis.
*   `User_ID` & `Session_ID`: Unique identifiers for tracking distinct users and visits.
*   `Source_Medium`: Origin of the traffic (e.g., google/organic).
*   `Device_Category`: Device type used for access.
*   `Converted`: Boolean flag indicating if a purchase was made.
*   `User_Journey`: The specific path taken through the website.

---

## 📷 Screenshots

### Overview Dashboard
*(Add screenshot of Overview tab here)*

### Traffic Analysis
*(Add screenshot of Traffic tab here)*

---

## 🤝 Contribution

Contributions are welcome! If you have suggestions for new metrics or visualizations, feel free to open an issue or submit a pull request.

1.  Fork the repository
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

**Developed by Prashaant C**
