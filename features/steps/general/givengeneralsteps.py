from behave import given, use_step_matcher
from lib.pages.basepage import BasePage
from lib.constants import Constants

use_step_matcher("re")


@given(u'I navigate to the kayak main page')
def visit_login(context):
    base_page = BasePage(context)
    country = context.config.userdata.get('country', 'co')
    url = Constants.COUNTRIES_URL[country]
    context.current_url = url
    base_page.visit_page(url)



