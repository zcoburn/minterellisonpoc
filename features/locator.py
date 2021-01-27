class locator(object):

#MinterEllisonPOC
    #Homepage
    img_logo                        = "(//img[@class='img-logo'])[1]"
    hamburger_menu                  = "//a[contains(.,'MENU')]"
    solr_search_box                 = "(//input[@name='q'])[2]"

    homepage_header                 = "//h1[contains(.,'Discover our legal and consulting services for your industry. Our people are ready whenever you need us.')]"
    thumbnail_title_item1           = "//h3[contains(.,'Tapping the potential of Hydrogen in Australia')]"
    footer_copyright_text           = "//p[contains(.,'© 2021 MinterEllison')]"

    #Perform Search
    autocomplete_item1              = "(//span[contains(@class,'solr-search-autocomplete-item__title')])[1]"
    search_button                   = "(//button[@type='submit'])[2]"

    global_search_header            = "//h1[@class='title']"
    global_time_list                = "//span[contains(@class,'time list')]"
    global_author_list              = "//span[@class='author list']"
