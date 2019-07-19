#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/StructureMap) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .address import Address
from .age import Age
from .annotation import Annotation
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .contactdetail import ContactDetail
from .contactpoint import ContactPoint
from .contributor import Contributor
from .count import Count
from .datarequirement import DataRequirement
from .distance import Distance
from .domainresource import DomainResource
from .dosage import Dosage
from .duration import Duration
from .expression import Expression
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .humanname import HumanName
from .identifier import Identifier
from .money import Money
from .parameterdefinition import ParameterDefinition
from .period import Period
from .quantity import Quantity
from .range import Range
from .ratio import Ratio
from .relatedartifact import RelatedArtifact
from .sampleddata import SampledData
from .signature import Signature
from .timing import Timing
from .triggerdefinition import TriggerDefinition
from .usagecontext import UsageContext


@dataclass
class StructureMapStructure(BackboneElement):
    """ Structure Definition used by this map.

    A structure definition used by this map. The structure definition may
    describe instances that are converted, or the instances that are produced.
    """
    resource_type: ClassVar[str] = "StructureMapStructure"
    alias: Optional[str] = None
    documentation: Optional[str] = None
    mode: str = None
    url: str = None

    def elementProperties(self):
        js = super(StructureMapStructure, self).elementProperties()
        js.extend([
            ("alias", "alias", str, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("mode", "mode", str, False, None, True),
            ("url", "url", str, False, None, True),
        ])
        return js


@dataclass
class StructureMapGroupRuleTargetParameter(BackboneElement):
    """ Parameters to the transform.
    """
    resource_type: ClassVar[str] = "StructureMapGroupRuleTargetParameter"
    valueBoolean: bool = None
    valueDecimal: float = None
    valueId: str = None
    valueInteger: int = None
    valueString: str = None

    def elementProperties(self):
        js = super(StructureMapGroupRuleTargetParameter, self).elementProperties()
        js.extend([
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueId", "valueId", str, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
        ])
        return js


@dataclass
class StructureMapGroupRuleTarget(BackboneElement):
    """ Content to create because of this mapping rule.
    """
    resource_type: ClassVar[str] = "StructureMapGroupRuleTarget"
    context: Optional[str] = None
    contextType: Optional[str] = None
    element: Optional[str] = None
    listMode: Optional[List[str]] = empty_list()
    listRuleId: Optional[str] = None
    parameter: Optional[List[StructureMapGroupRuleTargetParameter]] = empty_list()
    transform: Optional[str] = None
    variable: Optional[str] = None

    def elementProperties(self):
        js = super(StructureMapGroupRuleTarget, self).elementProperties()
        js.extend([
            ("context", "context", str, False, None, False),
            ("contextType", "contextType", str, False, None, False),
            ("element", "element", str, False, None, False),
            ("listMode", "listMode", str, True, None, False),
            ("listRuleId", "listRuleId", str, False, None, False),
            ("parameter", "parameter", StructureMapGroupRuleTargetParameter, True, None, False),
            ("transform", "transform", str, False, None, False),
            ("variable", "variable", str, False, None, False),
        ])
        return js


@dataclass
class StructureMapGroupRuleSource(BackboneElement):
    """ Source inputs to the mapping.
    """
    resource_type: ClassVar[str] = "StructureMapGroupRuleSource"
    check: Optional[str] = None
    condition: Optional[str] = None
    context: str = None
    defaultValueAddress: Optional[Address] = None
    defaultValueAge: Optional[Age] = None
    defaultValueAnnotation: Optional[Annotation] = None
    defaultValueAttachment: Optional[Attachment] = None
    defaultValueBase64Binary: Optional[str] = None
    defaultValueBoolean: Optional[bool] = None
    defaultValueCanonical: Optional[str] = None
    defaultValueCode: Optional[str] = None
    defaultValueCodeableConcept: Optional[CodeableConcept] = None
    defaultValueCoding: Optional[Coding] = None
    defaultValueContactDetail: Optional[ContactDetail] = None
    defaultValueContactPoint: Optional[ContactPoint] = None
    defaultValueContributor: Optional[Contributor] = None
    defaultValueCount: Optional[Count] = None
    defaultValueDataRequirement: Optional[DataRequirement] = None
    defaultValueDate: Optional[FHIRDate] = None
    defaultValueDateTime: Optional[FHIRDate] = None
    defaultValueDecimal: Optional[float] = None
    defaultValueDistance: Optional[Distance] = None
    defaultValueDosage: Optional[Dosage] = None
    defaultValueDuration: Optional[Duration] = None
    defaultValueExpression: Optional[Expression] = None
    defaultValueHumanName: Optional[HumanName] = None
    defaultValueId: Optional[str] = None
    defaultValueIdentifier: Optional[Identifier] = None
    defaultValueInstant: Optional[FHIRDate] = None
    defaultValueInteger: Optional[int] = None
    defaultValueMarkdown: Optional[str] = None
    defaultValueMoney: Optional[Money] = None
    defaultValueOid: Optional[str] = None
    defaultValueParameterDefinition: Optional[ParameterDefinition] = None
    defaultValuePeriod: Optional[Period] = None
    defaultValuePositiveInt: Optional[int] = None
    defaultValueQuantity: Optional[Quantity] = None
    defaultValueRange: Optional[Range] = None
    defaultValueRatio: Optional[Ratio] = None
    defaultValueReference: Optional[FHIRReference] = None
    defaultValueRelatedArtifact: Optional[RelatedArtifact] = None
    defaultValueSampledData: Optional[SampledData] = None
    defaultValueSignature: Optional[Signature] = None
    defaultValueString: Optional[str] = None
    defaultValueTime: Optional[FHIRDate] = None
    defaultValueTiming: Optional[Timing] = None
    defaultValueTriggerDefinition: Optional[TriggerDefinition] = None
    defaultValueUnsignedInt: Optional[int] = None
    defaultValueUri: Optional[str] = None
    defaultValueUrl: Optional[str] = None
    defaultValueUsageContext: Optional[UsageContext] = None
    defaultValueUuid: Optional[str] = None
    element: Optional[str] = None
    listMode: Optional[str] = None
    logMessage: Optional[str] = None
    max: Optional[str] = None
    min: Optional[int] = None
    type: Optional[str] = None
    variable: Optional[str] = None

    def elementProperties(self):
        js = super(StructureMapGroupRuleSource, self).elementProperties()
        js.extend([
            ("check", "check", str, False, None, False),
            ("condition", "condition", str, False, None, False),
            ("context", "context", str, False, None, True),
            ("defaultValueAddress", "defaultValueAddress", Address, False, "defaultValue", False),
            ("defaultValueAge", "defaultValueAge", Age, False, "defaultValue", False),
            ("defaultValueAnnotation", "defaultValueAnnotation", Annotation, False, "defaultValue", False),
            ("defaultValueAttachment", "defaultValueAttachment", Attachment, False, "defaultValue", False),
            ("defaultValueBase64Binary", "defaultValueBase64Binary", str, False, "defaultValue", False),
            ("defaultValueBoolean", "defaultValueBoolean", bool, False, "defaultValue", False),
            ("defaultValueCanonical", "defaultValueCanonical", str, False, "defaultValue", False),
            ("defaultValueCode", "defaultValueCode", str, False, "defaultValue", False),
            ("defaultValueCodeableConcept", "defaultValueCodeableConcept", CodeableConcept, False, "defaultValue", False),
            ("defaultValueCoding", "defaultValueCoding", Coding, False, "defaultValue", False),
            ("defaultValueContactDetail", "defaultValueContactDetail", ContactDetail, False, "defaultValue", False),
            ("defaultValueContactPoint", "defaultValueContactPoint", ContactPoint, False, "defaultValue", False),
            ("defaultValueContributor", "defaultValueContributor", Contributor, False, "defaultValue", False),
            ("defaultValueCount", "defaultValueCount", Count, False, "defaultValue", False),
            ("defaultValueDataRequirement", "defaultValueDataRequirement", DataRequirement, False, "defaultValue", False),
            ("defaultValueDate", "defaultValueDate", FHIRDate, False, "defaultValue", False),
            ("defaultValueDateTime", "defaultValueDateTime", FHIRDate, False, "defaultValue", False),
            ("defaultValueDecimal", "defaultValueDecimal", float, False, "defaultValue", False),
            ("defaultValueDistance", "defaultValueDistance", Distance, False, "defaultValue", False),
            ("defaultValueDosage", "defaultValueDosage", Dosage, False, "defaultValue", False),
            ("defaultValueDuration", "defaultValueDuration", Duration, False, "defaultValue", False),
            ("defaultValueExpression", "defaultValueExpression", Expression, False, "defaultValue", False),
            ("defaultValueHumanName", "defaultValueHumanName", HumanName, False, "defaultValue", False),
            ("defaultValueId", "defaultValueId", str, False, "defaultValue", False),
            ("defaultValueIdentifier", "defaultValueIdentifier", Identifier, False, "defaultValue", False),
            ("defaultValueInstant", "defaultValueInstant", FHIRDate, False, "defaultValue", False),
            ("defaultValueInteger", "defaultValueInteger", int, False, "defaultValue", False),
            ("defaultValueMarkdown", "defaultValueMarkdown", str, False, "defaultValue", False),
            ("defaultValueMoney", "defaultValueMoney", Money, False, "defaultValue", False),
            ("defaultValueOid", "defaultValueOid", str, False, "defaultValue", False),
            ("defaultValueParameterDefinition", "defaultValueParameterDefinition", ParameterDefinition, False, "defaultValue", False),
            ("defaultValuePeriod", "defaultValuePeriod", Period, False, "defaultValue", False),
            ("defaultValuePositiveInt", "defaultValuePositiveInt", int, False, "defaultValue", False),
            ("defaultValueQuantity", "defaultValueQuantity", Quantity, False, "defaultValue", False),
            ("defaultValueRange", "defaultValueRange", Range, False, "defaultValue", False),
            ("defaultValueRatio", "defaultValueRatio", Ratio, False, "defaultValue", False),
            ("defaultValueReference", "defaultValueReference", FHIRReference, False, "defaultValue", False),
            ("defaultValueRelatedArtifact", "defaultValueRelatedArtifact", RelatedArtifact, False, "defaultValue", False),
            ("defaultValueSampledData", "defaultValueSampledData", SampledData, False, "defaultValue", False),
            ("defaultValueSignature", "defaultValueSignature", Signature, False, "defaultValue", False),
            ("defaultValueString", "defaultValueString", str, False, "defaultValue", False),
            ("defaultValueTime", "defaultValueTime", FHIRDate, False, "defaultValue", False),
            ("defaultValueTiming", "defaultValueTiming", Timing, False, "defaultValue", False),
            ("defaultValueTriggerDefinition", "defaultValueTriggerDefinition", TriggerDefinition, False, "defaultValue", False),
            ("defaultValueUnsignedInt", "defaultValueUnsignedInt", int, False, "defaultValue", False),
            ("defaultValueUri", "defaultValueUri", str, False, "defaultValue", False),
            ("defaultValueUrl", "defaultValueUrl", str, False, "defaultValue", False),
            ("defaultValueUsageContext", "defaultValueUsageContext", UsageContext, False, "defaultValue", False),
            ("defaultValueUuid", "defaultValueUuid", str, False, "defaultValue", False),
            ("element", "element", str, False, None, False),
            ("listMode", "listMode", str, False, None, False),
            ("logMessage", "logMessage", str, False, None, False),
            ("max", "max", str, False, None, False),
            ("min", "min", int, False, None, False),
            ("type", "type", str, False, None, False),
            ("variable", "variable", str, False, None, False),
        ])
        return js


@dataclass
class StructureMapGroupRuleDependent(BackboneElement):
    """ Which other rules to apply in the context of this rule.
    """
    resource_type: ClassVar[str] = "StructureMapGroupRuleDependent"
    name: str = None
    variable: List[str] = empty_list()

    def elementProperties(self):
        js = super(StructureMapGroupRuleDependent, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("variable", "variable", str, True, None, True),
        ])
        return js


@dataclass
class StructureMapGroupRule(BackboneElement):
    """ Transform Rule from source to target.
    """
    resource_type: ClassVar[str] = "StructureMapGroupRule"
    dependent: Optional[List[StructureMapGroupRuleDependent]] = empty_list()
    documentation: Optional[str] = None
    name: str = None
    rule: Optional[List[StructureMapGroupRule]] = empty_list()
    source: List[StructureMapGroupRuleSource] = empty_list()
    target: Optional[List[StructureMapGroupRuleTarget]] = empty_list()

    def elementProperties(self):
        js = super(StructureMapGroupRule, self).elementProperties()
        js.extend([
            ("dependent", "dependent", StructureMapGroupRuleDependent, True, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("rule", "rule", StructureMapGroupRule, True, None, False),
            ("source", "source", StructureMapGroupRuleSource, True, None, True),
            ("target", "target", StructureMapGroupRuleTarget, True, None, False),
        ])
        return js


@dataclass
class StructureMapGroupInput(BackboneElement):
    """ Named instance provided when invoking the map.

    A name assigned to an instance of data. The instance must be provided when
    the mapping is invoked.
    """
    resource_type: ClassVar[str] = "StructureMapGroupInput"
    documentation: Optional[str] = None
    mode: str = None
    name: str = None
    type: Optional[str] = None

    def elementProperties(self):
        js = super(StructureMapGroupInput, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("mode", "mode", str, False, None, True),
            ("name", "name", str, False, None, True),
            ("type", "type", str, False, None, False),
        ])
        return js


@dataclass
class StructureMapGroup(BackboneElement):
    """ Named sections for reader convenience.

    Organizes the mapping into manageable chunks for human review/ease of
    maintenance.
    """
    resource_type: ClassVar[str] = "StructureMapGroup"
    documentation: Optional[str] = None
    extends: Optional[str] = None
    input: List[StructureMapGroupInput] = empty_list()
    name: str = None
    rule: List[StructureMapGroupRule] = empty_list()
    typeMode: str = None

    def elementProperties(self):
        js = super(StructureMapGroup, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("extends", "extends", str, False, None, False),
            ("input", "input", StructureMapGroupInput, True, None, True),
            ("name", "name", str, False, None, True),
            ("rule", "rule", StructureMapGroupRule, True, None, True),
            ("typeMode", "typeMode", str, False, None, True),
        ])
        return js


@dataclass
class StructureMap(DomainResource):
    """ A Map of relationships between 2 structures that can be used to transform
    data.
    """
    resource_type: ClassVar[str] = "StructureMap"
    contact: Optional[List[ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date: Optional[FHIRDate] = None
    description: Optional[str] = None
    experimental: Optional[bool] = None
    group: List[StructureMapGroup] = empty_list()
    identifier: Optional[List[Identifier]] = empty_list()
    import_fhir: Optional[List[str]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    name: str = None
    publisher: Optional[str] = None
    purpose: Optional[str] = None
    status: str = None
    structure: Optional[List[StructureMapStructure]] = empty_list()
    title: Optional[str] = None
    url: str = None
    useContext: Optional[List[UsageContext]] = empty_list()
    version: Optional[str] = None

    def elementProperties(self):
        js = super(StructureMap, self).elementProperties()
        js.extend([
            ("contact", "contact", ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("group", "group", StructureMapGroup, True, None, True),
            ("identifier", "identifier", Identifier, True, None, False),
            ("import_fhir", "import", str, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("name", "name", str, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("structure", "structure", StructureMapStructure, True, None, False),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, True),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js