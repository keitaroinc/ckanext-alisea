import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckanext.alisea import helpers as h


class AliseaPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "alisea")


    # ITemplateHelpers
    def get_helpers(self):
        return {
            'get_google_tag':h.get_google_tag
        }

    
