from ckan.plugins import toolkit as tk
import logging


def get_google_tag():
    gtag = tk.config.get('ckan.alisea.gtag')
    return gtag