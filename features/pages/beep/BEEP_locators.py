class Locator:
    header_title = '//h2[@data-testid="headerTitle"]'
    #choose_stores
    choose_notification = '//h2[@data-testid="selectStoreDescription"]'
    stores = '//li[@data-testid="store"]'
    #preference_selection
    preference = '//li[@data-testid="selectPrefrence"]'


    #ordering page
    no_i_am_not = '//button[@data-testid="noIamNot"]'
    yes_i_am = '//button[@data-testid="yesIam"]'
    bar = '//div[@id="root"]/main/section/div/div/div/summary'
    store_name = '//h1'
    back = '//div[@id="root"]/main/section/div/div/i'
    edit = '//div[@id="root"]/main/section/div/div/i[2]'
    back_in_store_name = '//div[@id="root"]/main/section/header/i'
    order_now = '//button[@data-testid="orderNow"]'
    items_increase = '//button[@data-testid="itemIncrease"]'
    first_item_add = '//div[@id="product-list"]/ol/li/div/ul/li/div[2]/button[2]'
    first_item_single_price = '//div[@id="product-list"]/ol/li/div/ul/li/div/div/span'
    first_item_quantity = '//div[@id="product-list"]/ol/li/div/ul/li/div[2]/span'
    item_simple_selection = '//li[@data-testid="itemDetailSimpleSelection"]'
    item_multiple_selection = '//div[@id="root"]/main/section/aside/div/div/ol/li[2]/ul/li[1]'
    item_detail_summary = '//p[@data-testid="itemDetailSummary"]'
    item_detail_add = '//div[@id="root"]/main/section/aside/div/div[2]/li/div[2]/button[2]'
    item_detail = '//div[@data-testid="itemDetail"]'
    item_detail_single_price = '//div[@id="root"]/main/section/aside/div/div[2]/li/div/div/span'
    item_detail_quantity = '//span[@data-testid="itemDetailQuantity"]'
    OK = '//button[@data-testid="OK"]'
    cart_label_number = '//span[@class="tag__number"]'
    clear_all = '//button[@data-testid="clearAll"]'
    category_right = '//h2[@data-testid="categoryRight"]'
    #checkout_page
    money = '//span[@data-testid="money"]'
    login = '//button[@class="warning__button"]'
    Pay = '//button[@data-testid="pay"]'
    #pickip_details
    pickip_details_title = '//div[@id="root"]/main/section/header/h2/span'
    customer_name = '//div[@data-testid="customerName"]/input'
    customer_phone_number = '//div[@data-testid="customerPhoneNumber"]/div/div/input'
    preorder_date = '//li[@data-testid="preOrderDate"]'
    preorder_hour = '//li[@data-testid="preOrderHour"]'
    deliver_to = '//input[@data-testid="deliverTo"]'
    # delivery_details
    delivery_name = '//form[@class="customer__form"]/div/input'
    delivery_mobile = '//form[@class="customer__form"]/div[2]/div/div/input'
    unit = '//form[@class="customer__form"]/div[4]/div'
    delivery_dialog_textarea = '//div[@id="root"]/main/section/aside/div/div/textarea'
    delivery_dialog_save = '//div[@id="root"]/main/section/aside/div/button'
    Continue = '//button[@data-testid="continue"]'
    #payment_selection
    payment_selector = '//li[@data-testid="paymentSelector"]'
    pay_now = '//button[@data-testid="payNow"]'
    #pay_via_card
    card_number = '//input[@id="cardNumber"]'
    valid_date = '//input[@id="validDate"]'
    cvv = '//input[@id="cvv"]'
    name_on_card = '//input[@id="name"]'
    pay_money = '//button[@data-testid="payMoney"]'
    # pay_via_online_banking
    bank = '//form[@id="bank-2c2p-form"]'
    #stripe
    test_payment = '//button[@name="success"]'
    #2c2p
    otp = '//input[@id="otp"]'
    proceed = '//input[@id="continue"]'
    #pay_via_online_banking
    pay_ = '//button[contains(text(),"Pay")]'
    #order_paid
    prepare = '//div[@id="root"]/main/section/div/p'
    phone_number = '//input[@class="react-phone-number-input__input react-phone-number-input__phone"]'
    customer_continue = '//button[@data-testid="customerContinue"]'
    view_receipt = '//button[contains(text(),"View Receipt")]'
    close = '//input[@id="root"]/main/section/header/figure/svg'
    order_number_label = '//label[contains(text(),"Your Order Number")]'
    pick_up_number = 'span[@class="thanks-pickup__id-number"]'
    check_my_balance = 'a[contains(text(),"Check My Balance")]'
    #scan
    choose_deliver_to_location = '//div[@data-testid="DeliverToBar"]'
    store_for_choice = '//ul[@class="store-card-list"]/li[3]'
    search_store = '//input[@data-testid="searchStore"]'
    input_store = '//input[@data-testid="inputStore"]'
    search_store_result_list = 'ul[@class="store-card-list"]'
    search_store_result = '//li[@data-testid="deliverStore"]'
    search_store_result_spare = '//div[@id="root"]/main/section[2]/div[2]/ul/li'
    collection = '//li[@data-testid="collection"]'
    scan_food_delivery = '//div[@id="root"]/main/aside/div/div/button[2]'
    scan_self_pickup = '//div[@id="root"]/main/aside/div/div/button'
    #deliver to
    search_address = '//input[@data-testid="searchAddress"]'
    searched_address_result = '//div[@data-testid="searchedAddressResult"]'
    search_address_result_spare_2 = '//div[@id="root"]/main/section/div/div/div[2]/div[2]/div'
    search_address_result_spare = '//div[@id="root"]/main/section/div/div[2]/div[2]/div'
    search_address_result_safari = '//div[@id="root"]/main/div/div/div[2]/div/div'

