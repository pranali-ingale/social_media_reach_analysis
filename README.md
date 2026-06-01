# Social Media Reach Analysis Dashboard

A comprehensive, interactive Streamlit dashboard for analyzing social media performance across multiple platforms with Indian audience insights. This project provides actionable marketing intelligence for content creators and businesses targeting the Indian digital market.

---
*Intern Name:* Pranali Ingale  
*Intern ID:* CITS2281
*Domain:* Data Analytics  
*Organization:* CODTECH IT Solutions

## Project Overview

The Social Media Reach Analysis Dashboard is a data analytics project designed to help content creators, digital marketers, and businesses understand their social media performance. The dashboard analyzes metrics across Instagram, Facebook, LinkedIn, and Twitter/X, providing insights specifically tailored to Indian audience patterns and engagement behaviors.

Key Highlights:
- Analyzes 2,500+ social media posts
- Indian Standard Time (IST) timezone optimization
- Platform-specific performance metrics
- Content type effectiveness analysis
- Automated marketing recommendations
- Interactive visualizations with filters

---

## Problem Statement

In today's digital landscape, content creators and businesses struggle with:
- Understanding which platforms perform best for their content
- Identifying optimal posting times for maximum engagement
- Determining which content types resonate with their audience
- Tracking follower growth and engagement trends
- Making data-driven decisions for social media strategy

This dashboard addresses these challenges by providing comprehensive analytics and AI-generated insights specifically for the Indian market.

---

## Dashboard Features

### Overview Page
- KPI Cards: Total Reach, Total Engagement, Total Impressions, Total Followers Gained, Best Performing Platform
- Platform Distribution: Visual breakdown of posts by platform
- Content Type Distribution: Analysis of content formats used
- Engagement Rate Comparison: Platform-wise engagement metrics

### Analytics Page
Interactive Filters:
- Platform Filter (Instagram, Facebook, LinkedIn, Twitter/X)
- Content Type Filter (Image, Video, Reel, Carousel, Story)
- Date Range Filter

8 Comprehensive Visualizations:
1. Reach Trend Analysis: Track reach over time
2. Platform Performance Comparison: Compare metrics across platforms
3. Content Type Performance: Analyze effectiveness by content format
4. Engagement Rate Analysis: Distribution and comparison
5. Best Posting Day: Identify optimal days for posting
6. Best Posting Time: Discover peak engagement hours (IST)
7. Followers Growth Trend: Track cumulative follower growth
8. Reach vs Engagement Scatter Plot: Correlation analysis

### Top Posts Page
- Top 10 Posts by Engagement Rate: Highest performing content
- Top 10 Posts by Reach: Widest reach content
- Top 10 Posts by Total Engagement: Most engaging content
- Viral Content Analysis: Posts with reach > 50,000
- Viral Content Breakdown: Platform and content type distribution

### Insights Page
Automated Insights:
- Best Platform for engagement
- Best Content Type
- Best Posting Day
- Best Posting Time (IST)

Marketing Recommendations:
- AI-generated strategic recommendations
- Platform-specific insights
- Content strategy guidance
- Posting schedule optimization
- Growth strategy suggestions

---

## Dataset Description

### Dataset Specifications
- Total Records: 2,500 posts
- Time Period: January 2024 - December 2024
- Platforms: Instagram, Facebook, LinkedIn, Twitter/X
- Timezone: Indian Standard Time (IST)

### Columns
| Column | Description | Data Type |
|--------|-------------|-----------|
| Post ID | Unique identifier for each post | String |
| Platform | Social media platform | Categorical |
| Post Date | Date of posting | Date |
| Posting Time | Time of posting (24-hour format, IST) | Time |
| Content Type | Type of content (Image, Video, Reel, Carousel, Story) | Categorical |
| Reach | Number of unique users reached | Integer |
| Impressions | Total number of views | Integer |
| Likes | Number of likes received | Integer |
| Comments | Number of comments received | Integer |
| Shares | Number of shares | Integer |
| Saves | Number of saves/bookmarks | Integer |
| Followers Gained | New followers from the post | Integer |
| Engagement Rate | Calculated engagement percentage | Float |

### Dataset Characteristics
- Platform Distribution: Instagram (35.6%), Facebook (29.1%), LinkedIn (21.4%), Twitter/X (13.9%)
- Content Type Distribution: Image (26.9%), Video (23.2%), Carousel (21.9%), Reel (19.6%), Story (8.4%)
- Average Reach: 28,714 per post
- Average Engagement Rate: 5.32%
- Peak Hours: 6 PM - 10 PM IST (reflecting Indian audience patterns)

---

## Screenshots Section

### Overview Page
- KPI cards showing key metrics at a glance
- Platform distribution pie chart
- Content type bar chart
- Engagement rate comparison

### Analytics Page
- Interactive filters sidebar
- 8 comprehensive visualizations
- Time-series analysis
- Platform and content comparisons

### Top Posts Page
- Ranked tables of top-performing content
- Viral content analysis
- Visual breakdowns of viral posts

### Insights Page
- Key metrics summary
- AI-generated recommendations
- Platform-specific insights
- Strategic guidance
---

## Key Insights

### Platform Performance
- Instagram shows the highest engagement rate for Reels and Stories
- Facebook performs well with Carousel and Video content
- LinkedIn excels with professional Image and Carousel posts
- Twitter/X shows strong engagement with Video and Image content

### Content Type Effectiveness
- Reels generate 1.5x more reach than other content types
- Videos show 1.3x higher engagement than static images
- Carousels perform well for educational content
- Stories have higher engagement but shorter lifespan

### Posting Patterns (IST)
- Peak Hours: 6 PM - 10 PM IST (40% of posts scheduled during peak)
- Best Days: Tuesday, Wednesday, Thursday show highest engagement
- Weekend Performance: Slightly lower engagement but higher reach
- Morning Posts: 9 AM - 11 AM shows moderate engagement

### Audience Behavior
- Indian audience is most active during evening hours
- Engagement peaks during dinner time (7 PM - 9 PM IST)
- Weekend content has higher share rates
- Professional content (LinkedIn) performs better on weekdays

---

## Marketing Recommendations

### Content Strategy
1. Prioritize Reels on Instagram: Focus on short-form video content for maximum reach
2. Diversify Content Mix: Maintain 40% Reels, 30% Images, 20% Videos, 10% Carousels
3. Platform-Specific Content: Tailor content format to each platform's strengths
4. Story Strategy: Use Stories for behind-the-scenes and real-time engagement

### Posting Schedule
1. Prime Time (6 PM - 10 PM IST): Schedule high-priority content during peak hours
2. Consistent Posting: Maintain regular posting schedule for algorithm favorability
3. Day-Specific Strategy: 
   - Tuesday-Thursday: Professional and educational content
   - Friday-Sunday: Entertainment and lifestyle content
4. Time Zone Optimization: All times in IST for Indian audience

### Platform Focus
1. Primary Platform: Allocate 40% of resources to the best-performing platform
2. Cross-Platform Strategy: Repurpose content across platforms with platform-specific tweaks
3. Platform Testing: A/B test content formats on each platform
4. Audience Segmentation: Tailor content to platform-specific audience demographics

### Growth Strategy
1. Engagement-Driven Content: Focus on content that drives saves and shares
2. Community Building: Respond to comments and foster community engagement
3. Collaborations: Partner with other creators for cross-promotion
4. Trend Utilization: Leverage trending topics and hashtags

### Performance Optimization
1. Monitor Metrics: Track engagement rate, reach, and follower growth weekly
2. Iterate Strategy: Adjust content strategy based on performance data
3. Quality Over Quantity: Focus on high-quality content over frequent posting
4. Analytics Review: Regularly review dashboard insights for optimization opportunities

---

## Tech Stack

- Python: Core programming language
- Streamlit: Interactive dashboard framework
- Pandas: Data manipulation and analysis
- NumPy: Numerical computing
- Matplotlib: Static visualizations
- Seaborn: Statistical visualizations
- Plotly: Interactive charts and graphs

---

## Project Structure

```
social_media_reach_analysis/
│
├── data/
│   └── social_media_data.csv          # Dataset with 2,500 records
│
├── outputs/
│   └── screenshots/                   # Dashboard screenshots
│
├── src/
│   ├── analysis.py                     # Data processing functions
│   └── generate_data.py                # Dataset generation script
│
├── app.py                              # Main Streamlit dashboard
├── requirements.txt                    # Python dependencies
├── .gitignore                          # Git ignore rules
└── README.md                           # Project documentation
```

---

## How To Run

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. Clone the repository
   ```bash
   git clone <repository-url>
   cd social_media_reach_analysis
   ```

2. Create a virtual environment (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On Mac/Linux
   source venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run the dashboard
   ```bash
   streamlit run app.py
   ```

5. Access the dashboard
   - The dashboard will open in your default web browser
   - Typically available at: http://localhost:8501

### Regenerating Dataset (Optional)
If you want to generate a new dataset with different parameters:

```bash
cd src
python generate_data.py
```

This will create a new social_media_data.csv file in the data/ directory.

---

## Usage Guide

### Navigation
- Use the sidebar to navigate between pages
- Apply filters to analyze specific subsets of data
- Interactive charts can be zoomed and hovered for details

### Filters
- Platform Filter: Select one or more platforms to analyze
- Content Type Filter: Filter by content format
- Date Range Filter: Analyze specific time periods

### Exporting Data
- Use the download button in the sidebar to export filtered data
- Download as CSV format
- File includes timestamp for version control

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

---

## Author
Pranali Ingale
BE in CSE[AIML] / 2nd year
---