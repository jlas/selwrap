# Wrapper for Python Selenium client

A wrapper for the Python Selenium client with features such as:
 * PageObject base class with useful methods like:
    * `refresh`
    * `scrollDown`
    * etc...
 * Shorter method names (e.g. `lookup_element_by_tag_name` -> `_tag`)
 * Automatic wait on all lookups
 * Easily ignore errors on lookups
