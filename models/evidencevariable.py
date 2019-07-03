#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/EvidenceVariable) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
from . import contactdetail
from . import datarequirement
from . import domainresource
from . import duration
from . import expression
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import relatedartifact
from . import timing
from . import triggerdefinition
from . import usagecontext


from . import domainresource

@dataclass
class EvidenceVariable(domainresource.DomainResource):
    """ A population, intervention, or exposure definition.

    The EvidenceVariable resource describes a "PICO" element that knowledge
    (evidence, assertion, recommendation) is about.
    """
    resource_type: ClassVar[str] = "EvidenceVariable"
    approvalDate: Optional[fhirdate.FHIRDate] = None
    author: Optional[List[contactdetail.ContactDetail]] = empty_list()
    characteristic: List[ EvidenceVariableCharacteristic] = empty_list()
    contact: Optional[List[contactdetail.ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date: Optional[fhirdate.FHIRDate] = None
    description: Optional[str] = None
    editor: Optional[List[contactdetail.ContactDetail]] = empty_list()
    effectivePeriod: Optional[period.Period] = None
    endorser: Optional[List[contactdetail.ContactDetail]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    jurisdiction: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    lastReviewDate: Optional[fhirdate.FHIRDate] = None
    name: Optional[str] = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    publisher: Optional[str] = None
    relatedArtifact: Optional[List[relatedartifact.RelatedArtifact]] = empty_list()
    reviewer: Optional[List[contactdetail.ContactDetail]] = empty_list()
    shortTitle: Optional[str] = None
    status: str = None
    subtitle: Optional[str] = None
    title: Optional[str] = None
    topic: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    type: Optional[str] = None
    url: Optional[str] = None
    useContext: Optional[List[usagecontext.UsageContext]] = empty_list()
    version: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.approvalDate = None
#        """ When the evidence variable was approved by publisher.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.author = None
#        """ Who authored the content.
#        List of `ContactDetail` items
#
# (represented as `dict` in JSON). """
#
#
#        self.characteristic = None
#        """ What defines the members of the evidence element.
#        List of `EvidenceVariableCharacteristic` items
#
# (represented as `dict` in JSON). """
#
#
#        self.contact = None
#        """ Contact details for the publisher.
#        List of `ContactDetail` items
#
# (represented as `dict` in JSON). """
#
#
#        self.copyright = None
#        """ Use and/or publishing restrictions.
#        Type `str`
#
#. """
#
#
#        self.date = None
#        """ Date last changed.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.description = None
#        """ Natural language description of the evidence variable.
#        Type `str`
#
#. """
#
#
#        self.editor = None
#        """ Who edited the content.
#        List of `ContactDetail` items
#
# (represented as `dict` in JSON). """
#
#
#        self.effectivePeriod = None
#        """ When the evidence variable is expected to be used.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#
#
#        self.endorser = None
#        """ Who endorsed the content.
#        List of `ContactDetail` items
#
# (represented as `dict` in JSON). """
#
#
#        self.identifier = None
#        """ Additional identifier for the evidence variable.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.jurisdiction = None
#        """ Intended jurisdiction for evidence variable (if applicable).
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.lastReviewDate = None
#        """ When the evidence variable was last reviewed.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.name = None
#        """ Name for this evidence variable (computer friendly).
#        Type `str`
#
#. """
#
#
#        self.note = None
#        """ Used for footnotes or explanatory notes.
#        List of `Annotation` items
#
# (represented as `dict` in JSON). """
#
#
#        self.publisher = None
#        """ Name of the publisher (organization or individual).
#        Type `str`
#
#. """
#
#
#        self.relatedArtifact = None
#        """ Additional documentation, citations, etc..
#        List of `RelatedArtifact` items
#
# (represented as `dict` in JSON). """
#
#
#        self.reviewer = None
#        """ Who reviewed the content.
#        List of `ContactDetail` items
#
# (represented as `dict` in JSON). """
#
#
#        self.shortTitle = None
#        """ Title for use in informal contexts.
#        Type `str`
#
#. """
#
#
#        self.status = None
#        """ draft | active | retired | unknown.
#        Type `str`
#
#. """
#
#
#        self.subtitle = None
#        """ Subordinate title of the EvidenceVariable.
#        Type `str`
#
#. """
#
#
#        self.title = None
#        """ Name for this evidence variable (human friendly).
#        Type `str`
#
#. """
#
#
#        self.topic = None
#        """ The category of the EvidenceVariable, such as Education, Treatment,
        Assessment, etc..
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.type = None
#        """ dichotomous | continuous | descriptive.
#        Type `str`
#
#. """
#
#
#        self.url = None
#        """ Canonical identifier for this evidence variable, represented as a
        URI (globally unique).
#        Type `str`
#
#. """
#
#
#        self.useContext = None
#        """ The context that the content is intended to support.
#        List of `UsageContext` items
#
# (represented as `dict` in JSON). """
#
#
#        self.version = None
#        """ Business version of the evidence variable.
#        Type `str`
#
#. """
#

#        super(EvidenceVariable, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(EvidenceVariable, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("author", "author", contactdetail.ContactDetail, {  # #}True, None, {  # #}False),
            ("characteristic", "characteristic", EvidenceVariableCharacteristic, {  # #}True, None, {  # #}True),
            ("contact", "contact", contactdetail.ContactDetail, {  # #}True, None, {  # #}False),
            ("copyright", "copyright", str, {  # #}False, None, {  # #}False),
            ("date", "date", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("description", "description", str, {  # #}False, None, {  # #}False),
            ("editor", "editor", contactdetail.ContactDetail, {  # #}True, None, {  # #}False),
            ("effectivePeriod", "effectivePeriod", period.Period, {  # #}False, None, {  # #}False),
            ("endorser", "endorser", contactdetail.ContactDetail, {  # #}True, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("name", "name", str, {  # #}False, None, {  # #}False),
            ("note", "note", annotation.Annotation, {  # #}True, None, {  # #}False),
            ("publisher", "publisher", str, {  # #}False, None, {  # #}False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, {  # #}True, None, {  # #}False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, {  # #}True, None, {  # #}False),
            ("shortTitle", "shortTitle", str, {  # #}False, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}True),
            ("subtitle", "subtitle", str, {  # #}False, None, {  # #}False),
            ("title", "title", str, {  # #}False, None, {  # #}False),
            ("topic", "topic", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("type", "type", str, {  # #}False, None, {  # #}False),
            ("url", "url", str, {  # #}False, None, {  # #}False),
            ("useContext", "useContext", usagecontext.UsageContext, {  # #}True, None, {  # #}False),
            ("version", "version", str, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
from . import contactdetail
from . import datarequirement
from . import duration
from . import expression
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import relatedartifact
from . import timing
from . import triggerdefinition
from . import usagecontext


from . import backboneelement

@dataclass
class EvidenceVariableCharacteristic(backboneelement.BackboneElement):
    """ What defines the members of the evidence element.

    A characteristic that defines the members of the evidence element. Multiple
    characteristics are applied with "and" semantics.
    """
    resource_type: ClassVar[str] = "EvidenceVariableCharacteristic"
    definitionCanonical: str = None
    definitionCodeableConcept:codeableconcept.CodeableConcept = None
    definitionDataRequirement:datarequirement.DataRequirement = None
    definitionExpression:expression.Expression = None
    definitionReference:fhirreference.FHIRReference = None
    definitionTriggerDefinition:triggerdefinition.TriggerDefinition = None
    description: Optional[str] = None
    exclude: Optional[bool] = None
    groupMeasure: Optional[str] = None
    participantEffectiveDateTime: Optional[fhirdate.FHIRDate] = None
    participantEffectiveDuration: Optional[duration.Duration] = None
    participantEffectivePeriod: Optional[period.Period] = None
    participantEffectiveTiming: Optional[timing.Timing] = None
    timeFromStart: Optional[duration.Duration] = None
    usageContext: Optional[List[usagecontext.UsageContext]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.definitionCanonical = None
#        """ What code or expression defines members?.
#        Type `str`
#
#. """
#
#
#        self.definitionCodeableConcept = None
#        """ What code or expression defines members?.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.definitionDataRequirement = None
#        """ What code or expression defines members?.
#        Type `DataRequirement`
#
# (represented as `dict` in JSON). """
#
#
#        self.definitionExpression = None
#        """ What code or expression defines members?.
#        Type `Expression`
#
# (represented as `dict` in JSON). """
#
#
#        self.definitionReference = None
#        """ What code or expression defines members?.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.definitionTriggerDefinition = None
#        """ What code or expression defines members?.
#        Type `TriggerDefinition`
#
# (represented as `dict` in JSON). """
#
#
#        self.description = None
#        """ Natural language description of the characteristic.
#        Type `str`
#
#. """
#
#
#        self.exclude = None
#        """ Whether the characteristic includes or excludes members.
#        Type `bool`
#
#. """
#
#
#        self.groupMeasure = None
#        """ mean | median | mean-of-mean | mean-of-median | median-of-mean |
        median-of-median.
#        Type `str`
#
#. """
#
#
#        self.participantEffectiveDateTime = None
#        """ What time period do participants cover.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.participantEffectiveDuration = None
#        """ What time period do participants cover.
#        Type `Duration`
#
# (represented as `dict` in JSON). """
#
#
#        self.participantEffectivePeriod = None
#        """ What time period do participants cover.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#
#
#        self.participantEffectiveTiming = None
#        """ What time period do participants cover.
#        Type `Timing`
#
# (represented as `dict` in JSON). """
#
#
#        self.timeFromStart = None
#        """ Observation time from study start.
#        Type `Duration`
#
# (represented as `dict` in JSON). """
#
#
#        self.usageContext = None
#        """ What code/value pairs define members?.
#        List of `UsageContext` items
#
# (represented as `dict` in JSON). """
#

#        super(EvidenceVariableCharacteristic, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(EvidenceVariableCharacteristic, self).elementProperties()
        js.extend([
            ("definitionCanonical", "definitionCanonical", str, {  # #}False, "definition", {  # #}True),
            ("definitionCodeableConcept", "definitionCodeableConcept", codeableconcept.CodeableConcept, {  # #}False, "definition", {  # #}True),
            ("definitionDataRequirement", "definitionDataRequirement", datarequirement.DataRequirement, {  # #}False, "definition", {  # #}True),
            ("definitionExpression", "definitionExpression", expression.Expression, {  # #}False, "definition", {  # #}True),
            ("definitionReference", "definitionReference", fhirreference.FHIRReference, {  # #}False, "definition", {  # #}True),
            ("definitionTriggerDefinition", "definitionTriggerDefinition", triggerdefinition.TriggerDefinition, {  # #}False, "definition", {  # #}True),
            ("description", "description", str, {  # #}False, None, {  # #}False),
            ("exclude", "exclude", bool, {  # #}False, None, {  # #}False),
            ("groupMeasure", "groupMeasure", str, {  # #}False, None, {  # #}False),
            ("participantEffectiveDateTime", "participantEffectiveDateTime", fhirdate.FHIRDate, {  # #}False, "participantEffective", {  # #}False),
            ("participantEffectiveDuration", "participantEffectiveDuration", duration.Duration, {  # #}False, "participantEffective", {  # #}False),
            ("participantEffectivePeriod", "participantEffectivePeriod", period.Period, {  # #}False, "participantEffective", {  # #}False),
            ("participantEffectiveTiming", "participantEffectiveTiming", timing.Timing, {  # #}False, "participantEffective", {  # #}False),
            ("timeFromStart", "timeFromStart", duration.Duration, {  # #}False, None, {  # #}False),
            ("usageContext", "usageContext", usagecontext.UsageContext, {  # #}True, None, {  # #}False),
        ])
        return js