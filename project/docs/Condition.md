
# Class: Condition


a constraint or condition to be applied, e.g. type=Class

URI: [kgviz:Condition](https://w3id.org/kgviz/Condition)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ConditionalProperty]++-%20conditions%200..1>[Condition&#124;type:string%20%3F;subset:string%20%3F],[StyleSheet]++-%20nodeFilter%200..1>[Condition],[StyleSheet],[ConditionalProperty])](https://yuml.me/diagram/nofunky;dir:TB/class/[ConditionalProperty]++-%20conditions%200..1>[Condition&#124;type:string%20%3F;subset:string%20%3F],[StyleSheet]++-%20nodeFilter%200..1>[Condition],[StyleSheet],[ConditionalProperty])

## Referenced by Class

 *  **None** *[conditions](conditions.md)*  <sub>0..1</sub>  **[Condition](Condition.md)**
 *  **None** *[nodeFilter](nodeFilter.md)*  <sub>0..1</sub>  **[Condition](Condition.md)**

## Attributes


### Own

 * [type](type.md)  <sub>0..1</sub>
     * Description: the logical type, eg INDIVIDUAL, CLASS, etc
     * Range: [String](types/String.md)
 * [subset](subset.md)  <sub>0..1</sub>
     * Description: the subset to which the node belongs
     * Range: [String](types/String.md)
