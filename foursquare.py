import sys
import time
from ghost import Ghost
ghost = Ghost(user_agent='Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7', viewport_size = (320, 480) )

username = ''
password = ''
placename = ''

if len(sys.argv) != 4:
	print 'Params: username password placename'
	exit(2)
else:
	username = sys.argv[1]
	password = sys.argv[2]
	placename = sys.argv[3]


print "Status: 1"

page, resources = ghost.open('https://foursquare.com/mobile/login?continue=%2Fmobile%2F')
ghost.wait_for_page_loaded()

print "Status: 2"
result, resources = ghost.set_field_value("input[name=username]", username)
result, resources = ghost.set_field_value("input[name=password]", password)
page, resources = ghost.fire_on("form", "submit", expect_loading=True)
ghost.wait_for_page_loaded()


print "Status: 3"
page, resources = ghost.open('https://foursquare.com/mobile/checkin')
ghost.wait_for_page_loaded()


print "Status: 4"
result, resources = ghost.set_field_value("input[name=q]", placename)
page, resources = ghost.fire_on("form", "submit", expect_loading=True)
ghost.wait_for_page_loaded()


print "Status: 5"

ghost.click('div.venue_block > a:first-child')
ghost.wait_for_page_loaded()

print "Status: 6"

ghost.click("input[value='check in']", expect_loading=True)
time.sleep(10)
#ghost.wait_for_page_loaded()

