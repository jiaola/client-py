#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DocumentReference) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class DocumentReferenceRelatesTo(BackboneElement):
    """ Relationships to other documents.

    Relationships that this document has with other document references that
    already exist.
    """
    resource_type: ClassVar[str] = "DocumentReferenceRelatesTo"
    code: str = None
    target: FHIRReference = None

    def elementProperties(self):
        js = super(DocumentReferenceRelatesTo, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("target", "target", FHIRReference, False, None, True),
        ])
        return js


@dataclass
class DocumentReferenceContext(BackboneElement):
    """ Clinical context of document.

    The clinical context in which the document was prepared.
    """
    resource_type: ClassVar[str] = "DocumentReferenceContext"
    encounter: Optional[List[FHIRReference]] = empty_list()
    event: Optional[List[CodeableConcept]] = empty_list()
    facilityType: Optional[CodeableConcept] = None
    period: Optional[Period] = None
    practiceSetting: Optional[CodeableConcept] = None
    related: Optional[List[FHIRReference]] = empty_list()
    sourcePatientInfo: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(DocumentReferenceContext, self).elementProperties()
        js.extend([
            ("encounter", "encounter", FHIRReference, True, None, False),
            ("event", "event", CodeableConcept, True, None, False),
            ("facilityType", "facilityType", CodeableConcept, False, None, False),
            ("period", "period", Period, False, None, False),
            ("practiceSetting", "practiceSetting", CodeableConcept, False, None, False),
            ("related", "related", FHIRReference, True, None, False),
            ("sourcePatientInfo", "sourcePatientInfo", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class DocumentReferenceContent(BackboneElement):
    """ Document referenced.

    The document and format referenced. There may be multiple content element
    repetitions, each with a different format.
    """
    resource_type: ClassVar[str] = "DocumentReferenceContent"
    attachment: Attachment = None
    format: Optional[Coding] = None

    def elementProperties(self):
        js = super(DocumentReferenceContent, self).elementProperties()
        js.extend([
            ("attachment", "attachment", Attachment, False, None, True),
            ("format", "format", Coding, False, None, False),
        ])
        return js


@dataclass
class DocumentReference(DomainResource):
    """ A reference to a document.

    A reference to a document of any kind for any purpose. Provides metadata
    about the document so that the document can be discovered and managed. The
    scope of a document is any seralized object with a mime-type, so includes
    formal patient centric documents (CDA), cliical notes, scanned paper, and
    non-patient specific documents like policy text.
    """
    resource_type: ClassVar[str] = "DocumentReference"
    authenticator: Optional[FHIRReference] = None
    author: Optional[List[FHIRReference]] = empty_list()
    category: Optional[List[CodeableConcept]] = empty_list()
    content: List[DocumentReferenceContent] = empty_list()
    context: Optional[DocumentReferenceContext] = None
    custodian: Optional[FHIRReference] = None
    date: Optional[FHIRDate] = None
    description: Optional[str] = None
    docStatus: Optional[str] = None
    identifier: Optional[List[Identifier]] = empty_list()
    masterIdentifier: Optional[Identifier] = None
    relatesTo: Optional[List[DocumentReferenceRelatesTo]] = empty_list()
    securityLabel: Optional[List[CodeableConcept]] = empty_list()
    status: str = None
    subject: Optional[FHIRReference] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(DocumentReference, self).elementProperties()
        js.extend([
            ("authenticator", "authenticator", FHIRReference, False, None, False),
            ("author", "author", FHIRReference, True, None, False),
            ("category", "category", CodeableConcept, True, None, False),
            ("content", "content", DocumentReferenceContent, True, None, True),
            ("context", "context", DocumentReferenceContext, False, None, False),
            ("custodian", "custodian", FHIRReference, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("docStatus", "docStatus", str, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("masterIdentifier", "masterIdentifier", Identifier, False, None, False),
            ("relatesTo", "relatesTo", DocumentReferenceRelatesTo, True, None, False),
            ("securityLabel", "securityLabel", CodeableConcept, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", FHIRReference, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js