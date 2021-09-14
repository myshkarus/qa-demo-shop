class NavigationPanelConstants:
    """Store constants related to NavigationPanel object"""

    # Navigation panel
    LINK_NAV_BOOKS_XPATH = ".//ul[@class='top-menu']//a[@href='/books']"
    LINK_NAV_COMPUTERS_XPATH = ".//ul[@class='top-menu']//a[@href='/computers']"
    LINK_NAV_ELECTRONICS_XPATH = ".//ul[@class='top-menu']//a[@href='/electronics']"
    LINK_NAV_APPAREL_SHOES_XPATH = ".//ul[@class='top-menu']//a[@href='/apparel-shoes']"
    LINK_NAV_DIGITAL_DOWNLOADS_XPATH = ".//ul[@class='top-menu']//a[@href='/digital-downloads']"
    LINK_NAV_JEWELRY_XPATH = ".//ul[@class='top-menu']//a[@href='/jewelry']"
    LINK_NAV_GIFT_CARDS_XPATH = ".//ul[@class='top-menu']//a[@href='/gift-cards']"

    # Navigation panel sublists
    LINK_NAV_DESKTOPS_XPATH = ".//div[@class='header-menu']/ul[@class='top-menu']//a[@href='/desktops']"
    LINK_NAV_NOTEBOOKS_XPATH = ".//div[@class='header-menu']/ul[@class='top-menu']//a[@href='/notebooks']"
    LINK_NAV_ACCESSORIES_XPATH = ".//div[@class='header-menu']/ul[@class='top-menu']//a[@href='/accessories']"
    LINK_NAV_CAMERA_PHOTO_XPATH = ".//div[@class='header-menu']/ul[@class='top-menu']//a[@href='/camera-photo']"
    LINK_NAV_CELL_PHONES_XPATH = ".//div[@class='header-menu']/ul[@class='top-menu']//a[@href='/cell-phones']"

    # Side navigation panel
    LINK_SIDE_BOOKS_XPATH = ".//div[@class='listbox']//a[@href='/books']"
    LINK_SIDE_COMPUTERS_XPATH = ".//div[@class='listbox']//a[@href='/computers']"
    LINK_SIDE_ELECTRONICS_XPATH = ".//div[@class='listbox']//a[@href='/electronics']"
    LINK_SIDE_APPAREL_SHOES_XPATH = ".//div[@class='listbox']//a[@href='/apparel-shoes']"
    LINK_SIDE_DIGITAL_DOWNLOADS_XPATH = ".//div[@class='listbox']//a[@href='/digital-downloads']"
    LINK_SIDE_JEWELRY_XPATH = ".//div[@class='listbox']//a[@href='/jewelry']"
    LINK_SIDE_GIFT_CARDS_XPATH = ".//div[@class='listbox']//a[@href='/gift-cards']"

    categories = ["BOOKS", "APPAREL & SHOES", "JEWELRY"]
    categories_xpath = [LINK_SIDE_BOOKS_XPATH, LINK_SIDE_APPAREL_SHOES_XPATH, LINK_SIDE_JEWELRY_XPATH]
    departments = [dep for dep in zip(categories, categories_xpath)]
