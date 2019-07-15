#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Composition) on 2019-07-15.
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
from . import narrative
from . import period

from . import domainresource

@dataclass
class Composition(domainresource.DomainResource):
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
    author: List[fhirreference.FHIRReference] = empty_list()
    category: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    confidentiality: Optional[str] = None
    custodian: Optional[fhirreference.FHIRReference] = None
    date:fhirdate.FHIRDate = None
    encounter: Optional[fhirreference.FHIRReference] = None
    event: Optional[List[CompositionEvent]] = empty_list()
    identifier: Optional[identifier.Identifier] = None
    relatesTo: Optional[List[CompositionRelatesTo]] = empty_list()
    section: Optional[List[CompositionSection]] = empty_list()
    status: str = None
    subject: Optional[fhirreference.FHIRReference] = None
    title: str = None
    type:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Composition, self).elementProperties()
        js.extend([
            ("attester", "attester", CompositionAttester, True, None, False),
            ("author", "author", fhirreference.FHIRReference, True, None, True),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("confidentiality", "confidentiality", str, False, None, False),
            ("custodian", "custodian", fhirreference.FHIRReference, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("event", "event", CompositionEvent, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("relatesTo", "relatesTo", CompositionRelatesTo, True, None, False),
            ("section", "section", CompositionSection, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("title", "title", str, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js

from . import backboneelement

@dataclass
class CompositionAttester(backboneelement.BackboneElement):
    """ Attests to accuracy of composition.

    A participant who has attested to the accuracy of the composition/document.
    """
    resource_type: ClassVar[str] = "CompositionAttester"
    mode: str = None
    party: Optional[fhirreference.FHIRReference] = None
    time: Optional[fhirdate.FHIRDate] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CompositionAttester, self).elementProperties()
        js.extend([
            ("mode", "mode", str, False, None, True),
            ("party", "party", fhirreference.FHIRReference, False, None, False),
            ("time", "time", fhirdate.FHIRDate, False, None, False),
        ])
        return js

@dataclass
class CompositionEvent(backboneelement.BackboneElement):
    """ The clinical service(s) being documented.

    The clinical service, such as a colonoscopy or an appendectomy, being
    documented.
    """
    resource_type: ClassVar[str] = "CompositionEvent"
    code: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    detail: Optional[List[fhirreference.FHIRReference]] = empty_list()
    period: Optional[period.Period] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CompositionEvent, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("detail", "detail", fhirreference.FHIRReference, True, None, False),
            ("period", "period", period.Period, False, None, False),
        ])
        return js

@dataclass
class CompositionRelatesTo(backboneelement.BackboneElement):
    """ Relationships to other compositions/documents.

    Relationships that this composition has with other compositions or
    documents that already exist.
    """
    resource_type: ClassVar[str] = "CompositionRelatesTo"
    code: str = None
    targetIdentifier:identifier.Identifier = None
    targetReference:fhirreference.FHIRReference = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CompositionRelatesTo, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("targetIdentifier", "targetIdentifier", identifier.Identifier, False, "target", True),
            ("targetReference", "targetReference", fhirreference.FHIRReference, False, "target", True),
        ])
        return js

@dataclass
class CompositionSection(backboneelement.BackboneElement):
    """ Composition is broken into sections.

    The root of the sections that make up the composition.
    """
    resource_type: ClassVar[str] = "CompositionSection"
    author: Optional[List[fhirreference.FHIRReference]] = empty_list()
    code: Optional[codeableconcept.CodeableConcept] = None
    emptyReason: Optional[codeableconcept.CodeableConcept] = None
    entry: Optional[List[fhirreference.FHIRReference]] = empty_list()
    focus: Optional[fhirreference.FHIRReference] = None
    mode: Optional[str] = None
    orderedBy: Optional[codeableconcept.CodeableConcept] = None
    section: Optional[List[CompositionSection]] = empty_list()
    text: Optional[narrative.Narrative] = None
    title: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CompositionSection, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("emptyReason", "emptyReason", codeableconcept.CodeableConcept, False, None, False),
            ("entry", "entry", fhirreference.FHIRReference, True, None, False),
            ("focus", "focus", fhirreference.FHIRReference, False, None, False),
            ("mode", "mode", str, False, None, False),
            ("orderedBy", "orderedBy", codeableconcept.CodeableConcept, False, None, False),
            ("section", "section", CompositionSection, True, None, False),
            ("text", "text", narrative.Narrative, False, None, False),
            ("title", "title", str, False, None, False),
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
try:
    from . import narrative
except ImportError:
    narrative = sys.modules[__package__ + '.narrative']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']