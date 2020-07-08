class Locator:

    blockui = '//div[@class="blockUI blockOverlay"]'
    modal_footer = '//div[@class="modal-footer"]'
    result_label = '//div[@class="select2-result-label"]'

# Sign Up page locators

    #start_free_trial = '//*[@id="header-nav"]/div/ul/li[6]/a'
    signup_email = '//*[@id="email"]'
    signup_password = '//*[@id="password"]'
    signup_country = '//*[@id="country"]'
    signup_button = '//*[@id="app"]/div/div[3]/div[2]/div/form/div[4]/button'
    step_two_signup_button = '//*[@id="app"]/div/div[2]/div[1]/form/div[5]/button'
    business_name = '//*[@id="businessname"]'
    input_domain = '//*[@id="domain"]'
    firstname = '//*[@id="firstname"]'
    lastname = '//*[@id="lastname"]'
    input_mobile_number = '//*[@id="app"]/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/input'
    input_business_type = '//*[@id="businesstype"]'
    input_number_of_stores = '//*[@id="numberofstores"]'  
    skip_tutorial_btn = '//*[@id="skip-onboarding"]'
    lets_go = '//*[@id="step1-complete"]'
    domain_error = '//*[@id="app"]/div/div[2]/div[1]/form/div[1]/div[2]/div[2]/p'
    capture_domain_frame = '//*[@id="app"]/div/div[2]/div[1]/form/div[1]/div[2]/div[2]'
    
# Login page locators

    login_username = '//*[@id="email"]'
    login_password = '//*[@id="password"]'
    login_button = '//*[@id="app"]/div/div[3]/div[2]/div/form/div[5]/button'
    verify_login = '/html/body/div[1]/div/ul/li[2]/a'

# Add products page locators

    product_name = '//*[@id="title"]' 
    sku =  '//*[@id="sku"]' 
    category = '//*[@id="productForm"]/div[1]/div[2]/div[1]/div/div/div/button/span[1]'
    add_category = '//*[@id="productForm"]/div[1]/div[2]/div[1]/div/div/span/a'
    enter_category = '/html/body/div[7]/div/div/div[2]/div/form/input'
    enter_category = '//*[contains(@class,"btn")]'
    ok_button = '/html/body/div[7]/div/div/div[3]/button[2]'
    #/html/body/div[8]/div/div/div[3]/button[2]
    enter_tag = '//*[@id="s2id_autogen1"]'
    supplier_button = '//*[@id="productForm"]/div[1]/div[3]/div[2]/div/div/button'
    supplier_dropdown = '//*[@id="productForm"]/div[1]/div[3]/div[2]/div/div/div/ul/li[1]'
    pricing_type = '//*[@id="productForm"]/div[1]/div[4]/div[1]/div/div/button'
    Fixed = '//*[@id="productForm"]/div[1]/div[4]/div[1]/div/div/div/ul/li[1]'
    Variable = '//*[@id="productForm"]/div[1]/div[4]/div[1]/div/div/div/ul/li[2]'
    Unit = '//*[@id="productForm"]/div[1]/div[4]/div[1]/div/div/div/ul/li[3]'
    cost = '//*[@id="cost"]'
    tax_inclusive_price = '//*[@id="unitPriceTaxInluded"]'
    tax_exclusive_price = '//*[@id="unitPrice"]'
    has_variants = '//*[@id="uniform-hasVariantsCheckbox"]/span'
    add_single_choice = '//*[@id="displayVariants"]/div[2]/a'
    add_multiple_choice = '//*[@id="displayVariants"]/div[4]/a'
    track_inventory_checkbox = '//*[@id="trackInventoryCheckbox"]'
    inventory_type = '//*[@id="inventoryType"]'
    inventory_type_btn = '//*[@id="stockInfoSection"]/div[1]/div/div/div/button'
    Simple = '//*[@id="stockInfoSection"]/div[1]/div/div/div/div/ul/li[1]'
    Composite = '//*[@id="stockInfoSection"]/div[1]/div/div/div/div/ul/li[2]'
    Serialized = '//*[@id="stockInfoSection"]/div[1]/div/div/div/div/ul/li[3]'
    #ul_xpath = '//*[@id="sortable"]'
    save_button = '//*[@id="saveButton"]'
    product_search = '//*[@id="datatable_ajax_filter"]/label/span/input'
    online_info_tab = '/html/body/div[3]/div[2]/div/div[2]/div[1]/div/ul/li[2]/a'
    online_name = '//*[@id="onlineTitle"]'
    sell_online = '//*[@id="uniform-isOnlineCheckbox"]'
    featured_products = '//*[@id="uniform-isFeaturedCheckbox"]'
    save_online = '//*[@id="saveOnlineInfoButton"]'
    delete_product = '//*[@id="productForm"]/div[2]/a[2]'
    confirm_delete_button = '//*[@id="deleteButton"]'
    
# Menu list locators
    text_Settings = '/html/body/div[3]/div[1]/div/ul/li[13]/a/i'
    partial_link_text_iPad_register = 'iPad Registers'

# iPad Register page locators
    text_add_ipad_register = '//*[contains(text(),"Add iPad Register")]'
    id_confirm_adding_new_register_yes = '//*[@id="confirmAdd"]/div/div[3]/button[2]'
    id_edit_register_form = '//*[@id=editRegisterForm"]'
    id_save_register = '//*[@id=saveButton"]'

# Transactions
    transaction_filter_search = '//div[@id="datatable_ajax_filter"]/label/span/input'
    transaction_table = '//table[@id="datatable_ajax"]/tbody/tr'
    searched_transaction_time = '//table[@id="datatable_ajax"]/tbody/tr/td/a'
# Transaction Details
    receipt_number_value = '//div[@class="form-body"]/div/div/div/div/p'
    transaction_type_value = '//div[@class="form-body"]/div[2]/div/div/div/p'
    cancelled_by_value = '//div[@class="form-body"]/div[5]/div/div/div/p'
    cancelled_at_value = '//div[@class="form-body"]/div[4]/div[2]/div/div/p'
    cancelled_reason_value = '//div[@class="form-body"]/div[5]/div[2]/div/div/p'


