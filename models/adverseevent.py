#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/AdverseEvent) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier

from . import domainresource

@dataclass
class AdverseEvent(domainresource.DomainResource):
    """ Medical care, research study or other healthcare event causing physical
    injury.

    Actual or  potential/avoided event causing unintended physical injury
    resulting from or contributed to by medical care, a research study or other
    healthcare setting factors that requires additional monitoring, treatment,
    or hospitalization, or that results in death.
    """
    resource_type: ClassVar[str] = "AdverseEvent"
    actuality: str = None
    category: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    contributor: Optional[List[fhirreference.FHIRReference]] = empty_list()
    date: Optional[fhirdate.FHIRDate] = None
    detected: Optional[fhirdate.FHIRDate] = None
    encounter: Optional[fhirreference.FHIRReference] = None
    event: Optional[codeableconcept.CodeableConcept] = None
    identifier: Optional[identifier.Identifier] = None
    location: Optional[fhirreference.FHIRReference] = None
    outcome: Optional[codeableconcept.CodeableConcept] = None
    recordedDate: Optional[fhirdate.FHIRDate] = None
    recorder: Optional[fhirreference.FHIRReference] = None
    referenceDocument: Optional[List[fhirreference.FHIRReference]] = empty_list()
    resultingCondition: Optional[List[fhirreference.FHIRReference]] = empty_list()
    seriousness: Optional[codeableconcept.CodeableConcept] = None
    severity: Optional[codeableconcept.CodeableConcept] = None
    study: Optional[List[fhirreference.FHIRReference]] = empty_list()
    subject:fhirreference.FHIRReference = None
    subjectMedicalHistory: Optional[List[fhirreference.FHIRReference]] = empty_list()
    suspectEntity: Optional[List[AdverseEventSuspectEntity]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(AdverseEvent, self).elementProperties()
        js.extend([
            ("actuality", "actuality", str, False, None, True),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("contributor", "contributor", fhirreference.FHIRReference, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("detected", "detected", fhirdate.FHIRDate, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("event", "event", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, False),
            ("recordedDate", "recordedDate", fhirdate.FHIRDate, False, None, False),
            ("recorder", "recorder", fhirreference.FHIRReference, False, None, False),
            ("referenceDocument", "referenceDocument", fhirreference.FHIRReference, True, None, False),
            ("resultingCondition", "resultingCondition", fhirreference.FHIRReference, True, None, False),
            ("seriousness", "seriousness", codeableconcept.CodeableConcept, False, None, False),
            ("severity", "severity", codeableconcept.CodeableConcept, False, None, False),
            ("study", "study", fhirreference.FHIRReference, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("subjectMedicalHistory", "subjectMedicalHistory", fhirreference.FHIRReference, True, None, False),
            ("suspectEntity", "suspectEntity", AdverseEventSuspectEntity, True, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class AdverseEventSuspectEntity(backboneelement.BackboneElement):
    """ The suspected agent causing the adverse event.

    Describes the entity that is suspected to have caused the adverse event.
    """
    resource_type: ClassVar[str] = "AdverseEventSuspectEntity"
    causality: Optional[List[AdverseEventSuspectEntityCausality]] = empty_list()
    instance:fhirreference.FHIRReference = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(AdverseEventSuspectEntity, self).elementProperties()
        js.extend([
            ("causality", "causality", AdverseEventSuspectEntityCausality, True, None, False),
            ("instance", "instance", fhirreference.FHIRReference, False, None, True),
        ])
        return js

@dataclass
class AdverseEventSuspectEntityCausality(backboneelement.BackboneElement):
    """ Information on the possible cause of the event.
    """
    resource_type: ClassVar[str] = "AdverseEventSuspectEntityCausality"
    assessment: Optional[codeableconcept.CodeableConcept] = None
    author: Optional[fhirreference.FHIRReference] = None
    method: Optional[codeableconcept.CodeableConcept] = None
    productRelatedness: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(AdverseEventSuspectEntityCausality, self).elementProperties()
        js.extend([
            ("assessment", "assessment", codeableconcept.CodeableConcept, False, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("productRelatedness", "productRelatedness", str, False, None, False),
        ])
        return js


import sys
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