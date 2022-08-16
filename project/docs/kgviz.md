
# kgviz


**metamodel version:** 1.7.0

**version:** 0.0.1


A data model for describing configurations / stylesheets for visualzing graphs, and
in particular Knowledge Graphs or Ontologies. These graphs are characterized by having meaningful edge labels,
node categories, IDs or URIs on each element, as well as additional rich metadata on the nodes or edges.

An example of a use of this is https://github.com/INCATools/obographviz


### Classes

 * [Condition](Condition.md) - a constraint or condition to be applied, e.g. type=Class
 * [ConditionalProperty](ConditionalProperty.md) - conditionally applied properties based on filters
 * [ElementConfiguration](ElementConfiguration.md) - Abstract parent for all coniguration classes
     * [AnyConfiguration](AnyConfiguration.md) - Generic configuration that inherits all aspects of both node and edge configurations
     * [PrefixConfiguration](PrefixConfiguration.md) - style for a particular prefix (e.g. GO)
     * [RelationConfiguration](RelationConfiguration.md) - style for a particular relation (for example, BFO:0000050 or rdfs:subClassOf).
 * [StyleSheet](StyleSheet.md) - A configuration for both global graph-level properties and element-level properties indicating how a KG should be rendered graphically

### Mixins

 * [ClusterSubgraphAspect](ClusterSubgraphAspect.md)
 * [EdgeAspect](EdgeAspect.md)
 * [EdgeProperty](EdgeProperty.md) - a property object for an edge/relation
 * [GeneralProperty](GeneralProperty.md) - abstract grouping for properties/configs
     * [EdgeProperty](EdgeProperty.md) - a property object for an edge/relation
     * [NodeProperty](NodeProperty.md)
 * [GraphvizAspect](GraphvizAspect.md)
     * [ClusterSubgraphAspect](ClusterSubgraphAspect.md)
     * [EdgeAspect](EdgeAspect.md)
     * [NodeAspect](NodeAspect.md)
     * [RootGraphAspect](RootGraphAspect.md)
     * [SubgraphAspect](SubgraphAspect.md)
 * [NodeAspect](NodeAspect.md)
 * [NodeProperty](NodeProperty.md)
 * [RootGraphAspect](RootGraphAspect.md)
 * [SubgraphAspect](SubgraphAspect.md)

### Slots

 * [arrowhead](arrowhead.md)
 * [arrowtail](arrowtail.md)
 * [cliqueRelations](cliqueRelations.md) - Set of properties that indicate identity relations whose symmetric reflexive transitive closure form a clique
 * [color](color.md) - Basic drawing color for graphics, not text. For the latter, use the fontcolor attribute.
 * [conditionalProperties](conditionalProperties.md)
 * [conditions](conditions.md)
 * [containmentRelations](containmentRelations.md) - Set of properties that indicate identity relations and can be used to create nesting boxes in displays
 * [displayAnnotations](displayAnnotations.md) - Display annotations for these selected properties
 * [excludeSingletons](excludeSingletons.md) - Remove nodes that have no incoming or outgoing edges
 * [fillcolor](fillcolor.md)
 * [fontcolor](fontcolor.md)
 * [graphvizSlot](graphvizSlot.md)
     * [clusterProperty](clusterProperty.md)
     * [edgeProperty](edgeProperty.md)
     * [graphProperty](graphProperty.md)
     * [nodeProperty](nodeProperty.md)
     * [subgraphProperty](subgraphProperty.md)
 * [highlightIds](highlightIds.md) - List of nodes to be visually demarcated
 * [id](id.md)
 * [label](label.md)
 * [labelFrom](labelFrom.md)
 * [nodeFilter](nodeFilter.md)
 * [penwidth](penwidth.md)
 * [prefixProperties](prefixProperties.md) - Collection of styles keyed by ID prefix
 * [properties](properties.md)
 * [reasoning](reasoning.md) - Set of reasoning or processing steps to be applied to graph
 * [relationProperties](relationProperties.md) - Collection of styles keyed by predicate ID
 * [style](style.md)
 * [styles](styles.md)
 * [subset](subset.md) - the subset to which the node belongs
 * [type](type.md) - the logical type, eg INDIVIDUAL, CLASS, etc

### Enums

 * [ArrowType](ArrowType.md)
 * [ReasoningType](ReasoningType.md)
 * [StyleType](StyleType.md)

### Subsets


### Types


#### Built in

 * **Bool**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Color](types/Color.md)  (**str**)  - e.g. red, green
 * [Node](types/Node.md)  (**str**)  - e.g. UBERON:0002101
 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
