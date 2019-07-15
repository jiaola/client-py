#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/OperationOutcome) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import domainresource

from . import domainresource

@dataclass
class OperationOutcome(domainresource.DomainResource):
    """ Information about the success/failure of an action.

    A collection of error, warning, or information messages that result from a
    system action.
    """
    resource_type: ClassVar[str] = "OperationOutcome"
    issue: List[ OperationOutcomeIssue] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(OperationOutcome, self).elementProperties()
        js.extend([
            ("issue", "issue", OperationOutcomeIssue, True, None, True),
        ])
        return js

from . import backboneelement

@dataclass
class OperationOutcomeIssue(backboneelement.BackboneElement):
    """ A single issue associated with the action.

    An error, warning, or information message that results from a system
    action.
    """
    resource_type: ClassVar[str] = "OperationOutcomeIssue"
    code: str = None
    details: Optional[codeableconcept.CodeableConcept] = None
    diagnostics: Optional[str] = None
    expression: Optional[List[str]] = empty_list()
    location: Optional[List[str]] = empty_list()
    severity: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(OperationOutcomeIssue, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("details", "details", codeableconcept.CodeableConcept, False, None, False),
            ("diagnostics", "diagnostics", str, False, None, False),
            ("expression", "expression", str, True, None, False),
            ("location", "location", str, True, None, False),
            ("severity", "severity", str, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']