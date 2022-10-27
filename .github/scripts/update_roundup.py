from datetime import datetime
from feedparser import FeedParserDict, parse
from markdownify import markdownify as md

FEED_URL = "https://www.obsidianroundup.org/blog/rss/"
ROUNDUP_FOLDER_PATH = "../../01 - Community/Obsidian Roundup"

def date_conversion(parsed_feed_datetime: FeedParserDict) -> datetime:
    """Converts published_parsed attribute of a feed item into a pythonic datetime object"""
    return datetime(year=parsed_feed_datetime.tm_year, month=parsed_feed_datetime.tm_mon, day=parsed_feed_datetime.tm_mday, hour=parsed_feed_datetime.tm_hour, minute=parsed_feed_datetime.tm_min, second=parsed_feed_datetime.tm_sec)

def datetime_from_parsed_feed_datetime(entry: FeedParserDict) -> str:
    """Returns ISO formatted string for feed published timestamp"""
    pythonic_datetime = date_conversion(entry.published_parsed)
    return pythonic_datetime.isoformat()

def date_from_parsed_feed_datetime(entry: FeedParserDict) -> str:
    """Returns ISO formatted string for feed published date"""
    pythonic_datetime = date_conversion(entry.published_parsed)
    return pythonic_datetime.strftime("%Y-%m-%d")

def does_previous_exist_in_hub():
    pass

def is_roundup_post(entry: FeedParserDict) -> bool:
    if entry.title.startswith('🌠'):
        return True
    else:
        return False

def convert_feed_html(html_content: str) -> str:
    return md(html_content)

def get_normalized_file_name(entry: FeedParserDict) -> str:
    return f"{date_from_parsed_feed_datetime(entry)} {entry.title[2:]}.md"

def generate_file_with_hub_yaml(entry: FeedParserDict) -> str:
    frontmatter: str = f"---\nlink: {entry.link}\nauthor: {entry.author}\npublished: {datetime_from_parsed_feed_datetime(entry)}\npublish: true\n---\n\n"
    return frontmatter+f"# {get_normalized_file_name(entry)}\n{entry.summary}\n\n"+convert_feed_html(entry.content[0].value)

def save_file(entry: FeedParserDict):
    file_contents: str = generate_file_with_hub_yaml(entry)
    file_name = f"{ROUNDUP_FOLDER_PATH}/{get_normalized_file_name(entry)}"
    with open(file_name, 'w', encoding='utf8') as roundup_file:
        roundup_file.write(file_contents)

def main():
    parsed_feed = parse(FEED_URL)
    for entry in parsed_feed.entries:
        if is_roundup_post(entry):
            # print(get_normalized_file_name(entry))
            save_file(entry)

if __name__ == "__main__":
    main()