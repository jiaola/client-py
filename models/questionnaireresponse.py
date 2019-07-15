#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/QuestionnaireResponse) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import backboneelement
from . import coding
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity

from . import domainresource

@dataclass
class QuestionnaireResponse(domainresource.DomainResource):
    """ A structured set of questions and their answers.

    A structured set of questions and their answers. The questions are ordered
    and grouped into coherent subsets, corresponding to the structure of the
    grouping of the questionnaire being responded to.
    """
    resource_type: ClassVar[str] = "QuestionnaireResponse"
    author: Optional[fhirreference.FHIRReference] = None
    authored: Optional[fhirdate.FHIRDate] = None
    basedOn: Optional[List[fhirreference.FHIRReference]] = empty_list()
    encounter: Optional[fhirreference.FHIRReference] = None
    identifier: Optional[identifier.Identifier] = None
    item: Optional[List[QuestionnaireResponseItem]] = empty_list()
    partOf: Optional[List[fhirreference.FHIRReference]] = empty_list()
    questionnaire: Optional[str] = None
    source: Optional[fhirreference.FHIRReference] = None
    status: str = None
    subject: Optional[fhirreference.FHIRReference] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(QuestionnaireResponse, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("authored", "authored", fhirdate.FHIRDate, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("item", "item", QuestionnaireResponseItem, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("questionnaire", "questionnaire", str, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class QuestionnaireResponseItem(backboneelement.BackboneElement):
    """ Groups and questions.

    A group or question item from the original questionnaire for which answers
    are provided.
    """
    resource_type: ClassVar[str] = "QuestionnaireResponseItem"
    answer: Optional[List[QuestionnaireResponseItemAnswer]] = empty_list()
    definition: Optional[str] = None
    item: Optional[List[QuestionnaireResponseItem]] = empty_list()
    linkId: str = None
    text: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(QuestionnaireResponseItem, self).elementProperties()
        js.extend([
            ("answer", "answer", QuestionnaireResponseItemAnswer, True, None, False),
            ("definition", "definition", str, False, None, False),
            ("item", "item", QuestionnaireResponseItem, True, None, False),
            ("linkId", "linkId", str, False, None, True),
            ("text", "text", str, False, None, False),
        ])
        return js

@dataclass
class QuestionnaireResponseItemAnswer(backboneelement.BackboneElement):
    """ The response(s) to the question.

    The respondent's answer(s) to the question.
    """
    resource_type: ClassVar[str] = "QuestionnaireResponseItemAnswer"
    item: Optional[List[QuestionnaireResponseItem]] = empty_list()
    valueAttachment: Optional[attachment.Attachment] = None
    valueBoolean: Optional[bool] = None
    valueCoding: Optional[coding.Coding] = None
    valueDate: Optional[fhirdate.FHIRDate] = None
    valueDateTime: Optional[fhirdate.FHIRDate] = None
    valueDecimal: Optional[float] = None
    valueInteger: Optional[int] = None
    valueQuantity: Optional[quantity.Quantity] = None
    valueReference: Optional[fhirreference.FHIRReference] = None
    valueString: Optional[str] = None
    valueTime: Optional[fhirdate.FHIRDate] = None
    valueUri: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(QuestionnaireResponseItemAnswer, self).elementProperties()
        js.extend([
            ("item", "item", QuestionnaireResponseItem, True, None, False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", False),
            ("valueDecimal", "valueDecimal", float, False, "value", False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", False),
            ("valueUri", "valueUri", str, False, "value", False),
        ])
        return js


import sys
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']