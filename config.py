from jinja2 import Environment, select_autoescape, FileSystemLoader


class Config:
    # Markup
    CONTENT_POST_DIR = "./content/posts"

    # Static directory
    IMAGE_DIR = "./static/img"
    TEMPLATE_DIR = "./static/templates"
    CSS_DIR = "./static/stylesheets"
    SCRIPTS_DIR = "./static/scripts"

    # Jinja environment variable
    JINJA_ENV = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        autoescape=False
    )
    
    # Build
    BUILD_DIR = "./build"
