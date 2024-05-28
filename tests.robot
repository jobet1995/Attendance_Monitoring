*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}          http://localhost:8000
${PRODUCT_NAME}      Test Product
${SUPPLIER_NAME}     Test Supplier
${WAREHOUSE_NAME}    Test Warehouse
${USER_EMAIL}        admin@example.com
${USER_PASSWORD}     adminpassword

*** Test Cases ***
Create Product
    [Documentation]    Create a new product
    [Tags]    CRUD
    ${csrf_token}    Get Csrf Token
    ${product_id}    Create Product    ${PRODUCT_NAME}    ${csrf_token}
    [Teardown]    Delete Product    ${product_id}    ${csrf_token}

Read Product
    [Documentation]    Read the created product
    [Tags]    CRUD
    ${csrf_token}    Get Csrf Token
    ${product_id}    Create Product    ${PRODUCT_NAME}    ${csrf_token}
    ${product_details}    Get Product Details    ${product_id}    ${csrf_token}
    Should Be Equal    ${product_details['product_name']}    ${PRODUCT_NAME}

Update Product
    [Documentation]    Update the created product
    [Tags]    CRUD
    ${csrf_token}    Get Csrf Token
    ${product_id}    Create Product    ${PRODUCT_NAME}    ${csrf_token}
    Update Product Details    ${product_id}    New Product Name    ${csrf_token}
    ${updated_product_details}    Get Product Details    ${product_id}    ${csrf_token}
    Should Be Equal    ${updated_product_details['product_name']}    New Product Name

Delete Product
    [Documentation]    Delete the created product
    [Tags]    CRUD
    ${csrf_token}    Get Csrf Token
    ${product_id}    Create Product    ${PRODUCT_NAME}    ${csrf_token}
    Delete Product    ${product_id}    ${csrf_token}
    ${product_details}    Run Keyword And Ignore Error    Get Product Details    ${product_id}    ${csrf_token}
    Should Be Equal As Strings    ${product_details['detail']}    Not found.

*** Keywords ***
Get Csrf Token
    [Return]    ${csrf_token}    # Assuming csrf token is already fetched in a previous keyword

Create Product
    [Arguments]    ${product_name}    ${csrf_token}
    ${data}    Create Dictionary    product_name=${product_name}
    ${headers}    Create Dictionary    Content-Type=application/json    X-CSRFToken=${csrf_token}
    ${response}    Post Request    ${BASE_URL}/api/products/    json=${data}    headers=${headers}
    ${product_id}    Set Variable    ${response.json()['id']}
    [Return]    ${product_id}

Get Product Details
    [Arguments]    ${product_id}    ${csrf_token}
    ${response}    Get Request    ${BASE_URL}/api/products/${product_id}/    headers=    X-CSRFToken=${csrf_token}
    [Return]    ${response.json()}

Update Product Details
    [Arguments]    ${product_id}    ${new_product_name}    ${csrf_token}
    ${data}    Create Dictionary    product_name=${new_product_name}
    ${headers}    Create Dictionary    Content-Type=application/json    X-CSRFToken=${csrf_token}
    ${response}    Put Request    ${BASE_URL}/api/products/${product_id}/    json=${data}    headers=${headers}

Delete Product
    [Arguments]    ${product_id}    ${csrf_token}
    ${headers}    Create Dictionary    Content-Type=application/json    X-CSRFToken=${csrf_token}
    ${response}    Delete Request    ${BASE_URL}/api/products/${product_id}/    headers=${headers}
