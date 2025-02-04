import argparse
import os
import sys

from notion.smoke_test import run_live_block_callback_test, run_live_collection_callback_test

# Following code is a sample. Input the code onto the terminal, with your own notion page URL and token_v2
# python3 run_smoke_test.py --page https://www.notion.so/fitcuration/Myam-Myam-Love-a0d22196f58f4efb8a38bcf9b3e06459 --token e26b797ce5beaf4170f2699fdab0b6be375175fa6ca66c9d1a06ca08bc70d578ae2203f408bbbc38554c20357876387a9942152d868ac7c98240be964fd88496257bf0fbe8372de88db5a41c106a

if __name__ == "__main__":
    description = "Run notion-py client smoke tests"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "--page", dest="page", help="page URL or ID", type=str
    )
    parser.add_argument(
        "--collection", dest="collection_page", help="collection URL or ID", type=str
    )
    parser.add_argument("--token", dest="token", help="token_v2", type=str)
    args = parser.parse_args()

    token = args.token
    if not token:
        # if you don't want your terminal to be filled with messy token, then input your token_v2 at "NOTION_TOKEN"
        token = os.environ.get("NOTION_TOKEN")
    if not token:
        print(
            "Must either pass --token option or set NOTION_TOKEN environment variable"
        )
        sys.exit(1)

    page = args.page
    if not page:
        page = os.environ.get("TESTS_PAGE")

    if not page:
        print(
            "Must either pass --page option or set PAGE environment variable"
        )
        sys.exit(1)

    collection_page = args.collection_page
    if not collection_page:
        collection_page = os.environ.get("PROJECTS_PAGE")

    if not collection_page:
        print(
            "Must either pass --collection option or set TESTS_PAGE environment variable"
        )
        sys.exit(1)

    #run_live_smoke_test(token, args.page)

    #run_live_block_callback_test(token, page)

    run_live_collection_callback_test(token, collection_page)
