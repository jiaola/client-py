#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Specimen) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import duration
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity

from . import domainresource

@dataclass
class Specimen(domainresource.DomainResource):
    """ Sample for analysis.

    A sample to be used for analysis.
    """
    resource_type: ClassVar[str] = "Specimen"
    accessionIdentifier: Optional[identifier.Identifier] = None
    collection: Optional[SpecimenCollection] = None
    condition: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    container: Optional[List[SpecimenContainer]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    note: Optional[List[annotation.Annotation]] = empty_list()
    parent: Optional[List[fhirreference.FHIRReference]] = empty_list()
    processing: Optional[List[SpecimenProcessing]] = empty_list()
    receivedTime: Optional[fhirdate.FHIRDate] = None
    request: Optional[List[fhirreference.FHIRReference]] = empty_list()
    status: Optional[str] = None
    subject: Optional[fhirreference.FHIRReference] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Specimen, self).elementProperties()
        js.extend([
            ("accessionIdentifier", "accessionIdentifier", identifier.Identifier, False, None, False),
            ("collection", "collection", SpecimenCollection, False, None, False),
            ("condition", "condition", codeableconcept.CodeableConcept, True, None, False),
            ("container", "container", SpecimenContainer, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("parent", "parent", fhirreference.FHIRReference, True, None, False),
            ("processing", "processing", SpecimenProcessing, True, None, False),
            ("receivedTime", "receivedTime", fhirdate.FHIRDate, False, None, False),
            ("request", "request", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class SpecimenCollection(backboneelement.BackboneElement):
    """ Collection details.

    Details concerning the specimen collection.
    """
    resource_type: ClassVar[str] = "SpecimenCollection"
    bodySite: Optional[codeableconcept.CodeableConcept] = None
    collectedDateTime: Optional[fhirdate.FHIRDate] = None
    collectedPeriod: Optional[period.Period] = None
    collector: Optional[fhirreference.FHIRReference] = None
    duration: Optional[duration.Duration] = None
    fastingStatusCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    fastingStatusDuration: Optional[duration.Duration] = None
    method: Optional[codeableconcept.CodeableConcept] = None
    quantity: Optional[quantity.Quantity] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SpecimenCollection, self).elementProperties()
        js.extend([
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("collectedDateTime", "collectedDateTime", fhirdate.FHIRDate, False, "collected", False),
            ("collectedPeriod", "collectedPeriod", period.Period, False, "collected", False),
            ("collector", "collector", fhirreference.FHIRReference, False, None, False),
            ("duration", "duration", duration.Duration, False, None, False),
            ("fastingStatusCodeableConcept", "fastingStatusCodeableConcept", codeableconcept.CodeableConcept, False, "fastingStatus", False),
            ("fastingStatusDuration", "fastingStatusDuration", duration.Duration, False, "fastingStatus", False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
        ])
        return js

@dataclass
class SpecimenContainer(backboneelement.BackboneElement):
    """ Direct container of specimen (tube/slide, etc.).

    The container holding the specimen.  The recursive nature of containers;
    i.e. blood in tube in tray in rack is not addressed here.
    """
    resource_type: ClassVar[str] = "SpecimenContainer"
    additiveCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    additiveReference: Optional[fhirreference.FHIRReference] = None
    capacity: Optional[quantity.Quantity] = None
    description: Optional[str] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    specimenQuantity: Optional[quantity.Quantity] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SpecimenContainer, self).elementProperties()
        js.extend([
            ("additiveCodeableConcept", "additiveCodeableConcept", codeableconcept.CodeableConcept, False, "additive", False),
            ("additiveReference", "additiveReference", fhirreference.FHIRReference, False, "additive", False),
            ("capacity", "capacity", quantity.Quantity, False, None, False),
            ("description", "description", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("specimenQuantity", "specimenQuantity", quantity.Quantity, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class SpecimenProcessing(backboneelement.BackboneElement):
    """ Processing and processing step details.

    Details concerning processing and processing steps for the specimen.
    """
    resource_type: ClassVar[str] = "SpecimenProcessing"
    additive: Optional[List[fhirreference.FHIRReference]] = empty_list()
    description: Optional[str] = None
    procedure: Optional[codeableconcept.CodeableConcept] = None
    timeDateTime: Optional[fhirdate.FHIRDate] = None
    timePeriod: Optional[period.Period] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SpecimenProcessing, self).elementProperties()
        js.extend([
            ("additive", "additive", fhirreference.FHIRReference, True, None, False),
            ("description", "description", str, False, None, False),
            ("procedure", "procedure", codeableconcept.CodeableConcept, False, None, False),
            ("timeDateTime", "timeDateTime", fhirdate.FHIRDate, False, "time", False),
            ("timePeriod", "timePeriod", period.Period, False, "time", False),
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
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']