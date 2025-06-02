def fetch_seo_data(keyword):
    seo_data = {
        "wireless-earbuds": {
            "search_volume": 2400,
            "keyword_difficulty": 37,
            "avg_cpc": 1.25
        },
        "protein-powder": {
            "search_volume": 8100,
            "keyword_difficulty": 65,
            "avg_cpc": 2.80
        },
        "best-laptops": {
            "search_volume": 5400,
            "keyword_difficulty": 72,
            "avg_cpc": 3.10
        },
        "budget-travel-tips": {
            "search_volume": 1600,
            "keyword_difficulty": 28,
            "avg_cpc": 0.95
        },
        "freelance-web-developer": {
            "search_volume": 2900,
            "keyword_difficulty": 49,
            "avg_cpc": 1.60
        }
    }

    slug = keyword.strip().lower()
    return seo_data.get(slug)