# Given a url startUrl and an interface HtmlParser, implement a web crawler to crawl all links that are under the same hostname as startUrl. 

#Return all urls obtained by your web crawler in any order.

# Your crawler should:

# Start from the page: startUrl
# Call HtmlParser.getUrls(url) to get all urls from a webpage of given url.
# Do not crawl the same link twice.
# Explore only the links that are under the same hostname as startUrl.


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
import collections

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
        Crawl all URLs under the same hostname as startUrl.
        
        Args:
            startUrl (str): URL to start crawling from
            htmlParser (HtmlParser): Parser to get URLs from a webpage
            
        Returns:
            List[str]: All URLs obtained by the crawler
            
        Approach:
        - Use BFS to crawl the web
        - Use a set to keep track of visited URLs
        - Use a queue to implement BFS
        - Use a domain to check if the URL is under the same hostname
        
        Time Complexity: O(n) where n is the number of URLs under the same hostname
        Space Complexity: O(n) to store visited URLs and the queue
        """
        visited = {startUrl}
        domain = startUrl.split("http://")[1].split("/")[0]
        ans = [startUrl]
        queue = collections.deque([startUrl])

        while queue:
            for _ in range(len(queue)):
                url = queue.popleft()
                check = htmlParser.getUrls(url)

                for new_url in check:
                    if new_url in visited:
                        continue
                    if new_url.split("http://")[1].split("/")[0] != domain:
                        continue
                    ans.append(new_url)
                    visited.add(new_url)
                    queue.append(new_url)

        return ans


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
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()