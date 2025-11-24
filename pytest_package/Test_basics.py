
# def login():
#     print('login execution')
#
# def logout():
#     print('logout execution')
#
# login()
# logout()

# to execute the function,we should give the function call.

# class Sample:
#
#     def login(self):
#         print('login execution')
#
#     def logout(self):
#         print('logout execution')
#
# sample_obj = Sample()
# sample_obj.login()
# sample_obj.logout()


#####################################################################
'''
Pytest  :   It is a unit testing framework.
            Testing the small portion of the entire code, we call it as unit testing.
            To perform unit testing in selenium we will go for Pytest

            To install pytest
            Go to command prompt -->    pip install pytest

            RULES
            *   The file_name should always start with test_
                Eg  :   test_filename.py
            *   The function names also should start with test_
                Eg  :   def test_funcname():
                            pass
            *   The class names should start with Test
                Eg  :   class TestClassName:
                            pass

            Pytest will automatically recognize the files, functions and the classes which are following the pytest rules.
            So, without giving the function call, we can execute the functions and without creating the objects and
                without calling the attributes, we can execute the classes

            To execute the pytest file
            Right click anywhere on the test_file --> open in --> terminal --> pytest test_filename.py -vs
                -v  --> Verbosity. This gives the detailed explanation about the code.
                -s  --> Scripting. This prints all the print statements

'''
from logging import exception


# def test_login():
#     print('login execution')
#
# def test_logout():
#     print('logout execution')


######################################################################################

# def test_login():
#     print('login execution')
#
# def signup():
#     print('signup execution')
#
# def test_signup():
#     print('signup execution')
#
#
# def test_logout():
#     print('logout execution')
#
# ''' here signup doesn't execute because it is not following the pytest rules.
# pytest doesnot recognize the function which are not following the rules.
# '''
################################################################################################

# def test_login():
#     print('login execution')
#     def test_logout():
#         print('logout execution')

''' in case of nested function pytest cannot recognize the inner test function.
it only recognize the outer test function.
'''


############################################################################################

# def test_login():
#     raise Exception
# def test_signup():
#     print('signup execution')
# def test_logout():
#     print('logout execution')
''' error in one test case doesn't affect the other test cases.
'''


############################################################################################

# def test_login():
#     print('login execution')
#
# def test_signup():
#     print('signup execution')
#
# def test_logout():
#     print('logout execution')
#
# test_login()
# test_signup()
# test_logout()

''' when we call the  function ,then execution will happens 2 times.
'''

##############################################################################################

# def add(a,b):
#     print(a+b)

# def test_add(a,b):
#     print(a+b)    ####### it will through error if we use parameter.

''' test function doesn't take any parameter
'''


############################################################################################
## with multiple funtions with the same name.
# def test_greet():
#     print('hallo vibha')
#
# def test_greet():
#     print('hallo piku')

''' if are having multiple test funtions with the same name then pytest will consider always the latest ourance.
'''


###########################################################################################

# class Sample:
#     def test_login(self):
#         print('login execution')
#     def test_signup(self):
#         print('signup execution')
#     def test_logout(self):
#         print('logout execution')
# ''' here class is not following the pytest rules. so i am getting 0 execution as a result.
# '''
# class TestSample:
#     def test_login(self):
#         print('login execution')
#     def test_signup(self):
#         print('signup execution')
#     def test_logout(self):
#         print('logout execution')

''' if the class doesn't follow the pytest rule then i will get the 0 execution , but when the class follows the pytest 
rules then i will get 3 execution.
'''
###############################################################################################

# class TestSample:
#     def login(self):
#         print('login execution')
#     def signup(self):
#         print('signup execution')
#     def logout(self):
#         print('logout execution')

''' here i am getting 0 execution because the attributes are not following the pytest rules.
'''

#################################################################################################

# class TestSample:
#     def test_login(self):
#         print('login execution')
#
#     def test_signup(self):
#         print('signup execution')
#
#     def test_logout(self):
#         print('logout execution')
#
# s = TestSample()
# s.test_login()
# s.test_signup()
# s.test_logout()

''' if we call the function then execution happens 2 times.
'''
#################################################################################################

# class TestSample:
#     def test_login(self):
#         print('login execution')
#
#     def test_signup(self):
#         pri('signup execution')
#
#     def test_logout(self):
#         print('logout execution')

''' if there is error in one test case it will not affect the other test cases.
'''
##################################################################################

# class TestSample:
#     def test_login(self,name):
#         print('')

'''
test_methods also donot take any parameters 
'''

######################################################################################

class TestSample:

    def __int__(self):
        pass

    def test_login(self):
        print('login execution')

    def test_logout(self):
        print('logout execution')

''' PytestCollectionWarning: cannot collect test class 'TestSample' because it has a __init__ constructor
'''
######################################################################################

# def test_login():
#     print('login execution')
#
# def test_logout():
#     print('logout execution')

