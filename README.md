# 🔍 CrawlScope - Website Crawler Access Checker

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained-Yes-green)](https://github.com/dhruvpandyadp/crawlscope)

**CrawlScope** is a powerful, user-friendly web application that analyzes your website's `robots.txt` file to determine which crawlers (search engines, AI bots, SEO tools, and more) are allowed or blocked from accessing your site. With **300+ verified crawlers** across **15 comprehensive categories**, CrawlScope provides detailed insights to optimize SEO, control AI training data usage, and manage bot access effectively.

![Crawler Analysis](https://img.shields.io/badge/Crawler%20Analysis-300%2B%20Crawlers-brightgreen)
![Categories](https://img.shields.io/badge/Categories-15-blue)
![Download Reports](https://img.shields.io/badge/Download-CSV%20Reports-orange)

## ✨ Key Features

### 🚀 **Comprehensive Crawler Analysis**
- 📊 **300+ Crawlers Analyzed** - Covers search engines, AI crawlers, SEO tools, social media bots, and more
- 🗂 **15 Categories** - Organized into Search Engines, AI Crawlers, SEO & Analytics, Social Media, and 11 other categories
- 🔍 **Access Status** - Clear ✅ Allowed or ❌ Blocked indicators for each crawler
- ⏱ **Crawl Delay** - Displays crawl delay settings for each user agent
- 📈 **Category Insights** - Summary metrics for allowed/blocked crawlers by category

### 🖼️ **Intuitive Interface**
- 🌐 **Easy URL Input** - Simply enter a website URL to analyze its `robots.txt`
- 📍 **Quick Navigation** - Jump links to category analysis, complete results, and raw `robots.txt` content
- 📋 **Detailed Tables** - Organized results with category, platform, user agent, access status, and crawl delay
- 📄 **Raw robots.txt View** - Expandable section to inspect the original file
- 📥 **CSV Export** - Download detailed analysis reports for offline use

### 💡 **Actionable Insights**
- 🔒 **Privacy Analysis** - Evaluate AI crawler access for data protection
- 🔍 **SEO Optimization** - Identify search engine blocks that may impact visibility
- 📊 **Analytics Access** - Assess SEO tool access for comprehensive insights
- 📱 **Social Media Sharing** - Check social platform crawler permissions
- ⚙️ **robots.txt Quality** - Suggestions for sitemap inclusion and rule optimization

### 🛠️ **Professional Features**
- ⚡ **Fast Analysis** - Instant parsing of `robots.txt` with real-time results
- 🌐 **Cross-platform** - Works on Windows, Mac, Linux, and mobile devices
- 🎨 **Responsive Design** - Optimized for both desktop and mobile browsers
- 🖌 **Light/Dark Mode** - Seamless support for modern UI preferences
- 🔄 **Error Handling** - Graceful handling of missing or inaccessible `robots.txt` files

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dhruvpandyadp/crawlscope.git
   ```
   ```bash
   cd crawlscope
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** and go to `http://localhost:8501`

## 💻 Usage

1. **Enter Website URL** - Input a URL (e.g., `example.com` or `https://example.com`)
2. **Analyze** - Click "🔍 Analyze Access Status" to process the `robots.txt` file
3. **View Results**:
   - **Summary Metrics**: Total crawlers, allowed, blocked, and block rate
   - **Category Analysis**: Breakdown of access by category
   - **Detailed Table**: Complete list of crawlers with access status and crawl delay
   - **Insights**: Actionable recommendations for SEO and privacy
4. **Download Report** - Export results as a CSV file
5. **Inspect robots.txt** - View the raw `robots.txt` content

## 📊 Analysis Categories

CrawlScope covers **336+ crawlers** across **15 categories**:

1. **Search Engines** - Google, Bing, Baidu, Yandex, DuckDuckGo, and 40+ others
2. **AI Crawlers** - ChatGPT, Claude, Perplexity, Gemini, and other LLM bots
3. **SEO & Analytics** - Ahrefs, Semrush, Moz, Screaming Frog, and 30+ tools
4. **Social Media** - Facebook, Twitter, LinkedIn, Instagram, TikTok, and more
5. **E-commerce & Shopping** - Amazon, eBay, Shopify, and comparison bots
6. **Security & Monitoring** - Cloudflare, Sucuri, Wordfence, and threat scanners
7. **Site Monitoring & Analytics** - Pingdom, UptimeRobot, Lighthouse, and more
8. **Content Aggregators & News** - Apple News, Google News, Flipboard, etc.
9. **Email & Marketing** - MailChimp, HubSpot, Marketo, and marketing bots
10. **Academic & Research** - Google Scholar, ResearchGate, JSTOR, etc.
11. **Archive & Backup** - Wayback Machine, Internet Archive, and backup services
12. **Development & Testing** - Selenium, Puppeteer, and testing frameworks
13. **Feed Readers & Aggregators** - Feedly, RSS services, and content syndication
14. **Infrastructure & CDN** - Cloudflare services and CDN providers
15. **Miscellaneous & Validators** - W3C validators, CMS platforms, and generic bots

## 📊 Example Insights

### Sample robots.txt Analysis
For a website with a restrictive `robots.txt`:
- **High Security Mode**: 75% of crawlers blocked - excellent for privacy
- **AI Privacy Strong**: 20/25 AI crawlers blocked (80%) - protecting content from training
- **SEO Warning**: 40% of search engines blocked - may impact visibility
- **Missing Sitemap**: Add `Sitemap: https://yoursite.com/sitemap.xml` for better indexing

### Performance Metrics
| Category | Total Crawlers | Allowed | Blocked | Block Rate |
|----------|----------------|---------|---------|------------|
| Search Engines | 45 | 32 | 13 | 28.9% |
| AI Crawlers | 25 | 5 | 20 | 80.0% |
| SEO & Analytics | 30 | 20 | 10 | 33.3% |
| Social Media | 20 | 15 | 5 | 25.0% |

## 🎨 Interface Highlights

### Navigation
- **Quick Links**: Jump to category analysis, complete table, `robots.txt` content, or insights
- **Category Grid**: Responsive buttons for direct access to each category
- **Summary Metrics**: Total crawlers, allowed, blocked, and block rate at a glance

### Results Display
- **Category Breakdown**: Metrics for each category with allowed/blocked counts
- **Detailed Table**: Full list of crawlers with user agents and access details
- **Insights Section**: Actionable recommendations for optimization

### Visual Design
- **Modern Styling**: Gradient headers, shadow effects, and responsive layout
- **Light/Dark Mode**: Seamless support for user preferences
- **Expandable robots.txt**: View raw content without cluttering the UI

## 🛠️ Technical Details

### Built With
- **[Streamlit](https://streamlit.io/)** - Web app framework for interactive UI
- **[urllib.robotparser](https://docs.python.org/3/library/urllib.robotparser.html)** - Robust `robots.txt` parsing
- **[pandas](https://pandas.pydata.org/)** - Data processing and CSV export
- **[requests](https://requests.readthedocs.io/)** - HTTP requests for fetching `robots.txt`
- **Python 3.7+** - Core programming language

### Architecture
- **URL Normalization**: Ensures consistent URL handling
- **robots.txt Parsing**: Accurate interpretation of rules and crawl delays
- **Crawler Database**: 336+ verified user agents across 15 categories
- **Results Processing**: Efficient DataFrame-based analysis
- **Insight Generation**: Dynamic recommendations based on block rates

### Performance Optimizations
- **Fast Fetching**: Timeout handling for `robots.txt` requests
- **Error Resilience**: Graceful handling of missing or malformed files
- **Responsive UI**: Optimized for desktop and mobile
- **Efficient Data Processing**: pandas for fast aggregation and reporting

## 📱 Browser Support

| Browser | URL Input | Analysis | Results | Download |
|---------|-----------|----------|---------|----------|
| Chrome | ✅ Full | ✅ Full | ✅ Full | ✅ Full |
| Firefox | ✅ Full | ✅ Full | ✅ Full | ✅ Full |
| Safari | ✅ Full | ✅ Full | ✅ Full | ✅ Full |
| Edge | ✅ Full | ✅ Full | ✅ Full | ✅ Full |
| Mobile Chrome | ✅ Full | ✅ Full | ✅ Responsive | ✅ Full |
| Mobile Safari | ✅ Full | ✅ Full | ✅ Responsive | ✅ Full |

## 🎯 Use Cases

### **SEO Optimization**
```
Scenario: Website needs to improve search engine visibility
Action: Analyze robots.txt to ensure Google, Bing, etc., are allowed
Result: Identify and fix blocks impacting SEO
Benefit: Improved search rankings and visibility
```

### **AI Data Privacy**
```
Scenario: Protect content from AI training datasets
Action: Check AI crawler access (e.g., GPTBot, ClaudeBot)
Result: Confirm 80% of AI crawlers blocked
Benefit: Control over content usage in LLM training
```

### **Social Media Sharing**
```
Scenario: Ensure social platforms can access content
Action: Verify Facebook, Twitter, and LinkedIn crawler access
Result: Optimize robots.txt for social sharing
Benefit: Enhanced social media visibility
```

### **Site Monitoring**
```
Scenario: Allow monitoring tools for uptime tracking
Action: Check access for Pingdom, UptimeRobot, etc.
Result: Ensure monitoring tools are unblocked
Benefit: Reliable site performance tracking
```

## 🚀 Advanced Features

### Analysis Engine
- **Comprehensive Crawler Database**: 336+ verified user agents
- **Accurate Parsing**: Handles complex `robots.txt` rules
- **Crawl Delay Support**: Reports delays for each crawler
- **Category Aggregation**: Summarizes access by category

### Professional UI
- **Responsive Navigation**: Jump links and category grid
- **Interactive Tables**: Sortable, filterable results
- **Insightful Metrics**: Visual summaries for quick understanding
- **Exportable Reports**: CSV downloads for offline analysis

### Developer-Friendly
- **Open Source**: MIT license for commercial use
- **Modular Code**: Easy to extend with new crawlers
- **Well-Documented**: Clear code comments and structure
- **Production Ready**: Robust error handling and edge case management

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Created by Dhruv Pandya**

- GitHub: [@dhruvpandya](https://github.com/dhruvpandyadp)
- LinkedIn: [Dhruv Pandya](https://linkedin.com/in/dhruvpandyadp)

## 🙏 Acknowledgments

- Streamlit team for an excellent web app framework
- Python `urllib.robotparser` for robust `robots.txt` parsing
- pandas contributors for efficient data handling
- Open source community for feedback and inspiration

---

## 🚀 Ready to Analyze Your Website?

**Understand your crawler access in seconds!**

```bash
# Get started in under a minute
git clone https://github.com/dhruvpandyadp/crawlscope.git
cd crawlscope
pip install -r requirements.txt
streamlit run app.py
```

### What You'll Get:
- ⚡ **Instant Analysis** of 336+ crawlers
- 📊 **Detailed Reports** with category breakdowns
- 💡 **Actionable Insights** for SEO and privacy
- 📥 **CSV Exports** for offline analysis
- 🌐 **Responsive UI** for desktop and mobile
- 🔍 **Comprehensive Coverage** across 15 categories

**Optimize your website's crawler access today!**

---

⭐ **If this tool helps you manage your site, please give it a star!** ⭐

[![GitHub stars](https://img.shields.io/github/stars/dhruvpandyadp/crawlscope.svg?style=social&label=Star)](https://github.com/dhruvpandyadp/crawlscope)
