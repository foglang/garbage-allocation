#Garbage allocation
>An outline for how html tags map to fog syntax and constructs

html|fog|status
---:|---|:----:
`<a>`|[unassigned](https://github.com/foglang/garbage-allocation/blob/master/tags/a/a.yaml)|
`<b>`|[variable access](https://github.com/foglang/garbage-allocation/blob/master/tags/b/b.yaml)|
`<br>`|[unassigned](https://github.com/foglang/garbage-allocation/blob/master/tags/br/br.yaml)|
`<code>`|[unassigned](https://github.com/foglang/garbage-allocation/blob/master/tags/code/code.yaml)|
`<div>`|[unassigned](https://github.com/foglang/garbage-allocation/blob/master/tags/div/div.yaml)|
`<em>`|[italics alias](https://github.com/foglang/garbage-allocation/blob/master/tags/i/i.yaml)|
`<hr>`|[unassigned](https://github.com/foglang/garbage-allocation/blob/master/tags/hr/hr.yaml)|
`<i>`|[operator](https://github.com/foglang/garbage-allocation/blob/master/tags/i/i.yaml)|
`<ins>`|[underline alias](https://github.com/foglang/garbage-allocation/blob/master/tags/u/u.yaml)|
`<li>`|[unassigned](https://github.com/foglang/garbage-allocation/blob/master/tags/li/li.yaml)|
`<ol>`|[unassigned](https://github.com/foglang/garbage-allocation/blob/master/tags/ol/ol.yaml)|
`<p>`|[ignored](https://github.com/foglang/garbage-allocation/blob/master/tags/p/p.yaml)|
`<pre>`|[rich text container](https://github.com/foglang/garbage-allocation/blob/master/tags/pre/pre.yaml)|
`<q>`|[unassigned](https://github.com/foglang/garbage-allocation/blob/master/tags/q/q.yaml)|
`<s>`|[undefine](https://github.com/foglang/garbage-allocation/blob/master/tags/s/s.yaml)|
`<strong>`|[bold alias](https://github.com/foglang/garbage-allocation/blob/master/tags/b/b.yaml)|
`<sub>`|[unassigned](https://github.com/foglang/garbage-allocation/blob/master/tags/sub/sub.yaml)|
`<sup>`|[unassigned](https://github.com/foglang/garbage-allocation/blob/master/tags/sup/sup.yaml)|
`<table>`|[variable definition structure](https://github.com/foglang/garbage-allocation/blob/master/tags/table/table.yaml)|
`<td>`|[component of table](https://github.com/foglang/garbage-allocation/blob/master/tags/td/td.yaml)|
`<title>`|[unassigned](https://github.com/foglang/garbage-allocation/blob/master/tags/title/title.yaml)|
`<tr>`|[component of table](https://github.com/foglang/garbage-allocation/blob/master/tags/tr/tr.yaml)|
`<u>`|[print data](https://github.com/foglang/garbage-allocation/blob/master/tags/u/u.yaml)|1
`<ul>`|[unassigned](https://github.com/foglang/garbage-allocation/blob/master/tags/ul/ul.yaml)|
`<var>`|[unassigned](https://github.com/foglang/garbage-allocation/blob/master/tags/var/var.yaml)|

##status translations
1 - will never change<br>
2 - we like this feature; unlikely to change<br>
3 - the feature works but has at least one flaw; could change<br>
4 - quick and dirty solution; likely to change<br>
5 - preposition or temporary solution

---

2015 foglang group `github.com/foglang`