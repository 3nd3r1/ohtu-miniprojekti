*** Settings ***
Resource    common.robot


*** Keywords ***
# Search Keywords -----------------------------------------------------------
Input And Submit Search Term
    [Arguments]    ${searchTerm}
    Input Text    name=search    ${searchTerm}
    Click Button    xpath=//button[contains(text(),'Search')]

Search Page Should Contain Reference
    [Arguments]    ${title}    ${author}    ${year}
    Search Page Should Be Open
    Page Should Contain    ${title}
    Page Should Contain    ${author}
    Page Should Contain    ${year}

Search Page Should Contain Extended Reference Details With Fields
    [Arguments]    &{fields}
    Search Page Should Be Open
    FOR    ${field_value_tuple}    IN    &{fields}
        Search Page Should Contain Reference Details Row With    ${field_value_tuple}[0]    ${field_value_tuple}[1]
    END

Search Page Should Contain Reference Details Row With
    [Arguments]    ${field}    ${value}
    ${detail_row_locator} =    Set Variable    xpath://td[@class='expanded-row-content']//table//tbody//tr
    Element Should Be Visible    ${detail_row_locator}//td//strong[text()='${field}']
    Element Should Be Visible    ${detail_row_locator}//td[text()='${value}']

Search Page Reference Count Should Be
    [Arguments]    ${count}
    Search Page Should Be Open
    ${page_count} =    Get Element Count    xpath://tr[@class='reference-row']
    Should Be Equal As Integers    ${page_count}    ${count}

Get Reference Row Locator
    [Arguments]    ${title}    ${author}    ${year}
    ${reference_row_locator} =    Set Variable
    ...    xpath://tr[contains(@class,'reference-row') and @data-title='${title}' and @data-author='${author}' and @data-year='${year}']
    RETURN    ${reference_row_locator}

Click Reference
    [Arguments]    ${title}    ${author}    ${year}
    ${reference_row_locator} =    Get Reference Row Locator    ${title}    ${author}    ${year}

    Search Page Should Be Open

    Wait Until Element Is Visible    ${reference_row_locator}
    Wait Until Element Is Enabled    ${reference_row_locator}
    Click Element    ${reference_row_locator}

# Raw BibTex Keywords ----------------------------------------------------------

Raw BibTex Page Should Contain Reference
    [Arguments]    ${reference_type}    ${title}    ${author}    ${year}
    Raw BibTex Page Should Be Open
    ${textbox} =    Get Text    xpath://pre[@id='bibtex-output']
    Container Should Contain Reference In Bibtex    ${textbox}    ${reference_type}    ${title}    ${author}    ${year}

Container Should Contain Reference In Bibtex
    [Arguments]    ${container}    ${reference_type}    ${title}    ${author}    ${year}
    Should Contain    ${container}    @${reference_type}{
    Should Contain    ${container}    title = "${title}"
    Should Contain    ${container}    author = "${author}"
    Should Contain    ${container}    year = ${year}
