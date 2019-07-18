#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Contract) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import attachment
from . import backboneelement
from . import codeableconcept
from . import coding
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity
from . import signature
from . import timing

from . import backboneelement

@dataclass
class ContractTermSecurityLabel(backboneelement.BackboneElement):
    """ Protection for the Term.

    Security labels that protect the handling of information about the term and
    its elements, which may be specifically identified..
    """
    resource_type: ClassVar[str] = "ContractTermSecurityLabel"
    category: Optional[List[coding.Coding]] = empty_list()
    classification:coding.Coding = None
    control: Optional[List[coding.Coding]] = empty_list()
    number: Optional[List[int]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ContractTermSecurityLabel, self).elementProperties()
        js.extend([
            ("category", "category", coding.Coding, True, None, False),
            ("classification", "classification", coding.Coding, False, None, True),
            ("control", "control", coding.Coding, True, None, False),
            ("number", "number", int, True, None, False),
        ])
        return js

@dataclass
class ContractTermOfferParty(backboneelement.BackboneElement):
    """ Offer Recipient.
    """
    resource_type: ClassVar[str] = "ContractTermOfferParty"
    reference: List[fhirreference.FHIRReference] = empty_list()
    role:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ContractTermOfferParty, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, True, None, True),
            ("role", "role", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js

@dataclass
class ContractTermOfferAnswer(backboneelement.BackboneElement):
    """ Response to offer text.
    """
    resource_type: ClassVar[str] = "ContractTermOfferAnswer"
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
        js = super(ContractTermOfferAnswer, self).elementProperties()
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

@dataclass
class ContractTermOffer(backboneelement.BackboneElement):
    """ Context of the Contract term.

    The matter of concern in the context of this provision of the agrement.
    """
    resource_type: ClassVar[str] = "ContractTermOffer"
    answer: Optional[List[ContractTermOfferAnswer]] = empty_list()
    decision: Optional[codeableconcept.CodeableConcept] = None
    decisionMode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    linkId: Optional[List[str]] = empty_list()
    party: Optional[List[ContractTermOfferParty]] = empty_list()
    securityLabelNumber: Optional[List[int]] = empty_list()
    text: Optional[str] = None
    topic: Optional[fhirreference.FHIRReference] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ContractTermOffer, self).elementProperties()
        js.extend([
            ("answer", "answer", ContractTermOfferAnswer, True, None, False),
            ("decision", "decision", codeableconcept.CodeableConcept, False, None, False),
            ("decisionMode", "decisionMode", codeableconcept.CodeableConcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("linkId", "linkId", str, True, None, False),
            ("party", "party", ContractTermOfferParty, True, None, False),
            ("securityLabelNumber", "securityLabelNumber", int, True, None, False),
            ("text", "text", str, False, None, False),
            ("topic", "topic", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class ContractTermAssetValuedItem(backboneelement.BackboneElement):
    """ Contract Valued Item List.
    """
    resource_type: ClassVar[str] = "ContractTermAssetValuedItem"
    effectiveTime: Optional[fhirdate.FHIRDate] = None
    entityCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    entityReference: Optional[fhirreference.FHIRReference] = None
    factor: Optional[float] = None
    identifier: Optional[identifier.Identifier] = None
    linkId: Optional[List[str]] = empty_list()
    net: Optional[money.Money] = None
    payment: Optional[str] = None
    paymentDate: Optional[fhirdate.FHIRDate] = None
    points: Optional[float] = None
    quantity: Optional[quantity.Quantity] = None
    recipient: Optional[fhirreference.FHIRReference] = None
    responsible: Optional[fhirreference.FHIRReference] = None
    securityLabelNumber: Optional[List[int]] = empty_list()
    unitPrice: Optional[money.Money] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ContractTermAssetValuedItem, self).elementProperties()
        js.extend([
            ("effectiveTime", "effectiveTime", fhirdate.FHIRDate, False, None, False),
            ("entityCodeableConcept", "entityCodeableConcept", codeableconcept.CodeableConcept, False, "entity", False),
            ("entityReference", "entityReference", fhirreference.FHIRReference, False, "entity", False),
            ("factor", "factor", float, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("linkId", "linkId", str, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("payment", "payment", str, False, None, False),
            ("paymentDate", "paymentDate", fhirdate.FHIRDate, False, None, False),
            ("points", "points", float, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, False, None, False),
            ("responsible", "responsible", fhirreference.FHIRReference, False, None, False),
            ("securityLabelNumber", "securityLabelNumber", int, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js

@dataclass
class ContractTermAssetContext(backboneelement.BackboneElement):
    """ Circumstance of the asset.
    """
    resource_type: ClassVar[str] = "ContractTermAssetContext"
    code: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    reference: Optional[fhirreference.FHIRReference] = None
    text: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ContractTermAssetContext, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("reference", "reference", fhirreference.FHIRReference, False, None, False),
            ("text", "text", str, False, None, False),
        ])
        return js

@dataclass
class ContractTermAsset(backboneelement.BackboneElement):
    """ Contract Term Asset List.
    """
    resource_type: ClassVar[str] = "ContractTermAsset"
    answer: Optional[List[ContractTermOfferAnswer]] = empty_list()
    condition: Optional[str] = None
    context: Optional[List[ContractTermAssetContext]] = empty_list()
    linkId: Optional[List[str]] = empty_list()
    period: Optional[List[period.Period]] = empty_list()
    periodType: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    relationship: Optional[coding.Coding] = None
    scope: Optional[codeableconcept.CodeableConcept] = None
    securityLabelNumber: Optional[List[int]] = empty_list()
    subtype: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    text: Optional[str] = None
    type: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    typeReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    usePeriod: Optional[List[period.Period]] = empty_list()
    valuedItem: Optional[List[ContractTermAssetValuedItem]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ContractTermAsset, self).elementProperties()
        js.extend([
            ("answer", "answer", ContractTermOfferAnswer, True, None, False),
            ("condition", "condition", str, False, None, False),
            ("context", "context", ContractTermAssetContext, True, None, False),
            ("linkId", "linkId", str, True, None, False),
            ("period", "period", period.Period, True, None, False),
            ("periodType", "periodType", codeableconcept.CodeableConcept, True, None, False),
            ("relationship", "relationship", coding.Coding, False, None, False),
            ("scope", "scope", codeableconcept.CodeableConcept, False, None, False),
            ("securityLabelNumber", "securityLabelNumber", int, True, None, False),
            ("subtype", "subtype", codeableconcept.CodeableConcept, True, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("typeReference", "typeReference", fhirreference.FHIRReference, True, None, False),
            ("usePeriod", "usePeriod", period.Period, True, None, False),
            ("valuedItem", "valuedItem", ContractTermAssetValuedItem, True, None, False),
        ])
        return js

@dataclass
class ContractTermActionSubject(backboneelement.BackboneElement):
    """ Entity of the action.
    """
    resource_type: ClassVar[str] = "ContractTermActionSubject"
    reference: List[fhirreference.FHIRReference] = empty_list()
    role: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ContractTermActionSubject, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, True, None, True),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class ContractTermAction(backboneelement.BackboneElement):
    """ Entity being ascribed responsibility.

    An actor taking a role in an activity for which it can be assigned some
    degree of responsibility for the activity taking place.
    """
    resource_type: ClassVar[str] = "ContractTermAction"
    context: Optional[fhirreference.FHIRReference] = None
    contextLinkId: Optional[List[str]] = empty_list()
    doNotPerform: Optional[bool] = None
    intent:codeableconcept.CodeableConcept = None
    linkId: Optional[List[str]] = empty_list()
    note: Optional[List[annotation.Annotation]] = empty_list()
    occurrenceDateTime: Optional[fhirdate.FHIRDate] = None
    occurrencePeriod: Optional[period.Period] = None
    occurrenceTiming: Optional[timing.Timing] = None
    performer: Optional[fhirreference.FHIRReference] = None
    performerLinkId: Optional[List[str]] = empty_list()
    performerRole: Optional[codeableconcept.CodeableConcept] = None
    performerType: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    reason: Optional[List[str]] = empty_list()
    reasonCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    reasonLinkId: Optional[List[str]] = empty_list()
    reasonReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    requester: Optional[List[fhirreference.FHIRReference]] = empty_list()
    requesterLinkId: Optional[List[str]] = empty_list()
    securityLabelNumber: Optional[List[int]] = empty_list()
    status:codeableconcept.CodeableConcept = None
    subject: Optional[List[ContractTermActionSubject]] = empty_list()
    type:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ContractTermAction, self).elementProperties()
        js.extend([
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("contextLinkId", "contextLinkId", str, True, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("intent", "intent", codeableconcept.CodeableConcept, False, None, True),
            ("linkId", "linkId", str, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("performerLinkId", "performerLinkId", str, True, None, False),
            ("performerRole", "performerRole", codeableconcept.CodeableConcept, False, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, True, None, False),
            ("reason", "reason", str, True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonLinkId", "reasonLinkId", str, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("requester", "requester", fhirreference.FHIRReference, True, None, False),
            ("requesterLinkId", "requesterLinkId", str, True, None, False),
            ("securityLabelNumber", "securityLabelNumber", int, True, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, True),
            ("subject", "subject", ContractTermActionSubject, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js

@dataclass
class ContractTerm(backboneelement.BackboneElement):
    """ Contract Term List.

    One or more Contract Provisions, which may be related and conveyed as a
    group, and may contain nested groups.
    """
    resource_type: ClassVar[str] = "ContractTerm"
    action: Optional[List[ContractTermAction]] = empty_list()
    applies: Optional[period.Period] = None
    asset: Optional[List[ContractTermAsset]] = empty_list()
    group: Optional[List[ContractTerm]] = empty_list()
    identifier: Optional[identifier.Identifier] = None
    issued: Optional[fhirdate.FHIRDate] = None
    offer: ContractTermOffer = None
    securityLabel: Optional[List[ContractTermSecurityLabel]] = empty_list()
    subType: Optional[codeableconcept.CodeableConcept] = None
    text: Optional[str] = None
    topicCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    topicReference: Optional[fhirreference.FHIRReference] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ContractTerm, self).elementProperties()
        js.extend([
            ("action", "action", ContractTermAction, True, None, False),
            ("applies", "applies", period.Period, False, None, False),
            ("asset", "asset", ContractTermAsset, True, None, False),
            ("group", "group", ContractTerm, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("issued", "issued", fhirdate.FHIRDate, False, None, False),
            ("offer", "offer", ContractTermOffer, False, None, True),
            ("securityLabel", "securityLabel", ContractTermSecurityLabel, True, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False),
            ("text", "text", str, False, None, False),
            ("topicCodeableConcept", "topicCodeableConcept", codeableconcept.CodeableConcept, False, "topic", False),
            ("topicReference", "topicReference", fhirreference.FHIRReference, False, "topic", False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class ContractSigner(backboneelement.BackboneElement):
    """ Contract Signatory.

    Parties with legal standing in the Contract, including the principal
    parties, the grantor(s) and grantee(s), which are any person or
    organization bound by the contract, and any ancillary parties, which
    facilitate the execution of the contract such as a notary or witness.
    """
    resource_type: ClassVar[str] = "ContractSigner"
    party:fhirreference.FHIRReference = None
    signature: List[signature.Signature] = empty_list()
    type:coding.Coding = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ContractSigner, self).elementProperties()
        js.extend([
            ("party", "party", fhirreference.FHIRReference, False, None, True),
            ("signature", "signature", signature.Signature, True, None, True),
            ("type", "type", coding.Coding, False, None, True),
        ])
        return js

@dataclass
class ContractRule(backboneelement.BackboneElement):
    """ Computable Contract Language.

    List of Computable Policy Rule Language Representations of this Contract.
    """
    resource_type: ClassVar[str] = "ContractRule"
    contentAttachment:attachment.Attachment = None
    contentReference:fhirreference.FHIRReference = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ContractRule, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True),
        ])
        return js

@dataclass
class ContractLegal(backboneelement.BackboneElement):
    """ Contract Legal Language.

    List of Legal expressions or representations of this Contract.
    """
    resource_type: ClassVar[str] = "ContractLegal"
    contentAttachment:attachment.Attachment = None
    contentReference:fhirreference.FHIRReference = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ContractLegal, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True),
        ])
        return js

@dataclass
class ContractFriendly(backboneelement.BackboneElement):
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
    contentAttachment:attachment.Attachment = None
    contentReference:fhirreference.FHIRReference = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ContractFriendly, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True),
        ])
        return js

@dataclass
class ContractContentDefinition(backboneelement.BackboneElement):
    """ Contract precursor content.

    Precusory content developed with a focus and intent of supporting the
    formation a Contract instance, which may be associated with and
    transformable into a Contract.
    """
    resource_type: ClassVar[str] = "ContractContentDefinition"
    copyright: Optional[str] = None
    publicationDate: Optional[fhirdate.FHIRDate] = None
    publicationStatus: str = None
    publisher: Optional[fhirreference.FHIRReference] = None
    subType: Optional[codeableconcept.CodeableConcept] = None
    type:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ContractContentDefinition, self).elementProperties()
        js.extend([
            ("copyright", "copyright", str, False, None, False),
            ("publicationDate", "publicationDate", fhirdate.FHIRDate, False, None, False),
            ("publicationStatus", "publicationStatus", str, False, None, True),
            ("publisher", "publisher", fhirreference.FHIRReference, False, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js

from . import domainresource

@dataclass
class Contract(domainresource.DomainResource):
    """ Legal Agreement.

    Legally enforceable, formally recorded unilateral or bilateral directive
    i.e., a policy or agreement.
    """
    resource_type: ClassVar[str] = "Contract"
    alias: Optional[List[str]] = empty_list()
    applies: Optional[period.Period] = None
    author: Optional[fhirreference.FHIRReference] = None
    authority: Optional[List[fhirreference.FHIRReference]] = empty_list()
    contentDefinition: Optional[ContractContentDefinition] = None
    contentDerivative: Optional[codeableconcept.CodeableConcept] = None
    domain: Optional[List[fhirreference.FHIRReference]] = empty_list()
    expirationType: Optional[codeableconcept.CodeableConcept] = None
    friendly: Optional[List[ContractFriendly]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    instantiatesCanonical: Optional[fhirreference.FHIRReference] = None
    instantiatesUri: Optional[str] = None
    issued: Optional[fhirdate.FHIRDate] = None
    legal: Optional[List[ContractLegal]] = empty_list()
    legalState: Optional[codeableconcept.CodeableConcept] = None
    legallyBindingAttachment: Optional[attachment.Attachment] = None
    legallyBindingReference: Optional[fhirreference.FHIRReference] = None
    name: Optional[str] = None
    relevantHistory: Optional[List[fhirreference.FHIRReference]] = empty_list()
    rule: Optional[List[ContractRule]] = empty_list()
    scope: Optional[codeableconcept.CodeableConcept] = None
    signer: Optional[List[ContractSigner]] = empty_list()
    site: Optional[List[fhirreference.FHIRReference]] = empty_list()
    status: Optional[str] = None
    subType: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    subject: Optional[List[fhirreference.FHIRReference]] = empty_list()
    subtitle: Optional[str] = None
    supportingInfo: Optional[List[fhirreference.FHIRReference]] = empty_list()
    term: Optional[List[ContractTerm]] = empty_list()
    title: Optional[str] = None
    topicCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    topicReference: Optional[fhirreference.FHIRReference] = None
    type: Optional[codeableconcept.CodeableConcept] = None
    url: Optional[str] = None
    version: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Contract, self).elementProperties()
        js.extend([
            ("alias", "alias", str, True, None, False),
            ("applies", "applies", period.Period, False, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("authority", "authority", fhirreference.FHIRReference, True, None, False),
            ("contentDefinition", "contentDefinition", ContractContentDefinition, False, None, False),
            ("contentDerivative", "contentDerivative", codeableconcept.CodeableConcept, False, None, False),
            ("domain", "domain", fhirreference.FHIRReference, True, None, False),
            ("expirationType", "expirationType", codeableconcept.CodeableConcept, False, None, False),
            ("friendly", "friendly", ContractFriendly, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", fhirreference.FHIRReference, False, None, False),
            ("instantiatesUri", "instantiatesUri", str, False, None, False),
            ("issued", "issued", fhirdate.FHIRDate, False, None, False),
            ("legal", "legal", ContractLegal, True, None, False),
            ("legalState", "legalState", codeableconcept.CodeableConcept, False, None, False),
            ("legallyBindingAttachment", "legallyBindingAttachment", attachment.Attachment, False, "legallyBinding", False),
            ("legallyBindingReference", "legallyBindingReference", fhirreference.FHIRReference, False, "legallyBinding", False),
            ("name", "name", str, False, None, False),
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False),
            ("rule", "rule", ContractRule, True, None, False),
            ("scope", "scope", codeableconcept.CodeableConcept, False, None, False),
            ("signer", "signer", ContractSigner, True, None, False),
            ("site", "site", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, True, None, False),
            ("subtitle", "subtitle", str, False, None, False),
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, True, None, False),
            ("term", "term", ContractTerm, True, None, False),
            ("title", "title", str, False, None, False),
            ("topicCodeableConcept", "topicCodeableConcept", codeableconcept.CodeableConcept, False, "topic", False),
            ("topicReference", "topicReference", fhirreference.FHIRReference, False, "topic", False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("url", "url", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
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
    from . import money
except ImportError:
    money = sys.modules[__package__ + '.money']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import signature
except ImportError:
    signature = sys.modules[__package__ + '.signature']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']