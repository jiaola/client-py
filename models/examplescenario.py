#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ExampleScenario) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import contactdetail
from . import domainresource
from . import fhirdate
from . import identifier
from . import usagecontext

from . import backboneelement

@dataclass
class ExampleScenarioProcessStepOperation(backboneelement.BackboneElement):
    """ Each interaction or action.
    """
    resource_type: ClassVar[str] = "ExampleScenarioProcessStepOperation"
    description: Optional[str] = None
    initiator: Optional[str] = None
    initiatorActive: Optional[bool] = None
    name: Optional[str] = None
    number: str = None
    receiver: Optional[str] = None
    receiverActive: Optional[bool] = None
    request: Optional[ExampleScenarioInstanceContainedInstance] = None
    response: Optional[ExampleScenarioInstanceContainedInstance] = None
    type: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExampleScenarioProcessStepOperation, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("initiator", "initiator", str, False, None, False),
            ("initiatorActive", "initiatorActive", bool, False, None, False),
            ("name", "name", str, False, None, False),
            ("number", "number", str, False, None, True),
            ("receiver", "receiver", str, False, None, False),
            ("receiverActive", "receiverActive", bool, False, None, False),
            ("request", "request", ExampleScenarioInstanceContainedInstance, False, None, False),
            ("response", "response", ExampleScenarioInstanceContainedInstance, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js

@dataclass
class ExampleScenarioProcessStepAlternative(backboneelement.BackboneElement):
    """ Alternate non-typical step action.

    Indicates an alternative step that can be taken instead of the operations
    on the base step in exceptional/atypical circumstances.
    """
    resource_type: ClassVar[str] = "ExampleScenarioProcessStepAlternative"
    description: Optional[str] = None
    step: Optional[List[ExampleScenarioProcessStep]] = empty_list()
    title: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExampleScenarioProcessStepAlternative, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("step", "step", ExampleScenarioProcessStep, True, None, False),
            ("title", "title", str, False, None, True),
        ])
        return js

@dataclass
class ExampleScenarioProcessStep(backboneelement.BackboneElement):
    """ Each step of the process.
    """
    resource_type: ClassVar[str] = "ExampleScenarioProcessStep"
    alternative: Optional[List[ExampleScenarioProcessStepAlternative]] = empty_list()
    operation: Optional[ExampleScenarioProcessStepOperation] = None
    pause: Optional[bool] = None
    process: Optional[List[ExampleScenarioProcess]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExampleScenarioProcessStep, self).elementProperties()
        js.extend([
            ("alternative", "alternative", ExampleScenarioProcessStepAlternative, True, None, False),
            ("operation", "operation", ExampleScenarioProcessStepOperation, False, None, False),
            ("pause", "pause", bool, False, None, False),
            ("process", "process", ExampleScenarioProcess, True, None, False),
        ])
        return js

@dataclass
class ExampleScenarioProcess(backboneelement.BackboneElement):
    """ Each major process - a group of operations.
    """
    resource_type: ClassVar[str] = "ExampleScenarioProcess"
    description: Optional[str] = None
    postConditions: Optional[str] = None
    preConditions: Optional[str] = None
    step: Optional[List[ExampleScenarioProcessStep]] = empty_list()
    title: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExampleScenarioProcess, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("postConditions", "postConditions", str, False, None, False),
            ("preConditions", "preConditions", str, False, None, False),
            ("step", "step", ExampleScenarioProcessStep, True, None, False),
            ("title", "title", str, False, None, True),
        ])
        return js

@dataclass
class ExampleScenarioInstanceVersion(backboneelement.BackboneElement):
    """ A specific version of the resource.
    """
    resource_type: ClassVar[str] = "ExampleScenarioInstanceVersion"
    description: str = None
    versionId: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExampleScenarioInstanceVersion, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("versionId", "versionId", str, False, None, True),
        ])
        return js

@dataclass
class ExampleScenarioInstanceContainedInstance(backboneelement.BackboneElement):
    """ Resources contained in the instance.

    Resources contained in the instance (e.g. the observations contained in a
    bundle).
    """
    resource_type: ClassVar[str] = "ExampleScenarioInstanceContainedInstance"
    resourceId: str = None
    versionId: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExampleScenarioInstanceContainedInstance, self).elementProperties()
        js.extend([
            ("resourceId", "resourceId", str, False, None, True),
            ("versionId", "versionId", str, False, None, False),
        ])
        return js

@dataclass
class ExampleScenarioInstance(backboneelement.BackboneElement):
    """ Each resource and each version that is present in the workflow.
    """
    resource_type: ClassVar[str] = "ExampleScenarioInstance"
    containedInstance: Optional[List[ExampleScenarioInstanceContainedInstance]] = empty_list()
    description: Optional[str] = None
    name: Optional[str] = None
    resourceId: str = None
    resourceType: str = None
    version: Optional[List[ExampleScenarioInstanceVersion]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExampleScenarioInstance, self).elementProperties()
        js.extend([
            ("containedInstance", "containedInstance", ExampleScenarioInstanceContainedInstance, True, None, False),
            ("description", "description", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("resourceId", "resourceId", str, False, None, True),
            ("resourceType", "resourceType", str, False, None, True),
            ("version", "version", ExampleScenarioInstanceVersion, True, None, False),
        ])
        return js

@dataclass
class ExampleScenarioActor(backboneelement.BackboneElement):
    """ Actor participating in the resource.
    """
    resource_type: ClassVar[str] = "ExampleScenarioActor"
    actorId: str = None
    description: Optional[str] = None
    name: Optional[str] = None
    type: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExampleScenarioActor, self).elementProperties()
        js.extend([
            ("actorId", "actorId", str, False, None, True),
            ("description", "description", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js

from . import domainresource

@dataclass
class ExampleScenario(domainresource.DomainResource):
    """ Example of workflow instance.
    """
    resource_type: ClassVar[str] = "ExampleScenario"
    actor: Optional[List[ExampleScenarioActor]] = empty_list()
    contact: Optional[List[contactdetail.ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date: Optional[fhirdate.FHIRDate] = None
    experimental: Optional[bool] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    instance: Optional[List[ExampleScenarioInstance]] = empty_list()
    jurisdiction: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    name: Optional[str] = None
    process: Optional[List[ExampleScenarioProcess]] = empty_list()
    publisher: Optional[str] = None
    purpose: Optional[str] = None
    status: str = None
    url: Optional[str] = None
    useContext: Optional[List[usagecontext.UsageContext]] = empty_list()
    version: Optional[str] = None
    workflow: Optional[List[str]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExampleScenario, self).elementProperties()
        js.extend([
            ("actor", "actor", ExampleScenarioActor, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instance", "instance", ExampleScenarioInstance, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, False),
            ("process", "process", ExampleScenarioProcess, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
            ("workflow", "workflow", str, True, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']