#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Procedure) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import age
from . import annotation
from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import range

from . import domainresource

@dataclass
class Procedure(domainresource.DomainResource):
    """ An action that is being or was performed on a patient.

    An action that is or was performed on or for a patient. This can be a
    physical intervention like an operation, or less invasive like long term
    services, counseling, or hypnotherapy.
    """
    resource_type: ClassVar[str] = "Procedure"
    asserter: Optional[fhirreference.FHIRReference] = None
    basedOn: Optional[List[fhirreference.FHIRReference]] = empty_list()
    bodySite: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    category: Optional[codeableconcept.CodeableConcept] = None
    code: Optional[codeableconcept.CodeableConcept] = None
    complication: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    complicationDetail: Optional[List[fhirreference.FHIRReference]] = empty_list()
    encounter: Optional[fhirreference.FHIRReference] = None
    focalDevice: Optional[List[ProcedureFocalDevice]] = empty_list()
    followUp: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    location: Optional[fhirreference.FHIRReference] = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    outcome: Optional[codeableconcept.CodeableConcept] = None
    partOf: Optional[List[fhirreference.FHIRReference]] = empty_list()
    performedAge: Optional[age.Age] = None
    performedDateTime: Optional[fhirdate.FHIRDate] = None
    performedPeriod: Optional[period.Period] = None
    performedRange: Optional[range.Range] = None
    performedString: Optional[str] = None
    performer: Optional[List[ProcedurePerformer]] = empty_list()
    reasonCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    reasonReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    recorder: Optional[fhirreference.FHIRReference] = None
    report: Optional[List[fhirreference.FHIRReference]] = empty_list()
    status: str = None
    statusReason: Optional[codeableconcept.CodeableConcept] = None
    subject:fhirreference.FHIRReference = None
    usedCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    usedReference: Optional[List[fhirreference.FHIRReference]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Procedure, self).elementProperties()
        js.extend([
            ("asserter", "asserter", fhirreference.FHIRReference, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("complication", "complication", codeableconcept.CodeableConcept, True, None, False),
            ("complicationDetail", "complicationDetail", fhirreference.FHIRReference, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("focalDevice", "focalDevice", ProcedureFocalDevice, True, None, False),
            ("followUp", "followUp", codeableconcept.CodeableConcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("performedAge", "performedAge", age.Age, False, "performed", False),
            ("performedDateTime", "performedDateTime", fhirdate.FHIRDate, False, "performed", False),
            ("performedPeriod", "performedPeriod", period.Period, False, "performed", False),
            ("performedRange", "performedRange", range.Range, False, "performed", False),
            ("performedString", "performedString", str, False, "performed", False),
            ("performer", "performer", ProcedurePerformer, True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("recorder", "recorder", fhirreference.FHIRReference, False, None, False),
            ("report", "report", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("usedCode", "usedCode", codeableconcept.CodeableConcept, True, None, False),
            ("usedReference", "usedReference", fhirreference.FHIRReference, True, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class ProcedureFocalDevice(backboneelement.BackboneElement):
    """ Manipulated, implanted, or removed device.

    A device that is implanted, removed or otherwise manipulated (calibration,
    battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as
    a focal portion of the Procedure.
    """
    resource_type: ClassVar[str] = "ProcedureFocalDevice"
    action: Optional[codeableconcept.CodeableConcept] = None
    manipulated:fhirreference.FHIRReference = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ProcedureFocalDevice, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, False, None, False),
            ("manipulated", "manipulated", fhirreference.FHIRReference, False, None, True),
        ])
        return js

@dataclass
class ProcedurePerformer(backboneelement.BackboneElement):
    """ The people who performed the procedure.

    Limited to "real" people rather than equipment.
    """
    resource_type: ClassVar[str] = "ProcedurePerformer"
    actor:fhirreference.FHIRReference = None
    function: Optional[codeableconcept.CodeableConcept] = None
    onBehalfOf: Optional[fhirreference.FHIRReference] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ProcedurePerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("function", "function", codeableconcept.CodeableConcept, False, None, False),
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, False, None, False),
        ])
        return js


import sys
try:
    from . import age
except ImportError:
    age = sys.modules[__package__ + '.age']
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
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
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']