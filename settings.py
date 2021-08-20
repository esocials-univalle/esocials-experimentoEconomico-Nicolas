from os import environ

SESSION_CONFIGS = [
    dict(
        name='Experimento_economico_formal_fijo',
        display_name="Contrato formal a término fijo",
        num_demo_participants=12,
        app_sequence=['laboratorio'],
        tipo="formal-fijo"
    ),
    dict(
        name='Experimento_economico_formal_indefinido',
        display_name="Contrato formal a término indefinido",
        num_demo_participants=12,
        app_sequence=['laboratorio'],
        tipo="formal-indefinido"
    ),
    dict(
        name='Experimento_economico_formal_servicios',
        display_name="Contrato formal por prestación de servicios",
        num_demo_participants=12,
        app_sequence=['laboratorio'],
        tipo="formal-servicios"
    ),
    dict(
        name='Experimento_economico_informal_fijo',
        display_name="Contrato informal a término fijo",
        num_demo_participants=12,
        app_sequence=['laboratorio'],
        tipo="informal-fijo"
    ),
    dict(
        name='Experimento_economico_informal_indefinido',
        display_name="Contrato informal a término indefinido",
        num_demo_participants=12,
        app_sequence=['laboratorio'],
        tipo="informal-indefinido"
    ),
    dict(
        name='Experimento_economico_informal_servicios',
        display_name="Contrato informal por prestación de servicios",
        num_demo_participants=12,
        app_sequence=['laboratorio'],
        tipo="informal-servicios"
    ),

]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'es'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'COP'
USE_POINTS = False

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'vp9)$5p%t+5vbf7lk#6^!8gvnm_)xf)wp@((rqxu3)=$-%7p#+'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
