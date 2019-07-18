#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/AllergyIntolerance) on 2019-07-18.
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

from . import backboneelement

@dataclass
class AllergyIntoleranceReaction(backboneelement.BackboneElement):
    """ Adverse Reaction Events linked to exposure to substance.

    Details about each adverse reaction event linked to exposure to the
    identified substance.
    """
    resource_type: ClassVar[str] = "AllergyIntoleranceReaction"
    description: Optional[str] = None
    exposureRoute: Optional[codeableconcept.CodeableConcept] = None
    manifestation: List[codeableconcept.CodeableConcept] = empty_list()
    note: Optional[List[annotation.Annotation]] = empty_list()
    onset: Optional[fhirdate.FHIRDate] = None
    severity: Optional[str] = None
    substance: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(AllergyIntoleranceReaction, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("exposureRoute", "exposureRoute", codeableconcept.CodeableConcept, False, None, False),
            ("manifestation", "manifestation", codeableconcept.CodeableConcept, True, None, True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("onset", "onset", fhirdate.FHIRDate, False, None, False),
            ("severity", "severity", str, False, None, False),
            ("substance", "substance", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

from . import domainresource

@dataclass
class AllergyIntolerance(domainresource.DomainResource):
    """ Allergy or Intolerance (generally: Risk of adverse reaction to a substance).

    Risk of harmful or undesirable, physiological response which is unique to
    an individual and associated with exposure to a substance.
    """
    resource_type: ClassVar[str] = "AllergyIntolerance"
    asserter: Optional[fhirreference.FHIRReference] = None
    category: Optional[List[str]] = empty_list()
    clinicalStatus: Optional[codeableconcept.CodeableConcept] = None
    code: Optional[codeableconcept.CodeableConcept] = None
    criticality: Optional[str] = None
    encounter: Optional[fhirreference.FHIRReference] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    lastOccurrence: Optional[fhirdate.FHIRDate] = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    onsetAge: Optional[age.Age] = None
    onsetDateTime: Optional[fhirdate.FHIRDate] = None
    onsetPeriod: Optional[period.Period] = None
    onsetRange: Optional[range.Range] = None
    onsetString: Optional[str] = None
    patient:fhirreference.FHIRReference = None
    reaction: Optional[List[AllergyIntoleranceReaction]] = empty_list()
    recordedDate: Optional[fhirdate.FHIRDate] = None
    recorder: Optional[fhirreference.FHIRReference] = None
    type: Optional[str] = None
    verificationStatus: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(AllergyIntolerance, self).elementProperties()
        js.extend([
            ("asserter", "asserter", fhirreference.FHIRReference, False, None, False),
            ("category", "category", str, True, None, False),
            ("clinicalStatus", "clinicalStatus", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("criticality", "criticality", str, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("lastOccurrence", "lastOccurrence", fhirdate.FHIRDate, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("onsetAge", "onsetAge", age.Age, False, "onset", False),
            ("onsetDateTime", "onsetDateTime", fhirdate.FHIRDate, False, "onset", False),
            ("onsetPeriod", "onsetPeriod", period.Period, False, "onset", False),
            ("onsetRange", "onsetRange", range.Range, False, "onset", False),
            ("onsetString", "onsetString", str, False, "onset", False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("reaction", "reaction", AllergyIntoleranceReaction, True, None, False),
            ("recordedDate", "recordedDate", fhirdate.FHIRDate, False, None, False),
            ("recorder", "recorder", fhirreference.FHIRReference, False, None, False),
            ("type", "type", str, False, None, False),
            ("verificationStatus", "verificationStatus", codeableconcept.CodeableConcept, False, None, False),
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