from behave import *
from features.pages.google.search_page import Search
from features.pages.google.results_page import Result
from hamcrest import assert_that, is_in, equal_to

@given(u'I am on google page')
def step_impl(context):
     context.search = Search(context.chrome_driver)


@when(u'fill in search box with keyword "wiki"')
def step_impl(context):
     context.chrome_driver.implicitly_wait(5)
     context.search.input_keyword("wikip")


@then(u'Verify the automatic matching results')
def step_impl(context):
     context.matching = context.search.get_automatic_matching()
     for i in context.matching:
          assert_that("wikip", is_in(i))


@step(u'select the first result in the dropdown list')
def step_impl(context):
     context.search.select_the_first_result_of_dropdown()


@then(u'Verify the direct is work')
def step_impl(context):
     context.chrome_driver.implicitly_wait(5)
     context.result = Result(context.chrome_driver)
     new_url = context.result.get_new_url()
     assert_that("search?source=", is_in(new_url))


@step(u'finish with Enter')
def step_impl(context):
     context.search.send_enter()


@step(u'click the search button')
def step_impl(context):
     context.search.click_search()


@then(u'Verify the searched results are correct')
def step_impl(context):
     context.results = context.result.get_keyword_results()
     for i in context.results:
          assert_that(i, equal_to("wikip"))