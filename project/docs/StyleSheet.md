
# Class: StyleSheet


A configuration for both global graph-level properties and element-level properties indicating how a KG should be rendered graphically

URI: [kgviz:StyleSheet](https://w3id.org/kgviz/StyleSheet)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Condition]<nodeFilter%200..1-++[StyleSheet&#124;style:StyleType%20%3F;styles:StyleType%20*;fillcolor:Color%20%3F;labelFrom:string%20%3F;highlightIds:Node%20*;displayAnnotations:Node%20*;cliqueRelations:Node%20*;containmentRelations:Node%20*;reasoning:ReasoningType%20*;excludeSingletons:boolean%20%3F],[ConditionalProperty]<conditionalProperties%200..*-++[StyleSheet],[PrefixConfiguration]<prefixProperties%200..*-++[StyleSheet],[RelationConfiguration]<relationProperties%200..*-++[StyleSheet],[RelationConfiguration],[PrefixConfiguration],[ConditionalProperty],[Condition])](https://yuml.me/diagram/nofunky;dir:TB/class/[Condition]<nodeFilter%200..1-++[StyleSheet&#124;style:StyleType%20%3F;styles:StyleType%20*;fillcolor:Color%20%3F;labelFrom:string%20%3F;highlightIds:Node%20*;displayAnnotations:Node%20*;cliqueRelations:Node%20*;containmentRelations:Node%20*;reasoning:ReasoningType%20*;excludeSingletons:boolean%20%3F],[ConditionalProperty]<conditionalProperties%200..*-++[StyleSheet],[PrefixConfiguration]<prefixProperties%200..*-++[StyleSheet],[RelationConfiguration]<relationProperties%200..*-++[StyleSheet],[RelationConfiguration],[PrefixConfiguration],[ConditionalProperty],[Condition])

## Attributes


### Own

 * [style](style.md)  <sub>0..1</sub>
     * Range: [StyleType](StyleType.md)
 * [styles](styles.md)  <sub>0..\*</sub>
     * Range: [StyleType](StyleType.md)
 * [fillcolor](fillcolor.md)  <sub>0..1</sub>
     * Range: [Color](types/Color.md)
 * [labelFrom](labelFrom.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [highlightIds](highlightIds.md)  <sub>0..\*</sub>
     * Description: List of nodes to be visually demarcated
     * Range: [Node](types/Node.md)
 * [displayAnnotations](displayAnnotations.md)  <sub>0..\*</sub>
     * Description: Display annotations for these selected properties
     * Range: [Node](types/Node.md)
 * [cliqueRelations](cliqueRelations.md)  <sub>0..\*</sub>
     * Description: Set of properties that indicate identity relations whose symmetric reflexive transitive closure form a clique
     * Range: [Node](types/Node.md)
     * Example: owl:equivalentClass None
     * Example: skos:exactMatch None
 * [containmentRelations](containmentRelations.md)  <sub>0..\*</sub>
     * Description: Set of properties that indicate identity relations and can be used to create nesting boxes in displays
     * Range: [Node](types/Node.md)
     * Example: rdfs:isDefinedBy None
 * [reasoning](reasoning.md)  <sub>0..\*</sub>
     * Description: Set of reasoning or processing steps to be applied to graph
     * Range: [ReasoningType](ReasoningType.md)
 * [excludeSingletons](excludeSingletons.md)  <sub>0..1</sub>
     * Description: Remove nodes that have no incoming or outgoing edges
     * Range: [Boolean](types/Boolean.md)
 * [relationProperties](relationProperties.md)  <sub>0..\*</sub>
     * Description: Collection of styles keyed by predicate ID
     * Range: [RelationConfiguration](RelationConfiguration.md)
 * [prefixProperties](prefixProperties.md)  <sub>0..\*</sub>
     * Description: Collection of styles keyed by ID prefix
     * Range: [PrefixConfiguration](PrefixConfiguration.md)
 * [conditionalProperties](conditionalProperties.md)  <sub>0..\*</sub>
     * Range: [ConditionalProperty](ConditionalProperty.md)
 * [nodeFilter](nodeFilter.md)  <sub>0..1</sub>
     * Range: [Condition](Condition.md)
