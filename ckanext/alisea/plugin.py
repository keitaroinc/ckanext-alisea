import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.lib.plugins import DefaultTranslation
from collections import OrderedDict
from ckanext.alisea import helpers as h


class AliseaPlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.ITranslation)
    plugins.implements(plugins.IFacets)
    

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "alisea")


    # ITemplateHelpers
    def get_helpers(self):
        return {
            'get_google_tag': h.get_google_tag
        }

    def update_config_schema(self, schema):

        ignore_missing = toolkit.get_validator('ignore_missing')
        validators = [ignore_missing]
        schema.update({
            'footer_left': validators,
            'footer_right': validators,
        })

        return schema
    
    def dataset_facets(self, facet_dict, package_type):
        new_facets = [
            ("country", "Country"),
            ("type_of_document", "Document Type"),
            ("type_of_alisea_product", "Type of Alisea Product"),
            ("language", "Language"),
            ("organization", "Organizations"),
            ("groups", "Groups"),
            ("agroecology_category", "Agroecology Category"),
            ("license_id", "Licence"),
            ("tags", "Tags"),

        ]
        return OrderedDict(new_facets)