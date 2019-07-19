#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Questionnaire) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity
from .usagecontext import UsageContext


@dataclass
class QuestionnaireItemInitial(BackboneElement):
    """ Initial value(s) when item is first rendered.

    One or more values that should be pre-populated in the answer when
    initially rendering the questionnaire for user input.
    """
    resource_type: ClassVar[str] = "QuestionnaireItemInitial"
    valueAttachment: Attachment = None
    valueBoolean: bool = None
    valueCoding: Coding = None
    valueDate: FHIRDate = None
    valueDateTime: FHIRDate = None
    valueDecimal: float = None
    valueInteger: int = None
    valueQuantity: Quantity = None
    valueReference: FHIRReference = None
    valueString: str = None
    valueTime: FHIRDate = None
    valueUri: str = None

    def elementProperties(self):
        js = super(QuestionnaireItemInitial, self).elementProperties()
        js.extend([
            ("valueAttachment", "valueAttachment", Attachment, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCoding", "valueCoding", Coding, False, "value", True),
            ("valueDate", "valueDate", FHIRDate, False, "value", True),
            ("valueDateTime", "valueDateTime", FHIRDate, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueQuantity", "valueQuantity", Quantity, False, "value", True),
            ("valueReference", "valueReference", FHIRReference, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueTime", "valueTime", FHIRDate, False, "value", True),
            ("valueUri", "valueUri", str, False, "value", True),
        ])
        return js


@dataclass
class QuestionnaireItemEnableWhen(BackboneElement):
    """ Only allow data when.

    A constraint indicating that this item should only be enabled
    (displayed/allow answers to be captured) when the specified condition is
    true.
    """
    resource_type: ClassVar[str] = "QuestionnaireItemEnableWhen"
    answerBoolean: bool = None
    answerCoding: Coding = None
    answerDate: FHIRDate = None
    answerDateTime: FHIRDate = None
    answerDecimal: float = None
    answerInteger: int = None
    answerQuantity: Quantity = None
    answerReference: FHIRReference = None
    answerString: str = None
    answerTime: FHIRDate = None
    operator: str = None
    question: str = None

    def elementProperties(self):
        js = super(QuestionnaireItemEnableWhen, self).elementProperties()
        js.extend([
            ("answerBoolean", "answerBoolean", bool, False, "answer", True),
            ("answerCoding", "answerCoding", Coding, False, "answer", True),
            ("answerDate", "answerDate", FHIRDate, False, "answer", True),
            ("answerDateTime", "answerDateTime", FHIRDate, False, "answer", True),
            ("answerDecimal", "answerDecimal", float, False, "answer", True),
            ("answerInteger", "answerInteger", int, False, "answer", True),
            ("answerQuantity", "answerQuantity", Quantity, False, "answer", True),
            ("answerReference", "answerReference", FHIRReference, False, "answer", True),
            ("answerString", "answerString", str, False, "answer", True),
            ("answerTime", "answerTime", FHIRDate, False, "answer", True),
            ("operator", "operator", str, False, None, True),
            ("question", "question", str, False, None, True),
        ])
        return js


@dataclass
class QuestionnaireItemAnswerOption(BackboneElement):
    """ Permitted answer.

    One of the permitted answers for a "choice" or "open-choice" question.
    """
    resource_type: ClassVar[str] = "QuestionnaireItemAnswerOption"
    initialSelected: Optional[bool] = None
    valueCoding: Coding = None
    valueDate: FHIRDate = None
    valueInteger: int = None
    valueReference: FHIRReference = None
    valueString: str = None
    valueTime: FHIRDate = None

    def elementProperties(self):
        js = super(QuestionnaireItemAnswerOption, self).elementProperties()
        js.extend([
            ("initialSelected", "initialSelected", bool, False, None, False),
            ("valueCoding", "valueCoding", Coding, False, "value", True),
            ("valueDate", "valueDate", FHIRDate, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueReference", "valueReference", FHIRReference, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueTime", "valueTime", FHIRDate, False, "value", True),
        ])
        return js


@dataclass
class QuestionnaireItem(BackboneElement):
    """ Questions and sections within the Questionnaire.

    A particular question, question grouping or display text that is part of
    the questionnaire.
    """
    resource_type: ClassVar[str] = "QuestionnaireItem"
    answerOption: Optional[List[QuestionnaireItemAnswerOption]] = empty_list()
    answerValueSet: Optional[str] = None
    code: Optional[List[Coding]] = empty_list()
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

    def elementProperties(self):
        js = super(QuestionnaireItem, self).elementProperties()
        js.extend([
            ("answerOption", "answerOption", QuestionnaireItemAnswerOption, True, None, False),
            ("answerValueSet", "answerValueSet", str, False, None, False),
            ("code", "code", Coding, True, None, False),
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
class Questionnaire(DomainResource):
    """ A structured set of questions.

    A structured set of questions intended to guide the collection of answers
    from end-users. Questionnaires provide detailed control over order,
    presentation, phraseology and grouping to allow coherent, consistent data
    collection.
    """
    resource_type: ClassVar[str] = "Questionnaire"
    approvalDate: Optional[FHIRDate] = None
    code: Optional[List[Coding]] = empty_list()
    contact: Optional[List[ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date: Optional[FHIRDate] = None
    derivedFrom: Optional[List[str]] = empty_list()
    description: Optional[str] = None
    effectivePeriod: Optional[Period] = None
    experimental: Optional[bool] = None
    identifier: Optional[List[Identifier]] = empty_list()
    item: Optional[List[QuestionnaireItem]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    lastReviewDate: Optional[FHIRDate] = None
    name: Optional[str] = None
    publisher: Optional[str] = None
    purpose: Optional[str] = None
    status: str = None
    subjectType: Optional[List[str]] = empty_list()
    title: Optional[str] = None
    url: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    version: Optional[str] = None

    def elementProperties(self):
        js = super(Questionnaire, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", FHIRDate, False, None, False),
            ("code", "code", Coding, True, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("derivedFrom", "derivedFrom", str, True, None, False),
            ("description", "description", str, False, None, False),
            ("effectivePeriod", "effectivePeriod", Period, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("item", "item", QuestionnaireItem, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", FHIRDate, False, None, False),
            ("name", "name", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("subjectType", "subjectType", str, True, None, False),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js