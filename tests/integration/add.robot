*** Settings ***
Documentation       Integraatio- ja hyväksymistestaus lähdeviitteiden lisäykselle

Resource            ../../resources/add.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Run Keywords
...                     Initialize Database    AND
...                     Reference Count In Database Should Be    0
Test Teardown       Initialize Database


*** Test Cases ***
User Should Be Able to Add An Article
    [Documentation]    Käyttäjänä pystyn lisäämään "article"-tyyppisen lähdeviitteen,
    ...    joka sisältää kentät (title, author, journal, year, volume, number, page) #1
    Go To Add Page
    Select Reference Type    article
    Set Field    article    author    Pekka Mikkola
    Set Field    article    title    Maijan artikkeli
    Set Field    article    journal    Maijan artikkelikokoelma
    Set Field    article    year    2011
    Submit Reference    article
    Reference Addition Should Be Confirmed
    Reference Count In Database Should Be    1

User Should Be Able to Add A Book
    [Documentation]    Käyttäjänä pystyn lisäämään "book"-tyyppisen lähdeviitteen #37
    Go To Add Page
    Select Reference Type    book
    Set Field    book    author    Maija Makkonen
    Set Field    book    title    Maijan kirja
    Set Field    book    year    2000
    Set Field    book    publisher    WSOY
    Submit Reference    book
    Reference Addition Should Be Confirmed
    Reference Count In Database Should Be    1

User Should Be Able to Add An Inproceedings
    [Documentation]    Käyttäjänä pystyn lisäämään "inproceeding"-tyyppisen lähdeviitteen #38
    Go To Add Page
    Select Reference Type    inproceedings
    Set Field    inproceedings    author    Maija
    Set Field    inproceedings    title    Maijan inproceedings
    Set Field    inproceedings    booktitle    Maijan kokoelma
    Set Field    inproceedings    year    2011
    Submit Reference    inproceedings
    Reference Addition Should Be Confirmed
    Reference Count In Database Should Be    1

User Should Not Be Able to Add An Article Without Required Fields
    [Documentation]    Ei user storya
    Go To Add Page
    Select Reference Type    article
    Set Field    article    author    Pekka Mikkola
    Set Field    article    title    Maijan artikkeli
    Set Field    article    journal    Maijan artikkelikokoelma
    Submit Reference    article
    Reference Addition Should Be Rejected With Invalid Field    article    year
    Reference Count In Database Should Be    0

User Should Be Able To Add An Article With A Valid DOI
    [Documentation]    Käyttäjänä pystyn lisäämään lähdeviitteen DOI-viitteen avulla #64
    Go To Add Page

    Set DOI    https://doi.org/10.1016/j.elerap.2011.05.004

    Selected Reference Type Should Be    article

    Submit Reference    article
    Reference Addition Should Be Confirmed
    Reference Count In Database Should Be    1

User Should Be Able To Add A Book With A Valid DOI
    [Documentation]    Käyttäjänä pystyn lisäämään lähdeviitteen DOI-viitteen avulla #64
    Go To Add Page

    Set DOI    http://dx.doi.org/10.1093/oso/9780195075939.001.0001

    Selected Reference Type Should Be    book

    Submit Reference    book
    Reference Addition Should Be Confirmed
    Reference Count In Database Should Be    1

User Should Be Able To Add An Inproceedings With A Valid DOI
    [Documentation]    Käyttäjänä pystyn lisäämään lähdeviitteen DOI-viitteen avulla #64
    Go To Add Page

    Set DOI    http://dx.doi.org/10.1145/1868914.1868941

    Selected Reference Type Should Be    inproceedings

    Submit Reference    inproceedings
    Reference Addition Should Be Confirmed
    Reference Count In Database Should Be    1

User Should Not Be Able To Add A Reference With An Invalid DOI
    [Documentation]    Käyttäjänä pystyn lisäämään lähdeviitteen DOI-viitteen avulla #64
    Go To Add Page

    Set DOI    invalid-doi

    Setting DOI Should Fail Rejected With Message    Invalid DOI

User Should Not Be Able To Add A Reference With Unsupported Type With DOI
    [Documentation]    Käyttäjänä pystyn lisäämään lähdeviitteen DOI-viitteen avulla #64
    Go To Add Page

    Set DOI    http://dx.doi.org/10.1007/978-3-031-30019-6_16

    Setting DOI Should Fail Rejected With Message    Unsupported reference type inbook
