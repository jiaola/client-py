#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Questionnaire) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import backboneelement
from . import codeableconcept
from . import coding
from . import contactdetail
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import usagecontext

from . import domainresource

@dataclass
class Questionnaire(domainresource.DomainResource):
    """ A structured set of questions.

    A structured set of questions intended to guide the collection of answers
    from end-users. Questionnaires provide detailed control over order,
    presentation, phraseology and grouping to allow coherent, consistent data
    collection.
    """
    resource_type: ClassVar[str] = "Questionnaire"
    approvalDate: Optional[fhirdate.FHIRDate] = None
    code: Optional[List[coding.Coding]] = empty_list()
    contact: Optional[List[contactdetail.ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date: Optional[fhirdate.FHIRDate] = None
    derivedFrom: Optional[List[str]] = empty_list()
    description: Optional[str] = None
    effectivePeriod: Optional[period.Period] = None
    experimental: Optional[bool] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    item: Optional[List[QuestionnaireItem]] = empty_list()
    jurisdiction: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    lastReviewDate: Optional[fhirdate.FHIRDate] = None
    name: Optional[str] = None
    publisher: Optional[str] = None
    purpose: Optional[str] = None
    status: str = None
    subjectType: Optional[List[str]] = empty_list()
    title: Optional[str] = None
    url: Optional[str] = None
    useContext: Optional[List[usagecontext.UsageContext]] = empty_list()
    version: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Questionnaire, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("code", "code", coding.Coding, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("derivedFrom", "derivedFrom", str, True, None, False),
            ("description", "description", str, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("item", "item", QuestionnaireItem, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("name", "name", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("subjectType", "subjectType", str, True, None, False),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class QuestionnaireItem(backboneelement.BackboneElement):
    """ Questions and sections within the Questionnaire.

    A particular question, question grouping or display text that is part of
    the questionnaire.
    """
    resource_type: ClassVar[str] = "QuestionnaireItem"
    answerOption: Optional[List[QuestionnaireItemAnswerOption]] = empty_list()
    answerValueSet: Optional[str] = None
    code: Optional[List[coding.Coding]] = empty_list()
    definition: Optional[str] = None
    enableBehavior: Optional[str] = None
    enableWhen: Optional[List[QuestionnaireItemEnableWhen]] = empty_list()
    initial: Optional[List[QuestionnaireItemInitial]] = empty_list()
    item: Optional[List[QuestionnaireItem]] = empty_list()
    linkId: str = None
    maxLength: Optional[int] = None
    prefix: Optional[str] = None
    readOnly: Optional[bool] = None
    repeats: Optional[bool] = None
    required: Optional[bool] = None
    text: Optional[str] = None
    type: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(QuestionnaireItem, self).elementProperties()
        js.extend([
            ("answerOption", "answerOption", QuestionnaireItemAnswerOption, True, None, False),
            ("answerValueSet", "answerValueSet", str, False, None, False),
            ("code", "code", coding.Coding, True, None, False),
            ("definition", "definition", str, False, None, False),
            ("enableBehavior", "enableBehavior", str, False, None, False),
            ("enableWhen", "enableWhen", QuestionnaireItemEnableWhen, True, None, False),
            ("initial", "initial", QuestionnaireItemInitial, True, None, False),
            ("item", "item", QuestionnaireItem, True, None, False),
            ("linkId", "linkId", str, False, None, True),
            ("maxLength", "maxLength", int, False, None, False),
            ("prefix", "prefix", str, False, None, False),
            ("readOnly", "readOnly", bool, False, None, False),
            ("repeats", "repeats", bool, False, None, False),
            ("required", "required", bool, False, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js

@dataclass
class QuestionnaireItemAnswerOption(backboneelement.BackboneElement):
    """ Permitted answer.

    One of the permitted answers for a "choice" or "open-choice" question.
    """
    resource_type: ClassVar[str] = "QuestionnaireItemAnswerOption"
    initialSelected: Optional[bool] = None
    valueCoding:coding.Coding = None
    valueDate:fhirdate.FHIRDate = None
    valueInteger: int = None
    valueReference:fhirreference.FHIRReference = None
    valueString: str = None
    valueTime:fhirdate.FHIRDate = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(QuestionnaireItemAnswerOption, self).elementProperties()
        js.extend([
            ("initialSelected", "initialSelected", bool, False, None, False),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", True),
        ])
        return js

@dataclass
class QuestionnaireItemEnableWhen(backboneelement.BackboneElement):
    """ Only allow data when.

    A constraint indicating that this item should only be enabled
    (displayed/allow answers to be captured) when the specified condition is
    true.
    """
    resource_type: ClassVar[str] = "QuestionnaireItemEnableWhen"
    answerBoolean: bool = None
    answerCoding:coding.Coding = None
    answerDate:fhirdate.FHIRDate = None
    answerDateTime:fhirdate.FHIRDate = None
    answerDecimal: float = None
    answerInteger: int = None
    answerQuantity:quantity.Quantity = None
    answerReference:fhirreference.FHIRReference = None
    answerString: str = None
    answerTime:fhirdate.FHIRDate = None
    operator: str = None
    question: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(QuestionnaireItemEnableWhen, self).elementProperties()
        js.extend([
            ("answerBoolean", "answerBoolean", bool, False, "answer", True),
            ("answerCoding", "answerCoding", coding.Coding, False, "answer", True),
            ("answerDate", "answerDate", fhirdate.FHIRDate, False, "answer", True),
            ("answerDateTime", "answerDateTime", fhirdate.FHIRDate, False, "answer", True),
            ("answerDecimal", "answerDecimal", float, False, "answer", True),
            ("answerInteger", "answerInteger", int, False, "answer", True),
            ("answerQuantity", "answerQuantity", quantity.Quantity, False, "answer", True),
            ("answerReference", "answerReference", fhirreference.FHIRReference, False, "answer", True),
            ("answerString", "answerString", str, False, "answer", True),
            ("answerTime", "answerTime", fhirdate.FHIRDate, False, "answer", True),
            ("operator", "operator", str, False, None, True),
            ("question", "question", str, False, None, True),
        ])
        return js

@dataclass
class QuestionnaireItemInitial(backboneelement.BackboneElement):
    """ Initial value(s) when item is first rendered.

    One or more values that should be pre-populated in the answer when
    initially rendering the questionnaire for user input.
    """
    resource_type: ClassVar[str] = "QuestionnaireItemInitial"
    valueAttachment:attachment.Attachment = None
    valueBoolean: bool = None
    valueCoding:coding.Coding = None
    valueDate:fhirdate.FHIRDate = None
    valueDateTime:fhirdate.FHIRDate = None
    valueDecimal: float = None
    valueInteger: int = None
    valueQuantity:quantity.Quantity = None
    valueReference:fhirreference.FHIRReference = None
    valueString: str = None
    valueTime:fhirdate.FHIRDate = None
    valueUri: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(QuestionnaireItemInitial, self).elementProperties()
        js.extend([
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", True),
            ("valueUri", "valueUri", str, False, "value", True),
        ])
        return js


import sys
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
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
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']