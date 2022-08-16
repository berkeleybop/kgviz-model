# Auto generated from kgviz.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-05-15 16:08
# Schema: kgviz
#
# id: https://w3id.org/kgviz/
# description: A data model for describing configurations / stylesheets for visualzing graphs, and in particular
#              Knowledge Graphs or Ontologies. These graphs are characterized by having meaningful edge labels,
#              node categories, IDs or URIs on each element, as well as additional rich metadata on the nodes or
#              edges. An example of a use of this is https://github.com/cmungall/obographviz
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from . graphviz import ArrowType, Color, StyleType
from linkml_runtime.linkml_model.types import Boolean, Integer, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
EX = CurieNamespace('ex', 'https://w3id.org/kgviz/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SDO = CurieNamespace('sdo', 'https://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = EX


# Types
class Node(str):
    """ e.g. UBERON:0002101 """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "Node"
    type_model_uri = EX.Node


# Class references
class RelationConfigurationId(extended_str):
    pass


class PrefixConfigurationId(extended_str):
    pass


@dataclass
class StyleSheet(YAMLRoot):
    """
    A configuration for both global graph-level properties and element-level properties indicating how a KG should be
    rendered graphically
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.StyleSheet
    class_class_curie: ClassVar[str] = "ex:StyleSheet"
    class_name: ClassVar[str] = "StyleSheet"
    class_model_uri: ClassVar[URIRef] = EX.StyleSheet

    style: Optional[Union[str, "StyleType"]] = None
    styles: Optional[Union[Union[str, "StyleType"], List[Union[str, "StyleType"]]]] = empty_list()
    fillcolor: Optional[str] = None
    labelFrom: Optional[str] = None
    highlightIds: Optional[Union[str, List[str]]] = empty_list()
    displayAnnotations: Optional[Union[str, List[str]]] = empty_list()
    cliqueRelations: Optional[Union[str, List[str]]] = empty_list()
    reasoning: Optional[Union[Union[str, "ReasoningType"], List[Union[str, "ReasoningType"]]]] = empty_list()
    excludeSingletons: Optional[Union[bool, Bool]] = None
    relationProperties: Optional[Union[Dict[Union[str, RelationConfigurationId], Union[dict, "RelationConfiguration"]], List[Union[dict, "RelationConfiguration"]]]] = empty_dict()
    prefixProperties: Optional[Union[Dict[Union[str, PrefixConfigurationId], Union[dict, "PrefixConfiguration"]], List[Union[dict, "PrefixConfiguration"]]]] = empty_dict()
    conditionalProperties: Optional[Union[Union[dict, "ConditionalProperty"], List[Union[dict, "ConditionalProperty"]]]] = empty_list()
    nodeFilter: Optional[Union[dict, "Condition"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.style is not None and not isinstance(self.style, StyleType):
            self.style = StyleType(self.style)

        if not isinstance(self.styles, list):
            self.styles = [self.styles]
        self.styles = [v if isinstance(v, StyleType) else StyleType(v) for v in self.styles]

        if self.fillcolor is not None and not isinstance(self.fillcolor, str):
            self.fillcolor = str(self.fillcolor)

        if self.labelFrom is not None and not isinstance(self.labelFrom, str):
            self.labelFrom = str(self.labelFrom)

        if not isinstance(self.highlightIds, list):
            self.highlightIds = [self.highlightIds]
        self.highlightIds = [v if isinstance(v, str) else str(v) for v in self.highlightIds]

        if not isinstance(self.displayAnnotations, list):
            self.displayAnnotations = [self.displayAnnotations]
        self.displayAnnotations = [v if isinstance(v, str) else str(v) for v in self.displayAnnotations]

        if not isinstance(self.cliqueRelations, list):
            self.cliqueRelations = [self.cliqueRelations]
        self.cliqueRelations = [v if isinstance(v, str) else str(v) for v in self.cliqueRelations]

        if not isinstance(self.reasoning, list):
            self.reasoning = [self.reasoning]
        self.reasoning = [v if isinstance(v, ReasoningType) else ReasoningType(v) for v in self.reasoning]

        if self.excludeSingletons is not None and not isinstance(self.excludeSingletons, Bool):
            self.excludeSingletons = Bool(self.excludeSingletons)

        self._normalize_inlined_as_dict(slot_name="relationProperties", slot_type=RelationConfiguration, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="prefixProperties", slot_type=PrefixConfiguration, key_name="id", keyed=True)

        if not isinstance(self.conditionalProperties, list):
            self.conditionalProperties = [self.conditionalProperties]
        self.conditionalProperties = [v if isinstance(v, ConditionalProperty) else ConditionalProperty(**v) for v in self.conditionalProperties]

        if self.nodeFilter is not None and not isinstance(self.nodeFilter, Condition):
            self.nodeFilter = Condition(**self.nodeFilter)

        super().__post_init__(**kwargs)


class ElementConfiguration(YAMLRoot):
    """
    Abstract parent for all coniguration classes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.ElementConfiguration
    class_class_curie: ClassVar[str] = "ex:ElementConfiguration"
    class_name: ClassVar[str] = "ElementConfiguration"
    class_model_uri: ClassVar[URIRef] = EX.ElementConfiguration


@dataclass
class RelationConfiguration(ElementConfiguration):
    """
    style for a particular relation (e.g. part-of)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.RelationConfiguration
    class_class_curie: ClassVar[str] = "ex:RelationConfiguration"
    class_name: ClassVar[str] = "RelationConfiguration"
    class_model_uri: ClassVar[URIRef] = EX.RelationConfiguration

    id: Union[str, RelationConfigurationId] = None
    color: Optional[str] = None
    penwidth: Optional[int] = None
    label: Optional[str] = None
    arrowhead: Optional[Union[str, "ArrowType"]] = None
    arrowtail: Optional[Union[str, "ArrowType"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            raise ValueError("id must be supplied")
        if not isinstance(self.id, RelationConfigurationId):
            self.id = RelationConfigurationId(self.id)

        if self.color is not None and not isinstance(self.color, str):
            self.color = str(self.color)

        if self.penwidth is not None and not isinstance(self.penwidth, int):
            self.penwidth = int(self.penwidth)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.arrowhead is not None and not isinstance(self.arrowhead, ArrowType):
            self.arrowhead = ArrowType(self.arrowhead)

        if self.arrowtail is not None and not isinstance(self.arrowtail, ArrowType):
            self.arrowtail = ArrowType(self.arrowtail)

        super().__post_init__(**kwargs)


@dataclass
class PrefixConfiguration(ElementConfiguration):
    """
    style for a particular prefix (e.g. GO)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.PrefixConfiguration
    class_class_curie: ClassVar[str] = "ex:PrefixConfiguration"
    class_name: ClassVar[str] = "PrefixConfiguration"
    class_model_uri: ClassVar[URIRef] = EX.PrefixConfiguration

    id: Union[str, PrefixConfigurationId] = None
    fillcolor: Optional[str] = None
    color: Optional[str] = None
    fontcolor: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PrefixConfigurationId):
            self.id = PrefixConfigurationId(self.id)

        if self.fillcolor is not None and not isinstance(self.fillcolor, str):
            self.fillcolor = str(self.fillcolor)

        if self.color is not None and not isinstance(self.color, str):
            self.color = str(self.color)

        if self.fontcolor is not None and not isinstance(self.fontcolor, str):
            self.fontcolor = str(self.fontcolor)

        super().__post_init__(**kwargs)


@dataclass
class AnyConfiguration(ElementConfiguration):
    """
    Generic configuration that inherits all aspects of both node and edge configurations
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.AnyConfiguration
    class_class_curie: ClassVar[str] = "ex:AnyConfiguration"
    class_name: ClassVar[str] = "AnyConfiguration"
    class_model_uri: ClassVar[URIRef] = EX.AnyConfiguration

    color: Optional[str] = None
    fontcolor: Optional[str] = None
    arrowhead: Optional[Union[str, "ArrowType"]] = None
    arrowtail: Optional[Union[str, "ArrowType"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.color is not None and not isinstance(self.color, str):
            self.color = str(self.color)

        if self.fontcolor is not None and not isinstance(self.fontcolor, str):
            self.fontcolor = str(self.fontcolor)

        if self.arrowhead is not None and not isinstance(self.arrowhead, ArrowType):
            self.arrowhead = ArrowType(self.arrowhead)

        if self.arrowtail is not None and not isinstance(self.arrowtail, ArrowType):
            self.arrowtail = ArrowType(self.arrowtail)

        super().__post_init__(**kwargs)


@dataclass
class ConditionalProperty(YAMLRoot):
    """
    conditionally applied properties based on filters
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.ConditionalProperty
    class_class_curie: ClassVar[str] = "ex:ConditionalProperty"
    class_name: ClassVar[str] = "ConditionalProperty"
    class_model_uri: ClassVar[URIRef] = EX.ConditionalProperty

    fillcolor: Optional[str] = None
    conditions: Optional[Union[dict, "Condition"]] = None
    properties: Optional[Union[dict, AnyConfiguration]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.fillcolor is not None and not isinstance(self.fillcolor, str):
            self.fillcolor = str(self.fillcolor)

        if self.conditions is not None and not isinstance(self.conditions, Condition):
            self.conditions = Condition(**self.conditions)

        if self.properties is not None and not isinstance(self.properties, AnyConfiguration):
            self.properties = AnyConfiguration(**self.properties)

        super().__post_init__(**kwargs)


@dataclass
class Condition(YAMLRoot):
    """
    a constraint or condition to be applied, e.g. type=Class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.Condition
    class_class_curie: ClassVar[str] = "ex:Condition"
    class_name: ClassVar[str] = "Condition"
    class_model_uri: ClassVar[URIRef] = EX.Condition

    type: Optional[str] = None
    subset: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.subset is not None and not isinstance(self.subset, str):
            self.subset = str(self.subset)

        super().__post_init__(**kwargs)


@dataclass
class GeneralProperty(YAMLRoot):
    """
    abstract grouping for properties/configs
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.GeneralProperty
    class_class_curie: ClassVar[str] = "ex:GeneralProperty"
    class_name: ClassVar[str] = "GeneralProperty"
    class_model_uri: ClassVar[URIRef] = EX.GeneralProperty

    penwidth: Optional[int] = None
    label: Optional[str] = None
    fontcolor: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.penwidth is not None and not isinstance(self.penwidth, int):
            self.penwidth = int(self.penwidth)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.fontcolor is not None and not isinstance(self.fontcolor, str):
            self.fontcolor = str(self.fontcolor)

        super().__post_init__(**kwargs)


@dataclass
class EdgeProperty(GeneralProperty):
    """
    a property object for an edge/relation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.EdgeProperty
    class_class_curie: ClassVar[str] = "ex:EdgeProperty"
    class_name: ClassVar[str] = "EdgeProperty"
    class_model_uri: ClassVar[URIRef] = EX.EdgeProperty

    arrowhead: Optional[Union[str, "ArrowType"]] = None
    arrowtail: Optional[Union[str, "ArrowType"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.arrowhead is not None and not isinstance(self.arrowhead, ArrowType):
            self.arrowhead = ArrowType(self.arrowhead)

        if self.arrowtail is not None and not isinstance(self.arrowtail, ArrowType):
            self.arrowtail = ArrowType(self.arrowtail)

        super().__post_init__(**kwargs)


@dataclass
class NodeProperty(GeneralProperty):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.NodeProperty
    class_class_curie: ClassVar[str] = "ex:NodeProperty"
    class_name: ClassVar[str] = "NodeProperty"
    class_model_uri: ClassVar[URIRef] = EX.NodeProperty

    color: Optional[str] = None
    fontcolor: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.color is not None and not isinstance(self.color, str):
            self.color = str(self.color)

        if self.fontcolor is not None and not isinstance(self.fontcolor, str):
            self.fontcolor = str(self.fontcolor)

        super().__post_init__(**kwargs)


# Enumerations
class ReasoningType(EnumDefinitionImpl):

    transitive_reduction = PermissibleValue(text="transitive_reduction")
    todo = PermissibleValue(text="todo")

    _defn = EnumDefinition(
        name="ReasoningType",
    )

# Slots

