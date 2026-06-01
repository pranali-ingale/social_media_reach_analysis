"""
Social Media Reach Analysis - Data Processing Module
This module contains functions to process and analyze social media data.
"""

import pandas as pd
import numpy as np
from datetime import datetime


def load_data(filepath):
    """
    Load social media data from CSV file.
    
    Args:
        filepath (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Loaded data
    """
    df = pd.read_csv(filepath)
    df['Post Date'] = pd.to_datetime(df['Post Date'])
    return df


def calculate_kpis(df):
    """
    Calculate Key Performance Indicators.
    
    Args:
        df (pd.DataFrame): Social media data
        
    Returns:
        dict: Dictionary containing KPIs
    """
    total_reach = df['Reach'].sum()
    total_engagement = df['Likes'].sum() + df['Comments'].sum() + df['Shares'].sum() + df['Saves'].sum()
    total_impressions = df['Impressions'].sum()
    total_followers_gained = df['Followers Gained'].sum()
    
    # Find best performing platform
    platform_performance = df.groupby('Platform')['Engagement Rate'].mean()
    best_platform = platform_performance.idxmax()
    
    return {
        'Total Reach': total_reach,
        'Total Engagement': total_engagement,
        'Total Impressions': total_impressions,
        'Total Followers Gained': total_followers_gained,
        'Best Performing Platform': best_platform
    }


def filter_data(df, platforms=None, content_types=None, date_range=None):
    """
    Filter data based on selected criteria.
    
    Args:
        df (pd.DataFrame): Original data
        platforms (list): List of platforms to include
        content_types (list): List of content types to include
        date_range (tuple): Tuple of (start_date, end_date)
        
    Returns:
        pd.DataFrame: Filtered data
    """
    filtered_df = df.copy()
    
    if platforms:
        filtered_df = filtered_df[filtered_df['Platform'].isin(platforms)]
    
    if content_types:
        filtered_df = filtered_df[filtered_df['Content Type'].isin(content_types)]
    
    if date_range:
        start_date, end_date = date_range
        filtered_df = filtered_df[
            (filtered_df['Post Date'] >= pd.to_datetime(start_date)) &
            (filtered_df['Post Date'] <= pd.to_datetime(end_date))
        ]
    
    return filtered_df


def get_reach_trend(df):
    """
    Calculate reach trend over time.
    
    Args:
        df (pd.DataFrame): Filtered data
        
    Returns:
        pd.DataFrame: Data with date and reach
    """
    reach_trend = df.groupby('Post Date')['Reach'].sum().reset_index()
    reach_trend = reach_trend.sort_values('Post Date')
    return reach_trend


def get_platform_performance(df):
    """
    Calculate performance metrics by platform.
    
    Args:
        df (pd.DataFrame): Filtered data
        
    Returns:
        pd.DataFrame: Platform performance metrics
    """
    platform_perf = df.groupby('Platform').agg({
        'Reach': 'sum',
        'Engagement Rate': 'mean',
        'Likes': 'sum',
        'Comments': 'sum',
        'Shares': 'sum',
        'Followers Gained': 'sum'
    }).reset_index()
    return platform_perf


def get_content_type_performance(df):
    """
    Calculate performance metrics by content type.
    
    Args:
        df (pd.DataFrame): Filtered data
        
    Returns:
        pd.DataFrame: Content type performance metrics
    """
    content_perf = df.groupby('Content Type').agg({
        'Reach': 'sum',
        'Engagement Rate': 'mean',
        'Likes': 'sum',
        'Shares': 'sum'
    }).reset_index()
    return content_perf


def get_best_posting_day(df):
    """
    Find the best day for posting based on engagement rate.
    
    Args:
        df (pd.DataFrame): Filtered data
        
    Returns:
        pd.DataFrame: Day-wise engagement data
    """
    df['Day of Week'] = df['Post Date'].dt.day_name()
    day_performance = df.groupby('Day of Week')['Engagement Rate'].mean().reset_index()
    
    # Order by day of week
    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_performance['Day of Week'] = pd.Categorical(
        day_performance['Day of Week'], 
        categories=days_order, 
        ordered=True
    )
    day_performance = day_performance.sort_values('Day of Week')
    
    return day_performance


def get_best_posting_time(df):
    """
    Find the best time for posting based on engagement rate.
    
    Args:
        df (pd.DataFrame): Filtered data
        
    Returns:
        pd.DataFrame: Hour-wise engagement data
    """
    df['Hour'] = df['Posting Time'].str.split(':').str[0].astype(int)
    hour_performance = df.groupby('Hour')['Engagement Rate'].mean().reset_index()
    hour_performance = hour_performance.sort_values('Engagement Rate', ascending=False)
    return hour_performance


def get_followers_growth(df):
    """
    Calculate followers growth trend over time.
    
    Args:
        df (pd.DataFrame): Filtered data
        
    Returns:
        pd.DataFrame: Date-wise followers growth
    """
    followers_trend = df.groupby('Post Date')['Followers Gained'].sum().reset_index()
    followers_trend = followers_trend.sort_values('Post Date')
    followers_trend['Cumulative Followers'] = followers_trend['Followers Gained'].cumsum()
    return followers_trend


def get_top_posts(df, metric='Reach', n=10):
    """
    Get top posts based on specified metric.
    
    Args:
        df (pd.DataFrame): Filtered data
        metric (str): Metric to sort by (Reach, Engagement Rate, Likes, etc.)
        n (int): Number of top posts to return
        
    Returns:
        pd.DataFrame: Top posts
    """
    top_posts = df.nlargest(n, metric)
    
    # Define columns to return, avoiding duplicates
    columns_to_return = ['Post ID', 'Platform', 'Post Date', 'Posting Time', 'Content Type']
    if metric != 'Engagement Rate':
        columns_to_return.append(metric)
    columns_to_return.append('Engagement Rate')
    
    result = top_posts[columns_to_return].copy()
    
    # Remove any duplicate columns that might exist
    result = result.loc[:, ~result.columns.duplicated()]
    
    return result


def get_viral_content(df, threshold=50000):
    """
    Identify viral content (posts with reach above threshold).
    
    Args:
        df (pd.DataFrame): Filtered data
        threshold (int): Reach threshold for viral content
        
    Returns:
        pd.DataFrame: Viral posts
    """
    viral_posts = df[df['Reach'] > threshold].sort_values('Reach', ascending=False)
    return viral_posts[['Post ID', 'Platform', 'Content Type', 'Reach', 
                        'Engagement Rate', 'Likes', 'Shares']]


def generate_insights(df):
    """
    Generate automated insights and recommendations.
    
    Args:
        df (pd.DataFrame): Filtered data
        
    Returns:
        dict: Dictionary containing insights and recommendations
    """
    # Best Platform
    platform_perf = df.groupby('Platform')['Engagement Rate'].mean()
    best_platform = platform_perf.idxmax()
    
    # Best Content Type
    content_perf = df.groupby('Content Type')['Engagement Rate'].mean()
    best_content = content_perf.idxmax()
    
    # Best Posting Day
    df['Day of Week'] = df['Post Date'].dt.day_name()
    day_perf = df.groupby('Day of Week')['Engagement Rate'].mean()
    best_day = day_perf.idxmax()
    
    # Best Posting Time
    df['Hour'] = df['Posting Time'].str.split(':').str[0].astype(int)
    hour_perf = df.groupby('Hour')['Engagement Rate'].mean()
    best_hour = hour_perf.idxmax()
    
    # Generate recommendation
    recommendation = (
        f"Focus on {best_platform} {best_content} posts on {best_day}s "
        f"between {best_hour}:00 and {(best_hour + 2) % 24}:00 IST "
        f"to maximize engagement."
    )
    
    # Platform-specific insights
    platform_insights = {}
    for platform in df['Platform'].unique():
        platform_data = df[df['Platform'] == platform]
        best_content_for_platform = platform_data.groupby('Content Type')['Engagement Rate'].mean().idxmax()
        avg_engagement = platform_data['Engagement Rate'].mean()
        
        platform_insights[platform] = {
            'Best Content Type': best_content_for_platform,
            'Average Engagement Rate': round(avg_engagement, 2),
            'Total Reach': platform_data['Reach'].sum(),
            'Total Followers Gained': platform_data['Followers Gained'].sum()
        }
    
    return {
        'Best Platform': best_platform,
        'Best Content Type': best_content,
        'Best Posting Day': best_day,
        'Best Posting Hour': best_hour,
        'Recommendation': recommendation,
        'Platform Insights': platform_insights
    }


def get_engagement_rate_distribution(df):
    """
    Get engagement rate distribution by platform.
    
    Args:
        df (pd.DataFrame): Filtered data
        
    Returns:
        pd.DataFrame: Engagement rate distribution
    """
    engagement_dist = df.groupby('Platform')['Engagement Rate'].describe()
    return engagement_dist


def calculate_total_engagement(df):
    """
    Calculate total engagement (likes + comments + shares + saves).
    
    Args:
        df (pd.DataFrame): Filtered data
        
    Returns:
        pd.Series: Total engagement per post
    """
    return df['Likes'] + df['Comments'] + df['Shares'] + df['Saves']
