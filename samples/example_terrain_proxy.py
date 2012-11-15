# encoding: utf-8

"""
Prepare Firefox with a special proxy configuration

Example terrain file to "inject" the proxy configuration.
"""

from lettuce import before, world, after
from splinter.browser import Browser
from salad.logger import logger


@before.all
def setup_browser():
    logger.info("Setting up firefox...")

    proxy_settings = {
        "network.proxy.type": 1,
        "network.proxy.http": "192.168.1.123",
        "network.proxy.http_port": 8080,
        "network.proxy.ssl": "192.168.1.123",
        "network.proxy.ssl_port": 8080,
        "network.proxy.ftp": "192.168.1.123",
        "network.proxy.ftp_port": 8080,
    }

    try:
        world.firefox = Browser("firefox", profile_preferences=proxy_settings)
    except:
        logger.warn("Error starting up firefox")


@after.all
def teardown_browser(total):
    logger.info("Tearing down firefox...")
    try:
        world.firefox.quit()
    except:
        logger.warn("Error tearing down firefox")
