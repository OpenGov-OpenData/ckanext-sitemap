import ckan.plugins as plugins
import ckanext.sitemap.view as view
from ckanext.sitemap import cli


class SitemapPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IBlueprint)
    plugins.implements(plugins.IClick)

    # IBlueprint
    def get_blueprint(self):
        return view.get_blueprints()

    # IClick
    def get_commands(self):
        return cli.get_commands()
