#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Immunization) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity

from . import backboneelement

@dataclass
class ImmunizationReaction(backboneelement.BackboneElement):
    """ Details of a reaction that follows immunization.

    Categorical data indicating that an adverse event is associated in time to
    an immunization.
    """
    resource_type: ClassVar[str] = "ImmunizationReaction"
    date: Optional[fhirdate.FHIRDate] = None
    detail: Optional[fhirreference.FHIRReference] = None
    reported: Optional[bool] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ImmunizationReaction, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("detail", "detail", fhirreference.FHIRReference, False, None, False),
            ("reported", "reported", bool, False, None, False),
        ])
        return js

@dataclass
class ImmunizationProtocolApplied(backboneelement.BackboneElement):
    """ Protocol followed by the provider.

    The protocol (set of recommendations) being followed by the provider who
    administered the dose.
    """
    resource_type: ClassVar[str] = "ImmunizationProtocolApplied"
    authority: Optional[fhirreference.FHIRReference] = None
    doseNumberPositiveInt: int = None
    doseNumberString: str = None
    series: Optional[str] = None
    seriesDosesPositiveInt: Optional[int] = None
    seriesDosesString: Optional[str] = None
    targetDisease: Optional[List[codeableconcept.CodeableConcept]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ImmunizationProtocolApplied, self).elementProperties()
        js.extend([
            ("authority", "authority", fhirreference.FHIRReference, False, None, False),
            ("doseNumberPositiveInt", "doseNumberPositiveInt", int, False, "doseNumber", True),
            ("doseNumberString", "doseNumberString", str, False, "doseNumber", True),
            ("series", "series", str, False, None, False),
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", int, False, "seriesDoses", False),
            ("seriesDosesString", "seriesDosesString", str, False, "seriesDoses", False),
            ("targetDisease", "targetDisease", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js

@dataclass
class ImmunizationPerformer(backboneelement.BackboneElement):
    """ Who performed event.

    Indicates who performed the immunization event.
    """
    resource_type: ClassVar[str] = "ImmunizationPerformer"
    actor:fhirreference.FHIRReference = None
    function: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ImmunizationPerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("function", "function", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class ImmunizationEducation(backboneelement.BackboneElement):
    """ Educational material presented to patient.

    Educational material presented to the patient (or guardian) at the time of
    vaccine administration.
    """
    resource_type: ClassVar[str] = "ImmunizationEducation"
    documentType: Optional[str] = None
    presentationDate: Optional[fhirdate.FHIRDate] = None
    publicationDate: Optional[fhirdate.FHIRDate] = None
    reference: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ImmunizationEducation, self).elementProperties()
        js.extend([
            ("documentType", "documentType", str, False, None, False),
            ("presentationDate", "presentationDate", fhirdate.FHIRDate, False, None, False),
            ("publicationDate", "publicationDate", fhirdate.FHIRDate, False, None, False),
            ("reference", "reference", str, False, None, False),
        ])
        return js

from . import domainresource

@dataclass
class Immunization(domainresource.DomainResource):
    """ Immunization event information.

    Describes the event of a patient being administered a vaccine or a record
    of an immunization as reported by a patient, a clinician or another party.
    """
    resource_type: ClassVar[str] = "Immunization"
    doseQuantity: Optional[quantity.Quantity] = None
    education: Optional[List[ImmunizationEducation]] = empty_list()
    encounter: Optional[fhirreference.FHIRReference] = None
    expirationDate: Optional[fhirdate.FHIRDate] = None
    fundingSource: Optional[codeableconcept.CodeableConcept] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    isSubpotent: Optional[bool] = None
    location: Optional[fhirreference.FHIRReference] = None
    lotNumber: Optional[str] = None
    manufacturer: Optional[fhirreference.FHIRReference] = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    occurrenceDateTime:fhirdate.FHIRDate = None
    occurrenceString: str = None
    patient:fhirreference.FHIRReference = None
    performer: Optional[List[ImmunizationPerformer]] = empty_list()
    primarySource: Optional[bool] = None
    programEligibility: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    protocolApplied: Optional[List[ImmunizationProtocolApplied]] = empty_list()
    reaction: Optional[List[ImmunizationReaction]] = empty_list()
    reasonCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    reasonReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    recorded: Optional[fhirdate.FHIRDate] = None
    reportOrigin: Optional[codeableconcept.CodeableConcept] = None
    route: Optional[codeableconcept.CodeableConcept] = None
    site: Optional[codeableconcept.CodeableConcept] = None
    status: str = None
    statusReason: Optional[codeableconcept.CodeableConcept] = None
    subpotentReason: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    vaccineCode:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Immunization, self).elementProperties()
        js.extend([
            ("doseQuantity", "doseQuantity", quantity.Quantity, False, None, False),
            ("education", "education", ImmunizationEducation, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("expirationDate", "expirationDate", fhirdate.FHIRDate, False, None, False),
            ("fundingSource", "fundingSource", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("isSubpotent", "isSubpotent", bool, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("lotNumber", "lotNumber", str, False, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", True),
            ("occurrenceString", "occurrenceString", str, False, "occurrence", True),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("performer", "performer", ImmunizationPerformer, True, None, False),
            ("primarySource", "primarySource", bool, False, None, False),
            ("programEligibility", "programEligibility", codeableconcept.CodeableConcept, True, None, False),
            ("protocolApplied", "protocolApplied", ImmunizationProtocolApplied, True, None, False),
            ("reaction", "reaction", ImmunizationReaction, True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("recorded", "recorded", fhirdate.FHIRDate, False, None, False),
            ("reportOrigin", "reportOrigin", codeableconcept.CodeableConcept, False, None, False),
            ("route", "route", codeableconcept.CodeableConcept, False, None, False),
            ("site", "site", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("subpotentReason", "subpotentReason", codeableconcept.CodeableConcept, True, None, False),
            ("vaccineCode", "vaccineCode", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


import sys
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']