#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Contract) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .money import Money
from .period import Period
from .quantity import Quantity
from .signature import Signature
from .timing import Timing


@dataclass
class ContractTermSecurityLabel(BackboneElement):
    """ Protection for the Term.

    Security labels that protect the handling of information about the term and
    its elements, which may be specifically identified..
    """
    resource_type: ClassVar[str] = "ContractTermSecurityLabel"
    category: Optional[List[Coding]] = empty_list()
    classification: Coding = None
    control: Optional[List[Coding]] = empty_list()
    number: Optional[List[int]] = empty_list()

    def elementProperties(self):
        js = super(ContractTermSecurityLabel, self).elementProperties()
        js.extend([
            ("category", "category", Coding, True, None, False),
            ("classification", "classification", Coding, False, None, True),
            ("control", "control", Coding, True, None, False),
            ("number", "number", int, True, None, False),
        ])
        return js


@dataclass
class ContractTermOfferParty(BackboneElement):
    """ Offer Recipient.
    """
    resource_type: ClassVar[str] = "ContractTermOfferParty"
    reference: List[FHIRReference] = empty_list()
    role: CodeableConcept = None

    def elementProperties(self):
        js = super(ContractTermOfferParty, self).elementProperties()
        js.extend([
            ("reference", "reference", FHIRReference, True, None, True),
            ("role", "role", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class ContractTermOfferAnswer(BackboneElement):
    """ Response to offer text.
    """
    resource_type: ClassVar[str] = "ContractTermOfferAnswer"
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
        js = super(ContractTermOfferAnswer, self).elementProperties()
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
class ContractTermOffer(BackboneElement):
    """ Context of the Contract term.

    The matter of concern in the context of this provision of the agrement.
    """
    resource_type: ClassVar[str] = "ContractTermOffer"
    answer: Optional[List[ContractTermOfferAnswer]] = empty_list()
    decision: Optional[CodeableConcept] = None
    decisionMode: Optional[List[CodeableConcept]] = empty_list()
    identifier: Optional[List[Identifier]] = empty_list()
    linkId: Optional[List[str]] = empty_list()
    party: Optional[List[ContractTermOfferParty]] = empty_list()
    securityLabelNumber: Optional[List[int]] = empty_list()
    text: Optional[str] = None
    topic: Optional[FHIRReference] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ContractTermOffer, self).elementProperties()
        js.extend([
            ("answer", "answer", ContractTermOfferAnswer, True, None, False),
            ("decision", "decision", CodeableConcept, False, None, False),
            ("decisionMode", "decisionMode", CodeableConcept, True, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("linkId", "linkId", str, True, None, False),
            ("party", "party", ContractTermOfferParty, True, None, False),
            ("securityLabelNumber", "securityLabelNumber", int, True, None, False),
            ("text", "text", str, False, None, False),
            ("topic", "topic", FHIRReference, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ContractTermAssetValuedItem(BackboneElement):
    """ Contract Valued Item List.
    """
    resource_type: ClassVar[str] = "ContractTermAssetValuedItem"
    effectiveTime: Optional[FHIRDate] = None
    entityCodeableConcept: Optional[CodeableConcept] = None
    entityReference: Optional[FHIRReference] = None
    factor: Optional[float] = None
    identifier: Optional[Identifier] = None
    linkId: Optional[List[str]] = empty_list()
    net: Optional[Money] = None
    payment: Optional[str] = None
    paymentDate: Optional[FHIRDate] = None
    points: Optional[float] = None
    quantity: Optional[Quantity] = None
    recipient: Optional[FHIRReference] = None
    responsible: Optional[FHIRReference] = None
    securityLabelNumber: Optional[List[int]] = empty_list()
    unitPrice: Optional[Money] = None

    def elementProperties(self):
        js = super(ContractTermAssetValuedItem, self).elementProperties()
        js.extend([
            ("effectiveTime", "effectiveTime", FHIRDate, False, None, False),
            ("entityCodeableConcept", "entityCodeableConcept", CodeableConcept, False, "entity", False),
            ("entityReference", "entityReference", FHIRReference, False, "entity", False),
            ("factor", "factor", float, False, None, False),
            ("identifier", "identifier", Identifier, False, None, False),
            ("linkId", "linkId", str, True, None, False),
            ("net", "net", Money, False, None, False),
            ("payment", "payment", str, False, None, False),
            ("paymentDate", "paymentDate", FHIRDate, False, None, False),
            ("points", "points", float, False, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("recipient", "recipient", FHIRReference, False, None, False),
            ("responsible", "responsible", FHIRReference, False, None, False),
            ("securityLabelNumber", "securityLabelNumber", int, True, None, False),
            ("unitPrice", "unitPrice", Money, False, None, False),
        ])
        return js


@dataclass
class ContractTermAssetContext(BackboneElement):
    """ Circumstance of the asset.
    """
    resource_type: ClassVar[str] = "ContractTermAssetContext"
    code: Optional[List[CodeableConcept]] = empty_list()
    reference: Optional[FHIRReference] = None
    text: Optional[str] = None

    def elementProperties(self):
        js = super(ContractTermAssetContext, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, True, None, False),
            ("reference", "reference", FHIRReference, False, None, False),
            ("text", "text", str, False, None, False),
        ])
        return js


@dataclass
class ContractTermAsset(BackboneElement):
    """ Contract Term Asset List.
    """
    resource_type: ClassVar[str] = "ContractTermAsset"
    answer: Optional[List[ContractTermOfferAnswer]] = empty_list()
    condition: Optional[str] = None
    context: Optional[List[ContractTermAssetContext]] = empty_list()
    linkId: Optional[List[str]] = empty_list()
    period: Optional[List[Period]] = empty_list()
    periodType: Optional[List[CodeableConcept]] = empty_list()
    relationship: Optional[Coding] = None
    scope: Optional[CodeableConcept] = None
    securityLabelNumber: Optional[List[int]] = empty_list()
    subtype: Optional[List[CodeableConcept]] = empty_list()
    text: Optional[str] = None
    type: Optional[List[CodeableConcept]] = empty_list()
    typeReference: Optional[List[FHIRReference]] = empty_list()
    usePeriod: Optional[List[Period]] = empty_list()
    valuedItem: Optional[List[ContractTermAssetValuedItem]] = empty_list()

    def elementProperties(self):
        js = super(ContractTermAsset, self).elementProperties()
        js.extend([
            ("answer", "answer", ContractTermOfferAnswer, True, None, False),
            ("condition", "condition", str, False, None, False),
            ("context", "context", ContractTermAssetContext, True, None, False),
            ("linkId", "linkId", str, True, None, False),
            ("period", "period", Period, True, None, False),
            ("periodType", "periodType", CodeableConcept, True, None, False),
            ("relationship", "relationship", Coding, False, None, False),
            ("scope", "scope", CodeableConcept, False, None, False),
            ("securityLabelNumber", "securityLabelNumber", int, True, None, False),
            ("subtype", "subtype", CodeableConcept, True, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", CodeableConcept, True, None, False),
            ("typeReference", "typeReference", FHIRReference, True, None, False),
            ("usePeriod", "usePeriod", Period, True, None, False),
            ("valuedItem", "valuedItem", ContractTermAssetValuedItem, True, None, False),
        ])
        return js


@dataclass
class ContractTermActionSubject(BackboneElement):
    """ Entity of the action.
    """
    resource_type: ClassVar[str] = "ContractTermActionSubject"
    reference: List[FHIRReference] = empty_list()
    role: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ContractTermActionSubject, self).elementProperties()
        js.extend([
            ("reference", "reference", FHIRReference, True, None, True),
            ("role", "role", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ContractTermAction(BackboneElement):
    """ Entity being ascribed responsibility.

    An actor taking a role in an activity for which it can be assigned some
    degree of responsibility for the activity taking place.
    """
    resource_type: ClassVar[str] = "ContractTermAction"
    context: Optional[FHIRReference] = None
    contextLinkId: Optional[List[str]] = empty_list()
    doNotPerform: Optional[bool] = None
    intent: CodeableConcept = None
    linkId: Optional[List[str]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    occurrenceDateTime: Optional[FHIRDate] = None
    occurrencePeriod: Optional[Period] = None
    occurrenceTiming: Optional[Timing] = None
    performer: Optional[FHIRReference] = None
    performerLinkId: Optional[List[str]] = empty_list()
    performerRole: Optional[CodeableConcept] = None
    performerType: Optional[List[CodeableConcept]] = empty_list()
    reason: Optional[List[str]] = empty_list()
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonLinkId: Optional[List[str]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    requester: Optional[List[FHIRReference]] = empty_list()
    requesterLinkId: Optional[List[str]] = empty_list()
    securityLabelNumber: Optional[List[int]] = empty_list()
    status: CodeableConcept = None
    subject: Optional[List[ContractTermActionSubject]] = empty_list()
    type: CodeableConcept = None

    def elementProperties(self):
        js = super(ContractTermAction, self).elementProperties()
        js.extend([
            ("context", "context", FHIRReference, False, None, False),
            ("contextLinkId", "contextLinkId", str, True, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("intent", "intent", CodeableConcept, False, None, True),
            ("linkId", "linkId", str, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", Timing, False, "occurrence", False),
            ("performer", "performer", FHIRReference, False, None, False),
            ("performerLinkId", "performerLinkId", str, True, None, False),
            ("performerRole", "performerRole", CodeableConcept, False, None, False),
            ("performerType", "performerType", CodeableConcept, True, None, False),
            ("reason", "reason", str, True, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonLinkId", "reasonLinkId", str, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("requester", "requester", FHIRReference, True, None, False),
            ("requesterLinkId", "requesterLinkId", str, True, None, False),
            ("securityLabelNumber", "securityLabelNumber", int, True, None, False),
            ("status", "status", CodeableConcept, False, None, True),
            ("subject", "subject", ContractTermActionSubject, True, None, False),
            ("type", "type", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class ContractTerm(BackboneElement):
    """ Contract Term List.

    One or more Contract Provisions, which may be related and conveyed as a
    group, and may contain nested groups.
    """
    resource_type: ClassVar[str] = "ContractTerm"
    action: Optional[List[ContractTermAction]] = empty_list()
    applies: Optional[Period] = None
    asset: Optional[List[ContractTermAsset]] = empty_list()
    group: Optional[List[ContractTerm]] = empty_list()
    identifier: Optional[Identifier] = None
    issued: Optional[FHIRDate] = None
    offer: ContractTermOffer = None
    securityLabel: Optional[List[ContractTermSecurityLabel]] = empty_list()
    subType: Optional[CodeableConcept] = None
    text: Optional[str] = None
    topicCodeableConcept: Optional[CodeableConcept] = None
    topicReference: Optional[FHIRReference] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ContractTerm, self).elementProperties()
        js.extend([
            ("action", "action", ContractTermAction, True, None, False),
            ("applies", "applies", Period, False, None, False),
            ("asset", "asset", ContractTermAsset, True, None, False),
            ("group", "group", ContractTerm, True, None, False),
            ("identifier", "identifier", Identifier, False, None, False),
            ("issued", "issued", FHIRDate, False, None, False),
            ("offer", "offer", ContractTermOffer, False, None, True),
            ("securityLabel", "securityLabel", ContractTermSecurityLabel, True, None, False),
            ("subType", "subType", CodeableConcept, False, None, False),
            ("text", "text", str, False, None, False),
            ("topicCodeableConcept", "topicCodeableConcept", CodeableConcept, False, "topic", False),
            ("topicReference", "topicReference", FHIRReference, False, "topic", False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ContractSigner(BackboneElement):
    """ Contract Signatory.

    Parties with legal standing in the Contract, including the principal
    parties, the grantor(s) and grantee(s), which are any person or
    organization bound by the contract, and any ancillary parties, which
    facilitate the execution of the contract such as a notary or witness.
    """
    resource_type: ClassVar[str] = "ContractSigner"
    party: FHIRReference = None
    signature: List[Signature] = empty_list()
    type: Coding = None

    def elementProperties(self):
        js = super(ContractSigner, self).elementProperties()
        js.extend([
            ("party", "party", FHIRReference, False, None, True),
            ("signature", "signature", Signature, True, None, True),
            ("type", "type", Coding, False, None, True),
        ])
        return js


@dataclass
class ContractRule(BackboneElement):
    """ Computable Contract Language.

    List of Computable Policy Rule Language Representations of this Contract.
    """
    resource_type: ClassVar[str] = "ContractRule"
    contentAttachment: Attachment = None
    contentReference: FHIRReference = None

    def elementProperties(self):
        js = super(ContractRule, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", Attachment, False, "content", True),
            ("contentReference", "contentReference", FHIRReference, False, "content", True),
        ])
        return js


@dataclass
class ContractLegal(BackboneElement):
    """ Contract Legal Language.

    List of Legal expressions or representations of this Contract.
    """
    resource_type: ClassVar[str] = "ContractLegal"
    contentAttachment: Attachment = None
    contentReference: FHIRReference = None

    def elementProperties(self):
        js = super(ContractLegal, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", Attachment, False, "content", True),
            ("contentReference", "contentReference", FHIRReference, False, "content", True),
        ])
        return js


@dataclass
class ContractFriendly(BackboneElement):
    """ Contract Friendly Language.

    The "patient friendly language" versionof the Contract in whole or in
    parts. "Patient friendly language" means the representation of the Contract
    and Contract Provisions in a manner that is readily accessible and
    understandable by a layperson in accordance with best practices for
    communication styles that ensure that those agreeing to or signing the
    Contract understand the roles, actions, obligations, responsibilities, and
    implication of the agreement.
    """
    resource_type: ClassVar[str] = "ContractFriendly"
    contentAttachment: Attachment = None
    contentReference: FHIRReference = None

    def elementProperties(self):
        js = super(ContractFriendly, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", Attachment, False, "content", True),
            ("contentReference", "contentReference", FHIRReference, False, "content", True),
        ])
        return js


@dataclass
class ContractContentDefinition(BackboneElement):
    """ Contract precursor content.

    Precusory content developed with a focus and intent of supporting the
    formation a Contract instance, which may be associated with and
    transformable into a Contract.
    """
    resource_type: ClassVar[str] = "ContractContentDefinition"
    copyright: Optional[str] = None
    publicationDate: Optional[FHIRDate] = None
    publicationStatus: str = None
    publisher: Optional[FHIRReference] = None
    subType: Optional[CodeableConcept] = None
    type: CodeableConcept = None

    def elementProperties(self):
        js = super(ContractContentDefinition, self).elementProperties()
        js.extend([
            ("copyright", "copyright", str, False, None, False),
            ("publicationDate", "publicationDate", FHIRDate, False, None, False),
            ("publicationStatus", "publicationStatus", str, False, None, True),
            ("publisher", "publisher", FHIRReference, False, None, False),
            ("subType", "subType", CodeableConcept, False, None, False),
            ("type", "type", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class Contract(DomainResource):
    """ Legal Agreement.

    Legally enforceable, formally recorded unilateral or bilateral directive
    i.e., a policy or agreement.
    """
    resource_type: ClassVar[str] = "Contract"
    alias: Optional[List[str]] = empty_list()
    applies: Optional[Period] = None
    author: Optional[FHIRReference] = None
    authority: Optional[List[FHIRReference]] = empty_list()
    contentDefinition: Optional[ContractContentDefinition] = None
    contentDerivative: Optional[CodeableConcept] = None
    domain: Optional[List[FHIRReference]] = empty_list()
    expirationType: Optional[CodeableConcept] = None
    friendly: Optional[List[ContractFriendly]] = empty_list()
    identifier: Optional[List[Identifier]] = empty_list()
    instantiatesCanonical: Optional[FHIRReference] = None
    instantiatesUri: Optional[str] = None
    issued: Optional[FHIRDate] = None
    legal: Optional[List[ContractLegal]] = empty_list()
    legalState: Optional[CodeableConcept] = None
    legallyBindingAttachment: Optional[Attachment] = None
    legallyBindingReference: Optional[FHIRReference] = None
    name: Optional[str] = None
    relevantHistory: Optional[List[FHIRReference]] = empty_list()
    rule: Optional[List[ContractRule]] = empty_list()
    scope: Optional[CodeableConcept] = None
    signer: Optional[List[ContractSigner]] = empty_list()
    site: Optional[List[FHIRReference]] = empty_list()
    status: Optional[str] = None
    subType: Optional[List[CodeableConcept]] = empty_list()
    subject: Optional[List[FHIRReference]] = empty_list()
    subtitle: Optional[str] = None
    supportingInfo: Optional[List[FHIRReference]] = empty_list()
    term: Optional[List[ContractTerm]] = empty_list()
    title: Optional[str] = None
    topicCodeableConcept: Optional[CodeableConcept] = None
    topicReference: Optional[FHIRReference] = None
    type: Optional[CodeableConcept] = None
    url: Optional[str] = None
    version: Optional[str] = None

    def elementProperties(self):
        js = super(Contract, self).elementProperties()
        js.extend([
            ("alias", "alias", str, True, None, False),
            ("applies", "applies", Period, False, None, False),
            ("author", "author", FHIRReference, False, None, False),
            ("authority", "authority", FHIRReference, True, None, False),
            ("contentDefinition", "contentDefinition", ContractContentDefinition, False, None, False),
            ("contentDerivative", "contentDerivative", CodeableConcept, False, None, False),
            ("domain", "domain", FHIRReference, True, None, False),
            ("expirationType", "expirationType", CodeableConcept, False, None, False),
            ("friendly", "friendly", ContractFriendly, True, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", FHIRReference, False, None, False),
            ("instantiatesUri", "instantiatesUri", str, False, None, False),
            ("issued", "issued", FHIRDate, False, None, False),
            ("legal", "legal", ContractLegal, True, None, False),
            ("legalState", "legalState", CodeableConcept, False, None, False),
            ("legallyBindingAttachment", "legallyBindingAttachment", Attachment, False, "legallyBinding", False),
            ("legallyBindingReference", "legallyBindingReference", FHIRReference, False, "legallyBinding", False),
            ("name", "name", str, False, None, False),
            ("relevantHistory", "relevantHistory", FHIRReference, True, None, False),
            ("rule", "rule", ContractRule, True, None, False),
            ("scope", "scope", CodeableConcept, False, None, False),
            ("signer", "signer", ContractSigner, True, None, False),
            ("site", "site", FHIRReference, True, None, False),
            ("status", "status", str, False, None, False),
            ("subType", "subType", CodeableConcept, True, None, False),
            ("subject", "subject", FHIRReference, True, None, False),
            ("subtitle", "subtitle", str, False, None, False),
            ("supportingInfo", "supportingInfo", FHIRReference, True, None, False),
            ("term", "term", ContractTerm, True, None, False),
            ("title", "title", str, False, None, False),
            ("topicCodeableConcept", "topicCodeableConcept", CodeableConcept, False, "topic", False),
            ("topicReference", "topicReference", FHIRReference, False, "topic", False),
            ("type", "type", CodeableConcept, False, None, False),
            ("url", "url", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js