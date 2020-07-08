class MPOnlineLocator:


# Marketplace Locators

    search_bar = '/html/body/div[2]/nav/div[3]/header-search-field/form/input'
    wishlist_icon = '/html/body/div[5]/main/product-list-container/div/section[2]/ul/li/a/div[1]/button'
    searched_product1 = '/html/body/div[5]/main/product-list-container/div/section[2]/ul/li/a/h3'  
    searched_product = '/html/body/div[5]/main/product-list-container/div/section[2]/ul/li/a/div[1]/div'
    no_result_found =  '/html/body/div[5]/main/product-list-container/div/div/h3'
    item_found = '/html/body/div[5]/main/product-list-container/div/section[2]/div[1]/div[1]/h3'
    stock_status = '/html/body/div[5]/main/section[1]/div/div[2]/stock-status/div/a'
    add_to_cart = '/html/body/div[5]/main/section[1]/div/div[2]/add-to-cart/button'
    checkout = '//*[@id="cart-modal"]/cart-modal-view/div/div/section[1]/div/div[2]/ul/li[2]/a'
    
# Customer Login with credentails

    login_email = '//*[@id="loginForm"]/div[1]/input[1]'
    login_password = '//*[@id="loginForm"]/div[1]/input[2]'
    email_error = '//*[@id="email-error"]'
    password_error = '//*[@id="password-error"]'
    signin = '//*[@id="loginForm"]/button'
    
# Checkout Step-1 

    login_checkout = '//*[@id="checkout-container"]/div/div/div[2]/aside/div[1]/a[1]'
    continue_step_one = '//*[@id="checkout-container"]/div/div/div[1]/div/form/fieldset[4]/div/div[2]/button'
    
    # Contact Info
    
    contact_email = '//*[@id="checkout-container"]/div/div/div[1]/div/form/fieldset[1]/input'
    contact_name = '//*[@id="checkout-container"]/div/div/div[1]/div/form/fieldset[2]/input'
    contact_phone = '//*[@id="checkout-container"]/div/div/div[1]/div/form/fieldset[3]/input'
    
# Checkout Step-2
    delivery_option = '//*[@id="checkout-container"]/div/div/div[1]/div/div[1]/div[1]/div[1]/div'
    pickup_option = '//*[@id="checkout-container"]/div/div/div[1]/div/div[1]/div/div[2]/div'
    
# Delivery Address
    add_new_address_button = '//*[@id="checkout-container"]/div/div/div[1]/div/div[1]/div[2]/fieldset[1]/div[2]/button'
    name = '//*[@id="checkout-container"]/div/div/div[1]/div/div[1]/div[2]/form/fieldset[1]/div/div[1]/input'
    phone = '//*[@id="checkout-container"]/div/div/div[1]/div/div[1]/div[2]/form/fieldset[1]/div/div[2]/input'
    address = '//*[@id="checkout-container"]/div/div/div[1]/div/div[1]/div[2]/form/fieldset[4]/input'
    postcode_selector = '//*[@id="checkout-container"]/div/div/div[1]/div/div[1]/div[2]/form/fieldset[5]/div/div'
    postcode = '//*[@id="react-select-2--value"]/div[2]/input'
    delivery_coverage = '//*[@id="checkout-container"]/div/div/div[1]/div/div[1]/div[2]/form/fieldset[5]/span[2]/span/div[2]/button'
    close_button = '//*[@id="shipping-areas-modal"]/shipping-areas-modal-view/div/button'
    add_address_button = '//*[@id="checkout-container"]/div/div/div[1]/div/div[1]/div[2]/form/fieldset[6]/button'
    
# Select Shipping Zone

    shipping_zone = '//*[@id="checkout-container"]/div/div/div[1]/div/div[1]/div[2]/fieldset[2]/div/div[1]/div'
    shipping_fee = '//*[@id="checkout-container"]/div/div/div[1]/div/div[1]/div[2]/fieldset[2]/div/div[1]/div/div[2]/h3'
    cart_shipping_fee = '//*[@id="checkout-container"]/div/div/div[2]/aside/div[2]/div[3]/div[1]/div[2]/span[2]'
    
# Pay now
    proceed_to_pay_delivery = '//*[@id="checkout-container"]/div/div/div[1]/div/div[1]/div[2]/fieldset[3]/div/div[2]/button'
    proceed_to_pay_pickup = '//*[@id="checkout-container"]/div/div/div[1]/div/div[1]/form/fieldset[3]/div/div[2]/button'
    
# Payment page

    proceed_to_pay = '//*[@id="payment"]/div[19]/div/button'
    

# Order Confirmation page

    order_confirmation_title = '/html/body/div[3]/main/h1'
    view_summary = '/html/body/div[3]/main/div/order-confirmation/div/div[1]/div/ul/li[1]/button'
    order_summary_delivery_fee = '/html/body/div[3]/main/div/order-confirmation/div/div[1]/div[2]/div[2]/div[1]/div[2]/span[2]/span'
    
    
    
    
    
    
    
    



    