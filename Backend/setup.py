from setuptools import setup
setup(
    name = "enpalme",
    packages = ['enpalme'],
    version = "0.1",
    use_scm_version = False,
    url = "https://uis.edu.co",
    setup_requires=["setuptools_scm"],
    description = "Módulo de para testear el protocolo RESTCONF",
    author = "Douglas Ramírez",
    install_requires = ["jetconf"],
    package_data = {
    "" : ["yang-library-data.json"]
    }
)
