import streamlit as st
import urllib.robotparser
import requests
from urllib.parse import urljoin, urlparse
import pandas as pd
from io import StringIO

# Configure page
st.set_page_config(
    page_title="CrawlScope - The Ultimate Website Crawler Access Checker",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling with light/dark mode support
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 1rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    
    .metric-container {
        background: #ffffff;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
    }
    
    .jump-links {
        background: var(--background-color, #f8f9fa);
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1.5rem 0;
        border-left: 4px solid #667eea;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .jump-links h4 {
        color: var(--text-color, #333333);
        margin-bottom: 1rem;
        font-size: 1.2rem;
    }
    
    .nav-section {
        margin-bottom: 1rem;
    }
    
    .nav-section-title {
        color: var(--text-color, #555555);
        font-size: 0.9rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .jump-link {
        display: inline-block;
        margin: 0.25rem;
        padding: 0.5rem 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        text-decoration: none;
        border-radius: 6px;
        font-weight: 500;
        font-size: 0.9rem;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
    }
    
    .jump-link:hover {
        background: linear-gradient(135deg, #556cd6 0%, #653a90 100%);
        color: white !important;
        text-decoration: none;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
    }
    
    .jump-link.category-link {
        background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
        font-size: 0.85rem;
        padding: 0.4rem 0.8rem;
    }
    
    .jump-link.category-link:hover {
        background: linear-gradient(135deg, #218838 0%, #1e7e84 100%);
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(40, 167, 69, 0.3);
    }
    
    .section-anchor {
        padding-top: 80px;
        margin-top: -80px;
    }
    
    .categories-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 0.25rem;
        margin-top: 0.5rem;
    }
    
    /* Footer styling for light/dark mode */
    .footer-container {
        text-align: center;
        padding: 1rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 1rem;
    }

    .footer-container p {
        margin: 0px 0px 0rem;
    }

        
    /* Dark mode support */
    @media (prefers-color-scheme: dark) {
        .jump-links {
            background: #1e1e1e;
            border-left: 4px solid #667eea;
        }
        
        .jump-links h4 {
            color: #ffffff;
        }
        
        .nav-section-title {
            color: #cccccc;
        }
    
    }
    
    /* Streamlit dark theme support */
    .stApp[data-theme="dark"] .jump-links {
        background: #0e1117;
        border-left: 4px solid #667eea;
    }
    
    .stApp[data-theme="dark"] .jump-links h4 {
        color: #fafafa;
    }
    
    .stApp[data-theme="dark"] .nav-section-title {
        color: #cccccc;
    }
    
        
    @media (max-width: 768px) {
        .jump-link {
            font-size: 0.8rem;
            padding: 0.4rem 0.8rem;
            margin: 0.2rem;
        }
        
        .categories-grid {
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        }
    }
</style>
""", unsafe_allow_html=True)

# Title and description
st.markdown("""
<div class="main-header">
    <h1>🔍 CrawlScope</h1>
    <p><strong>The Ultimate Crawler Access Checker - See Who Can Crawl Your Site</strong></p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
Analyze which search engines, AI crawlers, social media platforms, SEO tools, and other bots can access your website based on your robots.txt file configuration.
""")

# Sidebar with instructions
with st.sidebar:
    st.header("📋 How to Use CrawlScope")
    st.markdown("""
    1. Enter a website URL
    2. Click "Analyze Access Status"
    3. View results for all crawler categories
    4. Download detailed report (optional)
    """)
    
    st.header("ℹ️ About CrawlScope")
    st.markdown("""
    CrawlScope analyzes robots.txt files to determine which crawlers are allowed or blocked from accessing your website.
    
    **Get instant insights across all 15 comprehensive categories:**
    
    - **Search Engines** - Google, Bing, Baidu, Yandex, DuckDuckGo, and 40+ regional engines
    - **AI Crawlers** - ChatGPT, Claude, Perplexity, Gemini, and other LLM training bots  
    - **SEO & Analytics** - Ahrefs, Semrush, Moz, Screaming Frog, and 30+ SEO tools
    - **Social Media** - Facebook, Twitter, LinkedIn, Instagram, TikTok, and messaging platforms
    - **E-commerce & Shopping** - Amazon, eBay, Shopify, and shopping comparison bots
    - **Security & Monitoring** - Security scanners, threat detection, monitoring tools
    - **Site Monitoring & Analytics** - Uptime checkers, performance monitoring
    - **Content Aggregators & News** - Apple News, Google News, Flipbook, content aggregators
    - **Email & Marketing** - MailChimp, HubSpot, Marketo, email marketing platforms
    - **Academic & Research** - Google Scholar, ResearchGate, academic platforms
    - **Archive & Backup** - Wayback Machine, Internet Archive, backup services
    - **Development & Testing** - Selenium, Puppeteer, testing frameworks
    - **Feed Readers & Aggregators** - Feedly, RSS services, content syndication
    - **Infrastructure & CDN** - Cloudflare services, CDN providers
    - **Miscellaneous & Validators** - W3C validators, CMS platforms, generic bots
    
    **Total: 300+ verified crawlers** across all categories.
    
    Understand exactly which crawler types can access your content and optimize your robots.txt for better SEO, AI training control, and comprehensive bot management.
    """)

# Complete CRAWLERS dictionary
CRAWLERS = {
    "Search Engines": {
        # Google Ecosystem
        "Google": "Googlebot",
        "Google News": "Googlebot-News",
        "Google Images": "Googlebot-Image",
        "Google Video": "Googlebot-Video",
        "Google Other": "GoogleOther",
        "Google Shopping": "Storebot-Google",
        "Google Ads": "AdsBot-Google",
        "Google Ads Mobile": "AdsBot-Google-Mobile",
        "Google AdSense": "Mediapartners-Google",
        "Google Extended": "Google-Extended",
        "Google APIs": "APIs-Google",
        "Google API": "Google API",
        "Google Read Aloud": "Google-Read-Aloud",
        "Google Favicon": "Google Favicon",
        "Google Rich Snippets": "Google-AMPHTML",
        "Google Assistant": "Google-Assistant",
        "Google PageSpeed": "Google Page Speed",
        "Google Digital Asset Links": "Google Digital Asset Links",
        "Google Publisher Center": "Google Publisher Center",
        "Google Schema Markup Testing Tool": "Google Schema Markup Testing Tool",
        "Google AdWords Express": "Google-AdWords-Express",
        "Google AdWords Instant": "Google-Adwords-Instant",
        "Google Page Renderer": "Google-PageRenderer",
        # Microsoft / Bing
        "Bing": "BingBot",
        "Bing Preview": "BingPreview",
        "Bing Ads": "adidxbot",
        "MSN Bot": "msnbot",
        # Major Global Engines
        "Baidu": "Baiduspider",
        "Baidu Images": "Baiduspider-image",
        "Baidu News": "Baiduspider-news",
        "Yandex": "YandexBot",
        "Yandex Images": "YandexImages",
        "Yandex News": "YandexNews",
        "DuckDuckGo": "DuckDuckBot",
        "DuckDuckGo Assist": "DuckAssistBot",
        "Brave": "BraveBot",
        "Yahoo": "Slurp",
        "Yahoo Japan": "Y!J-ASC",
        # Privacy-Focused & Alternative
        "Ecosia": "ecosia",
        "Startpage": "Startpage",
        "Mojeek": "MojeekBot",
        "Qwant": "Qwantify",
        # Regional Search Engines
        "Naver (South Korea)": "Yeti",
        "Seznam (Czech Republic)": "SeznamBot",
        "360 Search (China)": "360Spider",
        "Sogou (China)": "Sogou spider",
        "CocCoc (Vietnam)": "coccocbot",
        "PetalBot (Huawei)": "PetalBot",
        # Apple Search
        "Apple Search": "Applebot",
        # Additional Search/Analysis
        "Alpha Bot": "AlphaBot",
        "Friendly Crawler": "FriendlyCrawler",
        "Seekr": "Seekr",
        "ZumBot": "ZumBot",
    },
    
    "AI Crawlers": {
        # OpenAI / ChatGPT
        "GPTBot (Training)": "GPTBot",
        "OAI-SearchBot (Search)": "OAI-SearchBot",
        "ChatGPT-User (Browsing)": "ChatGPT-User",
        "ChatGPT-User 2.0": "ChatGPT-User/2.0",
        # Anthropic / Claude
        "ClaudeBot": "ClaudeBot",
        "Claude Web": "Claude-Web",
        "Claude User": "Claude-User",
        "Claude SearchBot": "Claude-SearchBot",
        "Anthropic AI": "anthropic-ai",
        # Perplexity AI
        "PerplexityBot": "PerplexityBot",
        "Perplexity-User": "Perplexity-User",
        # Common Crawl
        "Common Crawl": "CCBot",
        # Big Tech AI
        "Google AI": "Google-Extended",
        "Google Agent Mariner": "GoogleAgent-Mariner",
        "Google Cloud Vertex": "CloudVertexBot",
        "Meta AI": "Meta-ExternalAgent",
        "Meta Facebook": "facebookexternalhit",
        "Apple AI": "Applebot-Extended",
        "Amazon AI": "Amazonbot",
        "Amazon Nova Act": "Nova Act",
        "ByteDance AI (TikTok)": "Bytespider",
        # AI-Powered Search Engines
        "You.com": "YouBot",
        "Kagi Search": "KagiBot",
        "AddSearch": "AddSearchBot",
        # Additional AI Companies
        "Cohere AI": "cohere-ai",
        "Cohere Training": "cohere-training-data-crawler",
        "Mistral AI User": "MistralAI-User",
        "DeepSeek": "DeepseekBot",
        "Grok AI": "GrokBot",
        "Hugging Face": "HuggingFaceBot",
        "Hugging Face Crawler": "huggingface",
        "Huawei PanGu": "PanguBot",
        "OpenAssistant": "OpenAssistantBot",
        # AI Content/Image Scrapers
        "Image Dataset": "img2dataset",
        "Magpie Crawler": "magpie-crawler",
        "News Please": "news-please",
        # AI Assistants
        "BigSur AI": "bigsur.ai",
        "Devin AI": "Devin",
        "Gemini Deep Research": "Gemini-Deep-Research",
        "Liner Bot": "LinerBot",
        "Qualified Bot": "QualifiedBot",
        # Research & Academic AI
        "Allen Institute for Artificial Intelligence (Ai2)": "AI2Bot",
        "Japan Research": "ICC-Crawler",
        "Diffbot": "Diffbot",
        "Omgili": "omgili",
        "Omgili Bot": "omgilibot",
        "Webz.io Extended": "Webzio-Extended",
        # Emerging AI Search
        "Timpi": "TimpiBot",
    },
    
    "SEO & Analytics": {
        # Major SEO Tools
        "Ahrefs": "AhrefsBot",
        "Ahrefs Site Audit": "Ahrefs Site Audit",
        "Semrush": "SemrushBot",
        "Semrush Site Audit": "SemrushBot-SA",
        "Majestic": "MJ12bot",
        "Moz": "rogerbot",
        "Moz Links": "dotbot",
        "Screaming Frog": "Screaming Frog SEO Spider",
        # Additional verified SEO bots
        "SerpStat": "serpstatbot",
        "LinkResearchTools": "LRTBot",
        "SEMScoop": "SEMScoopBot",
        "DeepCrawl": "DeepCrawlBot",
        "OnCrawl": "OnCrawlBot",
        "Botify": "BotifyBot",
        "Ryte": "RyteBot",
        "Sistrix": "SistrixBot",
        "SearchMetrics": "SearchMetricsBot",
        "BrightEdge": "BrightEdgeBot",
        "seoClarity": "seoClarityBot",
        # SEO Tools from Cloudflare
        "DataForSEO": "DataForSEO",
        "Siteimprove Crawl": "Siteimprove Crawl",
        "prerender": "prerender",
        "Barkrowler": "Barkrowler",
        # Marketing/Analytics Bots
        "ADmantX": "ADmantX",
        "Awario RSS": "AwarioRssBot",
        "Awario Smart": "AwarioSmartBot",
        "BLEX Bot": "BLEXBot",
        "Clarity Bot": "claritybot",
        "ImagesiftBot": "ImagesiftBot",
        "Meltwater": "Meltwater",
        "Pipl Bot": "PiplBot",
        "Senti Bot": "SentiBot",
        # Analytics Services from Cloudflare
        "FullStory": "FullStory",
        "Proximic": "Proximic",
        "Taboola": "Taboola",
        "klaviyo": "klaviyo",
    },
    
    "Social Media": {
        # Meta Platforms
        "Facebook": "facebookexternalhit",
        "Facebook Bot": "FacebookBot",
        "Instagram": "facebookexternalhit",
        "WhatsApp": "WhatsApp",
        # X (Twitter)
        "Twitter / X": "Twitterbot",
        # Professional Networks
        "LinkedIn": "LinkedInBot",
        # Other Major Social Platforms
        "Pinterest": "Pinterestbot",
        "TikTok": "Bytespider",
        "Reddit": "RedditBot",
        "YouTube": "YouTubeBot",
        "Snapchat": "SnapchatBot",
        "Skype": "SkypeUriPreview",
        "Bluesky": "Bluesky",
        # Messaging Apps
        "Telegram": "TelegramBot",
        "Slack": "Slackbot",
        "Slack Image Proxy": "Slack-ImgProxy",
        "Slack Link Expanding": "Slackbot-LinkExpanding",
        "Slack Image Proxy CF": "Slack Image Proxy",
        "Discord": "Discordbot",
        "WeChat": "WeChatBot",
        "Line": "LineBot",
        # Email/Social Extensions
        "YahooMailProxy": "YahooMailProxy",
        # Professional Networks
        "Xing": "XingBot",
        # Content Platforms
        "Medium": "MediumBot",
        "Substack": "SubstackBot",
        "Tumblr": "TumblrBot"
    },
    
    "Content Aggregators & News": {
        # News & Media Platforms
        "Apple News": "AppleNewsBot",
        "Flipboard": "FlipboardProxy",
        "SmartNews": "SmartNewsBot",
        "NewsBreak": "NewsBreakBot",
        "Yahoo News": "YahooNewsBot",
        "BBC": "BBCBot",
        "Reuters": "ReutersBot",
        "Associated Press": "APBot",
        # Content Aggregators
        "Buzz Bot": "Buzzbot",
        "NewsNow": "NewsNow",
        "Panscient": "panscient.com",
        "Scoop.it": "scoop.it",
    },
    
    "E-commerce & Shopping": {
        # Major E-commerce
        "Amazon": "Amazonbot",
        "eBay": "eBayBot",
        "Shopify": "ShopifyBot",
        "Shopify Captain Hook": "Shopify-Captain-Hook",
        "WooCommerce": "WooCommerceBot",
        "Magento": "MagentoBot",
        "Etsy": "EtsyBot",
        "Alibaba": "AlibabaBot",
        "AliExpress": "AliExpressBot",
        "Rakuten": "RakutenBot",
        "Zalando": "ZalandoBot",
        "PriceGrabber": "PriceGrabberBot",
        "Shopping.com": "ShoppingBot",
        "Kelkoo": "KelkooBot",
        "Nextag": "NextagBot",
        # Payment Processors
        "Stripe": "Stripe",
        "PayPal": "PayPal",
        "Adyen": "Adyen",
        "ChargeBee": "ChargeBee",
    },
    
    "Email & Marketing": {
        # Major Email/Marketing Platforms
        "MailChimp": "MailChimpBot",
        "Constant Contact": "ConstantContactBot",
        "SendGrid": "SendGridBot",
        "Campaign Monitor": "CampaignMonitorBot",
        "HubSpot": "HubSpotBot",
        "HubSpot Crawler": "HubSpot Crawler",
        "Marketo": "MarketoBot",
        "Pardot": "PardotBot",
        "ActiveCampaign": "ActiveCampaignBot",
        "ConvertKit": "ConvertKitBot",
        "AWeber": "AWeberBot"
    },
    
    "Security & Monitoring": {
        # Security & Monitoring Tools
        "Cloudflare": "CloudflareBot",
        "Sucuri": "SucuriBot",
        "Wordfence": "WordfenceBot",
        "SiteLock": "SiteLockBot",
        "Qualys": "QualysBot",
        "Nessus": "NessusBot",
        "OpenVAS": "OpenVASBot",
        "Shodan": "ShodanBot",
        "Censys": "CensysBot",
        "ZoomEye": "ZoomEyeBot",
        "BinaryEdge": "BinaryEdgeBot",
        # Security Services
        "Detectify": "Detectify",
        "OneTrust CMP Scanner": "Onetrust CMP Scanner",
        "Let's Encrypt": "Let's Encrypt",
        "ProjectShield URL Check": "ProjectShield Url Check",
        "Google Trust Services": "Google Trust Services (DCV Check)",
    },
    
    "Site Monitoring & Analytics": {
        # Site Monitoring Tools
        "Pingdom": "PingdomBot",
        "UptimeRobot": "UptimeRobotBot",
        "Site24x7": "Site24x7Bot",
        "StatusCake": "StatusCakeBot",
        "GTmetrix": "GTmetrixBot",
        "WebPageTest": "WebPageTestBot",
        "Lighthouse": "LighthouseBot",
        "Chrome Lighthouse": "Chrome-Lighthouse",
        "PageSpeed Insights": "PageSpeedBot",
        "Dareboost": "DareboostBot",
        "Google Site Verification": "Google-Site-Verification",
        "Google Association Service": "GoogleAssociationService",
        "Datadog Synthetics": "Datadog Synthetics",
        "Ghost Inspector": "Ghost Inspector",
        "Hotjar": "Hotjar",
        "New Relic": "NewRelicbot",
        "Uptime.com": "Uptime.com",
        "Catchpoint": "Catchpoint",
        # Major Monitoring Services
        "Better Uptime": "Better Uptime",
        "Grafana Synthetic Monitoring": "Grafana's Synthetic Monitoring",
        "Splunk Synthetics": "Splunk Synthetics",
        "Uptime LLC": "Uptime LLC",
        "Sentry Uptime Monitoring": "Sentry Uptime Monitoring",
        "LogicMonitor": "logicmonitor",
        "NodePing": "Nodeping",
        "Sentry": "Sentry",
    },
    
    "Academic & Research": {
        # Academic/Research Platforms
        "ResearchGate": "ResearchGateBot",
        "Academia.edu": "AcademiaBot",
        "JSTOR": "JSTORBot",
        "PubMed": "PubMedBot",
        "arXiv": "arXivBot",
        "Semantic Scholar": "SemanticScholarBot",
        "CORE": "COREBot",
        "CrossRef": "CrossRefBot",
        "ORCID": "ORCIDBot",
        "Turnitin Bot": "TurnitinBot",
    },
    
    "Archive & Backup": {
        # Archive & Backup Tools
        "Wayback Machine": "ia_archiver",
        "Internet Archive Bot": "archive.org_bot",
        "Internet Archive Extended": "ia_archiver-web.archive.org",
        "Wikipedia Bot": "IABot",
        "Archive.today": "archiveis_bot",
        "Portuguese Archive": "Arquivo-web-crawler",
        "French National Library": "bnf.fr_bot",
        "Turnitin Crawler": "Turnitin",
        "Heritrix": "heritrix",
        "HTTrack": "httrack",
        "Wget": "Wget",
        "cURL": "curl",
        "Nutch": "nutch"
    },
    
    "Development & Testing": {
        # Development Tools
        "Postman": "PostmanRuntime",
        "Insomnia": "insomnia",
        "Selenium": "selenium",
        "Puppeteer": "HeadlessChrome",
        "Playwright": "Playwright",
        "PhantomJS": "PhantomJS",
        "SlimerJS": "SlimerJS",
        "Cypress": "Cypress",
        "WebDriver": "webdriver",
        "Scrapy": "Scrapy",
        "cron-job.org": "cron-job.org",
        "Zapier": "Zapier",
        "Retool": "Retool",
        "VaultPress": "VaultPress",
        "Make Platform": "Make Platform",
    },
    
    "Feed Readers & Aggregators": {
        # Feed Readers
        "Feedly": "FeedlyBot",
        "Feedbin": "Feedbin",
        "Inoreader": "InoreaderBot",
        "NewsBlur": "NewsBlurBot",
        "The Old Reader": "OldReaderBot",
        "Flipboard": "FlipboardBot",
        "Pocket": "PocketBot",
        "Overcast": "Overcast",
        "Instapaper": "InstapaperBot",
        "ReadWise": "ReadWiseBot",
        "IFTTT": "IFTTT",
        "Google Image Proxy": "GoogleImageProxy",
        "Microsoft Preview": "MicrosoftPreview",
        # Content/Feed Services from Cloudflare
        "HubSpot Feed Fetcher": "HubSpot Feed Fetcher",
        "HubSpot Page Fetcher": "HubSpot Page Fetcher",
        "Google Feed Fetcher": "Google Feed Fetcher",
        "RSS API": "RSS API",
        "Pocket Casts Feed Parser": "Pocket Casts Feed Parser",
        "Blogtrottr": "Blogtrottr",
    },
    
    "Infrastructure & CDN": {
        # Cloudflare's own services and CDN bots
        "Cloudflare Prefetch": "Cloudflare Prefetch",
        "Cloudflare Traffic Manager": "Cloudflare-Traffic-Manager",
        "Cloudflare Healthchecks": "Cloudflare Healthchecks",
        "Cloudflare Stream Webhook": "Cloudflare Stream Webhook",
        "Cloudflare Custom Hostname Verification": "Cloudflare Custom Hostname Verification",
        "Cloudflare SSLDetector": "Cloudflare SSLDetector",
    },
    
    "Miscellaneous & Validators": {
        # W3C Validators
        "W3C Link Checker": "W3C_Validator",
        "W3C CSS Validator": "Jigsaw",
        "W3C Markup Validator": "W3C_Validator",
        # CMS & Platform Bots
        "WordPress": "WordPress",
        "Drupal": "DrupalBot",
        "Joomla": "JoomlaBot",
        "Typepad": "TypePadBot",
        # Other Bots
        "Robozilla": "Robozilla",
        "AASA-Bot": "AASA-Bot",
        "PSBot": "psbot",
        "SiteAuditBot": "SiteAuditBot",
        "FeedBurner": "FeedBurner",
        "Hatena Antenna": "Hatena Antenna",
        "InfoNaviRobot": "InfoNaviRobot",
        "Harvest": "Harvest",
        # Generic Patterns
        "Generic Bot": "bot",
        "Spider": "spider",
        "Crawler": "crawler"
    }
}

def normalize_url(url):
    """Normalize URL by adding protocol if missing"""
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    return url

def get_robots_txt_content(url):
    """Fetch robots.txt content from URL"""
    try:
        parsed_url = urlparse(url)
        robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
        response = requests.get(robots_url, timeout=10)
        if response.status_code == 200:
            return robots_url, response.text
        else:
            return robots_url, None
    except Exception as e:
        return None, str(e)

def parse_robots_txt(robots_content, base_url):
    """Parse robots.txt content and return RobotFileParser"""
    try:
        parser = urllib.robotparser.RobotFileParser()
        parser.set_url(urljoin(base_url, '/robots.txt'))
        # Parse the content directly
        lines = robots_content.split('\n')
        parser.parse(lines)
        return parser
    except Exception as e:
        st.error(f"Error parsing robots.txt: {str(e)}")
        return None

def check_crawler_access(parser, base_url, crawlers_dict):
    """Check access status for all crawlers"""
    results = []
    for category, crawlers in crawlers_dict.items():
        for name, user_agent in crawlers.items():
            try:
                can_access = parser.can_fetch(user_agent, base_url)
                crawl_delay = parser.crawl_delay(user_agent)
                results.append({
                    'Category': category,
                    'Platform': name,
                    'User Agent': user_agent,
                    'Access Status': '✅ Allowed' if can_access else '❌ Blocked',
                    'Crawl Delay': f"{crawl_delay}s" if crawl_delay else "None",
                    'Can Access': can_access
                })
            except Exception as e:
                results.append({
                    'Category': category,
                    'Platform': name,
                    'User Agent': user_agent,
                    'Access Status': f'⚠️ Error: {str(e)}',
                    'Crawl Delay': "N/A",
                    'Can Access': False
                })
    return results

def generate_insights(df, robots_content):
    """Generate accurate insights based on the analysis results"""
    insights = []
    
    if df.empty:
        return ["No data available for analysis"]
    
    total_crawlers = len(df)
    allowed_crawlers = (df['Can Access'] == True).sum()
    blocked_crawlers = total_crawlers - allowed_crawlers
    block_rate = (blocked_crawlers / total_crawlers) * 100
    
    # Overall access insights
    if block_rate > 70:
        insights.append(f"🔒 **High Security Mode**: {block_rate:.1f}% of crawlers are blocked - excellent for privacy protection")
    elif block_rate > 40:
        insights.append(f"⚖️ **Balanced Access**: {block_rate:.1f}% of crawlers are blocked - moderate protection")
    elif block_rate > 10:
        insights.append(f"🌐 **Open Policy**: {block_rate:.1f}% of crawlers are blocked - prioritizing visibility")
    else:
        insights.append(f"🚪 **Fully Open**: Only {block_rate:.1f}% of crawlers are blocked - maximum accessibility")
    
    # Category-specific insights
    category_stats = df.groupby('Category')['Can Access'].agg(['count', 'sum']).reset_index()
    category_stats['block_rate'] = ((category_stats['count'] - category_stats['sum']) / category_stats['count'] * 100).round(1)
    
    # AI Crawlers analysis
    ai_stats = category_stats[category_stats['Category'] == 'AI Crawlers']
    if not ai_stats.empty:
        ai_block_rate = ai_stats.iloc[0]['block_rate']
        ai_total = ai_stats.iloc[0]['count']
        ai_blocked = ai_stats.iloc[0]['count'] - ai_stats.iloc[0]['sum']
        
        if ai_block_rate > 80:
            insights.append(f"🤖 **AI Privacy Strong**: {ai_blocked}/{ai_total} AI crawlers blocked ({ai_block_rate:.1f}%) - protecting content from training")
        elif ai_block_rate > 50:
            insights.append(f"🤖 **AI Privacy Moderate**: {ai_blocked}/{ai_total} AI crawlers blocked ({ai_block_rate:.1f}%) - balanced AI access")
        else:
            insights.append(f"🤖 **AI Training Allowed**: Only {ai_blocked}/{ai_total} AI crawlers blocked ({ai_block_rate:.1f}%) - content available for training")
    
    # Search Engines analysis
    search_stats = category_stats[category_stats['Category'] == 'Search Engines']
    if not search_stats.empty:
        search_block_rate = search_stats.iloc[0]['block_rate']
        search_blocked = search_stats.iloc[0]['count'] - search_stats.iloc[0]['sum']
        
        if search_block_rate > 30:
            insights.append(f"⚠️ **SEO Warning**: {search_block_rate:.1f}% of search engines blocked - may impact search visibility")
        elif search_block_rate > 10:
            insights.append(f"🔍 **SEO Caution**: {search_block_rate:.1f}% of search engines blocked - monitor search impact")
        else:
            insights.append(f"✅ **SEO Friendly**: Only {search_block_rate:.1f}% of search engines blocked - excellent for visibility")
    
    # SEO & Analytics analysis
    seo_stats = category_stats[category_stats['Category'] == 'SEO & Analytics']
    if not seo_stats.empty:
        seo_block_rate = seo_stats.iloc[0]['block_rate']
        
        if seo_block_rate > 60:
            insights.append(f"📊 **Limited Analytics**: {seo_block_rate:.1f}% of SEO tools blocked - reduced insights available")
        elif seo_block_rate > 30:
            insights.append(f"📈 **Moderate Analytics**: {seo_block_rate:.1f}% of SEO tools blocked - some insights limited")
        else:
            insights.append(f"📊 **Full Analytics**: Only {seo_block_rate:.1f}% of SEO tools blocked - comprehensive insights available")
    
    # Social Media analysis
    social_stats = category_stats[category_stats['Category'] == 'Social Media']
    if not social_stats.empty:
        social_block_rate = social_stats.iloc[0]['block_rate']
        
        if social_block_rate > 50:
            insights.append(f"📱 **Social Privacy**: {social_block_rate:.1f}% of social platforms blocked - limited social sharing")
        else:
            insights.append(f"📱 **Social Friendly**: Only {social_block_rate:.1f}% of social platforms blocked - good for sharing")
    
    # FIXED: Robots.txt quality insights - more accurate logic
    if robots_content:
        lines = [line.strip() for line in robots_content.split('\n') if line.strip()]
        
        # Check for sitemap - only show if actually missing
        has_sitemap = any(line.lower().startswith('sitemap:') for line in lines)
        if not has_sitemap:
            insights.append("💡 **Missing Sitemap**: Add 'Sitemap: https://yoursite.com/sitemap.xml' to help crawlers find your content")
        
        # Check for meaningful wildcard usage - only show if actually using wildcards effectively
        has_meaningful_wildcards = False
        for line in lines:
            if line.lower().startswith('disallow:') and '*' in line:
                has_meaningful_wildcards = True
                break
            elif line.lower().startswith('user-agent:') and '*' in line:
                has_meaningful_wildcards = True
                break
        
        if has_meaningful_wildcards:
            insights.append("🎯 **Using Wildcards**: Good use of universal rules for efficient crawler management")
        
        # Check for very basic robots.txt
        meaningful_lines = [line for line in lines if line.lower().startswith(('user-agent:', 'disallow:', 'allow:', 'crawl-delay:', 'sitemap:'))]
        if len(meaningful_lines) < 3:
            insights.append("⚠️ **Simple robots.txt**: Consider adding more specific rules for better crawler control")
    else:
        insights.append("💡 **No robots.txt**: Creating a robots.txt file gives you control over crawler access")
    
    return insights

def create_category_anchor(category_name):
    """Create URL-safe anchor from category name"""
    return category_name.lower().replace(' ', '-').replace('&', 'and')

# Main interface
st.subheader("🌐 Website URL")
url_input = st.text_input(
    "Enter Website URL:",
    placeholder="example.com or https://example.com",
    help="Enter the website URL you want to analyze with CrawlScope",
    label_visibility="collapsed"
)

# Analyze button (removed category selection - analyzes all categories by default)
if st.button("🔍 Analyze Access Status", type="primary"):
    if url_input:
        with st.spinner("CrawlScope is analyzing robots.txt file..."):
            # Normalize URL
            normalized_url = normalize_url(url_input.strip())
            
            # Get robots.txt content
            robots_url, robots_content = get_robots_txt_content(normalized_url)
            
            if robots_content:
                st.success(f"✅ Successfully fetched robots.txt from: {robots_url}")
                
                # Parse robots.txt
                parser = parse_robots_txt(robots_content, normalized_url)
                
                if parser:
                    # Check crawler access for ALL categories
                    results = check_crawler_access(parser, normalized_url, CRAWLERS)
                    
                    # Create DataFrame
                    df = pd.DataFrame(results)
                    
                    # Display summary metrics
                    st.subheader("📊 CrawlScope Analysis Results")
                    
                    col1, col2, col3, col4 = st.columns(4)
                    total_crawlers = len(results)
                    allowed_crawlers = (df['Can Access'] == True).sum()
                    blocked_crawlers = total_crawlers - allowed_crawlers
                    
                    with col1:
                        st.metric("Total Crawlers", total_crawlers)
                    with col2:
                        st.metric("✅ Allowed", allowed_crawlers)
                    with col3:
                        st.metric("❌ Blocked", blocked_crawlers)
                    with col4:
                        st.metric("Block Rate", f"{(blocked_crawlers/total_crawlers)*100:.1f}%")
                    
                    # FIXED: Quick Navigation using Streamlit columns instead of HTML
                    st.markdown("---")
                    st.subheader("📍 Quick Navigation")
                    st.markdown("**Main Sections**")
                    
                    # Main section buttons
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.markdown('[📈 Category Analysis](#category-analysis)', unsafe_allow_html=True)
                    with col2:
                        st.markdown('[📋 Complete Analysis](#complete-analysis)', unsafe_allow_html=True)
                    with col3:
                        st.markdown('[📄 robots.txt Content](#robots-content)', unsafe_allow_html=True)
                    with col4:
                        st.markdown('[💡 Key Insights](#key-insights)', unsafe_allow_html=True)
                    
                    st.markdown("**Individual Categories**")
                    
                    # Category buttons in grid
                    categories = list(CRAWLERS.keys())
                    rows = [categories[i:i+3] for i in range(0, len(categories), 3)]
                    
                    for row in rows:
                        cols = st.columns(len(row))
                        for i, category in enumerate(row):
                            with cols[i]:
                                anchor = create_category_anchor(category)
                                st.markdown(f'[{category}](#{anchor})', unsafe_allow_html=True)
                    
                    st.markdown("---")
                    
                    # ANCHOR: Category Analysis
                    st.markdown('<div id="category-analysis" class="section-anchor"></div>', unsafe_allow_html=True)
                    st.subheader("📈 Category Analysis")
                    category_analysis = df.groupby('Category').agg({
                        'Can Access': ['count', 'sum']
                    }).round(2)
                    
                    category_analysis.columns = ['Total', 'Allowed']
                    category_analysis['Blocked'] = category_analysis['Total'] - category_analysis['Allowed']
                    category_analysis['Block Rate %'] = ((category_analysis['Blocked'] / category_analysis['Total']) * 100).round(1)
                    
                    st.dataframe(category_analysis, use_container_width=True)
                    
                    # Display results by category with ANCHORS
                    for category in CRAWLERS.keys():
                        if category in df['Category'].values:
                            # ANCHOR: Individual category sections
                            st.markdown(f'<div id="{create_category_anchor(category)}" class="section-anchor"></div>', unsafe_allow_html=True)
                            st.subheader(f"📋 {category}")
                            category_df = df[df['Category'] == category]
                            
                            # Show category summary
                            cat_total = len(category_df)
                            cat_allowed = (category_df['Can Access'] == True).sum()
                            cat_blocked = cat_total - cat_allowed
                            
                            col1, col2, col3 = st.columns(3)
                            with col1:
                                st.metric("Total", cat_total)
                            with col2:
                                st.metric("Allowed", cat_allowed, delta=f"{(cat_allowed/cat_total)*100:.1f}%")
                            with col3:
                                st.metric("Blocked", cat_blocked, delta=f"{(cat_blocked/cat_total)*100:.1f}%")
                            
                            # Create columns for better layout
                            for idx, row in category_df.iterrows():
                                col1, col2, col3 = st.columns([3, 2, 1])
                                with col1:
                                    st.write(f"**{row['Platform']}**")
                                with col2:
                                    st.write(row['Access Status'])
                                with col3:
                                    st.write(row['Crawl Delay'])
                    
                    # ANCHOR: Complete Analysis Table
                    st.markdown('<div id="complete-analysis" class="section-anchor"></div>', unsafe_allow_html=True)
                    st.subheader("📋 Complete Analysis Table")
                    display_df = df[['Category', 'Platform', 'User Agent', 'Access Status', 'Crawl Delay']]
                    st.dataframe(display_df, use_container_width=True)
                    
                    # ANCHOR: View robots.txt Content
                    st.markdown('<div id="robots-content" class="section-anchor"></div>', unsafe_allow_html=True)
                    with st.expander("📄 View robots.txt Content"):
                        st.text(robots_content)
                    
                    # Download option
                    csv = df.to_csv(index=False)
                    st.download_button(
                        label="📥 Download CrawlScope Results as CSV",
                        data=csv,
                        file_name=f"crawlscope_analysis_{urlparse(normalized_url).netloc}.csv",
                        mime="text/csv"
                    )
                    
                    # ANCHOR: Key Insights
                    st.markdown('<div id="key-insights" class="section-anchor"></div>', unsafe_allow_html=True)
                    st.subheader("💡 Key Insights")
                    insights = generate_insights(df, robots_content)
                    
                    for insight in insights:
                        st.info(insight)
                        
            else:
                st.error("❌ Could not fetch robots.txt file. The website might not have one or it's inaccessible.")
                st.info("💡 This means all crawlers are typically allowed by default.")
    else:
        st.warning("⚠️ Please enter a website URL")

# ENHANCED Footer with light/dark mode support
st.markdown("---")
st.markdown(
    f"""
    <div class="footer-container">
        <p>Built with ❤️ by <strong>Dhruv Pandya</strong> | Analyze Crawler Accessibility For Any Website</p>
        </div>
    """, 
    unsafe_allow_html=True
)
