Feature: Product search results page

  Scenario: Search results can be sorted by prices
    Given Open search results page
    When Select sort by price, high to low
    Then Verify filter applied (fist product price should be > last product price)


