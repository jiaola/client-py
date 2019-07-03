#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DocumentReference) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import backboneelement
from . import codeableconcept
from . import coding
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period


from . import domainresource

@dataclass
class DocumentReference(domainresource.DomainResource):
    """ A reference to a document.

    A reference to a document of any kind for any purpose. Provides metadata
    about the document so that the document can be discovered and managed. The
    scope of a document is any seralized object with a mime-type, so includes
    formal patient centric documents (CDA), cliical notes, scanned paper, and
    non-patient specific documents like policy text.
    """
    resource_type: ClassVar[str] = "DocumentReference"
    authenticator: Optional[fhirreference.FHIRReference] = None
    author: Optional[List[fhirreference.FHIRReference]] = empty_list()
    category: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    content: List[ DocumentReferenceContent] = empty_list()
    context: Optional[DocumentReferenceContext] = None
    custodian: Optional[fhirreference.FHIRReference] = None
    date: Optional[fhirdate.FHIRDate] = None
    description: Optional[str] = None
    docStatus: Optional[str] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    masterIdentifier: Optional[identifier.Identifier] = None
    relatesTo: Optional[List[DocumentReferenceRelatesTo]] = empty_list()
    securityLabel: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    status: str = None
    subject: Optional[fhirreference.FHIRReference] = None
    type: Optional[codeableconcept.CodeableConcept] = None

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
#        self.authenticator = None
#        """ Who/what authenticated the document.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.author = None
#        """ Who and/or what authored the document.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.category = None
#        """ Categorization of document.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.content = None
#        """ Document referenced.
#        List of `DocumentReferenceContent` items
#
# (represented as `dict` in JSON). """
#
#
#        self.context = None
#        """ Clinical context of document.
#        Type `DocumentReferenceContext`
#
# (represented as `dict` in JSON). """
#
#
#        self.custodian = None
#        """ Organization which maintains the document.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.date = None
#        """ When this document reference was created.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.description = None
#        """ Human-readable description.
#        Type `str`
#
#. """
#
#
#        self.docStatus = None
#        """ preliminary | final | appended | amended | entered-in-error.
#        Type `str`
#
#. """
#
#
#        self.identifier = None
#        """ Other identifiers for the document.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.masterIdentifier = None
#        """ Master Version Specific Identifier.
#        Type `Identifier`
#
# (represented as `dict` in JSON). """
#
#
#        self.relatesTo = None
#        """ Relationships to other documents.
#        List of `DocumentReferenceRelatesTo` items
#
# (represented as `dict` in JSON). """
#
#
#        self.securityLabel = None
#        """ Document security-tags.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.status = None
#        """ current | superseded | entered-in-error.
#        Type `str`
#
#. """
#
#
#        self.subject = None
#        """ Who/what is the subject of the document.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.type = None
#        """ Kind of document (LOINC if possible).
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#

#        super(DocumentReference, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DocumentReference, self).elementProperties()
        js.extend([
            ("authenticator", "authenticator", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("author", "author", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("category", "category", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("content", "content", DocumentReferenceContent, {  # #}True, None, {  # #}True),
            ("context", "context", DocumentReferenceContext, {  # #}False, None, {  # #}False),
            ("custodian", "custodian", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("date", "date", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("description", "description", str, {  # #}False, None, {  # #}False),
            ("docStatus", "docStatus", str, {  # #}False, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("masterIdentifier", "masterIdentifier", identifier.Identifier, {  # #}False, None, {  # #}False),
            ("relatesTo", "relatesTo", DocumentReferenceRelatesTo, {  # #}True, None, {  # #}False),
            ("securityLabel", "securityLabel", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}True),
            ("subject", "subject", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import backboneelement
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period


from . import backboneelement

@dataclass
class DocumentReferenceContent(backboneelement.BackboneElement):
    """ Document referenced.

    The document and format referenced. There may be multiple content element
    repetitions, each with a different format.
    """
    resource_type: ClassVar[str] = "DocumentReferenceContent"
    attachment:attachment.Attachment = None
    format: Optional[coding.Coding] = None

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
#        self.attachment = None
#        """ Where to access the document.
#        Type `Attachment`
#
# (represented as `dict` in JSON). """
#
#
#        self.format = None
#        """ Format/content rules for the document.
#        Type `Coding`
#
# (represented as `dict` in JSON). """
#

#        super(DocumentReferenceContent, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DocumentReferenceContent, self).elementProperties()
        js.extend([
            ("attachment", "attachment", attachment.Attachment, {  # #}False, None, {  # #}True),
            ("format", "format", coding.Coding, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period


@dataclass
class DocumentReferenceContext(backboneelement.BackboneElement):
    """ Clinical context of document.

    The clinical context in which the document was prepared.
    """
    resource_type: ClassVar[str] = "DocumentReferenceContext"
    encounter: Optional[List[fhirreference.FHIRReference]] = empty_list()
    event: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    facilityType: Optional[codeableconcept.CodeableConcept] = None
    period: Optional[period.Period] = None
    practiceSetting: Optional[codeableconcept.CodeableConcept] = None
    related: Optional[List[fhirreference.FHIRReference]] = empty_list()
    sourcePatientInfo: Optional[fhirreference.FHIRReference] = None

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
#        self.encounter = None
#        """ Context of the document  content.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.event = None
#        """ Main clinical acts documented.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.facilityType = None
#        """ Kind of facility where patient was seen.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.period = None
#        """ Time of service that is being documented.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#
#
#        self.practiceSetting = None
#        """ Additional details about where the content was created (e.g.
        clinical specialty).
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.related = None
#        """ Related identifiers or resources.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.sourcePatientInfo = None
#        """ Patient demographics from source.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#

#        super(DocumentReferenceContext, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DocumentReferenceContext, self).elementProperties()
        js.extend([
            ("encounter", "encounter", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("event", "event", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("facilityType", "facilityType", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("period", "period", period.Period, {  # #}False, None, {  # #}False),
            ("practiceSetting", "practiceSetting", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("related", "related", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("sourcePatientInfo", "sourcePatientInfo", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period


@dataclass
class DocumentReferenceRelatesTo(backboneelement.BackboneElement):
    """ Relationships to other documents.

    Relationships that this document has with other document references that
    already exist.
    """
    resource_type: ClassVar[str] = "DocumentReferenceRelatesTo"
    code: str = None
    target:fhirreference.FHIRReference = None

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
#        self.code = None
#        """ replaces | transforms | signs | appends.
#        Type `str`
#
#. """
#
#
#        self.target = None
#        """ Target of the relationship.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#

#        super(DocumentReferenceRelatesTo, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DocumentReferenceRelatesTo, self).elementProperties()
        js.extend([
            ("code", "code", str, {  # #}False, None, {  # #}True),
            ("target", "target", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
        ])
        return js