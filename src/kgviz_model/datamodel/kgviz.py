# Auto generated from kgviz.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-08-16T16:23:10
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
from jsonasobj2 import JsonObj, as_dict
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
from linkml_runtime.linkml_model.types import Boolean, Integer, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = "0.0.1"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
EX = CurieNamespace('ex', 'https://w3id.org/kgviz/')
GV = CurieNamespace('gv', 'https://w3id.org/kgviz/graphviz')
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


class Color(str):
    """ e.g. red, green """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "Color"
    type_model_uri = EX.Color


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
            self.styles = [self.styles] if self.styles is not None else []
        self.styles = [v if isinstance(v, StyleType) else StyleType(v) for v in self.styles]

        if self.fillcolor is not None and not isinstance(self.fillcolor, str):
            self.fillcolor = str(self.fillcolor)

        if self.labelFrom is not None and not isinstance(self.labelFrom, str):
            self.labelFrom = str(self.labelFrom)

        if not isinstance(self.highlightIds, list):
            self.highlightIds = [self.highlightIds] if self.highlightIds is not None else []
        self.highlightIds = [v if isinstance(v, str) else str(v) for v in self.highlightIds]

        if not isinstance(self.displayAnnotations, list):
            self.displayAnnotations = [self.displayAnnotations] if self.displayAnnotations is not None else []
        self.displayAnnotations = [v if isinstance(v, str) else str(v) for v in self.displayAnnotations]

        if not isinstance(self.cliqueRelations, list):
            self.cliqueRelations = [self.cliqueRelations] if self.cliqueRelations is not None else []
        self.cliqueRelations = [v if isinstance(v, str) else str(v) for v in self.cliqueRelations]

        if not isinstance(self.reasoning, list):
            self.reasoning = [self.reasoning] if self.reasoning is not None else []
        self.reasoning = [v if isinstance(v, ReasoningType) else ReasoningType(v) for v in self.reasoning]

        if self.excludeSingletons is not None and not isinstance(self.excludeSingletons, Bool):
            self.excludeSingletons = Bool(self.excludeSingletons)

        self._normalize_inlined_as_dict(slot_name="relationProperties", slot_type=RelationConfiguration, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="prefixProperties", slot_type=PrefixConfiguration, key_name="id", keyed=True)

        if not isinstance(self.conditionalProperties, list):
            self.conditionalProperties = [self.conditionalProperties] if self.conditionalProperties is not None else []
        self.conditionalProperties = [v if isinstance(v, ConditionalProperty) else ConditionalProperty(**as_dict(v)) for v in self.conditionalProperties]

        if self.nodeFilter is not None and not isinstance(self.nodeFilter, Condition):
            self.nodeFilter = Condition(**as_dict(self.nodeFilter))

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
    style for a particular relation (for example, BFO:0000050 or rdfs:subClassOf).

    Example of usage, where [relationProperties](relationProperties.md)
    specifies a collection of RelationConfigurations keyed by property.

    ```json
    {
    "relationProperties": {
    "rdfs:subClassOf": {
    "color": "black",
    "penwith": 3,
    "arrowhead": "open",
    "label": ""
    },
    "BFO:0000050": {
    "arrowhead": "tee",
    "color": "blue"
    }
    }
    }
    ```
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
            self.MissingRequiredField("id")
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
            self.MissingRequiredField("id")
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
            self.conditions = Condition(**as_dict(self.conditions))

        if self.properties is not None and not isinstance(self.properties, AnyConfiguration):
            self.properties = AnyConfiguration(**as_dict(self.properties))

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


class GraphvizAspect(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GV.GraphvizAspect
    class_class_curie: ClassVar[str] = "gv:GraphvizAspect"
    class_name: ClassVar[str] = "graphviz aspect"
    class_model_uri: ClassVar[URIRef] = EX.GraphvizAspect


class EdgeAspect(GraphvizAspect):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GV.EdgeAspect
    class_class_curie: ClassVar[str] = "gv:EdgeAspect"
    class_name: ClassVar[str] = "edge aspect"
    class_model_uri: ClassVar[URIRef] = EX.EdgeAspect


class NodeAspect(GraphvizAspect):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GV.NodeAspect
    class_class_curie: ClassVar[str] = "gv:NodeAspect"
    class_name: ClassVar[str] = "node aspect"
    class_model_uri: ClassVar[URIRef] = EX.NodeAspect


class RootGraphAspect(GraphvizAspect):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GV.RootGraphAspect
    class_class_curie: ClassVar[str] = "gv:RootGraphAspect"
    class_name: ClassVar[str] = "root graph aspect"
    class_model_uri: ClassVar[URIRef] = EX.RootGraphAspect


class SubgraphAspect(GraphvizAspect):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GV.SubgraphAspect
    class_class_curie: ClassVar[str] = "gv:SubgraphAspect"
    class_name: ClassVar[str] = "subgraph aspect"
    class_model_uri: ClassVar[URIRef] = EX.SubgraphAspect


class ClusterSubgraphAspect(GraphvizAspect):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GV.ClusterSubgraphAspect
    class_class_curie: ClassVar[str] = "gv:ClusterSubgraphAspect"
    class_name: ClassVar[str] = "cluster subgraph aspect"
    class_model_uri: ClassVar[URIRef] = EX.ClusterSubgraphAspect


# Enumerations
class ReasoningType(EnumDefinitionImpl):

    transitive_reduction = PermissibleValue(text="transitive_reduction")
    todo = PermissibleValue(text="todo")

    _defn = EnumDefinition(
        name="ReasoningType",
    )

class StyleType(EnumDefinitionImpl):

    dashed = PermissibleValue(text="dashed")
    dotted = PermissibleValue(text="dotted")
    solid = PermissibleValue(text="solid")
    invis = PermissibleValue(text="invis")
    bold = PermissibleValue(text="bold")
    tapered = PermissibleValue(text="tapered")
    filled = PermissibleValue(text="filled")
    striped = PermissibleValue(text="striped")
    wedged = PermissibleValue(text="wedged")
    diagonals = PermissibleValue(text="diagonals")
    rounded = PermissibleValue(text="rounded")

    _defn = EnumDefinition(
        name="StyleType",
    )

class ArrowType(EnumDefinitionImpl):

    normal = PermissibleValue(text="normal")
    inv = PermissibleValue(text="inv")
    dot = PermissibleValue(text="dot")
    invdot = PermissibleValue(text="invdot")
    odot = PermissibleValue(text="odot")
    invodot = PermissibleValue(text="invodot")
    none = PermissibleValue(text="none")
    tee = PermissibleValue(text="tee")
    empty = PermissibleValue(text="empty")
    invempty = PermissibleValue(text="invempty")
    diamond = PermissibleValue(text="diamond")
    odiamond = PermissibleValue(text="odiamond")
    ediamond = PermissibleValue(text="ediamond")
    crow = PermissibleValue(text="crow")
    box = PermissibleValue(text="box")
    obox = PermissibleValue(text="obox")
    open = PermissibleValue(text="open")
    halfopen = PermissibleValue(text="halfopen")
    vee = PermissibleValue(text="vee")

    _defn = EnumDefinition(
        name="ArrowType",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=EX.id, name="id", curie=EX.curie('id'),
                   model_uri=EX.id, domain=None, range=URIRef)

slots.highlightIds = Slot(uri=EX.highlightIds, name="highlightIds", curie=EX.curie('highlightIds'),
                   model_uri=EX.highlightIds, domain=None, range=Optional[Union[str, List[str]]])

slots.relationProperties = Slot(uri=EX.relationProperties, name="relationProperties", curie=EX.curie('relationProperties'),
                   model_uri=EX.relationProperties, domain=None, range=Optional[Union[Dict[Union[str, RelationConfigurationId], Union[dict, RelationConfiguration]], List[Union[dict, RelationConfiguration]]]])

slots.prefixProperties = Slot(uri=EX.prefixProperties, name="prefixProperties", curie=EX.curie('prefixProperties'),
                   model_uri=EX.prefixProperties, domain=None, range=Optional[Union[Dict[Union[str, PrefixConfigurationId], Union[dict, PrefixConfiguration]], List[Union[dict, PrefixConfiguration]]]])

slots.conditionalProperties = Slot(uri=EX.conditionalProperties, name="conditionalProperties", curie=EX.curie('conditionalProperties'),
                   model_uri=EX.conditionalProperties, domain=None, range=Optional[Union[Union[dict, ConditionalProperty], List[Union[dict, ConditionalProperty]]]])

slots.nodeFilter = Slot(uri=EX.nodeFilter, name="nodeFilter", curie=EX.curie('nodeFilter'),
                   model_uri=EX.nodeFilter, domain=None, range=Optional[Union[dict, Condition]])

slots.reasoning = Slot(uri=EX.reasoning, name="reasoning", curie=EX.curie('reasoning'),
                   model_uri=EX.reasoning, domain=None, range=Optional[Union[Union[str, "ReasoningType"], List[Union[str, "ReasoningType"]]]])

slots.excludeSingletons = Slot(uri=EX.excludeSingletons, name="excludeSingletons", curie=EX.curie('excludeSingletons'),
                   model_uri=EX.excludeSingletons, domain=None, range=Optional[Union[bool, Bool]])

slots.displayAnnotations = Slot(uri=EX.displayAnnotations, name="displayAnnotations", curie=EX.curie('displayAnnotations'),
                   model_uri=EX.displayAnnotations, domain=None, range=Optional[Union[str, List[str]]])

slots.cliqueRelations = Slot(uri=EX.cliqueRelations, name="cliqueRelations", curie=EX.curie('cliqueRelations'),
                   model_uri=EX.cliqueRelations, domain=None, range=Optional[Union[str, List[str]]])

slots.conditions = Slot(uri=EX.conditions, name="conditions", curie=EX.curie('conditions'),
                   model_uri=EX.conditions, domain=None, range=Optional[Union[dict, Condition]])

slots.properties = Slot(uri=EX.properties, name="properties", curie=EX.curie('properties'),
                   model_uri=EX.properties, domain=None, range=Optional[Union[dict, AnyConfiguration]])

slots.type = Slot(uri=EX.type, name="type", curie=EX.curie('type'),
                   model_uri=EX.type, domain=None, range=Optional[str])

slots.subset = Slot(uri=EX.subset, name="subset", curie=EX.curie('subset'),
                   model_uri=EX.subset, domain=None, range=Optional[str])

slots.graphviz_slot = Slot(uri=GV.graphviz_slot, name="graphviz slot", curie=GV.curie('graphviz_slot'),
                   model_uri=EX.graphviz_slot, domain=None, range=Optional[str])

slots.edge_property = Slot(uri=GV.edge_property, name="edge property", curie=GV.curie('edge_property'),
                   model_uri=EX.edge_property, domain=None, range=Optional[str])

slots.node_property = Slot(uri=GV.node_property, name="node property", curie=GV.curie('node_property'),
                   model_uri=EX.node_property, domain=None, range=Optional[str])

slots.graph_property = Slot(uri=GV.graph_property, name="graph property", curie=GV.curie('graph_property'),
                   model_uri=EX.graph_property, domain=None, range=Optional[str])

slots.subgraph_property = Slot(uri=GV.subgraph_property, name="subgraph property", curie=GV.curie('subgraph_property'),
                   model_uri=EX.subgraph_property, domain=None, range=Optional[str])

slots.cluster_property = Slot(uri=GV.cluster_property, name="cluster property", curie=GV.curie('cluster_property'),
                   model_uri=EX.cluster_property, domain=None, range=Optional[str])

slots.color = Slot(uri="str(uriorcurie)", name="color", curie=None,
                   model_uri=EX.color, domain=None, range=Optional[str])

slots.fontcolor = Slot(uri=GV.fontcolor, name="fontcolor", curie=GV.curie('fontcolor'),
                   model_uri=EX.fontcolor, domain=None, range=Optional[str])

slots.penwidth = Slot(uri="str(uriorcurie)", name="penwidth", curie=None,
                   model_uri=EX.penwidth, domain=None, range=Optional[int])

slots.label = Slot(uri=GV.label, name="label", curie=GV.curie('label'),
                   model_uri=EX.label, domain=None, range=Optional[str])

slots.arrowhead = Slot(uri=GV.arrowhead, name="arrowhead", curie=GV.curie('arrowhead'),
                   model_uri=EX.arrowhead, domain=None, range=Optional[Union[str, "ArrowType"]])

slots.arrowtail = Slot(uri=GV.arrowtail, name="arrowtail", curie=GV.curie('arrowtail'),
                   model_uri=EX.arrowtail, domain=None, range=Optional[Union[str, "ArrowType"]])

slots.styles = Slot(uri=GV.styles, name="styles", curie=GV.curie('styles'),
                   model_uri=EX.styles, domain=None, range=Optional[Union[Union[str, "StyleType"], List[Union[str, "StyleType"]]]])

slots.style = Slot(uri=GV.style, name="style", curie=GV.curie('style'),
                   model_uri=EX.style, domain=None, range=Optional[Union[str, "StyleType"]])

slots.fillcolor = Slot(uri=GV.fillcolor, name="fillcolor", curie=GV.curie('fillcolor'),
                   model_uri=EX.fillcolor, domain=None, range=Optional[str])

slots.labelFrom = Slot(uri=GV.labelFrom, name="labelFrom", curie=GV.curie('labelFrom'),
                   model_uri=EX.labelFrom, domain=None, range=Optional[str])