Level two
=========

This data is in **CSV** format and should be
converted to a **JSON** dictionary, with the
first item on the line as the key. The JSON
should contain the **same data** as the CSV
and should have **correct syntax** but
**dosesn't** need to be pretty formated.

Example
-------

```csv
AAA, 20, 32,
BBB, 5, 126
```
```json
{
	"AAA": [
		20,
		32
	],
	"BBB": [
		5,
		126
	]
}
```
