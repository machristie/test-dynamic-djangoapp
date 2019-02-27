import setuptools

setuptools.setup(
    name="test-dynamic-airavata-django-app",
    version="0.0.1",
    description="POC Django app for testing dynamic loading",
    packages=setuptools.find_packages(),
    install_requires=[
        'django>=1.11.16'
    ],
    entry_points="""
[airavata.djangoapp]
dynamic_djangoapp = dynamic_djangoapp.apps:DynamicDjangoAppConfig
""",
)
