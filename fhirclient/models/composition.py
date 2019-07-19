#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Composition) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .narrative import Narrative
from .period import Period


@dataclass
class CompositionSection(BackboneElement):
    """ Composition is broken into sections.

    The root of the sections that make up the composition.
    """
    resource_type: ClassVar[str] = "CompositionSection"
    author: Optional[List[FHIRReference]] = empty_list()
    code: Optional[CodeableConcept] = None
    emptyReason: Optional[CodeableConcept] = None
    entry: Optional[List[FHIRReference]] = empty_list()
    focus: Optional[FHIRReference] = None
    mode: Optional[str] = None
    orderedBy: Optional[CodeableConcept] = None
    section: Optional[List[CompositionSection]] = empty_list()
    text: Optional[Narrative] = None
    title: Optional[str] = None

    def elementProperties(self):
        js = super(CompositionSection, self).elementProperties()
        js.extend([
            ("author", "author", FHIRReference, True, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("emptyReason", "emptyReason", CodeableConcept, False, None, False),
            ("entry", "entry", FHIRReference, True, None, False),
            ("focus", "focus", FHIRReference, False, None, False),
            ("mode", "mode", str, False, None, False),
            ("orderedBy", "orderedBy", CodeableConcept, False, None, False),
            ("section", "section", CompositionSection, True, None, False),
            ("text", "text", Narrative, False, None, False),
            ("title", "title", str, False, None, False),
        ])
        return js


@dataclass
class CompositionRelatesTo(BackboneElement):
    """ Relationships to other compositions/documents.

    Relationships that this composition has with other compositions or
    documents that already exist.
    """
    resource_type: ClassVar[str] = "CompositionRelatesTo"
    code: str = None
    targetIdentifier: Identifier = None
    targetReference: FHIRReference = None

    def elementProperties(self):
        js = super(CompositionRelatesTo, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("targetIdentifier", "targetIdentifier", Identifier, False, "target", True),
            ("targetReference", "targetReference", FHIRReference, False, "target", True),
        ])
        return js


@dataclass
class CompositionEvent(BackboneElement):
    """ The clinical service(s) being documented.

    The clinical service, such as a colonoscopy or an appendectomy, being
    documented.
    """
    resource_type: ClassVar[str] = "CompositionEvent"
    code: Optional[List[CodeableConcept]] = empty_list()
    detail: Optional[List[FHIRReference]] = empty_list()
    period: Optional[Period] = None

    def elementProperties(self):
        js = super(CompositionEvent, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, True, None, False),
            ("detail", "detail", FHIRReference, True, None, False),
            ("period", "period", Period, False, None, False),
        ])
        return js


@dataclass
class CompositionAttester(BackboneElement):
    """ Attests to accuracy of composition.

    A participant who has attested to the accuracy of the composition/document.
    """
    resource_type: ClassVar[str] = "CompositionAttester"
    mode: str = None
    party: Optional[FHIRReference] = None
    time: Optional[FHIRDate] = None

    def elementProperties(self):
        js = super(CompositionAttester, self).elementProperties()
        js.extend([
            ("mode", "mode", str, False, None, True),
            ("party", "party", FHIRReference, False, None, False),
            ("time", "time", FHIRDate, False, None, False),
        ])
        return js


@dataclass
class Composition(DomainResource):
    """ A set of resources composed into a single coherent clinical statement with
    clinical attestation.

    A set of healthcare-related information that is assembled together into a
    single logical package that provides a single coherent statement of
    meaning, establishes its own context and that has clinical attestation with
    regard to who is making the statement. A Composition defines the structure
    and narrative content necessary for a document. However, a Composition
    alone does not constitute a document. Rather, the Composition must be the
    first entry in a Bundle where Bundle.type=document, and any other resources
    referenced from Composition must be included as subsequent entries in the
    Bundle (for example Patient, Practitioner, Encounter, etc.).
    """
    resource_type: ClassVar[str] = "Composition"
    attester: Optional[List[CompositionAttester]] = empty_list()
    author: List[FHIRReference] = empty_list()
    category: Optional[List[CodeableConcept]] = empty_list()
    confidentiality: Optional[str] = None
    custodian: Optional[FHIRReference] = None
    date: FHIRDate = None
    encounter: Optional[FHIRReference] = None
    event: Optional[List[CompositionEvent]] = empty_list()
    identifier: Optional[Identifier] = None
    relatesTo: Optional[List[CompositionRelatesTo]] = empty_list()
    section: Optional[List[CompositionSection]] = empty_list()
    status: str = None
    subject: Optional[FHIRReference] = None
    title: str = None
    type: CodeableConcept = None

    def elementProperties(self):
        js = super(Composition, self).elementProperties()
        js.extend([
            ("attester", "attester", CompositionAttester, True, None, False),
            ("author", "author", FHIRReference, True, None, True),
            ("category", "category", CodeableConcept, True, None, False),
            ("confidentiality", "confidentiality", str, False, None, False),
            ("custodian", "custodian", FHIRReference, False, None, False),
            ("date", "date", FHIRDate, False, None, True),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("event", "event", CompositionEvent, True, None, False),
            ("identifier", "identifier", Identifier, False, None, False),
            ("relatesTo", "relatesTo", CompositionRelatesTo, True, None, False),
            ("section", "section", CompositionSection, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", FHIRReference, False, None, False),
            ("title", "title", str, False, None, True),
            ("type", "type", CodeableConcept, False, None, True),
        ])
        return js