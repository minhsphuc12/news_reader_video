from playwright.sync_api import sync_playwright
from tqdm import tqdm

def fetch_article_content(url, browser):
    # with sync_playwright() as p:
        # browser = p.chromium.launch(headless=True)  # Use headless=False to see the browser
    page = browser.new_page()

    # Navigate to the article URL
    page.goto(url, wait_until='domcontentloaded')

    # Optional: Wait for the specific content to ensure it is loaded
    page.wait_for_selector('.sc-longform-header')

    # Scrape the full article content
    # Example: Fetching the full text from within <p> tags, modify as needed based on actual content structure
    article_content = page.query_selector_all('p')
    full_text = ' '.join([p.text_content() for p in article_content if p.text_content()])

    # Close the browser
    # browser.close()

    return full_text


# def scrape_articles(url):
url = 'https://thitruongtaichinhtiente.vn/'

with sync_playwright() as p:
    # Launch the browser in headless mode
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Go to the specified URL
    page.goto(url, wait_until='domcontentloaded')

    # Wait for the content to load (if necessary, adjust or add specific waits)
    page.wait_for_selector(".b-grid")

    # Extract data: headlines and contents
    articles = []
    article_containers = page.query_selector_all('.b-grid')
    # print(article_containers)
    for article in tqdm(article_containers):
        
        headline_element = article.query_selector('.b-grid__title > a')
        content_element = article.query_selector('.b-grid__desc > a')

        if headline_element and content_element:
            headline = headline_element.text_content()
            content = content_element.text_content()
            article_url = headline_element.get_attribute('href')
            full_content = fetch_article_content(article_url, browser)

            articles.append({
                'headline': headline,
                'content': content,
                'url': article_url,
                'full_content': full_content
            })

        else:
            print("Some elements were not found for an article, skipping.")


    # Close the browser
    browser.close()


    # return articles
len(articles)



# Display the results
for article in articles:
    print(f"Headline: {article['headline']}")
    print(f"Content: {article['content']}")
    print(f"URL: {article['url']}")
    print("-" * 80)