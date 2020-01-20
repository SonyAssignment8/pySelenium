from  setuptools import setup,find_packages
# setup(
#     name='amazon_app',
#     version=2.0,
#     package=find_packages
#
# )
setup(
    name='amazon_app',
    version=3.0,
    package=find_packages(exclude=['test_scripts'])

)
