# map
def find_check_boxes(driver):
    return driver.find_elements()


#def select_all_checkboxes(driver):
#    list_box = find_check_boxes(driver)
#    for i in list_box:
#        i.click()
#    return


# styu = map(address_of_function,collection)
# the address that retuerned by the map is the place where result is stored.
# we can do like this below


# whenver we wanted to perform the same action on the sequnce/collection of elementsthen we use map function
# the resut of map fun is an addess where the result will be store


# elements = lambda driver : driver.find_elements()
# map(lambda i : i.click(), elements())

# def find_check_boxes(driver):
#    return driver.find_elements()

def select_all_dropdown(driver):
    dropdown = find_check_boxes(driver)
    for i in dropdown:
        i.click()
    return