#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Procedure) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .age import Age
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .range import Range


@dataclass
class ProcedurePerformer(BackboneElement):
    """ The people who performed the procedure.

    Limited to "real" people rather than equipment.
    """
    resource_type: ClassVar[str] = "ProcedurePerformer"
    actor: FHIRReference = None
    function: Optional[CodeableConcept] = None
    onBehalfOf: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(ProcedurePerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", FHIRReference, False, None, True),
            ("function", "function", CodeableConcept, False, None, False),
            ("onBehalfOf", "onBehalfOf", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class ProcedureFocalDevice(BackboneElement):
    """ Manipulated, implanted, or removed device.

    A device that is implanted, removed or otherwise manipulated (calibration,
    battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as
    a focal portion of the Procedure.
    """
    resource_type: ClassVar[str] = "ProcedureFocalDevice"
    action: Optional[CodeableConcept] = None
    manipulated: FHIRReference = None

    def elementProperties(self):
        js = super(ProcedureFocalDevice, self).elementProperties()
        js.extend([
            ("action", "action", CodeableConcept, False, None, False),
            ("manipulated", "manipulated", FHIRReference, False, None, True),
        ])
        return js


@dataclass
class Procedure(DomainResource):
    """ An action that is being or was performed on a patient.

    An action that is or was performed on or for a patient. This can be a
    physical intervention like an operation, or less invasive like long term
    services, counseling, or hypnotherapy.
    """
    resource_type: ClassVar[str] = "Procedure"
    asserter: Optional[FHIRReference] = None
    basedOn: Optional[List[FHIRReference]] = empty_list()
    bodySite: Optional[List[CodeableConcept]] = empty_list()
    category: Optional[CodeableConcept] = None
    code: Optional[CodeableConcept] = None
    complication: Optional[List[CodeableConcept]] = empty_list()
    complicationDetail: Optional[List[FHIRReference]] = empty_list()
    encounter: Optional[FHIRReference] = None
    focalDevice: Optional[List[ProcedureFocalDevice]] = empty_list()
    followUp: Optional[List[CodeableConcept]] = empty_list()
    identifier: Optional[List[Identifier]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    location: Optional[FHIRReference] = None
    note: Optional[List[Annotation]] = empty_list()
    outcome: Optional[CodeableConcept] = None
    partOf: Optional[List[FHIRReference]] = empty_list()
    performedAge: Optional[Age] = None
    performedDateTime: Optional[FHIRDate] = None
    performedPeriod: Optional[Period] = None
    performedRange: Optional[Range] = None
    performedString: Optional[str] = None
    performer: Optional[List[ProcedurePerformer]] = empty_list()
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    recorder: Optional[FHIRReference] = None
    report: Optional[List[FHIRReference]] = empty_list()
    status: str = None
    statusReason: Optional[CodeableConcept] = None
    subject: FHIRReference = None
    usedCode: Optional[List[CodeableConcept]] = empty_list()
    usedReference: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(Procedure, self).elementProperties()
        js.extend([
            ("asserter", "asserter", FHIRReference, False, None, False),
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("bodySite", "bodySite", CodeableConcept, True, None, False),
            ("category", "category", CodeableConcept, False, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("complication", "complication", CodeableConcept, True, None, False),
            ("complicationDetail", "complicationDetail", FHIRReference, True, None, False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("focalDevice", "focalDevice", ProcedureFocalDevice, True, None, False),
            ("followUp", "followUp", CodeableConcept, True, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("location", "location", FHIRReference, False, None, False),
            ("note", "note", Annotation, True, None, False),
            ("outcome", "outcome", CodeableConcept, False, None, False),
            ("partOf", "partOf", FHIRReference, True, None, False),
            ("performedAge", "performedAge", Age, False, "performed", False),
            ("performedDateTime", "performedDateTime", FHIRDate, False, "performed", False),
            ("performedPeriod", "performedPeriod", Period, False, "performed", False),
            ("performedRange", "performedRange", Range, False, "performed", False),
            ("performedString", "performedString", str, False, "performed", False),
            ("performer", "performer", ProcedurePerformer, True, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("recorder", "recorder", FHIRReference, False, None, False),
            ("report", "report", FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", CodeableConcept, False, None, False),
            ("subject", "subject", FHIRReference, False, None, True),
            ("usedCode", "usedCode", CodeableConcept, True, None, False),
            ("usedReference", "usedReference", FHIRReference, True, None, False),
        ])
        return js