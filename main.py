from bs4 import BeautifulSoup
from datetime import datetime
from typing import List, Dict, NamedTuple
import argparse
import json
import os

from config import Config


config = Config()


def build(c: Config) -> None:
    generate_index(c)
    generate_posts(c)
    generate_styles(c)


def generate_index(c: Config) -> None:
    """ Index page for the static site """
    template = c.JINJA_ENV.get_template("index.html")
    output = template.render()

    rendered_file = "index.html"
    with open(f"{c.BUILD_DIR}/{rendered_file}", "w") as f:
        print("[LOG] Generated index.html...")
        f.write(output)


def generate_posts(c: Config) -> None:
    """ Generates the posts.html file (contains list of blogposts and sorts them)
        Also parses markdown files in ./content and writes to file in ./build
    """

    delete_posts(c)  # Clears build folder

    HTML_FILE = "posts.html"

    class PostToken(NamedTuple):
        title: str
        date: str
        intro: str
        filename: str
        file_location: str

    # Renders the template that redirects to all the posts
    template = c.JINJA_ENV.get_template(HTML_FILE)

    post_token_list = []
    post_folder = os.listdir(c.CONTENT_POST_DIR)
    for file in post_folder:
        # Reads md file from content folder
        with open(f"{c.CONTENT_POST_DIR}/{file}", "r") as f:
            content = f.read()
            content_template = c.JINJA_ENV.get_template("content.html")
            output = content_template.render(content=content)

        # Copies to build directory
        B_post_location = f"{c.BUILD_DIR}/posts/{file}"
        with open(B_post_location, "w") as f:
            print(f"[LOG] Creating content for {file}...")
            f.write(output)

        soup = BeautifulSoup(content, "html.parser")
        soup_title = soup.find("div", class_="title").get_text()
        soup_date = soup.find("div", class_="date").get_text()
        # add to nuzlocke-ssg
        soup_intro = soup.find("div", class_="intro").get_text()
        post_token = PostToken(
            title=soup_title,
            date=soup_date,
            intro=soup_intro,
            filename=file,
            file_location=f"/posts/{file}",
        )
        post_token_list.append(post_token)
        post_token_list.sort(key=lambda x: x.date, reverse=True)

    rendered_posts_html = template.render(posts=post_token_list)
    with open(f"{c.BUILD_DIR}/{HTML_FILE}", "w") as f:
        print(f"[LOG] Generated {HTML_FILE}...")
        f.write(rendered_posts_html)

#TODO: fix this; only works with 1 stylesheet
def generate_styles(c: Config) -> None:
    """ Parses stylesheets in ./static and writes to ./build/stylesheets """
    stylesheets_folder = os.listdir(c.CSS_DIR)
    for file in stylesheets_folder:
        # Reads stylesheets from static folder
        with open(f"{c.CSS_DIR}/{file}", "r") as f:
            css_file = f.read()

        # Writes into Build folder
        with open(f"{c.BUILD_DIR}/static/stylesheets/{file}", "w") as f:
            print("[LOG] Copying stylesheets to build folder...")
            f.write(css_file)


def new_post(c: Config) -> None:
    datetime_obj = datetime.now()
    current_date = datetime_obj.strftime("%m-%d-%Y")
    with open(f"{c.CONTENT_POST_DIR}/{datetime_obj}.html", "w") as f:
        f.write(
            f"<!-- Don't channge the classes or delete these -->\n"
            f"<div class='title'>Insert title here</div>\n"
            f"<div class='date'>{current_date}</div>\n"
            f"<div class='intro'>Insert intro here</div>\n"
        )


def delete_posts(c: Config) -> None:
    B_post_folder = os.listdir(f"{c.BUILD_DIR}/posts")
    for file in B_post_folder:
        file_path = os.path.join(f"{c.BUILD_DIR}/posts", file)
        os.remove(file_path)
        print(f"[LOG] Deleting {file} from ./build/posts folder")


def main() -> None:
    parser = argparse.ArgumentParser(description="Commands")
    parser.add_argument("command", type=str, help="builds site")
    args = parser.parse_args()

    if args.command == "build":
        if os.path.isdir(config.BUILD_DIR):
            print("Build directory exists")
        else:
            print("Build directory doesn't exist")
            os.mkdir(config.BUILD_DIR)
            os.mkdir(f"{config.BUILD_DIR}/posts")
            os.mkdir(f"{config.BUILD_DIR}/static")
            os.mkdir(f"{config.BUILD_DIR}/static/stylesheets")
        build(config)
    elif args.command == "newpost":
        new_post(config)
    elif args.command == "help":
        print(
            "Commands: \n"
            "build  |   generates the site and downloads assets \n"
            "newpost|   generates a markdown file for content"
        )
    else:
        print("Wrong command. Enter 'help'")


if __name__ == "__main__":
    main()
