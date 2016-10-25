from routes import index, version

def test_index():
    v = index()
    parts = v.split(" ")
    assert parts[2] == version


######################################
## IF you want to make the unit tests fail.
## Uncomment the following test case
#####################################

# def test_make_you_fail():
#     v = index()
#     parts = v.split(" ")
#     assert parts[1] == version
