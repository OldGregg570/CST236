import inspect
modules = ['behave', 'coverage', 'docutils', 'matplotlib', 'mock', 'nose2', 'numpy', 'pip', 'pywinauto', 'radon']


def test_all_local_modules():
    """ Import/check each module """
    try:
        mods = map(__import__, modules)
    except Exception:
        exit("importing modules raised ExceptionType unexpectedly!")

    for module in mods:
        interface = vars(module)
        for element in interface:
            member = getattr(module, element)

            """ create/check each class """
            if inspect.isclass(element):
                member.__init__()
            """ create/check each function """
            if inspect.isfunction(element):
                print member
                try:
                    member()
                except Exception:
                    exit("Call to " + str(element) + " failed")

"""
tests a list of locally installed python modules.
 Finding modules using pip module was bringing up things like Sphynx
 and other command line utilities, so I made this a static list
 """
test_all_local_modules()