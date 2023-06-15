from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "portfolio"
    #permite cambiar el nombre a uno publico en la app
    verbose_name = 'Portafolio'
