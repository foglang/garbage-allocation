#Garbage allocation
>An outline for how html tags map to fog syntax and constructs

html|fog|status
---:|---|:----:
`<b>`|[variable access](https://github.com/foglang/garbage-allocation/blob/master/tags/b/b.yaml)|
`<i>`|[operator](https://github.com/foglang/garbage-allocation/blob/master/tags/i/i.yaml)|
`<p>`|[ignored](https://github.com/foglang/garbage-allocation/blob/master/tags/p/p.yaml)|
`<pre>`|[rich text container](https://github.com/foglang/garbage-allocation/blob/master/tags/pre/pre.yaml)|
`<s>`|[undefine](https://github.com/foglang/garbage-allocation/blob/master/tags/s/s.yaml)|
`<table>`|[variable definition structure](https://github.com/foglang/garbage-allocation/blob/master/tags/table/table.yaml)|
`<td>`|[component of table](https://github.com/foglang/garbage-allocation/blob/master/tags/td/td.yaml)|
`<tr>`|[component of table](https://github.com/foglang/garbage-allocation/blob/master/tags/tr/tr.yaml)|
`<u>`|[print data](https://github.com/foglang/garbage-allocation/blob/master/tags/u/u.yaml)|1

##status translations
1 - will never change<br>
2 - we like this feature; unlikely to change<br>
3 - the feature works but has at least one flaw; could change<br>
4 - quick and dirty solution; likely to change<br>
5 - preposition or temporary solution

---

2015 foglang group `github.com/foglang`