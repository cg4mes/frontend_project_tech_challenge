@regression_tests

Feature: Validate element created dropdown column

  @elements_home_validate
  Scenario: Navigate to the Kayak home page and validate principal elements
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    Then The page "should" contain the next elements
      | name                   | type   |
      | title                  | h2     |
      | start_date             | div    |
      | end_date               | div    |
      | search                 | button |
      | origin                 | input |

  @url_validate
  Scenario: Validate URL of Home page
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    Then The url page should be equal to the next "https://www.kayak.com.co/" url

  @urls_validate
  Scenario Outline: Navigate between countries and validate the URL
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    When I navigate to the "<url>" URL
    Then The url page should be equal to the next "<url>" url

    Examples:
      | url                       |
      | https://www.kayak.com.my/ |
      | https://www.kayak.com.pr/ |
      | https://www.kayak.com.br/ |

  @menu_validate
  Scenario Outline: Navigate between menu options and validate the URL
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    When I select the "<option>" from the menu
    Then The url page should be equal to the next "<url>" url

    Examples:
      | option                  | url                           |
      | flights                 | /flights                      |
      | stays                   | /stays                        |
      | cars                    | /cars                         |