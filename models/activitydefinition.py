#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ActivityDefinition) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import age
from . import backboneelement
from . import codeableconcept
from . import contactdetail
from . import domainresource
from . import dosage
from . import duration
from . import expression
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import range
from . import relatedartifact
from . import timing
from . import usagecontext

from . import backboneelement

@dataclass
class ActivityDefinitionParticipant(backboneelement.BackboneElement):
    """ Who should participate in the action.

    Indicates who should participate in performing the action described.
    """
    resource_type: ClassVar[str] = "ActivityDefinitionParticipant"
    role: Optional[codeableconcept.CodeableConcept] = None
    type: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ActivityDefinitionParticipant, self).elementProperties()
        js.extend([
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js

@dataclass
class ActivityDefinitionDynamicValue(backboneelement.BackboneElement):
    """ Dynamic aspects of the definition.

    Dynamic values that will be evaluated to produce values for elements of the
    resulting resource. For example, if the dosage of a medication must be
    computed based on the patient's weight, a dynamic value would be used to
    specify an expression that calculated the weight, and the path on the
    request resource that would contain the result.
    """
    resource_type: ClassVar[str] = "ActivityDefinitionDynamicValue"
    expression:expression.Expression = None
    path: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ActivityDefinitionDynamicValue, self).elementProperties()
        js.extend([
            ("expression", "expression", expression.Expression, False, None, True),
            ("path", "path", str, False, None, True),
        ])
        return js

from . import domainresource

@dataclass
class ActivityDefinition(domainresource.DomainResource):
    """ The definition of a specific activity to be taken, independent of any
    particular patient or context.

    This resource allows for the definition of some activity to be performed,
    independent of a particular patient, practitioner, or other performance
    context.
    """
    resource_type: ClassVar[str] = "ActivityDefinition"
    approvalDate: Optional[fhirdate.FHIRDate] = None
    author: Optional[List[contactdetail.ContactDetail]] = empty_list()
    bodySite: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    code: Optional[codeableconcept.CodeableConcept] = None
    contact: Optional[List[contactdetail.ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date: Optional[fhirdate.FHIRDate] = None
    description: Optional[str] = None
    doNotPerform: Optional[bool] = None
    dosage: Optional[List[dosage.Dosage]] = empty_list()
    dynamicValue: Optional[List[ActivityDefinitionDynamicValue]] = empty_list()
    editor: Optional[List[contactdetail.ContactDetail]] = empty_list()
    effectivePeriod: Optional[period.Period] = None
    endorser: Optional[List[contactdetail.ContactDetail]] = empty_list()
    experimental: Optional[bool] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    intent: Optional[str] = None
    jurisdiction: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    kind: Optional[str] = None
    lastReviewDate: Optional[fhirdate.FHIRDate] = None
    library: Optional[List[str]] = empty_list()
    location: Optional[fhirreference.FHIRReference] = None
    name: Optional[str] = None
    observationRequirement: Optional[List[fhirreference.FHIRReference]] = empty_list()
    observationResultRequirement: Optional[List[fhirreference.FHIRReference]] = empty_list()
    participant: Optional[List[ActivityDefinitionParticipant]] = empty_list()
    priority: Optional[str] = None
    productCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    productReference: Optional[fhirreference.FHIRReference] = None
    profile: Optional[str] = None
    publisher: Optional[str] = None
    purpose: Optional[str] = None
    quantity: Optional[quantity.Quantity] = None
    relatedArtifact: Optional[List[relatedartifact.RelatedArtifact]] = empty_list()
    reviewer: Optional[List[contactdetail.ContactDetail]] = empty_list()
    specimenRequirement: Optional[List[fhirreference.FHIRReference]] = empty_list()
    status: str = None
    subjectCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    subjectReference: Optional[fhirreference.FHIRReference] = None
    subtitle: Optional[str] = None
    timingAge: Optional[age.Age] = None
    timingDateTime: Optional[fhirdate.FHIRDate] = None
    timingDuration: Optional[duration.Duration] = None
    timingPeriod: Optional[period.Period] = None
    timingRange: Optional[range.Range] = None
    timingTiming: Optional[timing.Timing] = None
    title: Optional[str] = None
    topic: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    transform: Optional[str] = None
    url: Optional[str] = None
    usage: Optional[str] = None
    useContext: Optional[List[usagecontext.UsageContext]] = empty_list()
    version: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ActivityDefinition, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("dosage", "dosage", dosage.Dosage, True, None, False),
            ("dynamicValue", "dynamicValue", ActivityDefinitionDynamicValue, True, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("intent", "intent", str, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("kind", "kind", str, False, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("library", "library", str, True, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("name", "name", str, False, None, False),
            ("observationRequirement", "observationRequirement", fhirreference.FHIRReference, True, None, False),
            ("observationResultRequirement", "observationResultRequirement", fhirreference.FHIRReference, True, None, False),
            ("participant", "participant", ActivityDefinitionParticipant, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("productCodeableConcept", "productCodeableConcept", codeableconcept.CodeableConcept, False, "product", False),
            ("productReference", "productReference", fhirreference.FHIRReference, False, "product", False),
            ("profile", "profile", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("specimenRequirement", "specimenRequirement", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False),
            ("subtitle", "subtitle", str, False, None, False),
            ("timingAge", "timingAge", age.Age, False, "timing", False),
            ("timingDateTime", "timingDateTime", fhirdate.FHIRDate, False, "timing", False),
            ("timingDuration", "timingDuration", duration.Duration, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("timingRange", "timingRange", range.Range, False, "timing", False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
            ("title", "title", str, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("transform", "transform", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


import sys
try:
    from . import age
except ImportError:
    age = sys.modules[__package__ + '.age']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import dosage
except ImportError:
    dosage = sys.modules[__package__ + '.dosage']
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
try:
    from . import expression
except ImportError:
    expression = sys.modules[__package__ + '.expression']
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
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
try:
    from . import relatedartifact
except ImportError:
    relatedartifact = sys.modules[__package__ + '.relatedartifact']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']