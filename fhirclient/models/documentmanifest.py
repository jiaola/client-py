#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DocumentManifest) on 2019-07-18.
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


@dataclass
class DocumentManifestRelated(BackboneElement):
    """ Related things.

    Related identifiers or resources associated with the DocumentManifest.
    """
    resource_type: ClassVar[str] = "DocumentManifestRelated"
    identifier: Optional[Identifier] = None
    ref: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(DocumentManifestRelated, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, False, None, False),
            ("ref", "ref", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class DocumentManifest(DomainResource):
    """ A list that defines a set of documents.

    A collection of documents compiled for a purpose together with metadata
    that applies to the collection.
    """
    resource_type: ClassVar[str] = "DocumentManifest"
    author: Optional[List[FHIRReference]] = empty_list()
    content: List[FHIRReference] = empty_list()
    created: Optional[FHIRDate] = None
    description: Optional[str] = None
    identifier: Optional[List[Identifier]] = empty_list()
    masterIdentifier: Optional[Identifier] = None
    recipient: Optional[List[FHIRReference]] = empty_list()
    related: Optional[List[DocumentManifestRelated]] = empty_list()
    source: Optional[str] = None
    status: str = None
    subject: Optional[FHIRReference] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(DocumentManifest, self).elementProperties()
        js.extend([
            ("author", "author", FHIRReference, True, None, False),
            ("content", "content", FHIRReference, True, None, True),
            ("created", "created", FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("masterIdentifier", "masterIdentifier", Identifier, False, None, False),
            ("recipient", "recipient", FHIRReference, True, None, False),
            ("related", "related", DocumentManifestRelated, True, None, False),
            ("source", "source", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", FHIRReference, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js