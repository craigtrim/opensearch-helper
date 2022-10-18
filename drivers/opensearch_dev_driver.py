from pprint import pprint

from baseblock import Enforcer

from opensearch_helper import OpenSearchDEV


def crud():

    bp = OpenSearchDEV()
    assert bp


def main():
    from drivers import IntegrationWrapper
    wrapper = IntegrationWrapper()

    wrapper.call(crud)

    wrapper.deconstruct_env()


if __name__ == "__main__":
    main()
