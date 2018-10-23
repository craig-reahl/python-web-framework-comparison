# To run this test do:
# pytest --pyargs addressbook2_dev.test_addressbook2
# or
# reahl unit
#
# To set up a demo database for playing with, do:
# pytest -o python_functions=demo_setup --pyargs addressbook2_dev.test_addressbook2
# or
# reahl demosetup

from __future__ import print_function, unicode_literals, absolute_import, division

from reahl.tofu.pytestsupport import with_fixtures
from reahl.webdev.tools import XPath
from reahl.web_dev.fixtures import WebFixture

from simple_tr import MyUI


@with_fixtures(WebFixture)
def test_can_translate_delimiter(web_fixture):
    """A user can log in by going to the Log in page.
       The name of the currently logged in user is displayed on the home page."""

    wsgi_app = web_fixture.new_wsgi_app(site_root=MyUI, enable_js=True)
    web_fixture.reahl_server.set_app(wsgi_app)
    browser = web_fixture.driver_browser

    #import pdb;pdb.set_trace()

    browser.open('/')

    assert not web_fixture.driver_browser.is_element_present(XPath.paragraph_containing('my=dash=delimited=sentence'))
    browser.type(XPath.input_labelled('Input Text'), 'my-dash-delimited-sentence')
    browser.type(XPath.input_labelled('Separated by (Regular Expression)'), '-')
    browser.type(XPath.input_labelled('Join with (Character String)'), '=')
    browser.click(XPath.button_labelled('Perform Tr'))
    assert web_fixture.driver_browser.wait_for_element_present(XPath.paragraph_containing('my=dash=delimited=sentence'))
