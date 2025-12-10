def showName(name):
    try:
        assert isinstance(name, str), 'Name must be a string'
        print("Name is:", name)
    except AssertionError as e:
        print('Error:', e)
    finally:
        print("Execution completed.")
    
name = 123
# name = "Alice"
showName(name)