Level four
==========

The INI format
--------------

> An INI file is a configuration file for computer
  software that consists of a text-based content
  with a structure and syntax comprising key–value
  pairs for properties, and sections that organize
  the properties.

that's the definition of an INI file from Wikipedia.
Practically it looks like this:
```ini
; last modified 1 April 2001 by John Doe
[owner]
name = John Doe
organization = Acme Widgets Inc.

[database]
; use IP address in case network name resolution is not working
server = 192.0.2.62     
port = 143
file = "payroll.dat"
```

The challenge
-------------

You will get an input in **INI** format and you could
convert it to **JSON** format.

### Example

```ini
[qd]
qm = 8298
qnqn = 4262
qoqo = 3400
; bla bla bla
[qp]
qq = 241
qyqyqy = 6908
```
```json
{
	"qd": {
		"qm": 8298,
		"qnqn": 4262,
	},
	"qp": {
		"qyqyqy": 6908
	}
}
```
