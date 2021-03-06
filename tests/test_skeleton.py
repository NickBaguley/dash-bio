# pylint: disable=E,W,C,R
# flake8: noqa
import os
from selenium.webdriver.common.keys import Keys
from pytest_dash.wait_for import (
    wait_for_text_to_equal,
    wait_for_element_by_css_selector
)
from .test_common_features import (
    init_demo_app,
    template_test_component,
    template_test_python_component_prop,
    PROP_TYPES,
    COMPONENT_REACT_BASE
)

# define app name once
APP_NAME = os.path.basename(__file__).replace(
    'test_', '').replace(
        '.py', '').replace(
            '_', '-')

# pass/fail strings
PASS = 'PASSED'
FAIL = 'FAILED'

# define any custom strings here (e.g., if you use
# a particular CSS selector a lot, assign it to a
# variable)


# Demo app tests

@init_demo_app(APP_NAME)
def test_click_app_name_from_gallery(dash_threaded):
    """Test that clicking on the given app goes to the expected URL."""
    assert dash_threaded.driver.current_url.replace('http://localhost:8050', '').strip('/') == \
        'dash-bio/{}'.format(APP_NAME)


# below, write tests for initial conditions; they will most likely
# make use of wait_for_text_to_equal and other similar functions

@init_demo_app(APP_NAME)
def test_INITIALCONDITION(dash_threaded):
    """Test some initial condition here (e.g., that the correct dataset
    has been loaded).
    """
    pass
# below, write tests for interactions with the app (e.g., selecting a
# value from a dropdown or filling in some sort of input); they will
# most likely make use of send_keys


@init_demo_app(APP_NAME)
def test_CHANGESOMETHING(dash_threaded):
    """Test the results of changing something here (e.g., the value
    of a dropdown).
    """
    pass

# Component tests

# for React components, we need to define a way to interact with the
# props directly (instead of through a graph component); to that end,
# we define a callback method that defines how exactly a prop is
# updated
# this callback will be used in the simple test app, which consists of
# the component, a single button, and two inputs


def COMPONENTNAME_props_callback(
        nclicks,
        prop_name,
        prop_value,
        prop_type=None
):
    """This function is the code of a callback which is triggered by
    the button on the simple app used in the test.
    :param nclicks (int): The n_clicks value of the button in the
                          simple app.
    :param prop_name (string): The name of the property that is to be
                               modified.
    :param prop_value (string): The value that is to be assigned to the
                                prop defined by prop_name.
    :prop_type (string): One of the predefined types in PROP_TYPES.
    :return: The value that is to be assigned to the prop defined by
             prop_name, after casting it to the correct type.
    """

    typed_prop_value = None

    # avoid triggering this callback when the button is first created
    if nclicks is not None:
        # cast the string representation of the desired prop value
        # into the appropriate type

        if prop_type in PROP_TYPES:
            typed_prop_value = PROP_TYPES[prop_type](prop_value)

        # define any other "translations" from a string to a datatype
        # below; e.g.,
        # elif prop_type == 'list': typed_prop_value = ...

    return typed_prop_value


# below, write tests for changing the props of a Python component
# (following this basic structure)
def test_PROPNAME_0(dash_threaded):
    """Test that some prop updates correctly when changed, for a pure Python component."""

    def assert_callback(
            nclicks,
            component_PROPNAME,
            input_PROPNAME
    ):
        """Determine the pass/fail status of this test.

        :param nclicks (int): The n_clicks value of the button in the
                              simple test app (not used here).
        :param component_PROPNAME (string): The value of PROPNAME for the
                                            component after it is set.
        :param input_PROPNAME (string): The value of PROPNAME that is sent
                                        to the component.

        :return (string): 'PASSED' for a test that passed, or 'FAILED'
                          for a test that failed
        """
        # avoid triggering this callback when the button is first created
        if nclicks is not None:
            # check for the pass/fail condition here; this is a
            # shallow comparison, so write your own if necessary
            if component_PROPNAME == input_PROPNAME:
                return PASS

        return FAIL

    # replace "None" with a string that defines the type of the prop
    # (e.g., 'int', 'float', 'list')
    prop_type = None

    template_test_python_component_prop(
        dash_threaded,
        APP_NAME,
        assert_callback,
        COMPONENTNAME_test_props_callback,
        PROPNAME,
        input_PROPNAME,
        prop_type=prop_type,
        # add any arguments you want to send to your component,
        # e.g.,
        # sequence='GATTACA',
        # showLineNumbers=False
    )


# alternatively, write tests for changing the props of a React component
# (following this basic structure)
def test_PROPNAME_1(dash_threaded):
    """Test that some prop updates correctly when changed, for a React component."""

    def assert_callback(
            nclicks,
            component_PROPNAME,
            input_PROPNAME
    ):
        """Determine the pass/fail status of this test.

        :param nclicks (int): The n_clicks value of the button in the
                              simple test app (not used here).
        :param component_PROPNAME (string): The value of PROPNAME for the
                                            component after it is set.
        :param input_PROPNAME (string): The value of PROPNAME that is sent
                                        to the component.

        :return (string): 'PASSED' for a test that passed, or 'FAILED'
                          for a test that failed
        """
        # avoid triggering this callback when the button is first created
        if nclicks is not None:
            # check for the pass/fail condition here; this is a
            # shallow comparison, so write your own if necessary
            if component_PROPNAME == input_PROPNAME:
                return PASS

        return FAIL

    # replace "None" with a string that defines the type of the prop
    # (e.g., 'int', 'float', 'list')
    prop_type = None

    template_test_component(
        dash_threaded,
        APP_NAME,
        assert_callback,
        COMPONENTNAME_test_props_callback,
        PROPNAME,
        input_PROPNAME,
        prop_type=prop_type,
        component_base=COMPONENT_REACT_BASE
        # add any arguments you want to send to your component,
        # e.g.,
        # sequence='GATTACA',
        # showLineNumbers=False
    )

    driver = dash_threaded.driver

    # driver.find_elements_by_class_name('...')
    # assert something about this element (before changing it)

    # trigger change of the component prop
    btn = wait_for_element_by_css_selector(driver, '#test-{}-btn'.format(APP_NAME))
    btn.click()

    # assert something different about the element
