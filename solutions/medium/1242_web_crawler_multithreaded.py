"""
Given a URL startUrl and an interface HtmlParser, implement a Multi-threaded web crawler to crawl all links that are under the same hostname as startUrl.

Return all URLs obtained by your web crawler in any order.

Your crawler should:

Start from the page: startUrl
Call HtmlParser.getUrls(url) to get all URLs from a webpage of a given URL.
Do not crawl the same link twice.
Explore only the links that are under the same hostname as startUrl.
"""


# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
from typing import List
from collections import deque
from concurrent import futures

class HtmlParser:
    """
    Mock HtmlParser class for testing purposes.
    """
    def __init__(self, url_map: dict):
        """
        Initialize with a mapping of URLs to their linked URLs.
        
        Args:
            url_map (dict): Dictionary mapping URLs to lists of linked URLs
        """
        self.url_map = url_map
    
    def getUrls(self, url: str) -> List[str]:
        """
        Mock implementation of getUrls.
        
        Args:
            url (str): URL to get links from
            
        Returns:
            List[str]: List of URLs linked from the given URL
        """
        return self.url_map.get(url, [])

class Solution:
    def crawl(self, startUrl: str, htmlParser: HtmlParser) -> List[str]:
        """
        Multi-threaded web crawler to find all URLs under the same hostname.
        
        Args:
            startUrl (str): URL to start crawling from
            htmlParser (HtmlParser): Parser to get URLs from a webpage
            
        Returns:
            List[str]: All URLs obtained by the crawler
            
        Approach:
        - Use ThreadPoolExecutor for parallel processing
        - Use a set to keep track of visited URLs
        - Use a queue to manage tasks
        - Use a lambda function to extract hostname
        - Process URLs in parallel while maintaining thread safety
        
        Time Complexity: O(n) where n is the number of URLs under the same hostname
        Space Complexity: O(n) to store visited URLs and the task queue
        """
        hostname = lambda url: url.split('/')[2]
        seen = {startUrl}
    
        with futures.ThreadPoolExecutor(max_workers=16) as executor:
            tasks = deque([executor.submit(htmlParser.getUrls, startUrl)])
            while tasks:
                for url in tasks.popleft().result():
                    if url not in seen and hostname(startUrl) == hostname(url):
                        seen.add(url)
                        tasks.append(executor.submit(htmlParser.getUrls, url))
        
        return list(seen)


def test_solution():
    """Test cases for the Solution class."""
    solution = Solution()
    
    # Test case 1: Simple case with one level of links
    url_map1 = {
        "http://news.yahoo.com": [
            "http://news.yahoo.com/news",
            "http://news.yahoo.com/news/topics/",
            "http://news.google.com"  # Different domain
        ]
    }
    parser1 = HtmlParser(url_map1)
    result1 = solution.crawl("http://news.yahoo.com", parser1)
    expected1 = ["http://news.yahoo.com", "http://news.yahoo.com/news", "http://news.yahoo.com/news/topics/"]
    assert sorted(result1) == sorted(expected1)
    
    # Test case 2: Multiple levels of links
    url_map2 = {
        "http://news.yahoo.com": ["http://news.yahoo.com/news"],
        "http://news.yahoo.com/news": ["http://news.yahoo.com/news/topics/"],
        "http://news.yahoo.com/news/topics/": ["http://news.yahoo.com/news/topics/politics/"]
    }
    parser2 = HtmlParser(url_map2)
    result2 = solution.crawl("http://news.yahoo.com", parser2)
    expected2 = [
        "http://news.yahoo.com",
        "http://news.yahoo.com/news",
        "http://news.yahoo.com/news/topics/",
        "http://news.yahoo.com/news/topics/politics/"
    ]
    assert sorted(result2) == sorted(expected2)
    
    # Test case 3: Circular links
    url_map3 = {
        "http://news.yahoo.com": ["http://news.yahoo.com/news"],
        "http://news.yahoo.com/news": ["http://news.yahoo.com"]
    }
    parser3 = HtmlParser(url_map3)
    result3 = solution.crawl("http://news.yahoo.com", parser3)
    expected3 = ["http://news.yahoo.com", "http://news.yahoo.com/news"]
    assert sorted(result3) == sorted(expected3)
    
    # Test case 4: No links
    url_map4 = {
        "http://news.yahoo.com": []
    }
    parser4 = HtmlParser(url_map4)
    result4 = solution.crawl("http://news.yahoo.com", parser4)
    assert result4 == ["http://news.yahoo.com"]
    
    # Test case 5: Multiple links to same URL
    url_map5 = {
        "http://news.yahoo.com": ["http://news.yahoo.com/news", "http://news.yahoo.com/news"],
        "http://news.yahoo.com/news": ["http://news.yahoo.com"]
    }
    parser5 = HtmlParser(url_map5)
    result5 = solution.crawl("http://news.yahoo.com", parser5)
    expected5 = ["http://news.yahoo.com", "http://news.yahoo.com/news"]
    assert sorted(result5) == sorted(expected5)
    
    # Test case 6: Large number of links (testing thread pool)
    url_map6 = {
        "http://news.yahoo.com": [f"http://news.yahoo.com/page{i}" for i in range(20)]
    }
    for i in range(20):
        url_map6[f"http://news.yahoo.com/page{i}"] = []
    parser6 = HtmlParser(url_map6)
    result6 = solution.crawl("http://news.yahoo.com", parser6)
    assert len(result6) == 21  # startUrl + 20 pages
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()