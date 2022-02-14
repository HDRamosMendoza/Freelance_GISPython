from selenium import webdriver

options = webdriver.ChromeOptions()

options.add_argument('headless')



browser = webdriver.Chrome(options=options)



url = "https://maps.googleapis.com/maps/vt?pb=!1m4!1m3!1i16!2i18746!3i34973!1m4!1m3!1i16!2i18747!3i34973!1m4!1m3!1i16!2i18746!3i34974!1m4!1m3!1i16!2i18746!3i34975!1m4!1m3!1i16!2i18747!3i34974!1m4!1m3!1i16!2i18747!3i34975!1m4!1m3!1i16!2i18748!3i34973!1m4!1m3!1i16!2i18749!3i34973!1m4!1m3!1i16!2i18748!3i34974!1m4!1m3!1i16!2i18748!3i34975!1m4!1m3!1i16!2i18749!3i34974!1m4!1m3!1i16!2i18749!3i34975!1m4!1m3!1i16!2i18750!3i34973!1m4!1m3!1i16!2i18751!3i34973!1m4!1m3!1i16!2i18750!3i34974!1m4!1m3!1i16!2i18750!3i34975!1m4!1m3!1i16!2i18751!3i34974!1m4!1m3!1i16!2i18751!3i34975!1m4!1m3!1i16!2i18746!3i34976!1m4!1m3!1i16!2i18747!3i34976!1m4!1m3!1i16!2i18748!3i34976!1m4!1m3!1i16!2i18749!3i34976!1m4!1m3!1i16!2i18750!3i34976!1m4!1m3!1i16!2i18751!3i34976!2m3!1e0!2sm!3i589319862!3m12!2ses!3sUS!5e18!12m4!1e68!2m2!1sset!2sRoadmap!12m3!1e37!2m1!1ssmartmaps!4e3!12m1!5b1&callback=_xdc_._l1ydzy&key=AIzaSyAWPokAejBaeyIOSzvNWaDFDWgcVmCPZxo&token=15375"

# url = "https://www.google.com/maps/place/Lucky+Dhaba/@30.653792,76.8165233,17z/data=!3m1!4b1!4m5!3m4!1s0x390feb3e3de1a031:0x862036ab85567f75!8m2!3d30.653792!4d76.818712"



browser.get(url)


'''
# review titles / username / Person who reviews

review_titles = browser.find_elements_by_class_name("section-review-title")

print([a.text for a in review_titles])

# review text / what did they think

review_text = browser.find_elements_by_class_name("section-review-review-content")

print([a.text for a in review_text])

# get the number of stars

stars = browser.find_elements_by_class_name("section-review-stars")

first_review_stars = stars[0]

active_stars = first_review_stars.find_elements_by_class_name("section-review-star-active")

print(f"the stars the first review got was {len(active_stars)}")
'''