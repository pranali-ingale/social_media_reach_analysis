"""
Generate realistic social media dataset for Indian audience analysis.
This script creates a dataset with 2500 records reflecting Indian social media patterns.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Configuration
NUM_RECORDS = 2500
START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2024, 12, 31)

# Platforms and their characteristics
PLATFORMS = ['Instagram', 'Facebook', 'LinkedIn', 'Twitter/X']
PLATFORM_WEIGHTS = [0.35, 0.30, 0.20, 0.15]  # Instagram most popular in India

# Content types
CONTENT_TYPES = ['Image', 'Video', 'Reel', 'Carousel', 'Story']

# Indian peak hours (IST)
PEAK_HOURS = [18, 19, 20, 21, 22]  # 6 PM to 10 PM IST
OFF_PEAK_HOURS = list(range(0, 24))

def generate_post_id(index):
    """Generate unique post ID"""
    return f"POST{str(index).zfill(5)}"

def generate_platform():
    """Select platform based on Indian market share"""
    return np.random.choice(PLATFORMS, p=PLATFORM_WEIGHTS)

def generate_date():
    """Generate random date within range"""
    days_between = (END_DATE - START_DATE).days
    random_days = random.randint(0, days_between)
    return START_DATE + timedelta(days=random_days)

def generate_time():
    """Generate posting time with Indian peak hours bias"""
    # 40% chance of posting during peak hours
    if random.random() < 0.4:
        hour = random.choice(PEAK_HOURS)
    else:
        hour = random.choice(OFF_PEAK_HOURS)
    minute = random.randint(0, 59)
    return f"{hour:02d}:{minute:02d}"

def generate_content_type(platform):
    """Generate content type based on platform"""
    if platform == 'Instagram':
        weights = [0.15, 0.20, 0.40, 0.15, 0.10]  # Reels popular on Instagram
    elif platform == 'Facebook':
        weights = [0.30, 0.25, 0.10, 0.25, 0.10]
    elif platform == 'LinkedIn':
        weights = [0.40, 0.20, 0.05, 0.30, 0.05]
    else:  # Twitter/X
        weights = [0.35, 0.30, 0.10, 0.20, 0.05]
    
    return np.random.choice(CONTENT_TYPES, p=weights)

def generate_metrics(platform, content_type, posting_hour):
    """Generate realistic metrics based on platform and content type"""
    # Base reach values for Indian audience (in thousands)
    if platform == 'Instagram':
        base_reach = np.random.randint(5000, 50000)
    elif platform == 'Facebook':
        base_reach = np.random.randint(3000, 40000)
    elif platform == 'LinkedIn':
        base_reach = np.random.randint(2000, 25000)
    else:  # Twitter/X
        base_reach = np.random.randint(1000, 20000)
    
    # Adjust for content type
    if content_type == 'Reel':
        base_reach = int(base_reach * 1.5)
    elif content_type == 'Video':
        base_reach = int(base_reach * 1.3)
    elif content_type == 'Story':
        base_reach = int(base_reach * 0.8)
    
    # Adjust for posting time (peak hours get more reach)
    if posting_hour in PEAK_HOURS:
        base_reach = int(base_reach * 1.4)
    
    # Generate other metrics
    impressions = int(base_reach * np.random.uniform(1.2, 2.5))
    likes = int(base_reach * np.random.uniform(0.02, 0.08))
    comments = int(likes * np.random.uniform(0.01, 0.05))
    shares = int(likes * np.random.uniform(0.005, 0.02))
    saves = int(likes * np.random.uniform(0.01, 0.03))
    followers_gained = int(likes * np.random.uniform(0.001, 0.01))
    
    # Calculate engagement rate
    total_engagement = likes + comments + shares + saves
    engagement_rate = (total_engagement / base_reach * 100) if base_reach > 0 else 0
    
    return {
        'Reach': base_reach,
        'Impressions': impressions,
        'Likes': likes,
        'Comments': comments,
        'Shares': shares,
        'Saves': saves,
        'Followers Gained': followers_gained,
        'Engagement Rate': round(engagement_rate, 2)
    }

# Generate dataset
data = []

for i in range(1, NUM_RECORDS + 1):
    platform = generate_platform()
    post_date = generate_date()
    posting_time = generate_time()
    posting_hour = int(posting_time.split(':')[0])
    content_type = generate_content_type(platform)
    
    metrics = generate_metrics(platform, content_type, posting_hour)
    
    row = {
        'Post ID': generate_post_id(i),
        'Platform': platform,
        'Post Date': post_date.strftime('%Y-%m-%d'),
        'Posting Time': posting_time,
        'Content Type': content_type,
        **metrics
    }
    
    data.append(row)

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
output_path = 'c:/Social_media_reach_analysis/social_media_reach_analysis/data/social_media_data.csv'
df.to_csv(output_path, index=False)

print(f"Dataset generated successfully with {len(df)} records!")
print(f"Saved to: {output_path}")
print("\nDataset Summary:")
print(df.describe())
print("\nPlatform Distribution:")
print(df['Platform'].value_counts())
print("\nContent Type Distribution:")
print(df['Content Type'].value_counts())
