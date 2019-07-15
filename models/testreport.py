#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/TestReport) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier

from . import domainresource

@dataclass
class TestReport(domainresource.DomainResource):
    """ Describes the results of a TestScript execution.

    A summary of information based on the results of executing a TestScript.
    """
    resource_type: ClassVar[str] = "TestReport"
    identifier: Optional[identifier.Identifier] = None
    issued: Optional[fhirdate.FHIRDate] = None
    name: Optional[str] = None
    participant: Optional[List[TestReportParticipant]] = empty_list()
    result: str = None
    score: Optional[float] = None
    setup: Optional[TestReportSetup] = None
    status: str = None
    teardown: Optional[TestReportTeardown] = None
    test: Optional[List[TestReportTest]] = empty_list()
    testScript:fhirreference.FHIRReference = None
    tester: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(TestReport, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("issued", "issued", fhirdate.FHIRDate, False, None, False),
            ("name", "name", str, False, None, False),
            ("participant", "participant", TestReportParticipant, True, None, False),
            ("result", "result", str, False, None, True),
            ("score", "score", float, False, None, False),
            ("setup", "setup", TestReportSetup, False, None, False),
            ("status", "status", str, False, None, True),
            ("teardown", "teardown", TestReportTeardown, False, None, False),
            ("test", "test", TestReportTest, True, None, False),
            ("testScript", "testScript", fhirreference.FHIRReference, False, None, True),
            ("tester", "tester", str, False, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class TestReportParticipant(backboneelement.BackboneElement):
    """ A participant in the test execution, either the execution engine, a client,
    or a server.
    """
    resource_type: ClassVar[str] = "TestReportParticipant"
    display: Optional[str] = None
    type: str = None
    uri: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(TestReportParticipant, self).elementProperties()
        js.extend([
            ("display", "display", str, False, None, False),
            ("type", "type", str, False, None, True),
            ("uri", "uri", str, False, None, True),
        ])
        return js

@dataclass
class TestReportSetup(backboneelement.BackboneElement):
    """ The results of the series of required setup operations before the tests
    were executed.
    """
    resource_type: ClassVar[str] = "TestReportSetup"
    action: List[ TestReportSetupAction] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(TestReportSetup, self).elementProperties()
        js.extend([
            ("action", "action", TestReportSetupAction, True, None, True),
        ])
        return js

@dataclass
class TestReportSetupAction(backboneelement.BackboneElement):
    """ A setup operation or assert that was executed.

    Action would contain either an operation or an assertion.
    """
    resource_type: ClassVar[str] = "TestReportSetupAction"
    assert_fhir: Optional[TestReportSetupActionAssert] = None
    operation: Optional[TestReportSetupActionOperation] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(TestReportSetupAction, self).elementProperties()
        js.extend([
            ("assert_fhir", "assert", TestReportSetupActionAssert, False, None, False),
            ("operation", "operation", TestReportSetupActionOperation, False, None, False),
        ])
        return js

@dataclass
class TestReportSetupActionAssert(backboneelement.BackboneElement):
    """ The assertion to perform.

    The results of the assertion performed on the previous operations.
    """
    resource_type: ClassVar[str] = "TestReportSetupActionAssert"
    detail: Optional[str] = None
    message: Optional[str] = None
    result: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(TestReportSetupActionAssert, self).elementProperties()
        js.extend([
            ("detail", "detail", str, False, None, False),
            ("message", "message", str, False, None, False),
            ("result", "result", str, False, None, True),
        ])
        return js

@dataclass
class TestReportSetupActionOperation(backboneelement.BackboneElement):
    """ The operation to perform.

    The operation performed.
    """
    resource_type: ClassVar[str] = "TestReportSetupActionOperation"
    detail: Optional[str] = None
    message: Optional[str] = None
    result: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(TestReportSetupActionOperation, self).elementProperties()
        js.extend([
            ("detail", "detail", str, False, None, False),
            ("message", "message", str, False, None, False),
            ("result", "result", str, False, None, True),
        ])
        return js

@dataclass
class TestReportTeardown(backboneelement.BackboneElement):
    """ The results of running the series of required clean up steps.

    The results of the series of operations required to clean up after all the
    tests were executed (successfully or otherwise).
    """
    resource_type: ClassVar[str] = "TestReportTeardown"
    action: List[ TestReportTeardownAction] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(TestReportTeardown, self).elementProperties()
        js.extend([
            ("action", "action", TestReportTeardownAction, True, None, True),
        ])
        return js

@dataclass
class TestReportTeardownAction(backboneelement.BackboneElement):
    """ One or more teardown operations performed.

    The teardown action will only contain an operation.
    """
    resource_type: ClassVar[str] = "TestReportTeardownAction"
    operation: TestReportSetupActionOperation = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(TestReportTeardownAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestReportSetupActionOperation, False, None, True),
        ])
        return js

@dataclass
class TestReportTest(backboneelement.BackboneElement):
    """ A test executed from the test script.
    """
    resource_type: ClassVar[str] = "TestReportTest"
    action: List[ TestReportTestAction] = empty_list()
    description: Optional[str] = None
    name: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(TestReportTest, self).elementProperties()
        js.extend([
            ("action", "action", TestReportTestAction, True, None, True),
            ("description", "description", str, False, None, False),
            ("name", "name", str, False, None, False),
        ])
        return js

@dataclass
class TestReportTestAction(backboneelement.BackboneElement):
    """ A test operation or assert that was performed.

    Action would contain either an operation or an assertion.
    """
    resource_type: ClassVar[str] = "TestReportTestAction"
    assert_fhir: Optional[TestReportSetupActionAssert] = None
    operation: Optional[TestReportSetupActionOperation] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(TestReportTestAction, self).elementProperties()
        js.extend([
            ("assert_fhir", "assert", TestReportSetupActionAssert, False, None, False),
            ("operation", "operation", TestReportSetupActionOperation, False, None, False),
        ])
        return js


import sys
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']