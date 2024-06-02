Feature: Product management in inventory system

    Scenario: Add a new product
        Given I am on the "Add Product" page
        When I enter the product details
        And I click on the "Add" button
        Then the product should be added to the inventory
        And I should see a confirmation message

    Scenario: Update a product
        Given I am viewing a product
        When I click on the "Update" button
        And I change the product details
        And I click on the "Save Changes" button
        Then the product details should be updated
        And I should see a confirmation message

    Scenario: Delete a product
        Given I am viewing a product
        When I click on the "Delete" button
        And I confirm the deletion
        Then the product should be removed from the inventory
        And I should not be able to find the product in the inventory

    Scenario: Search for a product
        Given I am on the "Products" page
        When I enter the name of a product into the search field
        And I click on the "Search" button
        Then I should see the product in the search results
