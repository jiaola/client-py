#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Composition) on 2019-07-03.
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
#        self.attester = None
#        """ Attests to accuracy of composition.
#        List of `CompositionAttester` items
#
# (represented as `dict` in JSON). """
#
#
#        self.author = None
#        """ Who and/or what authored the composition.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.category = None
#        """ Categorization of Composition.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.confidentiality = None
#        """ As defined by affinity domain.
#        Type `str`
#
#. """
#
#
#        self.custodian = None
#        """ Organization which maintains the composition.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.date = None
#        """ Composition editing time.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.encounter = None
#        """ Context of the Composition.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.event = None
#        """ The clinical service(s) being documented.
#        List of `CompositionEvent` items
#
# (represented as `dict` in JSON). """
#
#
#        self.identifier = None
#        """ Version-independent identifier for the Composition.
#        Type `Identifier`
#
# (represented as `dict` in JSON). """
#
#
#        self.relatesTo = None
#        """ Relationships to other compositions/documents.
#        List of `CompositionRelatesTo` items
#
# (represented as `dict` in JSON). """
#
#
#        self.section = None
#        """ Composition is broken into sections.
#        List of `CompositionSection` items
#
# (represented as `dict` in JSON). """
#
#
#        self.status = None
#        """ preliminary | final | amended | entered-in-error.
#        Type `str`
#
#. """
#
#
#        self.subject = None
#        """ Who and/or what the composition is about.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.title = None
#        """ Human Readable name/title.
#        Type `str`
#
#. """
#
#
#        self.type = None
#        """ Kind of composition (LOINC if possible).
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#

#        super(Composition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Composition, self).elementProperties()
        js.extend([
            ("attester", "attester", CompositionAttester, {  # #}True, None, {  # #}False),
            ("author", "author", fhirreference.FHIRReference, {  # #}True, None, {  # #}True),
            ("category", "category", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("confidentiality", "confidentiality", str, {  # #}False, None, {  # #}False),
            ("custodian", "custodian", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("date", "date", fhirdate.FHIRDate, {  # #}False, None, {  # #}True),
            ("encounter", "encounter", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("event", "event", CompositionEvent, {  # #}True, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}False, None, {  # #}False),
            ("relatesTo", "relatesTo", CompositionRelatesTo, {  # #}True, None, {  # #}False),
            ("section", "section", CompositionSection, {  # #}True, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}True),
            ("subject", "subject", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("title", "title", str, {  # #}False, None, {  # #}True),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import narrative
from . import period


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
#        self.mode = None
#        """ personal | professional | legal | official.
#        Type `str`
#
#. """
#
#
#        self.party = None
#        """ Who attested the composition.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.time = None
#        """ When the composition was attested.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#

#        super(CompositionAttester, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CompositionAttester, self).elementProperties()
        js.extend([
            ("mode", "mode", str, {  # #}False, None, {  # #}True),
            ("party", "party", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("time", "time", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import narrative
from . import period


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
#        """ Code(s) that apply to the event being documented.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.detail = None
#        """ The event(s) being documented.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.period = None
#        """ The period covered by the documentation.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#

#        super(CompositionEvent, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CompositionEvent, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("detail", "detail", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("period", "period", period.Period, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import narrative
from . import period


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
#        self.targetIdentifier = None
#        """ Target of the relationship.
#        Type `Identifier`
#
# (represented as `dict` in JSON). """
#
#
#        self.targetReference = None
#        """ Target of the relationship.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#

#        super(CompositionRelatesTo, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CompositionRelatesTo, self).elementProperties()
        js.extend([
            ("code", "code", str, {  # #}False, None, {  # #}True),
            ("targetIdentifier", "targetIdentifier", identifier.Identifier, {  # #}False, "target", {  # #}True),
            ("targetReference", "targetReference", fhirreference.FHIRReference, {  # #}False, "target", {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import narrative
from . import period


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
#        self.author = None
#        """ Who and/or what authored the section.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.code = None
#        """ Classification of section (recommended).
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.emptyReason = None
#        """ Why the section is empty.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.entry = None
#        """ A reference to data that supports this section.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.focus = None
#        """ Who/what the section is about, when it is not about the subject of
        composition.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.mode = None
#        """ working | snapshot | changes.
#        Type `str`
#
#. """
#
#
#        self.orderedBy = None
#        """ Order of section entries.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.section = None
#        """ Nested Section.
#        List of `CompositionSection` items
#
# (represented as `dict` in JSON). """
#
#
#        self.text = None
#        """ Text summary of the section, for human interpretation.
#        Type `Narrative`
#
# (represented as `dict` in JSON). """
#
#
#        self.title = None
#        """ Label for section (e.g. for ToC).
#        Type `str`
#
#. """
#

#        super(CompositionSection, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CompositionSection, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("code", "code", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("emptyReason", "emptyReason", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("entry", "entry", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("focus", "focus", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("mode", "mode", str, {  # #}False, None, {  # #}False),
            ("orderedBy", "orderedBy", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("section", "section", CompositionSection, {  # #}True, None, {  # #}False),
            ("text", "text", narrative.Narrative, {  # #}False, None, {  # #}False),
            ("title", "title", str, {  # #}False, None, {  # #}False),
        ])
        return js