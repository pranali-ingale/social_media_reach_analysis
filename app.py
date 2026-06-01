"""
Social Media Reach Analysis Dashboard
A comprehensive Streamlit dashboard for analyzing social media performance
across multiple platforms with Indian audience insights.
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import sys
import os

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from analysis import (
    load_data, calculate_kpis, filter_data, get_reach_trend,
    get_platform_performance, get_content_type_performance,
    get_best_posting_day, get_best_posting_time, get_followers_growth,
    get_top_posts, get_viral_content, generate_insights,
    calculate_total_engagement
)

# Page configuration
st.set_page_config(
    page_title="Social Media Reach Analysis Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    /* Main container styling */
    .main {
        background-color: #0e1117;
    }
    
    /* KPI Cards - Dark theme with high contrast */
    .stMetric {
        background-color: #1e2128;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        border: 1px solid #2d3748;
    }
    
    .stMetric label {
        color: #e2e8f0 !important;
        font-size: 14px;
        font-weight: 600;
    }
    
    .stMetric div[data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-size: 28px;
        font-weight: 700;
    }
    
    .stMetric div[data-testid="stMetricDelta"] {
        color: #68d391 !important;
        font-size: 13px;
    }
    
    /* Headings */
    h1, h2, h3 {
        color: #ffffff;
        font-weight: 700;
    }
    
    /* Subheadings */
    .stSubheader {
        color: #e2e8f0 !important;
    }
    
    /* Reduce padding */
    .css-1d391kg {
        padding-top: 1rem;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #1e2128;
    }
    
    /* Dataframe styling */
    .stDataFrame {
        background-color: #1e2128;
        border-radius: 8px;
    }
    
    /* Info boxes */
    .stInfo {
        background-color: #2d3748;
        border-left: 4px solid #4299e1;
    }
    
    .stSuccess {
        background-color: #276749;
        border-left: 4px solid #48bb78;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #4299e1;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 600;
    }
    
    .stButton > button:hover {
        background-color: #3182ce;
    }
    
    /* Download button */
    .stDownloadButton > button {
        background-color: #48bb78;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 600;
    }
    
    .stDownloadButton > button:hover {
        background-color: #38a169;
    }
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_dataset():
    """Load and cache the dataset."""
    data_path = 'data/social_media_data.csv'
    return load_data(data_path)

# Dataframe safety function
def safe_dataframe(df):
    """
    Remove duplicate columns and ensure dataframe is safe for display.
    
    Args:
        df (pd.DataFrame): Input dataframe
        
    Returns:
        pd.DataFrame: Safe dataframe with unique columns
    """
    if df is None or df.empty:
        return df
    
    # Remove duplicate columns
    df = df.loc[:, ~df.columns.duplicated()].copy()
    
    return df

# Initialize session state
if 'df' not in st.session_state:
    st.session_state.df = load_dataset()

df = st.session_state.df

# Sidebar
st.sidebar.title("📊 Social Media Dashboard")
st.sidebar.markdown("---")

# Platform filter in sidebar
all_platforms = df['Platform'].unique()
selected_platforms = st.sidebar.multiselect(
    "Select Platforms",
    options=all_platforms,
    default=all_platforms
)

# Content type filter in sidebar
all_content_types = df['Content Type'].unique()
selected_content_types = st.sidebar.multiselect(
    "Select Content Types",
    options=all_content_types,
    default=all_content_types
)

# Date range filter in sidebar
min_date = df['Post Date'].min().date()
max_date = df['Post Date'].max().date()
selected_date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Apply filters
filtered_df = filter_data(
    df,
    platforms=selected_platforms if selected_platforms else None,
    content_types=selected_content_types if selected_content_types else None,
    date_range=selected_date_range if len(selected_date_range) == 2 else None
)

# Export filtered data
st.sidebar.markdown("---")
st.sidebar.subheader("📥 Export Data")
csv = filtered_df.to_csv(index=False)
st.sidebar.download_button(
    label="Download Filtered Data (CSV)",
    data=csv,
    file_name=f'social_media_data_{datetime.now().strftime("%Y%m%d")}.csv',
    mime='text/csv'
)

# Navigation
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "Navigate to",
    ["📈 Overview", "📊 Analytics", "🏆 Top Posts", "💡 Insights"]
)

# Main content
st.title("Social Media Reach Analysis Dashboard")
st.markdown(f"**Analyzing {len(filtered_df):,} posts** | Indian Audience Insights (IST)")
st.markdown("---")

# OVERVIEW PAGE
if page == "📈 Overview":
    st.header("📈 Overview")
    st.markdown("Key Performance Indicators (KPIs) across all platforms")
    
    # Calculate KPIs
    kpis = calculate_kpis(filtered_df)
    
    # Display KPI cards with better spacing
    col1, col2, col3, col4, col5 = st.columns(5, gap="small")
    
    with col1:
        st.metric(
            label="Total Reach",
            value=f"{kpis['Total Reach']:,}",
            delta="Unique users reached"
        )
    
    with col2:
        total_eng = kpis['Total Engagement']
        st.metric(
            label="Total Engagement",
            value=f"{total_eng:,}",
            delta="Likes + Comments + Shares + Saves"
        )
    
    with col3:
        st.metric(
            label="Total Impressions",
            value=f"{kpis['Total Impressions']:,}",
            delta="Total views"
        )
    
    with col4:
        st.metric(
            label="Followers Gained",
            value=f"{kpis['Total Followers Gained']:,}",
            delta="Net growth"
        )
    
    with col5:
        st.metric(
            label="Best Platform",
            value=kpis['Best Performing Platform'],
            delta="Highest engagement rate"
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Platform distribution chart
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        st.subheader("Platform Distribution")
        platform_counts = filtered_df['Platform'].value_counts()
        fig_platform = px.pie(
            values=platform_counts.values,
            names=platform_counts.index,
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig_platform.update_layout(
            title="Posts by Platform",
            showlegend=True,
            height=350,
            margin=dict(l=0, r=0, t=30, b=0)
        )
        st.plotly_chart(fig_platform, use_container_width=True)
    
    with col2:
        st.subheader("Content Type Distribution")
        content_counts = filtered_df['Content Type'].value_counts()
        fig_content = px.bar(
            x=content_counts.index,
            y=content_counts.values,
            color=content_counts.index,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig_content.update_layout(
            title="Posts by Content Type",
            xaxis_title="Content Type",
            yaxis_title="Number of Posts",
            showlegend=False,
            height=350,
            margin=dict(l=0, r=0, t=30, b=0)
        )
        st.plotly_chart(fig_content, use_container_width=True)
    
    # Engagement rate by platform
    st.subheader("Average Engagement Rate by Platform")
    platform_engagement = filtered_df.groupby('Platform')['Engagement Rate'].mean().sort_values(ascending=False)
    fig_eng = px.bar(
        x=platform_engagement.index,
        y=platform_engagement.values,
        color=platform_engagement.index,
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    fig_eng.update_layout(
        title="Engagement Rate Comparison",
        xaxis_title="Platform",
        yaxis_title="Engagement Rate (%)",
        showlegend=False,
        height=350,
        margin=dict(l=0, r=0, t=30, b=0)
    )
    st.plotly_chart(fig_eng, use_container_width=True)

# ANALYTICS PAGE
elif page == "📊 Analytics":
    st.header("📊 Analytics")
    st.markdown("Detailed analysis with interactive visualizations")
    
    # 1. Reach Trend Analysis
    st.subheader("1. Reach Trend Analysis")
    reach_trend = get_reach_trend(filtered_df)
    fig_trend = px.line(
        reach_trend,
        x='Post Date',
        y='Reach',
        title='Reach Over Time',
        markers=True
    )
    fig_trend.update_layout(
        xaxis_title="Date",
        yaxis_title="Reach",
        height=350,
        margin=dict(l=0, r=0, t=30, b=0)
    )
    st.plotly_chart(fig_trend, use_container_width=True)
    
    # 2. Platform Performance Comparison
    st.subheader("2. Platform Performance Comparison")
    platform_perf = get_platform_performance(filtered_df)
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        fig_reach = px.bar(
            platform_perf,
            x='Platform',
            y='Reach',
            title='Total Reach by Platform',
            color='Platform',
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        fig_reach.update_layout(showlegend=False, height=300, margin=dict(l=0, r=0, t=30, b=0))
        st.plotly_chart(fig_reach, use_container_width=True)
    
    with col2:
        fig_eng_rate = px.bar(
            platform_perf,
            x='Platform',
            y='Engagement Rate',
            title='Average Engagement Rate by Platform',
            color='Platform',
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        fig_eng_rate.update_layout(showlegend=False, height=300, margin=dict(l=0, r=0, t=30, b=0))
        st.plotly_chart(fig_eng_rate, use_container_width=True)
    
    # 3. Content Type Performance
    st.subheader("3. Content Type Performance")
    content_perf = get_content_type_performance(filtered_df)
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        fig_content_reach = px.bar(
            content_perf,
            x='Content Type',
            y='Reach',
            title='Total Reach by Content Type',
            color='Content Type',
            color_discrete_sequence=px.colors.qualitative.Pastel1
        )
        fig_content_reach.update_layout(showlegend=False, height=300, margin=dict(l=0, r=0, t=30, b=0))
        st.plotly_chart(fig_content_reach, use_container_width=True)
    
    with col2:
        fig_content_eng = px.bar(
            content_perf,
            x='Content Type',
            y='Engagement Rate',
            title='Engagement Rate by Content Type',
            color='Content Type',
            color_discrete_sequence=px.colors.qualitative.Pastel1
        )
        fig_content_eng.update_layout(showlegend=False, height=300, margin=dict(l=0, r=0, t=30, b=0))
        st.plotly_chart(fig_content_eng, use_container_width=True)
    
    # 4. Engagement Rate Analysis
    st.subheader("4. Engagement Rate Distribution")
    fig_box = px.box(
        filtered_df,
        x='Platform',
        y='Engagement Rate',
        color='Platform',
        title='Engagement Rate Distribution by Platform'
    )
    fig_box.update_layout(height=350, margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig_box, use_container_width=True)
    
    # 5. Best Posting Day
    st.subheader("5. Best Posting Day")
    day_perf = get_best_posting_day(filtered_df)
    fig_day = px.bar(
        day_perf,
        x='Day of Week',
        y='Engagement Rate',
        title='Average Engagement Rate by Day of Week',
        color='Engagement Rate',
        color_continuous_scale='Viridis'
    )
    fig_day.update_layout(height=350, margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig_day, use_container_width=True)
    
    # 6. Best Posting Time
    st.subheader("6. Best Posting Time (IST)")
    hour_perf = get_best_posting_time(filtered_df)
    fig_hour = px.bar(
        hour_perf.head(10),
        x='Hour',
        y='Engagement Rate',
        title='Top 10 Best Posting Hours (IST)',
        color='Engagement Rate',
        color_continuous_scale='Plasma'
    )
    fig_hour.update_layout(
        xaxis_title="Hour (24-hour format, IST)",
        yaxis_title="Engagement Rate (%)",
        height=350,
        margin=dict(l=0, r=0, t=30, b=0)
    )
    st.plotly_chart(fig_hour, use_container_width=True)
    
    # 7. Followers Growth Trend
    st.subheader("7. Followers Growth Trend")
    followers_trend = get_followers_growth(filtered_df)
    fig_followers = px.line(
        followers_trend,
        x='Post Date',
        y='Cumulative Followers',
        title='Cumulative Followers Growth Over Time',
        markers=True
    )
    fig_followers.update_layout(
        xaxis_title="Date",
        yaxis_title="Cumulative Followers Gained",
        height=350,
        margin=dict(l=0, r=0, t=30, b=0)
    )
    st.plotly_chart(fig_followers, use_container_width=True)
    
    # 8. Reach vs Engagement Scatter Plot
    st.subheader("8. Reach vs Engagement Scatter Plot")
    filtered_df_copy = filtered_df.copy()
    filtered_df_copy['Total Engagement'] = calculate_total_engagement(filtered_df_copy)
    
    fig_scatter = px.scatter(
        filtered_df_copy,
        x='Reach',
        y='Total Engagement',
        color='Platform',
        size='Engagement Rate',
        hover_data=['Content Type', 'Post Date'],
        title='Reach vs Total Engagement by Platform',
        opacity=0.7
    )
    fig_scatter.update_layout(
        xaxis_title="Reach",
        yaxis_title="Total Engagement",
        height=450,
        margin=dict(l=0, r=0, t=30, b=0)
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# TOP POSTS PAGE
elif page == "🏆 Top Posts":
    st.header("🏆 Top Posts")
    st.markdown("Discover your best-performing content")
    
    # Top 10 Posts by Engagement Rate
    st.subheader("Top 10 Posts by Engagement Rate")
    top_engagement = get_top_posts(filtered_df, metric='Engagement Rate', n=10)
    top_engagement = safe_dataframe(top_engagement)
    st.dataframe(
        top_engagement,
        use_container_width=True,
        hide_index=True,
        height=300
    )
    
    # Highest Reach Posts
    st.subheader("Top 10 Posts by Reach")
    top_reach = get_top_posts(filtered_df, metric='Reach', n=10)
    top_reach = safe_dataframe(top_reach)
    st.dataframe(
        top_reach,
        use_container_width=True,
        hide_index=True,
        height=300
    )
    
    # Highest Engagement Posts
    st.subheader("Top 10 Posts by Total Engagement")
    filtered_df_copy = filtered_df.copy()
    filtered_df_copy['Total Engagement'] = calculate_total_engagement(filtered_df_copy)
    top_total_eng = get_top_posts(filtered_df_copy, metric='Total Engagement', n=10)
    top_total_eng = safe_dataframe(top_total_eng)
    st.dataframe(
        top_total_eng,
        use_container_width=True,
        hide_index=True,
        height=300
    )
    
    # Viral Content Analysis
    st.subheader("Viral Content Analysis (Reach > 50,000)")
    viral_posts = get_viral_content(filtered_df, threshold=50000)
    viral_posts = safe_dataframe(viral_posts)
    
    if len(viral_posts) > 0:
        st.dataframe(
            viral_posts,
            use_container_width=True,
            hide_index=True,
            height=300
        )
        
        # Viral content breakdown
        col1, col2 = st.columns(2, gap="medium")
        
        with col1:
            st.markdown("**Viral Content by Platform**")
            viral_platform = viral_posts['Platform'].value_counts()
            fig_viral_platform = px.pie(
                values=viral_platform.values,
                names=viral_platform.index,
                hole=0.4,
                title="Viral Posts Distribution by Platform"
            )
            fig_viral_platform.update_layout(height=300, margin=dict(l=0, r=0, t=30, b=0))
            st.plotly_chart(fig_viral_platform, use_container_width=True)
        
        with col2:
            st.markdown("**Viral Content by Type**")
            viral_content = viral_posts['Content Type'].value_counts()
            fig_viral_content = px.bar(
                x=viral_content.index,
                y=viral_content.values,
                color=viral_content.index,
                title="Viral Posts by Content Type"
            )
            fig_viral_content.update_layout(showlegend=False, height=300, margin=dict(l=0, r=0, t=30, b=0))
            st.plotly_chart(fig_viral_content, use_container_width=True)
    else:
        st.info("No viral content found with reach > 50,000 in the selected filters.")

# INSIGHTS PAGE
elif page == "💡 Insights":
    st.header("💡 Insights & Recommendations")
    st.markdown("AI-generated insights for your social media strategy")
    
    # Generate insights
    insights = generate_insights(filtered_df)
    
    # Display key insights with better spacing
    col1, col2, col3, col4 = st.columns(4, gap="small")
    
    with col1:
        st.metric(
            label="Best Platform",
            value=insights['Best Platform'],
            delta="Highest engagement"
        )
    
    with col2:
        st.metric(
            label="Best Content Type",
            value=insights['Best Content Type'],
            delta="Most engaging format"
        )
    
    with col3:
        st.metric(
            label="Best Day",
            value=insights['Best Posting Day'],
            delta="Optimal posting day"
        )
    
    with col4:
        st.metric(
            label="Best Hour (IST)",
            value=f"{insights['Best Posting Hour']}:00",
            delta="Peak engagement time"
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Main recommendation
    st.subheader("🎯 Primary Recommendation")
    st.success(insights['Recommendation'])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Platform-specific insights
    st.subheader("📱 Platform-Specific Insights")
    
    for platform, data in insights['Platform Insights'].items():
        with st.expander(f"{platform} Insights", expanded=False):
            col1, col2, col3, col4 = st.columns(4, gap="small")
            
            with col1:
                st.metric("Best Content", data['Best Content Type'])
            
            with col2:
                st.metric("Avg Engagement", f"{data['Average Engagement Rate']}%")
            
            with col3:
                st.metric("Total Reach", f"{data['Total Reach']:,}")
            
            with col4:
                st.metric("Followers Gained", f"{data['Total Followers Gained']:,}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Additional recommendations
    st.subheader("📋 Strategic Recommendations")
    
    recommendations = [
        {
            "category": "Content Strategy",
            "recommendation": f"Prioritize {insights['Best Content Type']} content on {insights['Best Platform']} for maximum engagement."
        },
        {
            "category": "Posting Schedule",
            "recommendation": f"Schedule posts for {insights['Best Posting Day']}s between {insights['Best Posting Hour']}:00 and {(insights['Best Posting Hour'] + 2) % 24}:00 IST."
        },
        {
            "category": "Audience Engagement",
            "recommendation": "Indian audience is most active during evening hours (6 PM - 10 PM IST). Plan your content accordingly."
        },
        {
            "category": "Platform Focus",
            "recommendation": f"{insights['Best Platform']} shows the highest engagement rate. Consider allocating more resources to this platform."
        },
        {
            "category": "Content Mix",
            "recommendation": "Maintain a diverse content mix with 40% Reels, 30% Images, 20% Videos, and 10% Carousels for optimal reach."
        },
        {
            "category": "Growth Strategy",
            "recommendation": "Focus on content that drives saves and shares to increase organic reach and follower growth."
        }
    ]
    
    for rec in recommendations:
        st.markdown(f"**{rec['category']}**")
        st.info(rec['recommendation'])
        st.markdown("<br>", unsafe_allow_html=True)
    
    # Performance summary
    st.subheader("📊 Performance Summary")
    
    summary_data = []
    for platform, data in insights['Platform Insights'].items():
        summary_data.append({
            'Platform': platform,
            'Best Content': data['Best Content Type'],
            'Avg Engagement Rate': f"{data['Average Engagement Rate']}%",
            'Total Reach': f"{data['Total Reach']:,}",
            'Followers Gained': f"{data['Total Followers Gained']:,}"
        })
    
    summary_df = pd.DataFrame(summary_data)
    summary_df = safe_dataframe(summary_df)
    st.dataframe(summary_df, use_container_width=True, hide_index=True)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #a0aec0; padding: 20px;'>
        <p style='margin: 5px 0;'>📊 Social Media Reach Analysis Dashboard</p>
        <p style='margin: 5px 0; font-size: 14px;'>Built for Indian Content Creators & Businesses</p>
        <p style='margin: 5px 0; font-size: 12px; color: #718096;'>Data reflects Indian audience patterns and IST timezone</p>
    </div>
    """,
    unsafe_allow_html=True
)
