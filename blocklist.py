# This file just contaisn the blocklist of the JWT tokents. 
# It will be imported by app and the logout resource so that tokens 
# can be added to the blocklsit when the user logs out

# Better to use a db for blocklist rather than a python set
BLOCKLIST = set()