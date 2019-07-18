#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DocumentManifest) on 2019-07-18.
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

from . import backboneelement

@dataclass
class DocumentManifestRelated(backboneelement.BackboneElement):
    """ Related things.

    Related identifiers or resources associated with the DocumentManifest.
    """
    resource_type: ClassVar[str] = "DocumentManifestRelated"
    identifier: Optional[identifier.Identifier] = None
    ref: Optional[fhirreference.FHIRReference] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DocumentManifestRelated, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("ref", "ref", fhirreference.FHIRReference, False, None, False),
        ])
        return js

from . import domainresource

@dataclass
class DocumentManifest(domainresource.DomainResource):
    """ A list that defines a set of documents.

    A collection of documents compiled for a purpose together with metadata
    that applies to the collection.
    """
    resource_type: ClassVar[str] = "DocumentManifest"
    author: Optional[List[fhirreference.FHIRReference]] = empty_list()
    content: List[fhirreference.FHIRReference] = empty_list()
    created: Optional[fhirdate.FHIRDate] = None
    description: Optional[str] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    masterIdentifier: Optional[identifier.Identifier] = None
    recipient: Optional[List[fhirreference.FHIRReference]] = empty_list()
    related: Optional[List[DocumentManifestRelated]] = empty_list()
    source: Optional[str] = None
    status: str = None
    subject: Optional[fhirreference.FHIRReference] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DocumentManifest, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, True, None, False),
            ("content", "content", fhirreference.FHIRReference, True, None, True),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("masterIdentifier", "masterIdentifier", identifier.Identifier, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False),
            ("related", "related", DocumentManifestRelated, True, None, False),
            ("source", "source", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
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